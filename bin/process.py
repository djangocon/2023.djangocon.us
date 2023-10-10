"""NOTE: You need to adjust the dates **per year**"""
import csv
from io import StringIO
import frontmatter
import inflection
import os
import typer

from datetime import date, datetime, time
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from pathlib import Path
from pydantic import BaseModel, ValidationError
from rich import print
from slugify import slugify
from typing import List, Literal, Optional
from urllib.parse import quote_plus
import pytz

# TODO: Pull this from _config.yml
CONFERENCE_TZ = pytz.timezone("America/New_York")
YEAR = 2023

# Define your rooms here
LACTATION_ROOM = "Room TBA"
QUIET_ROOM = "Room TBA"
LUNCH_ROOM = "Grand Ballroom I-II"
LARGE_TALK_ROOM = "Junior Ballroom"
SMALL_TALK_ROOM = "Grand Ballroom III"
BREAK_AREA = LUNCH_ROOM
REGISTRATION_AREA = f"In front of {LARGE_TALK_ROOM}"


class FrontmatterModel(BaseModel):
    """
    Our base class for our default "Frontmatter" fields.
    """

    date: Optional[datetime] = None
    layout: str
    permalink: Optional[str] = None
    published: bool = True
    redirect_from: Optional[List[str]] = None
    redirect_to: Optional[str] = None  # via the jekyll-redirect-from plugin
    sitemap: Optional[bool] = None
    title: str

    class Config:
        extra = "allow"


class Job(FrontmatterModel):
    hidden: bool = False
    layout: str = "base"
    name: str
    title: Optional[str] = None
    website: str
    website_text: str = "Apply here"


class Organizer(FrontmatterModel):
    github: Optional[str] = None
    hidden: bool = False
    layout: str = "base"
    name: str
    photo_url: Optional[str] = None
    slug: Optional[str] = None
    title: Optional[str] = None
    twitter: Optional[str] = None
    website: Optional[str] = None
    mastodon: Optional[str] = None


class Page(FrontmatterModel):
    description: Optional[str] = None
    heading: Optional[str] = None
    hero_text_align: Optional[str] = None  # homepage related
    hero_theme: Optional[str] = None  # homepage related
    layout: Optional[str] = None
    testimonial_img: Optional[str] = None  # homepage related
    testimonial_img_mobile: Optional[str] = None  # homepage related
    title: Optional[str] = None


class Post(FrontmatterModel):
    author: Optional[str] = None
    category: Optional[str] = "General"  # TODO: build a list of these
    categories: Optional[List[str]] = None
    date: datetime  # YYYY-MM-DD HH:MM:SS +/-TTTT
    image: Optional[str] = None
    layout: Optional[str] = "post"
    slug: Optional[str] = None
    tags: Optional[List[str]] = []


class Presenter(FrontmatterModel):
    company: Optional[str] = None
    github: Optional[str] = None
    hidden: bool = False
    layout: str = "speaker-template"
    name: str
    override_schedule_title: Optional[str] = None
    pronouns: Optional[str] = None
    photo_url: Optional[str] = None
    role: Optional[str] = None
    slug: Optional[str] = None
    title: Optional[str] = None
    twitter: Optional[str] = None
    website: Optional[str] = None
    website_text: str = "Apply here"
    mastodon: Optional[str] = None

    def __init__(self, **data):
        super().__init__(**data)

        # if slugs are blank default them to slugify(name)
        if not self.slug:
            self.slug = slugify(self.name)

        # if permalink is blank, let's build a new one
        if not self.permalink:
            self.permalink = f"/presenters/{self.slug}/"

        if self.mastodon and self.mastodon.startswith("@"):
            self.mastodon = migrate_mastodon_handle(handle=self.mastodon)
            print(f"🚜 converting {self.mastodon=}")


class Schedule(FrontmatterModel):
    abstract: Optional[str] = None
    accepted: bool = False
    category: Literal[
        "break",
        "lunch",
        "rooms",
        "social-event",
        "sprints",
        "talks",
        "tutorials",
    ]
    difficulty: Optional[str] = "All"
    end_date: Optional[datetime] = None
    group: Optional[
        Literal[
            "break",
            "lunch",
            "rooms",
            "social-event",
            "sprints",
            "talks",
            "tutorials",
        ]
    ] = None

    image: Optional[str] = None
    layout: Optional[str] = "session-details"  # TODO: validate against _layouts/*.html
    presenter_slugs: Optional[List[str]] = None
    presenters: Optional[List[dict]] = None  # TODO: break this into a sub-type
    published: bool = False
    room: Optional[str] = None
    schedule: Optional[str] = None
    schedule_layout: Optional[str] = None  # TODO: Validate for breaks, lunch, etc
    show_video_urls: Optional[bool] = None
    slides_url: Optional[str] = None
    summary: Optional[str] = None
    tags: Optional[List[str]] = None
    talk_slot: Optional[str] = "full"
    track: Optional[str] = None
    video_url: Optional[str] = None

    def __init__(self, **data):
        super().__init__(**data)

        # keep group in sync with category to work around a Jekyll
        # Collection bug that set category equal to the collection's
        # subfolder...
        if self.group != self.category:
            self.group = self.category


POST_TYPES = [
    {
        "path": "_jobs",
        "class_name": Job,
        "exclude_unset": True,
    },
    {
        "path": "_organizers",
        "class_name": Organizer,
        "exclude_unset": True,
    },
    {
        "path": "_pages",
        "class_name": Page,
        "exclude_unset": True,
    },
    {
        "path": "_posts",
        "class_name": Post,
        "exclude_unset": True,
    },
    {
        "path": "_presenters",
        "class_name": Presenter,
        "exclude_unset": True,
    },
    {
        "path": "_schedule/sprints",
        "class_name": Schedule,
        "exclude_unset": True,
    },
    {
        "path": "_schedule/talks",
        "class_name": Schedule,
        "exclude_unset": True,
    },
    {
        "path": "_schedule/tutorials",
        "class_name": Schedule,
        "exclude_unset": True,
    },
]


def migrate_mastodon_handle(*, handle: str) -> str:
    if not handle.startswith("@"):
        return handle

    username, domain = handle[1:].split("@")
    return f"https://{domain}/@{username}"


app = typer.Typer()


@app.command()
def fmt():
    for post_type in POST_TYPES:
        filenames = sorted(list(Path(post_type["path"]).glob("**/*")))

        for filename in filenames:
            try:
                post = frontmatter.loads(filename.read_text())
                data = post_type["class_name"](**post.metadata)
                post.metadata.update(
                    data.model_dump(exclude_unset=post_type["exclude_unset"])
                )
                filename.write_text(frontmatter.dumps(post) + os.linesep)
            except ValidationError as e:
                typer.secho(f"{filename}", fg="red")
                typer.echo(e.json())
            except Exception as e:
                typer.secho(f"{filename}::{e}", fg="red")


@app.command()
def validate():
    for post_type in POST_TYPES:
        filenames = sorted(list(Path(post_type["path"]).glob("**/*")))

        for filename in filenames:
            try:
                data = frontmatter.loads(filename.read_text())
                post_type["class_name"](**data.metadata)
            except ValidationError as e:
                print(f"[red]{filename}[/red]")
                print(e.json())
            except Exception as e:
                print(f"[red]{filename}::{e}[/red]")


@app.command()
def generate_lactation_room(
    event_date: datetime,
    link: str = "/news/childcare-lactation/",
    room_name: str = LACTATION_ROOM,
    start_time: str = "8:00",
    end_time: str = "17:30",
):
    category = "talks"
    parsed_start = parse(start_time).time()
    parsed_end = parse(end_time).time()
    if isinstance(event_date, date) and not isinstance(event_date, datetime):
        start = CONFERENCE_TZ.localize(datetime.combine(event_date, parsed_start))
        end = CONFERENCE_TZ.localize(datetime.combine(event_date, parsed_end))
    else:
        start = CONFERENCE_TZ.localize(
            datetime.combine(event_date.date(), parsed_start)
        )
        end = CONFERENCE_TZ.localize(datetime.combine(event_date.date(), parsed_end))
    post = frontmatter.loads(room_name)
    sched = Schedule(
        accepted=True,
        category="break",
        date=start,
        end_date=end,
        layout="session-details",
        link=link or None,
        permalink=None,
        room=room_name,
        schedule_layout="full",
        sitemap=False,
        talk_slot="full",
        title="Lactation Room",
    )
    post.metadata.update(sched.model_dump(exclude_unset=True))
    output_path = Path(
        f"_schedule/{category}/{sched.date.year}-{sched.date.month:0>2}"
        f"-{sched.date.day:0>2}-{sched.date.hour:0>2}-{sched.date.minute:0>2}-lactation-room.md"
    )
    output_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Saved to {output_path}")


@app.command()
def generate_quiet_room(
    event_date: datetime,
    room_name: str = QUIET_ROOM,
    start_time: str = "8:00",
    end_time: str = "18:00",
):
    category = "break"
    parsed_start = parse(start_time).time()
    parsed_end = parse(end_time).time()
    if isinstance(event_date, date) and not isinstance(event_date, datetime):
        start = CONFERENCE_TZ.localize(datetime.combine(event_date, parsed_start))
        end = CONFERENCE_TZ.localize(datetime.combine(event_date, parsed_end))
    else:
        start = CONFERENCE_TZ.localize(
            datetime.combine(event_date.date(), parsed_start)
        )
        end = CONFERENCE_TZ.localize(datetime.combine(event_date.date(), parsed_end))
    post = frontmatter.loads(room_name)
    sched = Schedule(
        accepted=True,
        category=category,
        date=start,
        end_date=end,
        layout="session-details",
        link=None,
        permalink=None,
        room=room_name,
        schedule_layout="full",
        sitemap=False,
        talk_slot="full",
        title="Quiet Room",
    )
    post.metadata.update(sched.model_dump(exclude_unset=True))
    output_path = Path(
        f"_schedule/talks/{sched.date.year}-{sched.date.month:0>2}-"
        f"{sched.date.day:0>2}-{sched.date.hour:0>2}-{sched.date.minute:0>2}-quiet-room.md"
    )
    output_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Saved to {output_path}")


@app.command()
def generate_registration_desk(
    event_date: datetime,
    location: str = REGISTRATION_AREA,
    start_time: str = "8:00",
    end_time: str = "18:00",
):
    category = "talks"
    if event_date.weekday() in {3, 4}:
        raise ValueError("We don't have a registration desk on sprint days")

    parsed_start = parse(start_time).time()
    parsed_end = parse(end_time).time()
    if isinstance(event_date, date) and not isinstance(event_date, datetime):
        start = CONFERENCE_TZ.localize(datetime.combine(event_date, parsed_start))
        end = CONFERENCE_TZ.localize(datetime.combine(event_date, parsed_end))
    else:
        start = CONFERENCE_TZ.localize(
            datetime.combine(event_date.date(), parsed_start)
        )
        end = CONFERENCE_TZ.localize(datetime.combine(event_date.date(), parsed_end))
    post = frontmatter.loads(location)
    sched = Schedule(
        accepted=True,
        category="break",
        date=start,
        end_date=end,
        layout="session-details",
        link=None,
        permalink=None,
        room=location,
        schedule_layout="full",
        sitemap=False,
        talk_slot="full",
        title="Registration",
    )
    post.metadata.update(sched.model_dump(exclude_unset=True))
    output_path = Path(
        f"_schedule/{category}/{sched.date.year}-{sched.date.month:0>2}-"
        f"{sched.date.day:0>2}-{sched.date.hour:0>2}-{sched.date.minute:0>2}-registration.md"
    )
    output_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Saved to {output_path}")


@app.command()
def generate_breakfast(start_time: datetime, location: str = LUNCH_ROOM):
    category = "talks"  # yes, I know...
    start_time = CONFERENCE_TZ.localize(start_time)
    if start_time.weekday in {3, 4}:
        category = "sprints"
    end_time = start_time + relativedelta(hours=1)
    post = frontmatter.loads(location)
    sched = Schedule(
        accepted=True,
        category="lunch",
        date=start_time,
        end_date=end_time,
        layout="session-details",
        link="/catering-menus/",  # TODO: Add/link to #DOW
        permalink=None,
        room=location,
        schedule_layout="full",
        sitemap=False,
        talk_slot="full",
        title="Breakfast",
    )
    post.metadata.update(sched.model_dump(exclude_unset=True))
    output_path = Path(
        f"_schedule/{category}/{sched.date.year}-{sched.date.month:0>2}-"
        f"{sched.date.day:0>2}-{sched.date.hour:0>2}-{sched.date.minute:0>2}-{slugify(sched.title)}.md"
    )
    output_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Saved to {output_path}")


@app.command()
def generate_break(
    start_time: datetime,
    duration_minutes: int = 30,
    location: str = BREAK_AREA,
):
    category = "talks"
    if start_time.weekday in {3, 4}:
        category = "sprints"
    start_time = CONFERENCE_TZ.localize(start_time)
    end_time = start_time + relativedelta(minutes=duration_minutes)
    post = frontmatter.loads(location)
    sched = Schedule(
        accepted=True,
        category="break",
        date=start_time,
        end_date=end_time,
        layout="session-details",
        link=None,  # TODO: Add/link to #DOW
        permalink=None,
        room=location,
        schedule_layout="full",
        sitemap=False,
        talk_slot="full",
        title="Break",
    )
    post.metadata.update(sched.model_dump(exclude_unset=True))
    output_path = Path(
        f"_schedule/{category}/{sched.date.year}-{sched.date.month:0>2}-"
        f"{sched.date.day:0>2}-{sched.date.hour:0>2}-{sched.date.minute:0>2}-{slugify(sched.title)}.md"
    )
    output_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Saved to {output_path}")


@app.command()
def generate_early_lunch(
    start_time: datetime,
    duration_minutes: int = 50,
    location: str = LUNCH_ROOM,
    track: int = 1,
):
    category = "talks"
    if start_time.weekday() == 6:
        raise ValueError("We don't have lightning talks on tutorial days")
    elif start_time.weekday() in {3, 4}:
        raise ValueError("We don't have lightning talks on sprint days")
    start_time = CONFERENCE_TZ.localize(start_time)
    end_time = start_time + relativedelta(minutes=duration_minutes)
    post = frontmatter.loads("")
    sched = Schedule(
        accepted=True,
        category="lunch",
        date=start_time,
        end_date=end_time,
        layout="session-details",
        link="/catering-menus/",  # TODO: Add/link to #DOW
        room=location,
        sitemap=False,
        title="Early Lunch",
        track=f"t{track}",
    )
    post.metadata.update(sched.model_dump(exclude_unset=True))
    output_path = Path(
        f"_schedule/{category}/{sched.date.year}-{sched.date.month:0>2}-"
        f"{sched.date.day:0>2}-{sched.date.hour:0>2}-{sched.date.minute:0>2}-t{track}-{slugify(sched.title)}.md"
    )
    output_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Saved to {output_path}")


@app.command()
def generate_lunch(
    start_time: datetime,
    duration_minutes: int = 45,
    location: str = LUNCH_ROOM,
):
    category = "talks"
    if start_time.weekday() == 6:
        category = "tutorials"
    elif start_time.weekday() in {3, 4}:
        category = "sprints"
    start_time = CONFERENCE_TZ.localize(start_time)
    end_time = start_time + relativedelta(minutes=duration_minutes)
    post = frontmatter.loads("")
    sched = Schedule(
        accepted=True,
        category=category,
        date=start_time,
        end_date=end_time,
        layout="session-details",
        link="/catering-menus/",  # TODO: Add/link to #DOW
        room=location,
        sitemap=False,
        talk_slot="full",
        title="Lunch",
    )
    post.metadata.update(sched.model_dump(exclude_unset=True))
    output_path = Path(
        f"_schedule/{category}/{sched.date.year}-{sched.date.month:0>2}-"
        f"{sched.date.day:0>2}-{sched.date.hour:0>2}-{sched.date.minute:0>2}-{slugify(sched.title)}.md"
    )
    output_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Saved to {output_path}")


@app.command()
def add_pronouns_from_csv(
    csv_path: str,
) -> None:
    """Load pronouns from the speaker info form and add them to speakers"""
    csv_data = csv.reader(
        Path(csv_path).read_text().splitlines(),
    )
    # field 1 = speaker 1 name
    # field 3 = speaker 1 pronouns
    # NOTE: as of 2023-07-19, nobody has filled in the second speaker details
    # and we only have one multi-speaker presentation, so it's fine to hand-update
    # that one
    pronouns = {row[1]: (row[3] or "").strip().casefold() for row in csv_data}
    speaker_paths = Path("_presenters").glob("*.md")
    for speaker in speaker_paths:
        post = frontmatter.loads(speaker.read_text())
        presenter = Presenter(**post.metadata)
        try:
            speaker_pronoun = pronouns[presenter.name]
        except KeyError:
            continue
        if not speaker_pronoun:
            continue
        presenter.pronouns = speaker_pronoun.casefold()
        output_path = Path(f"_presenters/{presenter.slug}.md")
        post.metadata.update(presenter.model_dump(exclude_unset=True))
        output_path.write_text(frontmatter.dumps(post) + "\n")


@app.command()
def generate_opening_remarks(
    start_time: datetime,
    duration_minutes: int = 15,
    speaker_name: str = "",
    location: str = LARGE_TALK_ROOM,
    track: int = 0,
):
    category = "talks"
    if start_time.weekday() not in range(0, 3):
        raise ValueError("We only have keynotes on talk days")
    start_time = CONFERENCE_TZ.localize(start_time)
    end_time = start_time + relativedelta(minutes=duration_minutes)
    if speaker_name:
        speaker_post = frontmatter.loads("")
        speaker = Presenter(
            name=speaker_name,
        )
        if (organizer_path := Path(f"_organizers/{speaker.slug}.md")).exists():
            organizer_post = frontmatter.loads(organizer_path.read_text())
            organizer = Organizer(**organizer_post.metadata)
            speaker.twitter = organizer.twitter
            speaker.github = organizer.github
            speaker.photo_url = organizer.photo_url
            speaker.website = organizer.website
            speaker.title = organizer.title
            speaker.mastodon = organizer.mastodon
        speaker_post.metadata.update(speaker.model_dump(exclude_unset=True))
        output_path = Path(f"_presenters/{speaker.slug}.md")
        output_path.write_text(frontmatter.dumps(speaker_post) + "\n")

    post = frontmatter.loads("")
    sched = Schedule(
        accepted=True,
        category=category,
        date=start_time,
        end_date=end_time,
        layout="session-details",
        permalink=f"/talks/opening-remarks-{start_time:%A}/".casefold(),
        room=location,
        schedule_layout="full",
        sitemap=True,
        title="Opening Remarks",
        track=f"t{track}",
    )
    if speaker_name:
        sched.presenter_slugs = [slugify(speaker_name)]
    post.metadata.update(sched.model_dump(exclude_unset=True))
    output_path = Path(
        f"_schedule/{category}/{sched.date.year}-{sched.date.month:0>2}-"
        f"{sched.date.day:0>2}-{sched.date.hour:0>2}-{sched.date.minute:0>2}-t{track}-{slugify(sched.title)}.md"
    )
    output_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Saved to {output_path}")


@app.command()
def generate_lightning_talks(
    start_time: datetime,
    duration_minutes: int = 50,
    location: str = LARGE_TALK_ROOM,
    track: int = 0,
):
    category = "talks"
    if start_time.weekday() == 6:
        raise ValueError("We don't have lightning talks on tutorial days")
    elif start_time.weekday() in {3, 4}:
        raise ValueError("We don't have lightning talks on tutorial days")
    start_time = CONFERENCE_TZ.localize(start_time)
    end_time = start_time + relativedelta(minutes=duration_minutes)
    post = frontmatter.loads("")
    sched = Schedule(
        accepted=True,
        category=category,
        date=start_time,
        end_date=end_time,
        layout="session-details",
        permalink=f"/talks/lightning-talks-{start_time:%A}/".casefold(),
        presenter_slugs=["kojo-idrissa"],
        room=location,
        sitemap=True,
        title="Lightning Talks",
        track=f"t{track}",
    )
    post.metadata.update(sched.model_dump(exclude_unset=True))
    output_path = Path(
        f"_schedule/{category}/{sched.date.year}-{sched.date.month:0>2}-"
        f"{sched.date.day:0>2}-{sched.date.hour:0>2}-{sched.date.minute:0>2}-t{track}-{slugify(sched.title)}.md"
    )
    output_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Saved to {output_path}")


@app.command()
def generate_keynote(
    start_time: datetime, duration_minutes: int = 45, location: str = LARGE_TALK_ROOM
):
    category = "talks"
    if start_time.weekday() == 6:
        raise ValueError("No keynotes on tutorial day")
    elif start_time.weekday() in {3, 4}:
        raise ValueError("No keynotes on tutorial day")
    start_time = CONFERENCE_TZ.localize(start_time)
    end_time = start_time + relativedelta(minutes=duration_minutes)
    post = frontmatter.loads(
        "Pay attention to our [blog](/news/) for keynote speakers!"
    )
    sched = Schedule(
        accepted=True,
        category=category,
        date=start_time,
        difficulty="All",
        end_date=end_time,
        layout="session-details",
        link=None,
        room=location,
        sitemap=True,
        talk_slot="full",
        title="Keynote (to be announced)",
        track="t1",
    )
    post.metadata.update(sched.model_dump(exclude_unset=True))
    output_path = Path(
        f"_schedule/{category}/{sched.date.year}-{sched.date.month:0>2}-"
        f"{sched.date.day:0>2}-{sched.date.hour:0>2}-{sched.date.minute:0>2}-{slugify(sched.title)}.md"
    )
    output_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Saved to {output_path}")


@app.command()
def generate_natalia_talk(
    start_time: datetime, duration_minutes: int = 45, location: str = LARGE_TALK_ROOM
):
    category = "talks"
    if start_time.weekday() == 6:
        raise ValueError("No keynotes on tutorial day")
    elif start_time.weekday() in {3, 4}:
        raise ValueError("No keynotes on tutorial day")
    start_time = CONFERENCE_TZ.localize(start_time)
    end_time = start_time + relativedelta(minutes=duration_minutes)
    speaker_post = frontmatter.loads("")
    speaker = Presenter(
        name="Natalia Bidart",
        slug="natalia-bidart",
        title="Django Fellow",
        mastodon="https://fosstodon.org/@nessita",
    )
    output_path = Path(f"_presenters/{speaker.slug}.md")
    speaker_post.metadata.update(speaker.model_dump(exclude_unset=True))
    output_path.write_text(frontmatter.dumps(speaker_post) + "\n")
    post = frontmatter.loads(
        """In this talk I'll share my personal journey of understanding diversity and inclusion.
Being part of a minority group, I have encountered numerous challenges, I've learned
a lot, and made my fair share of mistakes along the way.

This presentation is an opportunity to reflect on my experiences, sharing the lessons
learned and real-life stories that have shaped my view on the matter. Get ready for a
captivating array of anecdotes!

I'll openly discuss the challenges I've faced and the insights I've gained,
highlighting both successes and shortcomings, always offering a perspective rather than
definitive solutions or comprehensive analysis. I'll cover topics such as tone connotations,
inclusive[n|l]ess of different languages, the importance of company policies, quirks
derived from cultural and social norms, and more. In the final segment of this talk, I
will discuss my recent experience within the Django project and community as a whole.

This talk is not intended to provide a one-size-fits-all approach, but rather to inspire
thought, reflection, and positive change. I hope to encourage open dialogue among
attendees, as we explore strategies for creating a more inclusive, diverse and
equitable environment."""
    )
    sched = Schedule(
        accepted=True,
        category=category,
        date=start_time,
        difficulty="All",
        end_date=end_time,
        layout="session-details",
        link=None,
        presenter_slugs=["natalia-bidart"],
        room=location,
        schedule_layout="full",
        sitemap=True,
        title="Inside Out: My Journey of Understanding Inclusion",
        track="t1",
    )
    post.metadata.update(sched.model_dump(exclude_unset=True))
    output_path = Path(
        f"_schedule/{category}/{sched.date.year}-{sched.date.month:0>2}-"
        f"{sched.date.day:0>2}-{sched.date.hour:0>2}-{sched.date.minute:0>2}-{slugify(sched.title)}.md"
    )
    output_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Saved to {output_path}")


@app.command()
def generate_shots(
    height: int = 630,
    quality: int = 80,
    width: int = 1200,
):
    schedules = Path('_schedule').glob('**/*.md')
    used_talks: set[str] = set()
    for schedule in schedules:
        post = frontmatter.loads(schedule.read_text())
        if 'presenter_slugs' in post:
            used_talks |= set(post['presenter_slugs'])
    presenters = Path("_presenters").glob("*.md")
    presenters = sorted(presenters, key=os.path.getmtime)
    for presenter in presenters:
        post = frontmatter.loads(presenter.read_text())
        if post['slug'] not in used_talks:
            continue
        print(f"- output: ./static/img/social/presenters/{post['slug']}.png")
        print(f"  height: {height}")
        print(f"  quality: {quality}")
        print(f"  width: {width}")
        print(f"  url: https://{YEAR}.djangocon.us{post['permalink']}")
        print()


@app.command()
def generate_speaker_csv_for_loudswarm(output_path: Path):
    filenames = sorted(list(Path("_presenters").glob("**/*.md")))
    output: list[dict[str, str]] = []
    for filename in filenames:
        post = frontmatter.loads(filename.read_text())
        data = Presenter(**post.metadata)
        bio = post.content
        output.append(
            {
                "name": data.name,
                "attendee_email": "",
                "bio (can be html)": bio,
                "job_title": data.title,
                "company_name": data.company,
                "personal_website": data.website,
                "github_url": f"https://github.com/{data.github}"
                if data.github
                else "",
                "twitter_url": f"https://twitter.com/{data.twitter}"
                if data.twitter
                else "",
                "youtube_url": "",
                "display_email": "",  # TODO add mastodon?
            }
        )
    buffer = StringIO()
    writer = csv.DictWriter(buffer, list(output[0]))
    writer.writeheader()
    writer.writerows(output)
    output_path.write_text(buffer.getvalue())


@app.command()
def generate_schedule_csv_for_loudswarm(output_path: Path):
    filenames = sorted(list(Path("_schedule/talks").glob("**/*.md")))
    output: list[dict[str, str]] = []
    for filename in filenames:
        post = frontmatter.loads(filename.read_text())
        talk = Schedule(**post.metadata)
        if talk.room in {
            LUNCH_ROOM,
            QUIET_ROOM,
            REGISTRATION_AREA,
        } or talk.room.startswith("Tutorial Track"):
            continue
        output.append(
            {
                "name": talk.title,
                "track_name": talk.room,
                "description": post.content,
                "presenter_emails": "",
                "start": talk.date.isoformat(),
                "end": talk.end_date.isoformat(),
                "banner_name": "",
            }
        )
    buffer = StringIO()
    writer = csv.DictWriter(buffer, list(output[0]))
    writer.writeheader()
    writer.writerows(output)
    output_path.write_text(buffer.getvalue())


@app.command()
def generate_2023_placeholders(event_date: datetime, create_keynotes: bool = False):
    tutorial_date = event_date - relativedelta(weeks=1)
    talks_dates = [event_date + relativedelta(days=count) for count in [1, 2, 3]]
    sprints_dates = [event_date + relativedelta(days=count) for count in [4, 5]]
    break_times = [time(10, 40), time(15, 25)]
    talk_lunch_time = time(13, 20)
    tutorial_breakfast_time = time(8)
    talk_breakfast_times = [time(8), time(8, 30), time(8, 30)]
    lightning_talk_time = time(12, 30)
    # online tutorials for 2023, so no lunch
    sprint_lunch_time = time(12, 30)
    # tutorial_lunch_time = sprint_lunch_time
    keynote_time = time(9, 45)
    registration_open = time(8)
    # generate_registration_desk(tutorial_date)
    # generate_lactation_room(tutorial_date)
    # generate_quiet_room(tutorial_date)
    # generate_breakfast(datetime.combine(tutorial_date.date(), tutorial_breakfast_time))
    # generate_lunch(
    #     datetime.combine(tutorial_date.date(), tutorial_lunch_time), duration_minutes=60
    # )
    for talk_date, breakfast_time in zip(talks_dates, talk_breakfast_times):
        opening_time = datetime.combine(talk_date.date(), registration_open)
        generate_lactation_room(opening_time)
        generate_quiet_room(opening_time)
        generate_breakfast(datetime.combine(talk_date.date(), breakfast_time))
        generate_lunch(datetime.combine(talk_date.date(), talk_lunch_time))
        generate_lightning_talks(
            datetime.combine(talk_date.date(), lightning_talk_time)
        )
        generate_early_lunch(datetime.combine(talk_date.date(), lightning_talk_time))
        generate_registration_desk(
            datetime.combine(talk_date.date(), registration_open)
        )
        for break_time in break_times:
            timestamp = datetime.combine(talk_date.date(), break_time)
            generate_break(timestamp)
        if create_keynotes:
            generate_keynote(datetime.combine(talk_date.date(), keynote_time))
    for sprint_date in sprints_dates:
        opening_time = datetime.combine(sprint_date.date(), registration_open)
        generate_lactation_room(opening_time)
        generate_quiet_room(opening_time)
        generate_breakfast(datetime.combine(sprint_date.date(), breakfast_time))
        generate_lunch(datetime.combine(sprint_date.date(), sprint_lunch_time))
    generate_natalia_talk(talks_dates[-1].replace(hour=11, minute=10))


@app.command()
def process(
    process_presenters: bool = False, rename: bool = False, slug_max_length: int = 40
):
    filenames = sorted(list(Path("_schedule").glob("**/*.md")))

    for filename in filenames:
        try:
            dirty = False
            post = frontmatter.loads(filename.read_text())

            # TODO: Re-enable once we know everything works...
            data = Schedule(**post.metadata)
            post.metadata.update(data.model_dump(exclude_unset=True))

            slug = slugify(
                post["title"], max_length=slug_max_length, word_boundary=True
            )
            if isinstance(post["date"], str):
                # NOTE if you get weird results in 2022+ importing from papercall,
                # switch this to date = maya.when(post["date"]).datetime(
                #    to_timezone="US/Central", naive=True
                # )
                date = parse(post["date"]).astimezone(CONFERENCE_TZ)
            else:
                date = post["date"].astimezone(CONFERENCE_TZ)

            category = post.get("category")

            # TODO: Double check this...
            # if category in ["break", "lunch", "social-hour"]:
            #     category = "talk"

            category_plural = inflection.pluralize(category)

            permalink = post.get("permalink")
            presenters = post.get("presenters", list())
            track = post.get("track")

            # TODO: Move to Model and check category/to verify if this
            # should be changed
            if not permalink:
                permalink = "/".join(["", category_plural, slug, ""])
                post["permalink"] = permalink
                dirty = True

            if process_presenters:
                if presenters and len(presenters):
                    post["presenter_slugs"] = []
                    for presenter in presenters:
                        presenter = presenter.copy()
                        presenter_name = presenter.get("name")

                        if presenter_name:
                            presenter_slug = slugify(
                                presenter_name,
                                max_length=slug_max_length,
                                word_boundary=True,
                            )
                        else:
                            presenter_slug = None

                        if presenter_slug:
                            post["presenter_slugs"].append(presenter_slug)
                            presenter_post = frontmatter.loads(presenter.get("bio", ""))
                            del presenter["bio"]
                            presenter[
                                "layout"
                            ] = "speaker-template"  # 'presenter-details'
                            presenter["permalink"] = "/".join(
                                ["", "presenters", presenter_slug, ""]
                            )
                            presenter["slug"] = presenter_slug
                            presenter_post.metadata = presenter

                            presenter_filename = Path(
                                "_presenters", f"{presenter_slug}.md"
                            )

                            if not presenter_filename.parent.exists():
                                presenter_filename.parent.mkdirs()

                            presenter_filename.write_text(
                                frontmatter.dumps(presenter_post)
                            )

                        dirty = True
                        # post["presenters"] = post["presenter_slugs"]
                        # del post["presenter_slugs"]

                if post["presenter_slugs"] and len(post["presenter_slugs"]):
                    presenter_slug = post["presenter_slugs"][0]
                    image_url = (
                        f"https://{YEAR}.djangocon.us/presenters/{presenter_slug}"
                    )
                    image_url = quote_plus(image_url)
                    image_url = quote_plus(image_url)
                    image_url = f"https://v1.screenshot.11ty.dev/{image_url}/opengraph/"
                    post["image"] = image_url

            if dirty is True:
                filename.write_text(frontmatter.dumps(post) + "\n")

            if track and len(track):
                talk_filename = "-".join(
                    [
                        f"{date.year:04}",
                        f"{date.month:02}",
                        f"{date.day:02}",
                        f"{date.hour:02}",
                        f"{date.minute:02}",
                        f"{track}",
                        f"{slug}.md",
                    ]
                )

            else:
                talk_filename = "-".join(
                    [
                        f"{date.year:04}",
                        f"{date.month:02}",
                        f"{date.day:02}",
                        f"{date.hour:02}",
                        f"{date.minute:02}",
                        f"{slug}.md",
                    ]
                )

            target = Path(filename.parent, talk_filename)
            if not (filename.name == target.name):
                if rename:
                    typer.echo(f"renaming {talk_filename} to {target}")
                    filename.rename(target)
                else:
                    print(
                        f"we [yellow]would[/yellow] rename {talk_filename} to {target}"
                    )

        except Exception as e:
            typer.secho(f"{filename}:: {e}", fg="red")


if __name__ == "__main__":
    app()

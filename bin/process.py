import csv
from io import StringIO
from turtle import title
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
from typing import List, Literal, Optional, Union
from urllib.parse import quote_plus
import pytz

# TODO: Pull this from _config.yml
CONFERENCE_TZ = pytz.timezone("America/Los_Angeles")


class FrontmatterModel(BaseModel):
    """
    Our base class for our default "Frontmatter" fields.
    """

    date: Optional[datetime]
    layout: str
    permalink: Optional[str]
    published: bool = True
    redirect_from: Optional[List[str]]
    redirect_to: Optional[str]  # via the jekyll-redirect-from plugin
    sitemap: Optional[bool]
    title: str

    class Config:
        extra = "allow"


class Job(FrontmatterModel):
    hidden: bool = False
    layout: str = "base"
    name: str
    title: Optional[str]
    website: str
    website_text: str = "Apply here"


class Organizer(FrontmatterModel):
    github: Optional[str]
    hidden: bool = False
    layout: str = "base"
    name: str
    photo_url: Optional[str]
    slug: Optional[str]
    title: Optional[str]
    twitter: Optional[str]
    website: Optional[str]


class Page(FrontmatterModel):
    description: Optional[str]
    heading: Optional[str]
    hero_text_align: Optional[str]  # homepage related
    hero_theme: Optional[str]  # homepage related
    layout: Optional[str]
    testimonial_img: Optional[str]  # homepage related
    testimonial_img_mobile: Optional[str]  # homepage related
    title: Optional[str]


class Post(FrontmatterModel):
    author: Optional[str] = None
    category: Optional[str] = "General"  # TODO: build a list of these
    categories: Optional[List[str]]
    date: datetime  # YYYY-MM-DD HH:MM:SS +/-TTTT
    image: Optional[str] = None
    layout: Optional[str] = "post"
    slug: Optional[str] = None
    tags: Optional[List[str]]


class Presenter(FrontmatterModel):
    company: Optional[str]
    github: Optional[str]
    hidden: bool = False
    layout: str = "speaker-template"
    name: str
    override_schedule_title: Optional[str] = None
    pronouns: Optional[str]
    photo_url: Optional[str]
    role: Optional[str]
    slug: Optional[str] = None
    title: Optional[str]
    twitter: Optional[str]
    website: Optional[str]
    website_text: str = "Apply here"

    def __init__(self, **data):
        super().__init__(**data)

        # if slugs are blank default them to slugify(name)
        if not self.slug:
            self.slug = slugify(self.name)

        # if permalink is blank, let's build a new one
        if not self.permalink:
            self.permalink = f"/presenters/{self.slug}/"


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
    ]

    image: Optional[str]
    layout: Optional[str] = "session-details"  # TODO: validate against _layouts/*.html
    presenter_slugs: Optional[List[str]] = None
    presenters: List[dict] = None  # TODO: break this into a sub-type
    published: bool = False
    room: Optional[str]
    schedule: Optional[str]
    schedule_layout: Optional[str]  # TODO: Validate for breaks, lunch, etc
    show_video_urls: Optional[bool]
    slides_url: Optional[str]
    summary: Optional[str]
    tags: Optional[List[str]] = None
    talk_slot: Optional[str] = "full"
    track: Optional[str] = None
    video_url: Optional[str]

    def __init__(self, **data):
        super().__init__(**data)

        # keep group in sync with category to work around a Jekyll
        # Collection bug that set category equal to the collection's
        # subfolder...
        if self.group != self.category:
            self.group = self.category


POST_TYPES = [
    {"path": "_jobs", "class_name": Job},
    {"path": "_organizers", "class_name": Organizer},
    {"path": "_pages", "class_name": Page},
    {"path": "_posts", "class_name": Post},
    {"path": "_presenters", "class_name": Presenter},
    {"path": "_schedule/sprints", "class_name": Schedule},
    {"path": "_schedule/talks", "class_name": Schedule},
    {"path": "_schedule/tutorials", "class_name": Schedule},
]

app = typer.Typer()


@app.command()
def fmt():
    for post_type in POST_TYPES:
        filenames = sorted(list(Path(post_type["path"]).glob("**/*")))

        for filename in filenames:
            try:
                post = frontmatter.loads(filename.read_text())
                data = post_type["class_name"](**post.metadata)
                post.metadata.update(data.dict(exclude_unset=True))
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
                typer.secho(f"{filename}", fg="red")
                typer.echo(e.json())
            except Exception as e:
                typer.secho(f"{filename}::{e}", fg="red")


@app.command()
def generate_lactation_room(
    event_date: datetime,
    link: str = "",  # TODO update this to /news/lactation-room/ after we make the blog post
    room_name: str = "Private Dining Room",
    start_time: str = "8:00",
    end_time: str = "17:30",
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
        link=link or None,
        permalink=None,
        room=room_name,
        schedule_layout="full",
        sitemap=False,
        talk_slot="full",
        title="Lactation Room",
    )
    post.metadata.update(sched.dict(exclude_unset=True))
    output_path = Path(
        f"_schedule/{category}/{sched.date.year}-{sched.date.month:0>2}"
        f"-{sched.date.day:0>2}-{sched.date.hour:0>2}-{sched.date.minute:0>2}-lactation-room.md"
    )
    output_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Saved to {output_path}")


@app.command()
def generate_quiet_room(
    event_date: datetime,
    room_name: str = "Santa Fe 3",
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
    post.metadata.update(sched.dict(exclude_unset=True))
    output_path = Path(
        f"_schedule/{category}/{sched.date.year}-{sched.date.month:0>2}-"
        f"{sched.date.day:0>2}-{sched.date.hour:0>2}-{sched.date.minute:0>2}-quiet-room.md"
    )
    output_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Saved to {output_path}")


@app.command()
def generate_registration_desk(
    event_date: datetime,
    location: str = "In front of Salon A",
    start_time: str = "8:00",
    end_time: str = "18:00",
):
    category = "break"
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
        category=category,
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
    post.metadata.update(sched.dict(exclude_unset=True))
    output_path = Path(
        f"_schedule/{category}/{sched.date.year}-{sched.date.month:0>2}-"
        f"{sched.date.day:0>2}-{sched.date.hour:0>2}-{sched.date.minute:0>2}-registration.md"
    )
    output_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Saved to {output_path}")


@app.command()
def generate_breakfast(start_time: datetime, location: str = "West Lawn"):
    category = "lunch"  # yes, I know...
    start_time = CONFERENCE_TZ.localize(start_time)
    end_time = start_time + relativedelta(hours=1)
    post = frontmatter.loads(location)
    sched = Schedule(
        accepted=True,
        category=category,
        date=start_time,
        end_date=end_time,
        layout="session-details",
        link="/catering-menus/",
        permalink=None,
        room=location,
        schedule_layout="full",
        sitemap=False,
        talk_slot="full",
        title="Continental Breakfast",
    )
    post.metadata.update(sched.dict(exclude_unset=True))
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
    location: str = "West Lawn",
):
    category = "break"
    start_time = CONFERENCE_TZ.localize(start_time)
    end_time = start_time + relativedelta(minutes=duration_minutes)
    post = frontmatter.loads(location)
    sched = Schedule(
        accepted=True,
        category=category,
        date=start_time,
        end_date=end_time,
        layout="session-details",
        link=None,
        permalink=None,
        room=location,
        schedule_layout="full",
        sitemap=False,
        talk_slot="full",
        title="Break",
    )
    post.metadata.update(sched.dict(exclude_unset=True))
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
    location: str = "West Lawn",
    track: int = 1,
):
    category = "lunch"
    if start_time.weekday() == 6:
        raise ValueError("We don't have lightning talks on tutorial days")
    elif start_time.weekday() in {3, 4}:
        raise ValueError("We don't have lightning talks on sprint days")
    start_time = CONFERENCE_TZ.localize(start_time)
    end_time = start_time + relativedelta(minutes=duration_minutes)
    post = frontmatter.loads("")
    sched = Schedule(
        accepted=True,
        category=category,
        date=start_time,
        end_date=end_time,
        layout="session-details",
        link="/catering-menus/",
        room=location,
        sitemap=False,
        title="Early Lunch",
        track=f"t{track}",
    )
    post.metadata.update(sched.dict(exclude_unset=True))
    output_path = Path(
        f"_schedule/{category}/{sched.date.year}-{sched.date.month:0>2}-"
        f"{sched.date.day:0>2}-{sched.date.hour:0>2}-{sched.date.minute:0>2}-t{track}-{slugify(sched.title)}.md"
    )
    output_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Saved to {output_path}")


@app.command()
def generate_lunch(
    start_time: datetime,
    duration_minutes: int = 40,
    location: str = "West Lawn",
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
        link="/catering-menus/",
        room=location,
        sitemap=False,
        talk_slot="full",
        title="Lunch",
    )
    post.metadata.update(sched.dict(exclude_unset=True))
    output_path = Path(
        f"_schedule/{category}/{sched.date.year}-{sched.date.month:0>2}-"
        f"{sched.date.day:0>2}-{sched.date.hour:0>2}-{sched.date.minute:0>2}-{slugify(sched.title)}.md"
    )
    output_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Saved to {output_path}")


@app.command()
def generate_opening_remarks(
    start_time: datetime,
    duration_minutes: int = 15,
    speaker_name: str = "",
    location: str = "Salon A-E",
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
        speaker_post.metadata.update(speaker.dict(exclude_unset=True))
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
    post.metadata.update(sched.dict(exclude_unset=True))
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
    location: str = "Salon A-E",
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
        schedule_layout="full",
        sitemap=True,
        title="Lightning Talks",
        track=f"t{track}",
    )
    post.metadata.update(sched.dict(exclude_unset=True))
    output_path = Path(
        f"_schedule/{category}/{sched.date.year}-{sched.date.month:0>2}-"
        f"{sched.date.day:0>2}-{sched.date.hour:0>2}-{sched.date.minute:0>2}-t{track}-{slugify(sched.title)}.md"
    )
    output_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Saved to {output_path}")


@app.command()
def generate_keynote(
    start_time: datetime, duration_minutes: int = 45, location: str = "Salon A-E"
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
    post.metadata.update(sched.dict(exclude_unset=True))
    output_path = Path(
        f"_schedule/{category}/{sched.date.year}-{sched.date.month:0>2}-"
        f"{sched.date.day:0>2}-{sched.date.hour:0>2}-{sched.date.minute:0>2}-{slugify(sched.title)}.md"
    )
    output_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Saved to {output_path}")


@app.command()
def generate_shots(
    height: int = 512,
    quality: int = 80,
    width: int = 1024,
):
    presenters = Path("_presenters").glob("*.md")
    presenters = sorted(presenters, key=os.path.getmtime)
    for presenter in presenters:
        post = frontmatter.loads(presenter.read_text())
        print(f"- output: ./static/img/social/presenters/{post['slug']}.png")
        print(f"  height: {height}")
        print(f"  quality: {quality}")
        print(f"  width: {width}")
        print(f"  url: https://2022.djangocon.us{post['permalink']}")
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
                "display_email": "",
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
            "West Lawn",
            "Private Dining Room",
            "Santa Fe 3",
            "In front of Salon A",
        }:
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
def generate_2022_placeholders(event_date: datetime, create_keynotes: bool = False):
    tutorial_date = event_date
    talks_dates = [event_date + relativedelta(days=count) for count in [1, 2, 3]]
    sprints_dates = [event_date + relativedelta(days=count) for count in [4, 5]]
    break_times = [time(10, 40), time(15, 20)]
    talk_lunch_time = time(13, 20)
    tutorial_breakfast_time = time(8)
    talk_breakfast_times = [time(8), time(8, 30), time(8, 30)]
    lightning_talk_time = time(12, 30)
    tutorial_lunch_time = sprint_lunch_time = time(12, 30)
    keynote_time = time(9, 45)
    registration_open = time(8)
    generate_registration_desk(tutorial_date)
    generate_lactation_room(tutorial_date)
    generate_quiet_room(tutorial_date)
    generate_breakfast(datetime.combine(tutorial_date.date(), tutorial_breakfast_time))
    generate_lunch(
        datetime.combine(tutorial_date.date(), tutorial_lunch_time), duration_minutes=60
    )
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
            post.metadata.update(data.dict(exclude_unset=True))

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
                    image_url = f"https://2022.djangocon.us/presenters/{presenter_slug}"
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

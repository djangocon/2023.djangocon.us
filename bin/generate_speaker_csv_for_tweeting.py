import frontmatter
import typer

from io import StringIO
from csv import DictWriter
from datetime import datetime
from pathlib import Path
from pydantic import BaseModel, Field, ValidationError
from typing import List, Optional

app = typer.Typer()


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
    photo_url: Optional[str]
    role: Optional[str]
    title: Optional[str]
    twitter: Optional[str]
    website: Optional[str]
    website_text: str = "Apply here"


class Schedule(FrontmatterModel):
    abstract: Optional[str] = None
    accepted: bool = False
    category: Optional[str] = "talk"
    difficulty: Optional[str] = "All"
    image: Optional[str]
    layout: Optional[str] = "session-details"  # TODO: validate against _layouts/*.html
    presenter_slugs: Optional[List[str]] = None
    presenters: List[dict] = None  # TODO: break this into a sub-type
    published: bool = False
    room: Optional[str]
    schedule: Optional[str]
    schedule_layout: Optional[str] = Field(
        alias="schedule-layout"
    )  # TODO: Validate for breaks, lunch, etc
    show_video_urls: Optional[bool]
    slides_url: Optional[str]
    summary: Optional[str]
    end_date: Optional[datetime] = None
    tags: Optional[List[str]] = None
    talk_slot: Optional[str] = "full"
    track: Optional[str] = None
    video_url: Optional[str]


POST_TYPES = [
    {"path": "_posts", "class_name": Post},
    {"path": "_presenters", "class_name": Presenter},
    {"path": "_schedule/talks", "class_name": Schedule},
    {"path": "_schedule/tutorials", "class_name": Schedule},
    {"path": "_schedule/sprints", "class_name": Schedule},
]

REPO_ROOT = Path(__file__).parent.parent

@app.command()
def main(output_file: Path):
    """
    Loop through all talks and speakers and generate a CSV of data for the comms team to tweet using

    The schedule path should be something like "_schedule"
    """
    schedule_path = REPO_ROOT / '_schedule'
    speaker_path = REPO_ROOT / "_presenters"
    csv_data = []
    for talk in schedule_path.glob('*/*.md'):
        try:
            post = frontmatter.loads(talk.read_text())
            data = Schedule(**post.metadata)
            speakers: List[Presenter] = []
            if not data.presenter_slugs:
                continue
            for slug in data.presenter_slugs:
                speaker_file = speaker_path / f'{slug}.md'
                speaker_post = frontmatter.loads(speaker_file.read_text())
                speakers.append(Presenter(**speaker_post.metadata))
        except ValidationError as e:
                typer.secho(f"{talk}", fg="red")
                typer.echo(e.json())
                raise
        except Exception as e:
                typer.secho(f"{talk}::{e}", fg="red")
        else:
            twitter_handles = []
            for speaker in speakers:
                if speaker.twitter:
                    if not speaker.twitter.startswith("@"):
                        twitter_handles.append(f'@{speaker.twitter}')
                    else:
                        twitter_handles.append(speaker.twitter)
            csv_data.append({
                'title': data.title,
                'speakers': ', '.join(speaker.name for speaker in speakers),
                'twitter_handles': ', '.join(twitter_handles)
            })
            print(csv_data[-1])

    buffer = StringIO()
    writer = DictWriter(buffer, fieldnames=['title', 'speakers', 'twitter_handles'])
    writer.writeheader()
    writer.writerows(csv_data)
    output_file.write_text(buffer.getvalue())


if __name__ == "__main__":
    app()

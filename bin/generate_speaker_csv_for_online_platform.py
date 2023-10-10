import frontmatter
import shutil
import typer

from io import StringIO
from csv import DictWriter
from pathlib import Path
from pydantic import BaseModel, Field, ValidationError
from typing import List, Optional

from process import Presenter as BasePresenter, Schedule


class Presenter(BasePresenter):
    """Add the content field to be used for the presenter's bio"""

    content: Optional[str] = None


app = typer.Typer()


PRESENTER_TYP = [
    {"path": "_presenters", "class_name": Presenter},
]

REPO_ROOT = Path(__file__).parent.parent


def copy_files_to_folder(file_paths, destination_folder):
    # Create the destination folder if it doesn't exist
    destination_folder = Path(destination_folder)
    destination_folder.mkdir(parents=True, exist_ok=True)
    for file_path in file_paths:
        file_path = Path(file_path)
        destination_path = destination_folder / file_path.name
        shutil.copy2(file_path, destination_path)


@app.command()
def main(output_file: Path, output_images: Path):
    """
    Loop through all talks and speakers and generate a CSV of data for the online
    platform.

    The schedule path should be something like "_schedule"
    """
    schedule_path = REPO_ROOT / "_schedule"
    speaker_path = REPO_ROOT / "_presenters"
    csv_data = []
    image_paths = []
    for talk in schedule_path.glob("*/*.md"):
        try:
            post = frontmatter.loads(talk.read_text())
            data = Schedule(**post.metadata)
            speakers: List[Presenter] = []
            if not data.presenter_slugs:
                continue
            for slug in data.presenter_slugs:
                speaker_file = speaker_path / f"{slug}.md"
                speaker_post = frontmatter.loads(speaker_file.read_text())
                speakers.append(
                    Presenter(**speaker_post.metadata, content=speaker_post.content)
                )
        except ValidationError as e:
            typer.secho(f"{talk}", fg="red")
            typer.echo(e.json())
            # raise
        except Exception as e:
            typer.secho(f"{talk}::{e}", fg="red")
        else:
            for speaker in speakers:
                csv_data.append(
                    {
                        "attendee_name": speaker.name,
                        "attendee_email": None,
                        "bio": speaker.content,
                        "job_title": speaker.title,
                        "company_name": speaker.company,
                        "linkedin_url": None,
                        "github_url": f"https://github.com/{speaker.github}",
                        "twitter_url": f"https://twitter.com/{speaker.twitter}",
                        "youtube_url": None,
                        "mastodon_url": speaker.mastodon,
                        "display_email": None,
                        "website_url": speaker.website,
                    }
                )
                if speaker.photo_url:
                    image_paths.append("../" + speaker.photo_url[1:])

    buffer = StringIO()
    writer = DictWriter(
        buffer,
        fieldnames=[
            "attendee_name",
            "attendee_email",
            "bio",
            "job_title",
            "company_name",
            "linkedin_url",
            "github_url",
            "twitter_url",
            "youtube_url",
            "mastodon_url",
            "display_email",
            "website_url",
        ],
    )
    writer.writeheader()
    writer.writerows(csv_data)
    output_file.write_text(buffer.getvalue())
    copy_files_to_folder(image_paths, output_images)


if __name__ == "__main__":
    app()

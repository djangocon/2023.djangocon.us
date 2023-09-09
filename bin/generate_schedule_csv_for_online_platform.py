import frontmatter
import typer

from io import StringIO
from csv import DictWriter
from pathlib import Path
from pydantic import BaseModel, Field, ValidationError
from typing import Optional

from process import Schedule as BaseSchedule


class Schedule(BaseSchedule):
    """Add the content field to be used for the presenter's bio"""
    content: Optional[str] = None


app = typer.Typer()


REPO_ROOT = Path(__file__).parent.parent


@app.command()
def main(output_file: Path):
    """
    Loop through all talks and speakers and generate a CSV of data for the comms team to tweet using

    The schedule path should be something like "_schedule"
    """
    schedule_path = REPO_ROOT / "_schedule"
    csv_data = []
    for talk in schedule_path.glob("*/*.md"):
        try:
            post = frontmatter.loads(talk.read_text())
            data = Schedule(**post.metadata, content=post.content)
            if not data.presenter_slugs:
                continue
        except ValidationError as e:
            typer.secho(f"{talk}", fg="red")
            typer.echo(e.json())
            # raise
        except Exception as e:
            typer.secho(f"{talk}::{e}", fg="red")
        else:
            csv_data.append(
                {
                    "talk_title": data.title,
                    "track_name": data.track,
                    "description": data.abstract,
                    "presenter_emails": None,
                    "start": data.date,
                    "end": data.end_date,
                }
            )

    buffer = StringIO()
    writer = DictWriter(buffer, fieldnames=[
        "talk_title",
        "track_name",
        "description",
        "presenter_emails",
        "start",
        "end",
    ])
    writer.writeheader()
    writer.writerows(csv_data)
    output_file.write_text(buffer.getvalue())


if __name__ == "__main__":
    app()

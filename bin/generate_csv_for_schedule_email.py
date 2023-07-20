import csv
import json
import pathlib
import sys
from io import StringIO

import frontmatter

from process import Presenter, Schedule, CONFERENCE_TZ


def load_presenters() -> dict[str, Presenter]:
    presenters = pathlib.Path("../_presenters").glob("*.md")
    result = (
        Presenter(**frontmatter.loads(presenter.read_text()).metadata)
        for presenter in presenters
    )
    return {p.slug: p for p in result}


def load_schedules() -> list[Schedule]:
    schedules = pathlib.Path("../_schedule").glob("*/*.md")
    parsed = (
        Schedule(**frontmatter.loads(schedule.read_text()).metadata)
        for schedule in schedules
    )
    return (
        sched
        for sched in parsed
        if sched.category in {"talks", "tutorials"}
        and sched.presenter_slugs
        and "lightning talks" not in sched.title.casefold()
    )


def load_pretalx_speakers(json_file: pathlib.Path) -> dict[str, str]:
    data = json.loads(json_file.read_text())
    return {presenter["Name"]: presenter["E-Mail"] for presenter in data}


def generate_csv_row_dicts(
    talk: Schedule,
    presenters: dict[str, Presenter],
    emails: dict[str, str],
) -> list[dict[str, str]]:
    """Generate dictionaries suitable for use by a csv.DictWriter for a talk, 1 per speaker"""
    start = talk.date.astimezone(CONFERENCE_TZ)
    base_dict = {
        "time": start.strftime(f"%A, %B %-d at %-I:%M:%S %p %Z ({CONFERENCE_TZ})"),
    }
    # Hi [name], your [talk format] at [time]
    if talk.room == "Online talks":
        base_dict["talk_format"] = f"pre-recorded talk titled {talk.title} will air"
    elif talk.room.casefold().startswith("tutorial track"):
        base_dict["talk_format"] = f"online tutorial titled {talk.title} will start"
    else:
        base_dict["talk_format"] = f"in-person talk titled {talk.title} will start"
    return [
        {
            "name": presenters[slug].name,
            "email": emails.get(presenters[slug].name, ""),
            **base_dict,
        }
        for slug in talk.presenter_slugs
    ]


def main():
    schedule = load_schedules()
    presenters = load_presenters()
    emails = {}
    if len(sys.argv) > 1:
        print(sys.argv)
        emails = load_pretalx_speakers(pathlib.Path(sys.argv[-1]))
    buffer = StringIO()
    writer = csv.DictWriter(buffer, fieldnames=["name", "email", "time", "talk_format"])
    for talk in schedule:
        writer.writerows(
            generate_csv_row_dicts(
                talk=talk,
                presenters=presenters,
                emails=emails,
            )
        )
    pathlib.Path("../schedule_email_csv").write_text(buffer.getvalue())


if __name__ == "__main__":
    main()

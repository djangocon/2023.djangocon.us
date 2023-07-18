import pathlib
from typing import Any, Iterable

import frontmatter
import yaml

from process import Presenter, Schedule


HEADER = """---
author: DjangoCon US Organizers
category: General
date: 2023-07-10 12:00:00-04:00
image: /static/img/blog/speaking-2023.jpg
layout: post
post_photo_alt: Speaker addressing a crowd at DjangoCon US 2022 in San Diego
post_photo_url: /static/img/blog/speaking-2023.jpg
title: Announcing Our DjangoCon US 2023 Talks!
---

We are delighted to present our tutorial and talk lineup!

The final talk and tutorial schedule will be announced soon. If you haven’t purchased your ticket yet, [they’re still on sale]({{site.ticket_link}}).

Congratulations to the presenters of the tutorials and talks below!
"""

FOOTER = """
Congratulations to all our speakers!

If you’d like to check out these talks and more, [tickets are still on sale]({{site.ticket_link}}).
Tutorials (sold separately from conference registration) are $195 each, and we will have the schedule
for those up soon. We hope to see you in Durham!
"""

LINE_TEMPLATE = """- {talk["title"]} by {talk["presenters"][0]["name"]} {urls}"""

TUTORIAL_HEADER = """## Tutorials (Sunday, October 8)

_Tutorials will only be available online due to venue availabilty limitations._"""

TALK_HEADER = """## Talks (Monday, October 16 through Wednesday, October 18)

_All talks will be available live for those with online-only tickets. They will be posted to YouTube after the conference for free._
"""


def load_path(path: pathlib.Path) -> list[dict]:
    """Load the talks and return a list of dicts"""
    assert path.is_dir()
    return_data = []
    for yaml_file in sorted(path.glob("*.md")):
        with open(yaml_file, "r") as yaml_file_obj:
            yaml_data = yaml_file_obj.read()
        return_data.append(yaml.safe_load(yaml_data.split("---")[1]))
    return return_data


def generate_urls(presenter: Presenter) -> str:
    urls = []
    if presenter.github:
        urls.append(f"[github](https://github.com/{presenter.github})")
    if presenter.twitter:
        urls.append(f"[twitter](https://twitter.com/{presenter.twitter})")
    if presenter.mastodon:
        urls.append(f"[mastodon]({presenter.mastodon})")
    if presenter.website:
        urls.append(f"[website]({presenter.website})")
    if not urls:
        return ""
    return f'({", ".join(urls)})'


def format_talk(talk: dict[str, Any], presenters: Iterable[Presenter]) -> str:
    presenter_details = [
        f"{presenter.name} {generate_urls(presenter=presenter)}"
        for presenter in sorted(
            (p for p in presenters if p.slug in talk["presenter_slugs"]),
            key=lambda p: talk["presenter_slugs"].index(p.slug),
        )
    ]
    return f'{" and ".join(presenter_details)} - {talk["title"]}'


def parse_talks(talks: list[dict], presenters: dict[str, Presenter]) -> list[str]:
    return [
        f'- {format_talk(talk, presenters=(presenter for slug, presenter in presenters.items() if slug in talk.get("presenter_slugs", {})))}'
        for talk in sorted(
            talks,
            key=lambda t: presenters[t["presenter_slugs"][0]].name
            if "presenter_slugs" in t and t["presenter_slugs"]
            else "none",
        )
        if "Lightning Talks" not in talk["title"]
        and talk["category"] in {"talks", "tutorials"}
        and talk.get("presenter_slugs")
    ]


def load_presenters() -> dict[str, Presenter]:
    presenters = pathlib.Path("../_presenters").glob("*.md")
    result = (
        Presenter(**frontmatter.loads(presenter.read_text()).metadata)
        for presenter in presenters
    )
    return {p.slug: p for p in result}


def generate_template(talk_lines: list[str], tutorial_lines: list[str]) -> str:
    talks = "\n".join(talk_lines)
    tutorials = "\n".join(tutorial_lines)
    return f"{HEADER}\n\n{TUTORIAL_HEADER}\n\n{tutorials}\n\n{TALK_HEADER}\n\n{talks}\n\n{FOOTER}"


def main():
    path = pathlib.Path("../_schedule/talks")
    tutorial_path = pathlib.Path("../_schedule/tutorials")
    talks = load_path(path)
    tutorials = load_path(tutorial_path)
    presenters = load_presenters()
    talk_lines = parse_talks(talks, presenters=presenters)
    tutorial_lines = parse_talks(tutorials, presenters=presenters)
    blog_post = generate_template(talk_lines, tutorial_lines)
    print(blog_post)


if __name__ == "__main__":
    main()

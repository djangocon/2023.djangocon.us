---
abstract: "By now most of us have heard of, or used, Python type hints. Since being
  added to Python in 3.5, they've spread to every corner of the Python ecosystem.\r\n\r\nThese
  days many libraries are built from the ground up with type hints. But type hints
  don't have to live inline with the code, or even in the same repo. Anyone can write
  standalone type hints (also called stubs) for a framework like Django, and eventually
  people did.\r\n\r\nIn this talk I'll show you how to use a great set of type stubs
  for Django called [django-types](https://github.com/sbdchd/django-types), how to
  check your type hints with [pyright](https://github.com/microsoft/pyright), some
  of the challenges with adding type hints to Django code, and how to make type hints
  and type checking a real productivity boost."
accepted: true
category: talks
date: 2022-10-17 17:40:00-07:00
end_date: 2022-10-17 18:30:00-07:00
group: talks
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Fkyle-bebak%252F/opengraph/
layout: session-details
permalink: /talks/type-checking-your-django-code-with-and/
presenter_slugs:
- kyle-bebak
published: true
room: Online talks
schedule_layout: full
sitemap: true
slug: type-checking-your-django-code-with-django-types-and-pyright
summary: ''
tags: null
title: Type checking your Django code with django-types and Pyright
track: t2
---

Among the topics we'll cover are:

- A brief history of Django type stubs
- Which type stubs, and which type checker: `django-stubs` or `django-types`, `mypy` or `pyright`?
- Starting a project with type hints, or adding type hints to an existing project
- Where to focus: adding type hints to Django models and views
- Workarounds for when the type stubs aren't quite right
- Configuring `pyright` for type checking: running `pyright` on the host, in a container, on a CI server
- `pyright` and LSP clients: turning your text editor (Vim, Emacs, Sublime Text, VS Code, etc) into a full-fledged Python/Django IDE
- Type hints for documentation, code navigation, and refactoring

There will be live coding in the presentation. All code is open-sourced on GitHub, and links will be provided.

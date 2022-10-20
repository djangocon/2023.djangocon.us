---
abstract: "This talk will cover the latest updates in the Django documentation ecosystem:
  \r\n\r\n* Authoring: Markdown support in Sphinx with MyST\r\n* Design: Modern Sphinx
  themes like Furo\r\n* User Experience: Newly released Sphinx extensions that make
  your documentation more usable like sphinx-copybutton, sphinx-tabs, sphinx-hoverxref,
  and sphinx-design. \r\n* Deployment: Read the Docs now supporting pre-build compilation
  steps and additional documentation tools\r\n\r\nThis talk will give you an overview
  of the landscape in 2022, and show how easy it is to use these new projects with
  an existing documentation project."
accepted: true
category: talks
date: 2022-10-17 12:00:00-07:00
end_date: 2022-10-17 12:25:00-07:00
group: talks
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Feric-holscher%252F/opengraph/
layout: session-details
permalink: /talks/documenting-django-code-in-2022/
presenter_slugs:
- eric-holscher
published: true
room: Salon F-H
sitemap: true
slug: documenting-django-code-in-2022
summary: ''
tags: null
title: Documenting Django Code in 2022
track: t1
---

There have been a number of updates in the Python & Django documentation ecosystem, and this talk is an overview of those changes. The goal is to give everyone in attendance the tools that they need to help their organization or open source project build good documentation culture.

Authoring: Historically using Sphinx & reStructuredText has been the standard in the Django community, but not using Markdown has been a historical barrier to adoption, especially when adapting standards inside a company that aren't just using Python. With Sphinx having solid Markdown support, this worry has now been mostly removed, and enables the full power of Sphinx without having to learn a new markdown format.

Design: Similarly, the style of the documentation that is created has been a very important consideration for most projects and companies. With new Sphinx themes like the Furo theme, it's much easier to have a modern theme that is customizable enough to make it fit into the style of the rest of your site and brand.

User experience: Once you have the basic authoring and styles for your documentation, there are a number of ways to improve the user experience of the site. In this section we cover a few of the newest Sphinx extensions that provide a nicer UX for users:

* sphinx-copybotton: A simple extension that adds a copy button to every code block
* sphinx-tabs: An extension that lets you have nice toggable tabs in your docs, for example multiple language examples
* sphinx-hoverxref: An extension that gives you automatic tooltips on links to your documentation and other sphinx documentation via intersphinx
* sphinx-design: A toolkit that adds a large number of design elements easily to your docs (buttons, grids, cards, etc.)

Deployment: On the deployment side, there have also been a number of updates to Read the Docs, which is a common deployment platform. They now support pre-build steps that allow you to do a number of things before the building of your documentation. This talk will cover a few examples of valuable pre-build steps like generating API documentation from an external tool, doing a check in your git repo to see if you should even run the build, and a few other options.

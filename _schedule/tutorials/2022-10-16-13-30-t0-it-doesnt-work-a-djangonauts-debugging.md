---
abstract: This tutorial covers the tools and strategies a Django developer can use
  to resolve bugs. Debugging is an extremely useful skill for developers, but there
  aren’t many resources for improvement. This tutorial aims to serve as one of those
  resources. It’s best suited for beginners to web development and/or Django.
accepted: true
category: tutorials
date: 2022-10-16 13:30:00-07:00
difficulty: All
end_date: 2022-10-16 17:00:00-07:00
group: tutorials
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Ftim-schilling%252F/opengraph/
layout: session-details
permalink: /tutorials/it-doesnt-work-a-djangonauts-debugging/
presenter_slugs:
- tim-schilling
published: true
room: Balboa I & II
sitemap: true
slug: it-doesnt-work-a-djangonauts-debugging-tool-kit
summary: ''
tags: null
title: “It doesn’t work” - A Djangonaut’s debugging tool kit
track: t0
---

Debugging is the unsung skill for a developer. Eventually all developers encounter a 500 error, a blank page or perhaps the worst of them all, the phrase “it doesn’t work.” This tutorial will help prepare you for that inevitable bout with bewilderment by showcasing the tools and debugging strategies available to Django developers.

This tutorial is best suited for beginner developers, folks new to Django or new to web development. The topics this tutorial will cover are:

- Debugging
- Reading a stacktrace.
- Using the browser developer tools.
- Using the Django Debug Toolbar.
- Looking at Django source code to understand how it works.
- Profiling a method.
- Analyzing a SQL query

For the two labs in the tutorial,  starter code will be provided so you can follow along or go at your own pace. If you choose to implement this code you will need the following:

- Python 3.7+
- Foundational knowledge of Python
- Basic understanding of Django
  - Completing the Django Girls or standard Django tutorial should suffice.
- A desire to learn


Outline
--------

- Introduction
  - Who I am
  - Tutorial overview
- Reminder to be empathic and polite
- What is debugging
  - When something is weird, investigate!
  - Understand when to stop.
- How to debug a problem / Asking the right questions
  - What did you try, what did you expect and what did you see?
  - Double think: Everything works and anything could be broken.
- The tools at our disposal
  - Error messages and stacktraces
  - Debuggers and print statements.
  - The browser developer tools
    - Console
    - Networking panel
    - Debugger
  - Django Debug Toolbar
    - Analyzing a SQL query
    - Profiling code
  - The source code
- Lab 0 - Project setup
- Lab 1 - Getting acquainted with the basics
  - Rendering a page doesn’t work.
    - Terminal output
  - Submitting a form doesn’t work
    - Browser Developer Tools / Network panel
    - Terminal output
  - Content is rendering as expected
    - Debug code / print statement
- Lab 2 - Next level debugging
  - Pages are rendering slowly, help!
    - Django Debug Toolbar - History Panel
    - Django Debug Toolbar - SQL Panel
    - SQL Formatter - https://sqlformat.org/
    - SQL Explain formatter - https://explain.depesz.com/
  - The web app breaks after a while.
    - Django Debug Toolbar - Profiling panel
  - The counts on the page are wrong.
    - Django Debug Toolbar - SQL Panel
    - SQL Formatter - https://sqlformat.org/
  - Stale data is showing.
    - Django Debug Toolbar - Cache Panel
    - Django Debug Toolbar - SQL Panel
- Conclusion
  - Further resources
  - Gratitude

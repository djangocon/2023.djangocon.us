---
abstract: By an order of magnitude, Celery remains one of the most popular Django-adjacent
  packages for Python. In this talk, I'll explore what continues to make Celery a
  go-to solution for background and scheduled jobs with Django, how to integrate Celery
  with a Django project, and some common patterns to use (and avoid!) when writing
  tasks with Celery.
accepted: true
category: talks
date: 2023-10-18 14:05:00-04:00
end_date: 2023-10-18 14:50:00-04:00
group: talks
image: https://2023.djangocon.us//static/img/social/presenters/tobias-mcnulty.png
layout: session-details
permalink: /talks/how-to-schedule-tasks-with-celery-and-django/
presenter_slugs:
- tobias-mcnulty
published: true
room: Junior Ballroom
schedule_layout: full
sitemap: true
slug: how-to-schedule-tasks-with-celery-and-django
summary: ''
tags:
- celery
title: How to Schedule Tasks with Celery and Django
track: t0
---

Celery is a distributed system for message processing in Python first released in 2009, not long after Django itself. With over 20,000 stars on GitHub, it remains one of the most popular Django-adjacent Python packages. Similarly, my colleague Dan's post on the Caktus blog, "How to Use Celery for Scheduling Tasks," is by an order of magnitude one of the most popular pieces of content on our site.

In this talk, I'll explore what continues to make Celery a popular choice for message processing and background jobs, including:
- The fundamentals of integrating Celery with a Django project
- What is a message broker and how to choose one
- What is a result backend and how to choose one
- How to run tasks on pre-defined schedules, via settings and/or the database
- How to break apart long-running tasks to maximize scalability
- Other common patterns and anti-patterns when writing tasks with Celery

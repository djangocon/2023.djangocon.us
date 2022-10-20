---
abstract: Not many people would think that using Django and a PostgreSQL database
  is a good idea for working with time series data and all its complexity in terms
  of volume and structure. However, we found out that even the most unusual choices
  can work, if you have a good reason for doing so. In this talk, we will share our
  successful experience developing a system with time series data requirements using
  Django and Timescale, a PostgreSQL based time series database, and the reasons that
  led us to use this stack. Find out the challenges we faced, pros and cons, and how
  Django saved the day.
accepted: true
category: talks
date: 2022-10-17 10:40:00-07:00
end_date: 2022-10-17 11:05:00-07:00
group: talks
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Fjoaquin-scocozza%252F/opengraph/
layout: session-details
permalink: /talks/working-with-time-series-data-using-and/
presenter_slugs:
- joaquin-scocozza
published: true
room: Online talks
schedule_layout: full
sitemap: true
slug: working-with-time-series-data-using-django-and-timescale
summary: ''
tags: null
talk_slot: full
title: Working with time series data using Django and Timescale
track: t2
---

For the last two years we’ve been working on a software development project based on displaying and processing telemetry data for multiple services. The product is a cloud-based, heavy-data application that provides users with key insights after processing a variety of metrics.

In the app's first development phase, we explored the best options for gathering and processing high volume streams of data and presenting it in an efficient way. We finally opted for using Timescale, a relational PostgreSQL based time series database that combined with Django was a successful choice for this project.

In this talk we want to share the experience of creating a time series system based on Django and Timescale, our learning points and challenges faced in the process.

We’ll cover:
- Business case context
- Basics of time series data and different alternatives we evaluated
- Quick overview of the solution, the Timescale database and how we managed to still leverage the power of Django
- Review several examples of what went smoothly and what didn't

This is an entry level talk for people interested in time series, even those who are unfamiliar with the concept, but want to learn. Basic Django and database knowledge is recommended but all people are welcome.

---
abstract: After deploying a project in production and generating new data, it's common
  that some response time issues arise. We don't always code having this in mind since
  probably at the beginning of a project there won't be enough data to cause this
  concern. Therefore, it's important not only to take this into account when developing
  in order to prevent performance issues in the future, but also to be able to debug
  and detect the cause after they happen. After working in several projects over the
  years, I’ve found some good practices, tips and tricks that have helped me to prevent
  high response times or decrease them, making the process more efficient, and improving
  the overall user experience and satisfaction.
accepted: true
category: talks
date: 2022-10-18 17:10:00-07:00
end_date: 2022-10-18 17:35:00-07:00
group: talks
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Fcarmela-beiro%252F/opengraph/
layout: session-details
permalink: /talks/tips-and-tricks-for-optimizing-django/
presenter_slugs:
- carmela-beiro
published: true
room: Salon A-E
sitemap: true
slug: tips-and-tricks-for-optimizing-django-response-times
summary: ''
tags: null
title: Tips and tricks for optimizing Django response times
track: t0
---

Over the last 6 years I've been working on many different projects that needed to manage great amounts of data. I've stumbled upon some common response time issues that could arise while developing production web applications in Django.

This talk will present some of these real use cases and how to prevent and solve them using best practices, most of them proposed by Django in their documentation, and different debug tools. The idea is also to stand out the importance of understanding which queries are performed under the hood in Django in order to determine what's the best solution in case response times need to be improved.

We’ll cover:
What could improve or prevent high response times in the Django admin. How to determine what's the cause if this happens.
What could improve or prevent high response times with DRF. How to determine what's the cause if this happens.
Understanding which queries are performed by Django and what we could do to improve them, such as checking the execution plan, which indexes are being used and their order, restricting the attributes in select clauses, filters and joins.
What other options there are if no improvements could be done (cache, pre-calculated tables with Celery, materialized views)

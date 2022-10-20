---
abstract: A common Django project bad practice is serializing ORM objects without
  properly loading relationships, causing N+1 query issues. Django don´t have an obvious
  way to avoid that, but some techniques and libs can help to produce better code
  without too many unnecessary queries.
accepted: true
category: talks
date: 2022-10-17 17:10:00-07:00
end_date: 2022-10-17 17:35:00-07:00
group: talks
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Fiuri-de-silvio%252F/opengraph/
layout: session-details
permalink: /talks/django-from-queryset-to-serialization/
presenter_slugs:
- iuri-de-silvio
published: true
room: Salon F-H
sitemap: true
slug: django-from-queryset-to-serialization
summary: ''
tags: null
title: Django from queryset to serialization
track: t1
---

Django don´t have an obvious way to avoid N+1 queries during objects serialization and it is easy to miss the right way in large projects.

This talk aims to show how I joined a project with a rudimentary serialization solution and improved it to be able to handle serializations without causing N+1 queries by accident, using django-qserializer (I'm the author).

I will discuss other solutions, how to do that with plain Django, how DRF do the same thing, how other libs can contribute or make your code worse.

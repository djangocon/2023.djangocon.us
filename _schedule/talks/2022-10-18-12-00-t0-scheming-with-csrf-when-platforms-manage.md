---
abstract: When you choose to host your Django sites on managed platforms, you delegate
  responsibility to those platforms. But when you also can't control what those platforms
  do, you might find yourself with things that don't work as expected. What follows
  is a warning to why being explicit in Django's settings is a very good idea.
accepted: true
category: talks
date: 2022-10-18 12:00:00-07:00
difficulty: All
end_date: 2022-10-18 12:25:00-07:00
group: talks
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Fkatie-mclaughlin%252F/opengraph/
layout: session-details
permalink: /talks/scheming-with-csrf-when-platforms-manage/
presenter_slugs:
- katie-mclaughlin
published: true
room: Salon A-E
sitemap: true
slug: scheming-with-csrf-when-platforms-manage-to-break-things
summary: ''
tags: null
title: 'Scheming with CSRF: When platforms manage to break things.'
track: t0
---

When Django 4.0 was released, a small change to the `CSRF_TRUSTED_ORIGINS` was in the change notes: the scheme must now be provided.

This change would cause any deployment on Cloud Run to fail. But not App Engine. 🤔

Follow along as we dive into the complexities that Django saves you from, what managed services handle for you (that you have no control over), and what happens when these things don't work as expected. We'll dive into PEP-3333, CGI specifications, WSGI implementations, and what happens when the standards don't actually tell you what to do.

Attendees will come away with an understanding of how important it is to set `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` to prevent all this in the first place.

A note on Audience Level: This talk is written to be accessible to beginners, while tackling advanced topics. This speaker is happy to help any attendee lost with the content after the talk in the conference hallway ✨

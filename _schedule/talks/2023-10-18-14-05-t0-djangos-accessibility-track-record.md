---
abstract: Ever wonder how accessible Django is? Sites built with Django, the admin,
  the docs. Let’s find out! We will leverage the HTTP Archive’s websites technology
  dataset to quantitatively review common accessibility issues on Django projects
  – and then we’ll dive into Django’s implementation choices to understand the results.
accepted: true
category: talks
date: 2023-10-18 14:05:00-04:00
end_date: 2023-10-18 14:50:00-04:00
layout: session-details
permalink: /talks/djangos-accessibility-track-record/
presenter_slugs:
- thibaud-colas
published: true
room: Junior Ballroom
sitemap: true
slug: djangos-accessibility-track-record
summary: ''
tags:
- accessibility
title: Django’s accessibility track record
track: t0
---

There are great accessibility guidelines out there. Great tools to evaluate individual websites too. Between the big picture and individual projects, we can look at what Django specifically does – and what changes at the level of the framework could improve large swaths of the Django web.

We will start by looking at the HTTP Archive’s dataset of 8M websites, 30’000 of which are built with Django. We can identify which issues are common compared to other frameworks, and review specific issues in more depth to understand where they might appear in Django.

We can then look into the implementation details to understand exactly how users of assistive technology would benefit or be harmed by Django’s design choices. And accordingly highlight the correct approach.

A practical example of this where we can go very deep is Django’s implementation of HTML forms. Django’s default markup previously left a lot to be desired, and it being “the default” led to a lot of websites shipping with accessibility issues. This has been improved from release to release, addressing basic issues and introducing more advanced patterns like ARIA attributes for errors.
---
abstract: This talk explores the potential of Django custom model managers and querysets,
  guiding beginners through their utilization for more efficient and maintainable
  development, showcasing practical patterns along the way.
accepted: true
category: talks
date: 2023-10-16 14:55:00-04:00
end_date: 2023-10-16 15:20:00-04:00
group: talks
image: https://2023.djangocon.us//static/img/social/presenters/josh-thomas.png
layout: session-details
permalink: /talks/custom-model-managers-and-querysets-graduating-from-django-beginner-to-orm-master/
presenter_slugs:
- josh-thomas
published: true
room: Grand Ballroom III
sitemap: true
slides_url: /static/slides/joshthomas-custommanagers.pdf
slug: custom-model-managers-and-querysets-graduating-from-django-beginner-to-orm-master
summary: ''
tags:
- ORM
title: 'Custom Model Managers and QuerySets: Graduating from Django Beginner to ORM
  Master'
track: t1
---

In my journey as a Django developer, I know the moment when I did not consider myself a beginner anymore: when I started leveraging Django custom model managers and querysets. Initially they can seem intimidating and potentially complex. However, they can help make your use of the ORM more efficient, allow you to encapsulate complex and repetitive queries, and provide an API surface area that makes it easier to introduce certain changes to Model fields and queries, among other benefits.

Outline:
- A general overview of Model Managers/QuerySets
- How to define a custom Manager/QuerySet and either override the built-in one Django provides or add additional ones.
- The difference between a custom model manager and queryset and where you may use one over the other
- A few useful patterns I keep reaching for:
	- `.for_user(user)` - filtering a queryset to include only the objects a user has access to
	- `.with_complicated_legacy_raw_SQL_query()` - when migrating a legacy system to Django, I used this extensively before translating the original raw SQL into Django ORM
	- `.exclude_some_condition(condition)` - excluding certain objects based on a condition

This talk is aimed at beginners and intermediates with a basic familiarity with the Django ORM. Towards the end of the talk, we will dip our toes in more advanced parts of the ORM (annotations/aggregations, subqueries, etc.) to show the potential of custom Managers/QuerySets.

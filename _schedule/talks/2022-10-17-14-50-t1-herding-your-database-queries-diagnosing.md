---
abstract: Django ORM makes it easy to persist and retrieve DB information.  However
  it is also easy to accidentally introduce a lot of DB queries in your request flow
  if you are not careful.  This talk goes over some scenarios where this can take
  place, and demonstrates approaches to finding, eliminating and ultimately protecting
  against these excessive and/or expensive queries.
accepted: true
category: talks
date: 2022-10-17 14:50:00-07:00
end_date: 2022-10-17 15:15:00-07:00
group: talks
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Filya-bass%252F/opengraph/
layout: session-details
permalink: /talks/herding-your-database-queries-diagnosing/
presenter_slugs:
- ilya-bass
published: true
room: Salon F-H
sitemap: true
slug: herding-your-database-queries-diagnosing-improving-and-guarding-performance-of-db-interactions-in-your-django-apps
summary: ''
tags: null
title: 'Herding your database queries: diagnosing, improving and guarding performance
  of DB interactions in your Django apps'
track: t1
---

Django ORM allows to seamlessly represent DB data as instances of Python classes (models).  This includes relationships between objects, such that when a model (A) has a foreign key relationship (let’s say field name ‘related_b’) to another model (B), all you need to do to navigate from an instance of A (a) to the related instance of B (b) is “a.related_b”.  By default, this will fetch “b” from the database, which is both amazingly convenient and also terrifying.  I say terrifying with some degree of jest, but also plenty of seriousness that will be appreciated by those of us who know what it’s like to deal with a production database that is melting under load.  While Django provides ways of dealing with this, such as select_related and prefetch_related, as well as cached properties, the need for intervention is not easy to realize until the said database starts melting.  In an application that has any degree of complexity, it would be advisable to guard against excessive queries at some granular level, such as, for example, a request.  The talk will cover:

* How to Implement a middleware class that can accumulate and report on different sources of DB queries encountered during a request
* A few non-trivial examples of excessive queries and showing various practical approaches to eliminating them
* How to write tests that guard against increases in number of DB queries
* How to ensure that all your endpoints are covered in the above tests

If you are familiar with basic workings of Django models and how they are persisted in relational databases, this talk will give some ideas for how to optimize your database interactions, especially in more complex and high-scale applications.

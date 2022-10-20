---
abstract: "Django's migration system is one of its greatest strengths as a framework.
  \ It can automatically generate migrations based on your changes to your models
  and can detect which migrations need to be applied to a database.  But, as the size
  of your development team and user base scale, there are pitfalls that you need to
  be aware of.  Not all migrations can be safely reversed, and trying to rewind bad
  migrations on a production database can cause a data disaster.  Not all migrations
  can be safely deployed without downtime, and trying to deploy them can give your
  users and your engineers a wall of errors.\r\n\r\nThis talk will cover the following:\r\n1.
  How to manage migrations across multiple code branches\r\n2. Reversible migrations:
  how to write migrations so that they can be safely undone\r\n3. Backwards compatible
  migrations: which migrations can be run as part of a deploy without causing downtime
  or errors\r\n4. Handling failed migrations as part of a deployment"
accepted: true
category: talks
date: 2022-10-18 12:00:00-07:00
difficulty: Intermediate
end_date: 2022-10-18 12:25:00-07:00
group: talks
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Fbenjamin-zags-zagorsky%252F/opengraph/
layout: session-details
permalink: /talks/django-migrations-pitfalls-and-solutions/
presenter_slugs:
- benjamin-zags-zagorsky
published: true
room: Salon F-H
sitemap: true
slug: django-migrations-pitfalls-and-solutions
summary: ''
tags: null
title: 'Django Migrations: Pitfalls and Solutions'
track: t1
---

Django's migration system is one of its greatest strengths as a framework.  It can automatically generate migrations based on your changes to your models and can detect which migrations need to be applied to a database.  But, as the size of your development team and user base scale, there are pitfalls that you need to be aware of.  Not all migrations can be safely reversed, and trying to rewind bad migrations on a production database can cause a data disaster.  Not all migrations can be safely deployed without downtime, and trying to deploy them can give your users and your engineers a wall of errors.

This talk will cover the following:
1. How to manage migrations across multiple code branches
2. Reversible migrations: how to write migrations so that they can be safely undone
3. Backwards compatible migrations: which migrations can be run as part of a deploy without causing downtime or errors
4. Handling failed migrations as part of a deployment

This talk assumes familiarity with the management commands `makemigrations` and `migrate`.  It's likely to be most helpful for people working on a Django project where there are many branches being worked on simultaneously or for those working on applications with moderate to high uptime requirements.

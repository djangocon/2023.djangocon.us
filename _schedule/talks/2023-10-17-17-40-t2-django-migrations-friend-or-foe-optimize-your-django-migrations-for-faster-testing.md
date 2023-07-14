---
abstract: "Django migrations are a great tool, but after years of changes in a project
  they can become very numerous, slowing down tests.\r\nIs it possible to optimize
  them?"
accepted: true
category: talks
date: 2023-10-17 17:40:00-04:00
end_date: 2023-10-17 18:05:00-04:00
layout: session-details
permalink: /talks/django-migrations-friend-or-foe-optimize-your-django-migrations-for-faster-testing/
presenter_slugs:
- denny-biasiolli
published: true
room: Online talks
schedule_layout: full
sitemap: true
slug: django-migrations-friend-or-foe-optimize-your-django-migrations-for-faster-testing
summary: ''
tags:
- ORM
title: Django migrations, friend or foe? Optimize your Django migrations for faster
  testing
track: t2
---

Django migrations are a great tool for keeping track of changes you made to your models over time.
After years of changes in a project they can become very numerous and you may notice that it takes a long time to create the test database.

`squashmigrations` can help you reduce an existing set of many migrations down to one (or sometimes a few), which still represent the same changes.
However it has some limitations, and it could work in a way you don't need.

Let's inspect this command and the alternative of creating migrations "from scratch" in an existing project for improving your tests speed.

- inspecting django migration commands
    - `makemigrations`
    - `migrate`
    - `showmigrations`
    - `sqlmigrate`
- creating a sample project with multiple migrations
- analyzing test performances
- inspecting the `squashmigrations` command
- squashing migrations in the sample project and comparing performances
- not enough? Let's try an "exotic/drastic" way to squash our migrations
- comparing performances of the "exotic/drastic" solution

The key point of this talk is to speed up django testing in projects with many migrations
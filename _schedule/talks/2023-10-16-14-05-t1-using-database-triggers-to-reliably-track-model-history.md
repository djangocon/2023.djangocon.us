---
abstract: "Tracking model history is an essential aspect of many problems encountered
  in web applications, from simple audit trails to preserving values of fields during
  state transitions. There are a wide array of approaches to do this with Django apps,
  almost all of which are subject to performance penalties, require unstructured JSON
  fields to track history, or can easily be bypassed accidentally in application code.\r\n\r\nIn
  this talk, we show a new way to to track history in Django with database triggers.
  We specifically focus on Postgres databases using the [django-pghistory](https://github.com/opus10/django-pghistory)
  app. We discuss the benefits of using database triggers for history in the context
  of simplicity, performance, and reliability. We also discuss the benefits of using
  structured history tables and how this can allow engineers to solve complex history-related
  modeling problems.\r\n\r\nAttendees of this talk will be exposed to a totally new
  way to think about history tracking in their application, along with an understanding
  of the pros and cons of using database triggers to track history in practice."
accepted: true
category: talks
date: 2023-10-16 14:05:00-04:00
end_date: 2023-10-16 14:50:00-04:00
group: talks
layout: session-details
permalink: /talks/using-database-triggers-to-reliably-track-model-history/
presenter_slugs:
- wes-kendall
- maxwell-muoto
published: true
room: Grand Ballroom III
sitemap: true
slug: using-database-triggers-to-reliably-track-model-history
summary: ''
tags:
- postgres
title: Using database triggers to reliably track model history
track: t1
---

Tracking model history is an essential aspect of many web applications, as it allows developers to monitor and analyze changes made to the data over time. In Django, the majority of history tracking apps are implemented in Python at the application level, making a tamper-proof audit trail nearly impossible to implement accurately.

By utilizing triggers, developers can automate the process of capturing and storing changes made to models within the database itself. This approach offers several benefits. Firstly, it reduces the complexity of manually implementing and maintaining history tracking functionality in Django code. Triggers provide a centralized and standardized mechanism to monitor modifications, ensuring consistency and accuracy across multiple models and applications.

Secondly, triggers enable the tracking of changes at a database level, resulting in improved performance and reduced overhead. Since the triggers are executed within the database engine, they can efficiently capture modifications without requiring additional round-trips between the application and the database. This efficiency is particularly valuable when dealing with large datasets or frequently updated models.

Furthermore, triggers provide a reliable and tamper-proof history of model changes. By operating at the database level, triggers can capture modifications regardless of whether they originate from Django or other external sources. This capability ensures that all changes to the model are consistently tracked, eliminating the risk of data loss or incomplete history.

Additionally, utilizing triggers for model history tracking in Django promotes data integrity and compliance with auditing requirements. By maintaining a comprehensive record of changes, developers can trace back and analyze the evolution of data, helping to identify potential issues, perform forensic analysis, or meet regulatory obligations.

In this talk, we show how to implement history tracking using [django-pghistory](hub.com/opus10/django-pghistory), an app that uses Postgres triggers to track historical changes. We discuss the philosophy of django-pghistory and how it models historical changes so that engineers can use structured history tables that mirror tracked models. We show how users can attach free-form context from the application to group together changes, forming a more coherent audit trail. We also discuss several other application-specific examples of using django-pghistory in practice, for example, using conditional history triggers to track and snapshot specific events.

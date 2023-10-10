---
abstract: A case study of a single-application ETL system to scrape and enrich complex
  nested data and then expose it via GraphQL and Discord. It will dive into how to
  use these various async-based libraries together in a small footprint app.
accepted: true
category: talks
date: 2023-10-17 12:00:00-04:00
end_date: 2023-10-17 12:25:00-04:00
group: talks
image: https://2023.djangocon.us//static/img/social/presenters/noah-kantrowitz.png
layout: session-details
permalink: /talks/swiss-army-django-small-footprint-etl/
presenter_slugs:
- noah-kantrowitz
published: true
room: Junior Ballroom
sitemap: true
slug: swiss-army-django-small-footprint-etl
summary: ''
tags:
- how I used Django
title: 'Swiss Army Django: Small Footprint ETL'
track: t0
---

ETL systems have become commonplace in our world, from tiny personal web scrapers to complex distributed data pipelines. With Django offering a fully async API, new possibilities have opened to simplify the many different microservices into a single Python application that hosts the scrapers, query systems, and administrative interface all in one box. With this comes simplified code and deployment, and many other benefits.

This talk will cover a case study in building this kind of all-in-one ETL system, the components used, and how they all fit together. This includes both API and web scrapers, GraphQL for querying and streaming, and a Discord interface for notifications and control.

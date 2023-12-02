---
abstract: As the most popular and mature solution for asynchronous task queues in
  Python’s ecosystem, Celery is an essential tool for Django projects. But running
  Celery tasks with high reliability is a challenge. The settings are tricky, tasks
  can be lost in multiple ways, task code has opaque limitations, proper monitoring
  isn’t trivial, and more. In this talk, we’ll share what we learned to be necessary
  for running Celery reliably after years of running it in production.
accepted: true
category: talks
date: 2023-10-17 10:40:00-04:00
end_date: 2023-10-17 11:05:00-04:00
group: talks
image: https://2023.djangocon.us//static/img/social/presenters/flavio-juvenal.png
layout: session-details
permalink: /talks/mixing-reliability-with-celery-for-delicious-async-tasks/
presenter_slugs:
- flavio-juvenal
published: true
room: Online talks
schedule_layout: full
sitemap: true
slug: mixing-reliability-with-celery-for-delicious-async-tasks
summary: ''
tags:
- celery
title: Mixing reliability with Celery for delicious async tasks
track: t2
video_url: https://youtu.be/VuONiF99Oqc
---

Celery is essential for asynchronous processing in Django backends. In multiple Django projects, we used far beyond the use case of sending emails without blocking HTTP responses. Celery helped us aggregate data, fill caches, run ETL workflows, parallelize heavy workloads, sync with external services, set up periodic background jobs, and much more.

But as with any distributed system, running Celery reliably in production is challenging. Due to the many issues we’ve seen on Celery, we considered many times replacing it with other task queues. But we never found another library with the features Celery offers. So we had to learn to work around its shortcomings and pitfalls. After years of running it in multiple Django projects, we faced and solved several reliability problems. We remediated concurrency hazards. We dealt with lost tasks in multiple edges of the architecture. We read tons of docs, articles, and issues to properly tweak settings. We fixed weird serialization bugs after version upgrades. We found what kind of monitoring really needed.

In this talk, you will learn how to configure, use and monitor Celery successfully in production. Celery performs well in simple contexts, because of that it might induce a false sense of safety that can be misleading as usage picks up and flows become more complex. Understanding the many ways it can fail as projects grow will help developers to prepare in advance.

Outline:
- [2 minutes] Common concurrency issues
- [5 minutes] Recommended settings
  - What Broker and Result Backend to use
  - What happens when using others
  - Serialization: pickle or not?
  - Thresholds and limits
  - Timeouts and expires
- [5 minutes] How tasks can be lost and how Celery (tries) to solve that
  - ACKS_LATE, idempotency, and retries
  - Why that task again? Visibility timeout, prefetches, and automatic redelivering
  - Dead worker process, lost task
  - You need atomicity too
- [5 minutes] Don’t use Celery canvas workflows: you need DB-level state
- [2 minutes] Multiple queues and workers will save you from complex incidents
- [2 minutes] The only monitoring you can trust: probe tasks
- [2 minutes] Graceful shutdowns: Celery and Continuous Deployment
- [3 minutes] Questions

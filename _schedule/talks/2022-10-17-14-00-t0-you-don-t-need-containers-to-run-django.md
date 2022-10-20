---
abstract: For those not using containers, uWSGI has been the de-facto way of deploying
  Django to production. But now that project is no longer being developed and it can
  be hard to choose an alternative. In this talk we'll take a look at stablished solutions
  such as gunicorn and cherrypy and compare them to newer async implementations such
  as Daphene and Uvicorn. We'll score each of them on how they handle production workloads
  and discuss best practices to achieve a reliable site.
accepted: true
category: talks
date: 2022-10-17 14:00:00-07:00
end_date: 2022-10-17 14:45:00-07:00
group: talks
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Feduardo-felipe-castegnaro%252F/opengraph/
layout: session-details
permalink: /talks/you-don-t-need-containers-to-run-django/
presenter_slugs:
- eduardo-felipe-castegnaro
published: true
room: Salon A-E
sitemap: true
slug: you-don-t-need-containers-to-run-django-in-production
summary: ''
tags: null
title: You Don't Need Containers to Run Django in Production
track: t0
---

While containers have a lot of advantages they can also bring a lot complexity into deploying Django to production, but you don't need them to have a stable, reliable site.

To get started, you need to choose a web server. In this talk we'll compare synchronous servers, like gunicorn and cherrypy, to asynchronous servers such as Daphne and Uvicorn. We'll look at benchmarks, how they are configured, how they are managed and what they do to avoid resource contention and improve reliability of your site.

We'll also take a look at how your server of choice can be restarted during deploy by using supervisord or systemd.

By the end you'll be more informed on how to deploy your code, the complexities associated with it and have a set of best practices that can be used to bootstrap your production environment.

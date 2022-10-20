---
abstract: At JPL, we’re building a web hosting platform powered by Django and Wagtail
  CMS.  A key architectural goal was to reduce operational costs and overhead by running
  a large number of sites using a shared codebase, hosted together within an autoscaling
  container cluster.  An additional goal was to give each site its own database and
  file storage location.  To meet these goals, we’ve built a management layer that
  runs alongside Django to handle networking, cluster configuration, state synchronization
  and health monitoring.
accepted: true
category: talks
date: 2022-10-18 15:50:00-07:00
end_date: 2022-10-18 16:35:00-07:00
group: talks
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Faddison-hardy%252F/opengraph/
layout: session-details
permalink: /talks/a-management-layer-for-scalable-django/
presenter_slugs:
- addison-hardy
- james-ray
published: true
room: Salon F-H
sitemap: true
slug: a-management-layer-for-scalable-multitenant-django
summary: ''
tags: null
title: A Management Layer for Scalable, Multitenant Django
track: t1
---

## Networking

To handle networking within the containers, the management layer integrates with Nginx and uWSGI.  During container startup, and when network configuration changes, the management layer generates Nginx site files and uWSGI config files on the fly based on current platform state.

We are running uWSGI in “emperor” mode, which allows us to create (and configure) separate uWSGI workers for each site.  Within the uWSGI config files, we are setting an environment variable based on each site’s unique identifier.  As uWSGI initializes each worker, it also initializes Django.  We use that environment variable in our Django settings files to configure the database, cache key prefix, AWS S3 bucket (for file storage) and other site-specific settings.  This allows all platform sites to share a single codebase, but keeps each site’s data completely separate.

## Cluster Configuration

All cluster configuration data is stored in a Postgres database, which serves as the source of truth for platform state.  The management layer exposes an API and web dashboard for querying the current platform state and making configuration changes.  Administrators can perform actions like creating new sites, associating hostnames with sites, managing user permissions and monitoring platform health.

## State Synchronization

Within each container, the management layer listens for state change events on a Postgres notification channel.  The change events are sent as JSON, and include the event type, timestamp and any associated metadata.  When a configuration change is made via the API, the container that handled the API request will broadcasts that change event to the entire cluster.  The management layer also performs regular integrity checks to ensure the state of each container matches the state of the platform.

## Health Monitoring

The management layer performs automated healthchecks within each container by sending an internal request to each hostname associated with a site on the platform.  The response codes and latency for those requests are then stored and used to power monitoring tools and alerts via the API and web dashboard.

If an issue is detected, the management layer will attempt to resolve the issue by querying the latest platform state, and regenerating configuration files.  If the issue persists, the container will be automatically replaced within the cluster.

---
abstract: "Django is an excellent framework for constructing web sites.\r\n\r\nWebsockets
  provide the ability to create and manage persistent connections, allowing for \r\nbidirectional
  communication without the overhead created by HTTP.\r\n\r\nHTMX greatly reduces
  the need for writing JavaScript in the browser to support websocket\r\nconnections.\r\n\r\nRunning
  all these also requires components such as redis, nginx, and daphne, which need\r\ntheir
  own configuration.\r\n\r\nThis tutorial will be a guided walk-through of all these
  components together, showing one\r\nway to build and deploy a web site.\r\n\r\nYou
  will see an example of:\r\n - Using Django to create the basic page that gets everything
  started,\r\n - Creating Consumers in Channels for handling the server-side of the
  websocket connections\r\n - Creating background worker processes that interact with
  those consumers\r\n - Using htmx, with the websocket plugin and a custom extension,
  to enhance the client\r\n - All the other components configured to support this
  environment (nginx, uwsgi, daphne, redis)\r\n\r\nParticipants should have some knowledge
  of Django - at least to the level of having completed\r\neither the official Django
  Tutorial or the Django Girls tutorial. They should also have a\r\nbasic understanding
  of HTML and CSS. Knowledge of asynchronous programming, or the python\r\nasyncio
  library, is _not_ required."
accepted: true
category: tutorials
date: 2022-10-16 13:30:00-07:00
difficulty: All
end_date: 2022-10-16 17:00:00-07:00
group: tutorials
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Fken-whitesell%252F/opengraph/
layout: session-details
permalink: /tutorials/a-detailed-review-for-using-django-and/
presenter_slugs:
- ken-whitesell
published: true
room: Cabrillo 1
sitemap: true
slug: a-detailed-review-for-using-django-channels-and-htmx-to-create-dynamic-and-interactive-web-sites
summary: ''
tags: null
title: A detailed review for using Django, Channels, and HTMX to create dynamic and
  interactive web sites
track: t2
---

The tutorial will cover an overview of the architecture, along with a line-by-line review
of all the components involved in the system.

This review includes:

Django:
- Authentication
- Models
- View
- Template
- HTMX initialization

Channels:
- Consumer
  - Key methods (connect, disconnect, receive)
  - incoming messages
    - "dispatch" method
  - Library: django-channels-presence
  - Channel layer
  - async vs sync

Workers:
- Channel layer
- async vs sync
- message format
  - "dispatch" method

Redis:
- Channels
  - Channel names
  - Read / Write
  - Group send

HTMX:
- Basic HTMX
- The ws extension
- The transformResponse function

nginx:
- Segregating HTTP from websocket connections
- Handling static files

uwsgi:
- Running Django application

daphne:
- Running Channels consumers
- Running Workers

Bringing it all together:
- Running it natively
- Building docker containers

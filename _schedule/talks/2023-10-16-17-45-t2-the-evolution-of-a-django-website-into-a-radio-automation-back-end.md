---
abstract: What started as a Website to show the schedule of a free radio, has resurfaced
  as the back-end of a radio automation software suite that provides the schedule
  through a REST API.
accepted: true
category: talks
date: 2023-10-16 17:45:00-04:00
end_date: 2023-10-16 18:10:00-04:00
group: talks
layout: session-details
permalink: /talks/the-evolution-of-a-django-website-into-a-radio-automation-back-end/
presenter_slugs:
- ernesto-rico-schmidt
published: true
room: Online talks
schedule_layout: full
sitemap: true
slug: the-evolution-of-a-django-website-into-a-radio-automation-back-end
summary: ''
tags:
- wagtail/butter/other CMS
- how I used Django
title: The evolution of a Django Website into a radio automation back-end
track: t2
---

There are both commercial and open-source solutions for radio automation, but the requirements of free radios are very different from commercial radios, specially regarding the scheduling options and the end-user interface.

With AURA, we are developing a free and open-source software automation suite for free radios.

At the core of AURA is `steering`, a Django application that serves as the "source of truth" for the schedule and acts as an OpenID Connect provider for the components of the suite.

First, I'll describe the situation free radios in Austria face: The commercial radio automation software available, and the only supposedly free solution, currently in use at some radio stations in Austria, has showed that a (Java) monolith and a single developer are not the best approach for the rather complex and varied schedule and play-out requirements of free radios.

This moved a group of free radios in Austria to start the development of a free and open-source software suite of radio management, program scheduling and play-out automation software: AURA.

Second, I'll give a short overview of the distributed architecture and the components of AURA, and focus on how it distinguishes from the monoliths that are currently in use at some of the free radios in Austria.

Then, I'll explain the data models behind the Django application, with a special focus on the recurrence rules and the schedule conflict resolution, the most complex parts of `steering`.

I will focus on the architecture decisions we took during the planing and development, and how the open-source development is a better and more sustainable approach to a common problem for free radio stations.

I will show small snippets of code of the most interesting parts of the Django application, and explain the rationale behind them, specially the recurrence rules, and the schedule conflict resolution.

In this case Django is not providing a Web application or a Web site but it is providing a REST API and acts as the back-end of a software suite, and serves as the "source of truth" for the scheduling and the play-out automation of the radio station.

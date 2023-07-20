---
abstract: "Django and Vue both have unique front-end strengths. Django’s context-driven
  template views offer rapid development of pages directly from back-end model content.
  Vue’s modern reactive components provide powerful tools for building complex UIs
  within the rich Javascript ecosystem.\r\n\r\nDo we have to choose one or the other,
  or is there a way to combine both front-end frameworks in a single project without
  compromising their strengths? \r\n\r\nThis talk will demonstrate step-by-step how
  to intermingle Vue SFCs within Django Templates, such that targeted areas can be
  enriched with Vue while retaining the flexibility and convenience of Django Templates
  in the remainder."
accepted: true
category: talks
date: 2023-10-16 12:00:00-04:00
end_date: 2023-10-16 12:25:00-04:00
group: talks
layout: session-details
permalink: /talks/vue-django-combining-django-templates-and-vue-single-file-components-without-compromise/
presenter_slugs:
- mike-hoolehan
published: true
room: Grand Ballroom II-III
sitemap: true
slug: vue-django-combining-django-templates-and-vue-single-file-components-without-compromise
summary: ''
tags:
- JS/HTMX/misc frontend tech
title: 'Vue + Django: Combining Django Templates and Vue Single File Components without
  compromise'
track: t1
---

Typical solutions to integrating Django and Vue forgo much of the strengths of one in lieu of the other. For example, a common approach is to use Django Rest Framework as back-end while writing the entire front-end in Vue, making it difficult to utilize Django templates in places it could be expedient. A second approach is to use Vue within Django templates using browser <script> includes, but then lost is the ability to use Vue's Single File Components (SFCs).

This talk will explain a unique approach to intermingling Django Templates and Vue that preserves the strengths of both.

Starting with a minimal Django project, I will demonstrate the addition of Vue components into a final working app that combines both front-end frameworks. Topics such as information passing from Django to Vue, maintaining Vuex state between pages, and deferred loading of Vue resources will also be explored.

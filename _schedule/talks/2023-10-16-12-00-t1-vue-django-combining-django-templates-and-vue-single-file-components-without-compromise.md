---
abstract: "Django and Vue both have unique front-end strengths. Django’s context-driven
  template views offer rapid development directly from back-end model content. 
  Vue’s modern reactive components provide powerful tools for building complex UIs 
  within the rich JavaScript ecosystem.\r\n\r\nDo we have to choose one or the other, 
  or is there a way to combine both front-end frameworks without compromising their 
  strengths?\r\n\r\nLearn how to inject Vue SFCs directly into Django Templates, with 
  no need for REST APIs, such that targeted areas can be enriched with Vue while 
  retaining the flexibility and convenience of Django Templates in the remainder."
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
room: Grand Ballroom III
sitemap: true
slug: vue-django-combining-django-templates-and-vue-single-file-components-without-compromise
summary: ''
tags:
- JS/HTMX/misc frontend tech
title: 'Vue + Django: Combining Django Templates and Vue Single File Components without
  compromise'
track: t1
---

There is a common misconception that Django's template-based views and "heavyweight" JavaScript frameworks such as Vue cannot co-exist without considerable compromise; that we are forced to choose between the two. For example, we may use Django Rest Framework as back-end while writing a JavaScript SPA front-end, making it difficult to utilize Django templates where convenient. Or we may use JavaScript frameworks from Django templates using browser `<script>` includes, but then lost is much of the tooling, testability, and ecosystem of the modern build-based JavaScript framework. This dilemma leads many Django developers to choose lighter-weight no-build Javascript frameworks as a means to add dynamic user experience.

However, there is no need for compromise. **Vue can, surprisingly easily, be mingled directly into Django templates**, allowing us to mix-and-match these two front-end technologies as we wish, without sacrificing the strengths of either.

This talk will explain a unique new approach to integrating Vue 3 within Django Templates. Starting with a minimal Django project, I will demonstrate the addition of Vue components into a templated app, harmoniously combining both front-end frameworks. We will explore topics such as information passing from Django to Vue, Vite configuration and tooling, persistent state management with Pinia, and resources to jumpstart your own project.

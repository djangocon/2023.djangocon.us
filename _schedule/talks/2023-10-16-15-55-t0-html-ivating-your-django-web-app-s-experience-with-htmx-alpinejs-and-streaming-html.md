---
abstract: "Many Python developers who build web applications rely on JavaScript-heavy
  Single-Page Applications (SPAs) to achieve dynamic user experiences. However, these
  SPAs have challenges, including increased complexity, slower load times, and complicated
  build pipelines. But an alternative approach exists that delivers an exceptional
  user experience without the drawbacks of SPAs!\r\n\r\nThis talk will explore how
  you can leverage the power of HTMX, AlpineJS, and Django's ability to stream HTML
  to create web applications with a significantly improved user experience. We will
  delve into the principles and techniques that make this approach a compelling alternative
  to SPAs."
accepted: true
category: talks
date: 2023-10-16 15:55:00-04:00
end_date: 2023-10-16 16:40:00-04:00
layout: session-details
permalink: /talks/html-ivating-your-django-web-app-s-experience-with-htmx-alpinejs-and-streaming-html/
presenter_slugs:
- chris-may
published: true
room: Junior Ballroom
sitemap: true
slug: html-ivating-your-django-web-app-s-experience-with-htmx-alpinejs-and-streaming-html
summary: ''
tags:
- JS/HTMX/misc frontend tech
title: HTML-ivating your Django web app's experience with HTMX, AlpineJS, and streaming
  HTML.
track: t0
---

The rise of SPAs has brought many benefits, but it has also introduced complexity and performance overheads that can be overwhelming. As Django developers, we know the power and elegance of the Django framework, and we believe it can deliver a better user experience without the need for heavy JavaScript frameworks.

In this talk, we will dive into the concepts of HTMX, a lightweight library that allows us to update parts of the HTML directly from the server, and AlpineJS, a minimal JavaScript framework for enhancing interactivity. We will explore how these tools can be integrated seamlessly with Django to create modern web apps with enhanced user experiences.

Additionally, we'll see how Django 4.2's `StreamingHttpResponse` lays the foundation for better experiences of views that require slow queries, microservice calls, or APIs.

### Key points:
1. Understanding the limitations of JavaScript-heavy SPAs:
   - Increased complexity and maintenance overhead
   - Slower initial load times and performance implications
2. Introduction to HTMX: Learn how to leverage HTMX to update parts of the HTML directly from the server, eliminating the need for heavy JavaScript frameworks.
3. Enhancing Interactivity with AlpineJS: Discover how to add lightweight JavaScript interactions to your Django app using AlpineJS, improving the user experience without sacrificing simplicity.
4. Streaming HTML for Performance: Explore how to stream HTML to deliver a fast and interactive experience, even in slow network connections or large datasets.
5. Case Study: Dive into a real-world example of a web app that leveraged streaming HTML to achieve impressive user experiences.

By the end of this talk, attendees will be inspired to leverage HTMX, AlpineJS, and streaming HTML to create modern web applications with exceptional user experiences. They will gain insights into the benefits and trade-offs of this approach compared to JavaScript-heavy SPAs and leave with practical tips and best practices for implementing these techniques in their Django projects.
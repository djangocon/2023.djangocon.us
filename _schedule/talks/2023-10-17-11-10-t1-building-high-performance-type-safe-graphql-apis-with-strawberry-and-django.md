---
abstract: "GraphQL has gained popularity for its ability to offer more flexibility
  and performance over traditional REST APIs. Strawberry is a new and fast-growing
  GraphQL library for Python, inspired by dataclasses functionality, that offers a
  modern and intuitive API for building GraphQL APIs using type hints.\r\n\r\nIn this
  talk, we will explore the basics of building a GraphQL API with Strawberry and how
  it can be integrated with Django in a performant and type-safe way, by generating
  its types and resolvers directly from Django models. We will also compare and contrast
  the benefits and drawbacks of GraphQL versus REST APIs, including how GraphQL can
  help improve frontend development workflows.\r\n\r\nAttendees will come away with
  an understanding of how Strawberry can help simplify the process of building and
  maintaining GraphQL APIs, and how to use its powerful features to optimize for performance,
  safety, and flexibility, while also covering its drawbacks and how to avoid some
  common issues."
accepted: true
category: talks
date: 2023-10-17 11:10:00-04:00
end_date: 2023-10-17 11:55:00-04:00
group: talks
layout: session-details
permalink: /talks/building-high-performance-type-safe-graphql-apis-with-strawberry-and-django/
presenter_slugs:
- thiago-bellini-ribeiro
published: true
room: Grand Ballroom III
sitemap: true
slug: building-high-performance-type-safe-graphql-apis-with-strawberry-and-django
summary: ''
tags:
- APIs
- optimization/speed
title: Building high-performance, type-safe GraphQL APIs with Strawberry and Django
track: t1
---

In this talk, we will explore the world of GraphQL APIs with Strawberry, a new Python library that makes it easy to create GraphQL APIs with Django. We will dive into what GraphQL is, how it compares to traditional RESTful APIs, and what makes Strawberry stand out from other Python GraphQL libraries.

One of the biggest challenges in GraphQL API development is the N+1 problem, where queries can become exponentially slow as more data is requested. We will discuss how data loaders can help solve this problem, and go in-depth on how to use them in Strawberry. In this topic we will also cover how the Strawberry Django integration leverages query introspection and user defined hints to automatically call .only(…)/.select_related(…)/.prefetch_related(…) on querysets, making your queries more efficient and avoiding common pitfalls. This is especially important in high-traffic, production environments where performance is critical.

Finally, we will showcase some of the benefits of using Strawberry and Django together, including a type-safe approach to API development and streamlined code maintenance. By the end of this talk, you'll have the knowledge and tools you need to create high-performance GraphQL APIs with Strawberry and Django.

It will be presented in the following order:

- Intro
- Quick overview of what a GraphQL API looks like and its advantages
- Writing general GraphQL APIs using Strawberry
- Integrating the Django ORM with Strawberry
- Some common pitfalls, with emphasis on the N+1 problem
- GraphQL tools to avoid those pitfalls and how to use them with Strawberry
- How the Strawberry Django integration uses introspection to automatically overcome those pitfalls and also improve performance when executing Django querysets

---
abstract: This workshop will teach you how to create a production ready GraphQL API
  using Python and Strawberry. We will be using using Django as our framework of choice,
  but most of the concept will be applicable to other frameworks too.
accepted: true
category: tutorials
date: 2022-10-16 09:00:00-07:00
difficulty: All
end_date: 2022-10-16 12:30:00-07:00
group: tutorials
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Fpatrick-arminio%252F/opengraph/
layout: session-details
permalink: /tutorials/build-a-production-ready-graphql-api/
presenter_slugs:
- patrick-arminio
published: true
room: Sierra 5
sitemap: true
slug: build-a-production-ready-graphql-api-using-python
summary: ''
tags: null
title: Build a production ready GraphQL API using Python
track: t1
---

Agenda of the worshop

- Workshop introduction
	- The introduction will explain the goal of the workshop and make sure everyone is ready to start
- Intro to type hints
	- Before looking at what GraphQL is, we'll do a short introduction on type hints in Python, since we'll be using the a lot during the workshop.
- Introduction to GraphQL
	- Here we'll be looking at what GraphQL is, how it works and why it has been created
- Our first GraphQL API
	- Here we'll get our hands dirty by creating our first GraphQL API using Strawberry. We'll also take time to see how to configure Strawberry with Django.
- Let's test our API
	- I'm a big fan of TDD, so before continuing with our workshop we'll quickly see how to test our GraphQL API using pytest.
- Schema design
	- In this section we'll spend time taking a look at how to design a GraphQL schema. We'll also understand the difference between queries and mutations.
- Authentication
	- In this section we'll implement authentication to our GraphQL API. We'll discuss session based auth vs JWT authentication.
- **Bonus**
   - Performance / Monitoring / Observability
	- In this section we'll discuss how we can add observability/monitoring to our APIs and make sure we can keep our API performant over time.
	- We'll also see how we can use dataloaders to make our queries efficient. We'll also talk about other potential performance improvements (SQL optimisation, Static Queries and more)

	- Integration with React
		- In this section we'll see how we can use GraphQL with a frontend framework like React.
	- Subscriptions
		- In this section we'll see what subscriptions are in GraphQL and how you can leverage them to build realtime APIs.

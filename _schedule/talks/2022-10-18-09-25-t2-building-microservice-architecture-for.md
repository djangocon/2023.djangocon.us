---
abstract:
  Armed with knowledge of Django development, we delve into the different
  types of microservices and the high-level design principles we should follow when
  we design them
accepted: true
category: talks
date: 2022-10-18 09:25:00-07:00
end_date: 2022-10-18 09:55:00-07:00
group: talks
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Fsyed-ansab-waqar-gillani%252F/opengraph/
layout: session-details
permalink: /talks/building-microservice-architecture-for/
presenter_slugs:
  - syed-ansab-waqar-gillani
  - syed-muhammad-dawoud-sheraz-ali
published: true
room: Online talks
schedule_layout: full
sitemap: true
slug: building-microservice-architecture-for-scale-with-django
summary: ""
tags: null
title: Building Microservice Architecture for scale with Django
track: t2
---

Monoliths are codebases that grew too big and too difficult to reason about by a single developer or even a team of developers, their complexity has reached a point where changing even just a couple of lines of code can have unintended and unknown consequences in other parts. A microservice is a single purpose software application that resides somewhere on the web, is a small-scale codebase and can be reasoned about easily.

Working with Open EdX projects, there are over 100+ applications and over 0.7 million lines of code, a single change in a monolith could have had disastrous results.The entire Open EdX codebase is divided into a combination of over 14 services with various application functionalities.

Topics to cover:

- Understanding the Monolith and Microservice architecture - What are the difference between monolith and microservice architectures and what architectures are used when? (Sample: https://articles.microservices.com/monolithic-vs-microservices-architecture-5c4848858f59)

- Anatomy of a Django Microservice - Explaining different types of microservices and how they are built using Django, how they communicate with each other and how we avoid data duplication across all services to reduce maintenance. (Sample: https://medium.com/@akiva10b/microservice-infrastructure-with-django-8f985e86a057)

- Design Principles with SOLID Building Blocks - Understanding the components of SOLID Design principles and how they are implemented with Django implementations (https://medium.com/@vubon.roy/solid-principles-with-python-examples-10e1f3d91259)

- Design Principles with 12 Factors Apps - Understanding the components of 12 factor app Design principles and how they are implemented with Django implementations. (https://12factor.net/)

Target Audience:

This talk is directed towards Developers using Python or Django to engineer microservice architecture, primarily those who aspire to scale their products without establishing any vulnerable dependency inside the architecture. The talk focuses on various problems that may arise while engineering a microservice architecture and what is the best way to address these problems.

By the end of the talk, the audience should understand the benefits and limitations of microservice built architecture in general and the Django implementations of services in particular. They should also know where to get additional information on setting up their own architecture.

Additional notes:

Me and Dawoud Sheraz, both, are part of the development team at Arbisoft/edX, where we have engineered microservice architecture in the Open edX project to reduce dependency and coupling.

Inspiration:

Designing Microservices with Django - Akos Hochrein

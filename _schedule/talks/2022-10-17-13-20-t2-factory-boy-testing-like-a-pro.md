---
abstract: How to test complex objects using the library factory_boy. The lessons I’ve
  learned using the tool in a Django monolith containing 230+ tables and 75k+ relevant
  lines of code for over 3 years.
accepted: true
category: talks
date: 2022-10-17 13:20:00-07:00
difficulty: Intermediate
end_date: 2022-10-17 14:05:00-07:00
group: talks
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Fcamila-maia%252F/opengraph/
layout: session-details
permalink: /talks/factory-boy-testing-like-a-pro/
presenter_slugs:
- camila-maia
published: true
room: Online talks
schedule_layout: full
sitemap: true
slug: factory-boy-testing-like-a-pro
summary: ''
tags: null
title: 'factory_boy: testing like a pro'
track: t2
---

After working using the factory_boy library for over 3 years on a Django monolith containing +230 tables, +2200 relevant files, and +75k relevant lines of code, I've collected and listed all my biggest learnings.

In this presentation, I try to share some of my experiences, showing what I consider to be good practices in using factory_boy in complex systems.

Content:

* A short introduction of myself
* factory_boy: what is it? - the definition and the purpose of the tool
* Example application - a quick overview of the application we will use to demonstrate the best practices
* How to install factory_boy
* How to use factory_boy
* Best Practices:
1. Factories must represent their models
2. Do not rely on defaults from factories
3. Factories must have only the required data. if the field is nullable -> under traits.
4. Build over create
5. If FK is in the table -> SubFactory. If FK is in the other table -> RelatedFactory + trait
6. Fixtures only to wrap factories in the test file
7. Avoid using fixtures on shared files like conftest
* Wrapping up

Repository: https://github.com/camilamaia/factory-boy-best-practices

---
abstract: Proxy models are part of Django’s inheritance styles, but how to they work,
  how are they different from other inheritance styles that Django provide, practically
  where can they be applied in real world scenarios. Using simple code snippets and
  practical examples lets explore proxy models.
accepted: true
category: talks
date: 2023-10-18 14:55:00-04:00
end_date: 2023-10-18 15:20:00-04:00
group: talks
layout: session-details
permalink: /talks/one-database-table-one-model-many-behaviours-proxy-model/
presenter_slugs:
- ronald-maravanyika
published: true
room: Junior Ballroom
schedule_layout: full
sitemap: true
slug: one-database-table-one-model-many-behaviours-proxy-model
summary: ''
tags:
- ORM
title: 'One database table, one model, many behaviours: Proxy model'
track: t0
---

At times, when inheriting a model one doesn’t want to create a table in the database, you maybe looking to change just the pythonic behaviour of the data without necessarily creating a new table, for example you might be looking  to ordering the data while maintain the original model data structure, this is where Django proxy models come in play, this talk will highlight, what are proxy models, how they are created using the model’s Meta class and how they can make your life easier as a developer.

Furthermore, confusion around which restrictions are imposed on base class by Django when using proxy models will be brought to rest during this talk. The possibilities of proxy models inheriting  multiple abstract models will be covered in this talk. Proxy mode manipulation of the Model manager and when to manipulate the Manager will also be part of the talk’s package. Being fairly similar to unmanaged models, the talk will highlight the most common differences  and when to use each of them.

Reading through the Django proxy model, or even reading through the first paragraph above makes one say “cool stuff !!!” and then the next thing you forget about it. This is because finding the practical application of proxy models in real world scenarios is difficult. This talk will showcase practical aspects of using proxy model through the use on an abstract base class, equipping developers mind with an image or the possibilities of this proxy model.

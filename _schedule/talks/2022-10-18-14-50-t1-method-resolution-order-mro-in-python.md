---
abstract: "It’s time to stop succumbing with common pitfalls when deciding the order
  of precedence of methods in multiple inheritances. This diamond problem is solved
  using DLR algo in Python2 and C3 linearization in Python3.\r\n\r\nWe’ll learn about
  MRO (Method Resolution order) which defines the class search path in Python."
accepted: true
category: talks
date: 2022-10-18 14:50:00-07:00
end_date: 2022-10-18 15:15:00-07:00
group: talks
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Fsanyam-khurana%252F/opengraph/
layout: session-details
permalink: /talks/method-resolution-order-mro-in-python/
presenter_slugs:
- sanyam-khurana
published: true
room: Salon F-H
sitemap: true
slug: method-resolution-order-mro-in-python
summary: ''
tags: null
title: Method Resolution Order (MRO) in Python
track: t1
---

Imagine implementing inheritance in a programming language. At first, it looks like all the methods and attributes will be inherited by the child class. While it works for the majority of scenarios, as soon as we hit multiple-inheritance, deciding what method/attribute will take precedence, becomes a  daunting task.

This is also known as the diamond problem. While some languages use an algorithm such as right-first-depth-first search to solve this, Python 2 used Depth-first from Left to Right (DLR) and Python3 uses C3 Linearization Algorithm. Getting hold of this information will help you not succumbing to the common pitfalls with the arrangement of name lookups in a class hierarchy.

MRO (Method Resolution Order) defines the class search path for linearizing the class ancestor tree. We’ll also have a look at how C3 algorithm is monotonic as it guarantees that base class declaration is preserved and subclasses appear before base classes. We’ll further explore MRO using `__bases__`, `__base__`, `__mro__` magic methods.

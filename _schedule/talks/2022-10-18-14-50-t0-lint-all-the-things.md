---
abstract: Code that’s uniform is easier to read, write, and debug, but writing down
  your standards and conventions in a README that no one reads isn’t enough. The explosion
  of CI and linter tools allow you to no only document your standards and conventions,
  but make sure people actually adhere to them.
accepted: true
category: talks
date: 2022-10-18 14:50:00-07:00
end_date: 2022-10-18 15:15:00-07:00
group: talks
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Fluke-lee%252F/opengraph/
layout: session-details
permalink: /talks/lint-all-the-things/
presenter_slugs:
- luke-lee
published: true
room: Salon A-E
sitemap: true
slug: lint-all-the-things
summary: ''
tags: null
title: Lint All the Things!
track: t0
---

Many teams document the conventions for their projects. However, documentation gets out of date, forgotten, or sometimes ignored. Simple documentation requires team members to constantly remember all the ‘rules’ for your project. You can better enforce those rules and free up your team members to think about harder problems using linting tools like flake8, import linter, and pre-commit.

These tools provide tons of useful stuff out of the box, but you can push them so much further with customization. This allows your project to formally document conventions, but also enforce them automatically on every commit, merge, and build. This can make code reviews faster and more focused on the problems your code is meant to solve.

This talk will introduce tools like flake8, import linter, and pre-commit along with some of their built-in functionality. Then, we’ll briefly explore some ways to customize them to fit your projects’ specific needs. Some examples of custom linter rules we’ll tour are:

- Code formatted automatically and uniformly
- Code doesn’t import across architecture layers violating separation of concerns
- Common conventions are used
- Common anti-patterns are avoided
- Specific layers are fully tested
- Proper git commit message formatting
- Merge commits don’t exist in topic/feature branches

Finally, we’ll discuss ways to use those custom linter rules on every commit, merge, and build with continuous integration or git hooks.

By the end of the talk, you’ll see several real-world linter rules used on Kraken, which is a large Django-based project used to supply green energy to millions of users across the world. In addition, expect no shortage of ideas for your own projects along the way!

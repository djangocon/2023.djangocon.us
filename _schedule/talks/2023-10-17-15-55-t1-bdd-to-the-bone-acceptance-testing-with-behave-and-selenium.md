---
abstract: "Have you ever felt that unit tests just weren’t enough?   It just feels
  like there’s always something wrong when your customers start to use your application.
  \ All your unit tests pass, so where does the problem stem from?  It turns out we
  need to start thinking like *users*, not *developers* .\r\n\r\nIn this talk, you'll
  get a look at the the `behave` library to explore executable specifications and
  \ behavior driven development. You'll learn effective practices around specification
  testing and how to integrate that into your workflow. You'll also learn how to drive
  automated testing of a Django App through the web browser, via the _selenium_ library."
accepted: true
category: talks
date: 2023-10-17 15:55:00-04:00
end_date: 2023-10-17 16:20:00-04:00
layout: session-details
permalink: /talks/bdd-to-the-bone-acceptance-testing-with-behave-and-selenium/
presenter_slugs:
- pat-viafore
published: true
room: Grand Ballroom II-III
sitemap: true
slug: bdd-to-the-bone-acceptance-testing-with-behave-and-selenium
summary: ''
tags:
- testing
title: 'BDD To The Bone: Acceptance Testing with Behave and Selenium'
track: t1
---

It's easy to get caught up in testing metrics. We all do it. We aim for 100% code coverage, try to hit all branches, write good integration tests, and all the other good developer practices. These all indicate that we are building our product right, but are we building the right product?

There's a different mentality when it comes to answering this question. We, as developers, can't just make sure that the code does what *we* want it to do. We need to think about what our users want. We need good requirements and specifications and we need to make sure that we are covering user acceptance testing. 

In this talk, we're going to discuss why requirements are hard to get right, and how we can solve some of those problems. We'll introduce strong traceabilty with executable specifications and then talk about how to tie that directly to your Python tests. 

We'll discuss behavior driven development, primarily with the `behave` library. After we cover the basics, we'll look at a Django application and talk about the challenges in performing user acceptance testing on websites. We'll use the `selenium` library to drive website interactions through Python, and tie it all together with acceptance tests. 

This talk assumes basic knowledge of testing practices, Python, and HTML/JavaScript.
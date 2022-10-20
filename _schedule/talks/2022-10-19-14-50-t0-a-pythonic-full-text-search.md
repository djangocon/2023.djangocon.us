---
abstract: Keeping in mind the pythonic principle that _"simple is better than complex"_
  we'll see how to implement *full-text search* in a web service using only latest
  versions of *Django* and *PostgreSQL* and we'll analyze the advantages compared
  to more complex solutions based on external services.
accepted: true
category: talks
date: 2022-10-19 14:50:00-07:00
end_date: 2022-10-19 15:15:00-07:00
group: talks
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Fpaolo-melchiorre%252F/opengraph/
layout: session-details
permalink: /talks/a-pythonic-full-text-search/
presenter_slugs:
- paolo-melchiorre
published: true
room: Salon A-E
schedule_layout: full
sitemap: true
slug: a-pythonic-full-text-search
summary: ''
tags: null
title: A pythonic full-text search
track: t0
---

A **full-text search** on a website is the best way to make its **contents** easily accessible to **users** because it returns better results and is in fact used in *online search engines* or *social networks*.

The implementation of full-text search can be complex and many adopt the strategy of using **dedicated search engines** in addition to the **database**, but in most cases this strategy turns out to be a big problem of **architecture** and **performance**.

In this talk we'll see a **pythonic** way to implement full-text search on a website using only Django and PostgreSQL, taking advantage of all the **innovations** introduced in latest years, and we'll analyze the **problems** of using additional search engines with examples deriving from my experience (e.g. *djangopoject.com* or *readthedocs.org*).

Through this talk you can learn how to add a full-text search on your **website**, if it's based on **Django** and **PostgreSQL**, or you can learn how to update the search function of your website if you use other search engines.

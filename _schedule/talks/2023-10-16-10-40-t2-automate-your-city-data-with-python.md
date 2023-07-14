---
abstract: Every week, in every city, hundreds if not thousands of decisions, big and
  small, are being made about the places where we all live. Most of the time, these
  decisions are hidden behind old systems, arcane websites, or poorly formatted PDFs.
  With the power of Datasette, Python data tooling, and Github actions, you can quickly
  set up a low-or-no-cost city data pipeline, and help us all better understand the
  decisions being made where we live.
accepted: true
category: talks
date: 2023-10-16 10:40:00-04:00
end_date: 2023-10-16 11:05:00-04:00
group: talks
layout: session-details
permalink: /talks/automate-your-city-data-with-python/
presenter_slugs:
- philip-james
published: true
room: Online talks
schedule_layout: full
sitemap: true
slug: automate-your-city-data-with-python
summary: ''
tags:
- how I used Django
title: Automate Your City Data with Python
track: t2
---

It is very hard for the average resident of a U.S. or Canadian city to know what’s going on with their civic government. It’s even harder for them to get any sort of historical context on why things are the way they are. Let’s take my hometown, the City of Alameda. Six months ago if you wanted to know which city meetings had discussed rent control, your options were:

- Have a friend who is a constant watcher of Alameda meetings / the #alamtg hashtag and could tell you
- Go through every meeting minutes on the Alameda Legistar and hope you figured it out

This is pretty common across a lot of civic government. I don’t think municipalities are willfully trying to hide this information from residents, and I don’t think it’s ineptitude. I think most cities, even the large ones, are understaffed, and without a concerted push it’s hard to make “visibility of city documents” a priority.

What if we could have SQL-backed full text search of city meeting minutes? Well, thanks to Datasette, Python, AWS, and some Github actions, we can! 

Here's the process:

1. Figure out where official city minutes are hosted
2. Write a script to fetch and format those city minutes
3. Upload all the fetched minutes to AWS S3
4. Run s3-ocr across the corpus of minutes
5. Download the ocr’d pages into a sqlite DB
6. Deploy a datasette instance to fly.io with that sqlite DB.
7. Post to twitter so people know about it.

In this talk, I will cover this whole process in detail, including how to automate it, so that you can apply this process to your city, county, state, school board, or any other civic government you're interested in!

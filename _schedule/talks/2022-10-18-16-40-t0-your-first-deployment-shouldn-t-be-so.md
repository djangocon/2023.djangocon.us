---
abstract: The `django-simple-deploy` project is a standalone management command that
  automatically configures a Django project for hosting on a number of different platforms.
  It greatly simplifies the process of making your first Django deployment. This talk
  will describe how the project works on the surface and under the hood, and will
  include a live demo.
accepted: true
category: talks
date: 2022-10-18 16:40:00-07:00
end_date: 2022-10-18 17:05:00-07:00
group: talks
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Feric-matthes%252F/opengraph/
layout: session-details
permalink: /talks/your-first-deployment-shouldn-t-be-so/
presenter_slugs:
- eric-matthes
published: true
room: Salon A-E
sitemap: true
slug: your-first-deployment-shouldn-t-be-so-hard
summary: ''
tags: null
title: Your First Deployment Shouldn't Be So Hard!
track: t0
---

About This Talk
===

When people are first learning Django, they do a lot of work to reach the point where they have a project that works locally. Then they think, "All right! Now I can deploy my project and everyone can see how wonderful it is!"

What comes next? They have to identify a hosting service, hopefully find docs that are up to date enough to use, make a bunch of changes to their project, hope for no typos or misunderstandings, and maybe they'll end up with a deployed project. Many projects languish on local systems because of how difficult it can be to carry out your first deployment.

I've written `django-simple-deploy` as a standalone management command that inspects a local project, and automatically configures the project for deployment to the specified hosting platform. If a project is being tracked with Git and has a requirements file, and you have an account on a hosting platform with their CLI installed, you can deploy in a few steps without ever visiting the hosting platform's docs.

This talk will cover:
- A live demo.
- Why the Django community needs a project like `django-simple-deploy`.
- What does this mean for people who have just finished the Polls tutorial?
- What does this mean for hosting companies?
- How it works: What changes does `django-simple-deploy` make to your project?
- How it works: How does `django-simple-deploy` make these changes?
- Deep dive: How do you test a Django project that acts on another Django project, and targets a remote platform?
- Open questions (my open questions)
- Contributing

This talk is not just for beginners. Beginners will benefit from knowing about a simple deployment tool, but intermediate developers will probably learn something from peeking under the hood of a management command that acts on another project. And people who teach Django will probably appreciate having a tool that configures a project for deployment, without having to talk their students through all the steps of deploying to a specific platform.

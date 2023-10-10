---
abstract: "Production server infrastructure is a complicated beast that requires configuring
  and coordinating dozens of tools and services.  You have a new Django application
  and you're ready to deploy it; what next?  You have an existing Django application
  and you set up the servers yourself; what can you do better?\r\n\r\nI’m the co-founder
  CTO of [Zagaran, Inc.](https://zagaran.com), a software consulting company.  Over
  the past 10 years, we’ve built, maintained, and deployed dozens of Django websites,
  and have an extensive playbook for how to do that well.  In this talk, we'll draw
  from that playbook and go through the main issues for a creating a robust and secure
  Django deployment.  For each issue, we'll look at the technologies and techniques
  to solve it.  We'll focus on AWS as a hosting platform, but the techniques at play
  will work on any major cloud provider.  This talk will cover the following:\r\n*
  Application hosting\r\n* Resilience to server failures\r\n* Automating deployment\r\n*
  Secrets management\r\n* File storage\r\n* Error monitoring\r\n* Server maintenance\r\n*
  (and more!)"
accepted: true
category: talks
date: 2023-10-16 15:55:00-04:00
end_date: 2023-10-16 16:40:00-04:00
group: talks
image: https://2023.djangocon.us//static/img/social/presenters/benjamin-zags-zagorsky.png
layout: session-details
permalink: /talks/hosting-and-devops-for-django/
presenter_slugs:
- benjamin-zags-zagorsky
published: true
room: Grand Ballroom III
sitemap: true
slug: hosting-and-devops-for-django
summary: ''
tags:
- deployment
title: Hosting and DevOps for Django
track: t1
---

Production server infrastructure is a complicated beast that requires configuring and coordinating dozens of tools and services.  You have a new Django application and you're ready to deploy it; what next?  You have an existing Django application and you set up the servers yourself; what can you do better?  One mistake in a server setup can lead to major downtime or a security breach of a website.  Short of that, it can cause a lot of headaches for developers as complexity spirals out of control.

I’m the co-founder CTO of [Zagaran, Inc.](https://zagaran.com), a software consulting company.  Over the past 10 years, we’ve built, maintained, and deployed dozens of Django websites, and have an extensive playbook for how to do that well.  In this talk, I draw from that playbook and go through the main ingredients for creating a robust and secure Django deployment.  For each piece, we'll look at the technologies and techniques to do it well.  We'll focus on AWS as a hosting platform, but these approaches work on any major cloud provider.

This talk is aimed at anyone that is working with the servers and/or deployment process of a production Django project.  For people setting up a new set of servers for a Django project, this talk should be a good overview of the approach they need to take.  For people with an existing server setup for a Django project, this talk should help them identify issues that they had missed and ways to make their servers easier to manage.

In this talk, we'll look at three main ways to host an application:
1. Platform as a Service
2. Managed Container Service
3. Kubernetes

With that as framing, we'll cover the following other aspects of DevOps:
* Application hosting
* Server security
* Automating deployments
* Databases and migrations
* Secrets management
* File storage
* Server monitoring
* Server maintenance
* (and more!)

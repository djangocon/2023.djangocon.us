---
abstract: Beginners often stumble when it’s finally time to get their Django app online.
  Instead of another deployment recipe, this talk seeks to explain the fundamental
  concepts of deploying a Django app and equip developers to think through the process
  for themselves when they’re ready to make the transition from their code editor
  to the web.
accepted: true
category: talks
date: 2023-10-17 17:15:00-04:00
end_date: 2023-10-17 17:40:00-04:00
group: talks
image: https://2023.djangocon.us//static/img/social/presenters/james-walters.png
layout: session-details
permalink: /talks/what-django-deployment-is-really-about/
presenter_slugs:
- james-walters
published: true
room: Grand Ballroom III
sitemap: true
slug: what-django-deployment-is-really-about
summary: ''
tags:
- deployment
title: What Django Deployment is Really About
track: t1
video_url: https://youtu.be/t-wsiW5mkgA
---

People often spend so much time learning how to build apps in Django that when it comes time for deployment, it feels like a whole new world that they don't understand. Deployment recipes might help them get their app online--but then again they might not, if the steps that worked yesterday don't work today. Even if they do get online, they might not understand that deployment process anymore than they did before.

Instead of offering another set of steps, I think we can help beginners to make sense of deployment by reducing the entire process to four major areas of concern and equipping them to think through each of these on its own terms:

1. Static Files - why do I have to worry about these now? I thought `{% raw %}{% static %}{% endraw %}` was handling it?
2. Database - does my sqlite3 file not work in deployment? How do I use my cloud provider's remote DB?
3. WSGI Server -  how do I run my app in production? Doesn't manage.py runserver work? I've never heard of WSGI, what is it and why does it matter to my Django project?
4. Web Server (Apache/nginx/PaaS) - What do I need to understand about web servers like Apache or nginx to get my project online? Do I even need to configure a web server if I go with PaaS?

We'll also consider:
- Django's deployment checklist
- django-simple-deploy

A link to slides will be posted after the talk at http://james.walters.click/

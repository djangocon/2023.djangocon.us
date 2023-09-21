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

## Motivation

One mistake in a server setup can lead to major downtime or a security breach of a website.  Short of that, it can cause a lot of headaches for developers.  This talk will cover the key issues that people encounter in creating and maintaining production deployments, and present one or more battle-tested solutions to each of those problems.

There are a lot of technologies involved in a good server setup, and the list at first may seem overwhelming.  This talk is going to be an overview of the technologies in question.  For each suggested technology, the goal is to leave the audience with an understanding of where each technology fits in the deployment ecosystem and what they would be using it for, so they know what documentation to look for when they are working with it.

## Target Audience

This talk is aimed at anyone that is working with the servers and/or deployment process of a production Django project.  For people setting up a new set of servers for a Django project, this talk should be a good overview of the approach they need to take.  For people with an existing server setup for a Django project, this talk should help them identify issues that they had missed and ways to make their servers easier to manage.

## Technological goals

A good server setup has the following properties:

* Server setup is resilient to individual server failures
* Deployments are robust and fully automated
* Code can be tested on a representative environment (ex. staging) before being deployed to production
* Data and secrets are properly secured and backed-up
* Errors are sent to developers
* Servers can be analyzed for problems
* Resources can be scaled in response to load

These properties are the framing for the talk.  All the technologies and techniques in this talk serve at least one of these goals.

## Outline

The following is an outline of the presentation.  Each bullet point roughly corresponds to one slide (on average, one minute of content).

Intro:
* Who I am
* Motivation
* Goals of a good deployment
* Talk outline

Hosting:
* Elastic beanstalk
* ECS
* EKS (Kubernetes)
* Terraform
* Gunicorn
* Docker
* Load balancers

Deployment:
* Deploying EB
* Deploying ECS
* Deploying EKS
* Full continuous deployment (zero-click deployments)
* Updating system packages

Databases and Migrations:
* RDS and backups
* Encryption in transit and at rest
* Security groups for RDS
* Running migrations on EB (configure a deployment command)
* Running migrations on ECS (run a task)
* Running migrations on EKS (run a job)
* Django Migrations race condition
* Downtime flag for deployments
* Automatic database resizing

Static assets and Media:
* WhiteNoise plus on-server hosting for static assets
* CloudFront for static assets
* django-storages + S3 for media assets
* Encryption in transit and at rest

Secrets management:
* django-environ
* Amazon secrets manager

HTTPS:
* Amazon certificate manager
* Disabling insecure versions of SSL and Amazon SSL policies
* HTTP -> HTTPS redirect

Monitoring/Error Reporting:
* Sentry (error monitoring tool)
* UptimeRobot (uptime monitoring tool)
* DataDog (error monitoring plus profiling tool)

Performance:
* CloudWatch (profiling tool)
* NewRelic (profiling tool)
* Load testing
* Manual scaling
* Auto-scaling

Extras:
* Dependency pinning: use pip-tools or poetry
* SSH-ing on to a server: use Amazon Session Manager; for EKS, install Amazon SSM agent

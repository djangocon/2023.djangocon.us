---
abstract: Multitenancy is a broad spectrum, ranging from using separate databases
  for each tenant to using a shared database and schema. This talk will present a
  “lightweight” multitenancy use case that we’ve run into across different projects
  in various contexts.  We will present a simple custom solution using Django Rest
  Framework and explain why it worked for our needs. We will also go over which cases
  could use a similar approach (and which could not), as well as a different approach
  using an existing library.
accepted: true
category: talks
date: 2023-10-17 17:15:00-04:00
end_date: 2023-10-17 17:40:00-04:00
group: talks
image: https://2023.djangocon.us//static/img/social/presenters/eliana-rosselli.png
layout: session-details
permalink: /talks/an-approach-to-lightweight-tenancy-management-using-django-rest-framework/
presenter_slugs:
- eliana-rosselli
published: true
room: Junior Ballroom
sitemap: true
slug: an-approach-to-lightweight-tenancy-management-using-django-rest-framework
summary: ''
tags:
- APIs
- how I used Django
title: An approach to lightweight tenancy management using Django Rest Framework
track: t0
video_url: https://youtu.be/BW9ju19u1zU
---

Over the last few years, I have run into the same multitenancy use case across different projects. This scenario is a “lightweight” multitenancy use case, where we have a tenant model and tenants are instances of this model; all tenants share the same database, schema, and application instance. Resources belong to a single tenant, but users can belong to multiple tenants. Almost all API routes need to be nested under the tenant id, with urls of the form `api/tenants/tenant-id/some-resource`. The challenges we faced were how to effectively nest our API urls and how to consistently restrict access to resources, so that users could only access those resources that belong to tenants that the user has permission to access.

We’ll cover:
- A brief description of the use case and multitenancy
- How we implemented nested routes in our API using [drf-nested-routers](https://github.com/alanjds/drf-nested-routers)
- How we wrote a custom viewset to centralize all logic related to checking that the user has permission to access resources under a specific tenant
- Custom model manager to avoid accidentally leaking information from other tenants
- Uses and limitations of our approach
- A different approach using an existing library ([drf-access-policy](https://github.com/rsinger86/drf-access-policy))

Anyone with experience in Django is welcome!

---
abstract: In this session, we will explore, how we can use Django for only serving
  APIs with advanced functionalities like REST endpoints, proper JSON responses, custom
  permissions, and custom responses based on the user access level. We will also see
  how we can customize the Django default Admin Panel to optimize it. Additionally,
  we will also see how we can write unit tests for our APIs and follow Test Driven
  Development with our Django Backend.
accepted: true
category: tutorials
date: 2022-10-16 13:30:00-07:00
difficulty: All
end_date: 2022-10-16 17:00:00-07:00
group: tutorials
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Fkuldeep-pisda%252F/opengraph/
layout: session-details
permalink: /tutorials/using-django-for-serving-rest-apis-with/
presenter_slugs:
- kuldeep-pisda
published: true
room: Sierra 5
sitemap: true
slug: using-django-for-serving-rest-apis-with-permission-control-and-customizing-the-default-admin-panel
summary: ''
tags: null
title: Using Django for serving REST APIs with permission control and customizing
  the default admin panel
track: t1
---

In the session, we will see how we can use Django to serve APIs.
- Create REST Endpoints quickly with DRF.
- Implement proper permissions on the REST endpoints, for example, an admin can perform any operation on any data. But a specific user can perform a limited operation on certain specific resources.
- Respond with different responses as per the defined user's permission level. For example, the admin will get all the fields in the response, but a normal user will get only a selected field of the model.
- Implement Pagination on the REST endpoint.
- Create custom endpoints on the REST Endpoints.

Customizing Admin Panel:
- Modifying the default list in the admin panel.
- Add a custom field in the list in the admin panel.
- Adding filters based on a field of the model.
- Adding search functionality for a model.
- Customizing how forms are displayed in the admin panel.
- Implementing Validations
- Customizing Admin Panel Templates

Writing Tests for our Backend APIs
- Creating Factory for Models.
- Integrating with Faker
- Writing test for all the REST endpoints.
- Implementing our tests as PyTests.
- Writing a single test and running it with different parameters with parameterization.

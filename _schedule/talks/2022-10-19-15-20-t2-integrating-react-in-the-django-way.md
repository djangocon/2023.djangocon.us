---
abstract: Many times we would like to use React in our Django project to make highly
  interactive user interfaces. You don't want to isolate your frontend and backend,
  also configuring tools like Babel, Webpack, and Webpack Dev Server, deter you from
  using React in your project? Well, django-webpack-dev-server is a command-line reusable
  django package that installs the required dependencies and configures a React application
  in your project with just a single command.
accepted: true
category: talks
date: 2022-10-19 15:20:00-07:00
end_date: 2022-10-19 15:45:00-07:00
group: talks
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Fjiten-sidhpura%252F/opengraph/
layout: session-details
permalink: /talks/integrating-react-in-the-django-way/
presenter_slugs:
- jiten-sidhpura
published: true
room: Online talks
schedule_layout: full
sitemap: true
slug: integrating-react-in-the-django-way
summary: ''
tags: null
title: Integrating React in the Django way!
track: t2
---

## Why Frontend Frameworks are getting Popular?

Your User Interface is the first impression you make on your website visitors. Thus User Interface is a critical component of your web application. It becomes necessary to make it simple, efficient, and at the same time attractive. Developing complex user interfaces with traditional methods like Vanilla Javascript or Jquery library is time-consuming and can get messy after some time. Nowadays, there are many frontend frameworks such as React, Angular, Vue, and more. These frameworks make the process of frontend development much cleaner, faster, and easier.

## How to use React with Django?

The most common solution shown by many tutorials and blogs on the Internet is to develop two isolated projects, one for the frontend and the other for the backend. All the interactions between these two projects happen through APIs. This approach is used in large projects since they generally have dedicated teams for the backend and frontend. But this approach may not be suitable for individual or small-scale projects due to a variety of reasons like the cost for deployment, time consumption, and losses of features provided by Django Framework (forms).

A more Django-friendly approach would be to serve a single template (HTML) document, and then let React take over. This approach gives you the liberty to use plain HTML and Vanilla Javascript for simple pages or forms, and for highly interactive pages, one can take advantage of React. Using HTML and Vanilla Javascript for the simple pages can help reduce the bundle size of the frontend and thus help in reducing the loading time and improving the overall User Experience.

## Why did I develop this Package?

When I decided to integrate Django and React, it took me two full days only to configure the project. I had many errors while writing the Webpack configuration file and many dependencies issues. After this experience, I realized why not automate these steps so other users will not get demotivated from trying Django and React, and this is how django_webpack_dev_server was born.

## How this Package Helps you!

The package provides a command to set up a React app in both Javascript and Typescript programming languages. The resulting app would be a Django app with a webpack configuration with CSS and SCSS support. The webpack dev server would proxy the Django server in the development phase. After running the build script, the frontend code gets bundled into a single Javascript file and is available for Django to serve from an HTML template. After the setup, it is easy to install other npm packages and modify the webpack configuration as per specific requirements. Since the package is used in development only, there is no need to add it to the requirements.txt file of the production environment.

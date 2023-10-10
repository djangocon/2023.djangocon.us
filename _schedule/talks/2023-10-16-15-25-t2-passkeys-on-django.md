---
abstract: "Passkeys is a state-of-the-art technology that extends Web Authentication
  API allowing the user to use a key stored on a device to log in on a new device.
  The technology is supported by Apple, Google, and Microsoft and is available now
  on recent iOS/iPad, Andriod as well as Mac OS X Ventura.\r\nPasskeys allow the users
  to log in only through their private keys. It doesn't require the entry of a username
  and/or password, which provides a faster as well as safer environment for the users.\r\nGoogle
  released Passkeys for all users to log in with on May 3, 2023.\r\nThe talk will
  discuss what is Passkeys and how it is more secure and phishing resistant, also
  it will show how to integrate them in your current Django project in a few lines
  of code."
accepted: true
category: talks
date: 2023-10-16 15:25:00-04:00
end_date: 2023-10-16 15:50:00-04:00
group: talks
image: https://2023.djangocon.us//static/img/social/presenters/mohamed-elkalioby.png
layout: session-details
permalink: /talks/passkeys-on-django/
presenter_slugs:
- mohamed-elkalioby
published: true
room: Online talks
schedule_layout: full
sitemap: true
slug: passkeys-on-django
summary: ''
tags:
- external services
- security
title: Passkeys on Django
track: t2
---

Web Authentication API (WebAuthn) is a phishing-proof technology that is expected to replace passwords. The technology is available since 2019, but in 2022, Apple, Google, and Microsoft agreed to support Passkeys, solving challenges facing the wide deployment of WebAuthn API. Passkeys is an extension to WebAuthn that allows the user to use a key credential stored in a device to log in on another device. e.g. you can use the key stored on your phone to log in on a browser on a Windows device. The communication is done over Bluetooth Low Energy (BLE). Passkeys are now supported on iOS/iPad 16, Mac OS X Ventura, and Andriod phones, and can be used by Chromium-based browsers and Safari.
The talk will cover the following
*  what is WebAuthn and how it is phishing resistant even during a man-in-the-middle attack,
* challenges in WebAuthn,
* what are Passkeys and how they solved WebAuth challenges,
* State of Passkeys,
* Demo the usage of passkeys and their user experience.
* How to integrate passkeys in your current Django project by `django-passkeys`.

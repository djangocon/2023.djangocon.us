---
abstract: Can you predict lightning strikes using Django and AWS? Yes! Learn how to
  take an algorithm and idea from a Jupyter Notebook to production ready and cloud
  native.
accepted: true
category: talks
date: 2022-10-17 14:50:00-07:00
end_date: 2022-10-17 15:15:00-07:00
group: talks
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Fcalvin-hendryx-parker%252F/opengraph/
layout: session-details
permalink: /talks/predict-lightning-strikes-using-django/
presenter_slugs:
- calvin-hendryx-parker
published: true
room: Salon A-E
sitemap: true
slug: predict-lightning-strikes-using-django-and-aws
summary: ''
tags: null
title: Predict Lightning Strikes using Django and AWS
track: t0
---

Predicting a lightning strike with 99.6% accuracy requires advanced algorithms, expert developers and data — a lot of data. FLASH Scientific Technology pulls data from a variety of sources including weather radars and location-specific information like altitude, moisture, wind direction and temperature. It was imperative that FLASH develop an application that could pull, read and process the data both quickly and accurately.

In this case study and product demo, you’ll learn how to take an algorithm and idea from a Jupyter Notebook to production ready and cloud native.

(1) Optimize Python code structure
-- As the Zen of Python states, “simple is better than complex.” The first part of this presentation will focus on the importance of reviewing and simplifying code to ensure faster data processing speeds and that the code is easy to both read and duplicate.
(2) Build fast, efficient and accurate APIs with Django
--Once the code is optimized, it’s ready for production. You’ll learn how we built an interface that could both request data from various web services and quickly make accurate predictions using FLASH’s proprietary and patent-issued algorithm. Specifically, this talk will feature:
        1. best practices and lessons learned, including insight into why we stored all of the Django application elements in a single library;
        2. why all of the data needed to be pulled directly from the cache; and
        3. why the algorithm was kept separate.
(3) Deploy serverless and scalable applications using AWS Lambda and AWS Fargate
--Finally, this talk will:
        1. showcase how the Django application we built integrates seamlessly with the serverless components of AWS including AWS Lambda and AWS Fargate;
        2. unveil the secrets of building Python Container Images for AWS Lambda (Hint: by using container images for Lambda code vs. manually submitting .zip files we saved significant time, money, and effort. We also reduced errors associated with manual changes.);
        3. review the importance of building applications to be serverless from the beginning.
(4) Product Demo
-- Today, the application — which initially took minutes to make lightning strike predictions with 99.6% accuracy and a 15- to 25-minute lead time (saving time, money and lives) — can predict when and where lightning will strike in just seconds. The presentation will conclude with a demo of the product, which is deployed with GitLab CI/CD merge request pipeline.

Both beginner and intermediate developers will benefit from this talk, and it is ideal for developers wanting to learn how to use Django for complex predictive-technology projects.

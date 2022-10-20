---
abstract: How can Django help us move the needle away from climate change? At Energy
  Solutions, we help utilities manage energy demand by running efficiency programs
  incentivizing the adoption of energy efficient and electrified technologies. These
  energy efficiency programs are managed through a Django website we call Iris. In
  this talk, I will highlight some of the more interesting parts of the Iris Django
  backend that we have built in the past 3 years.
accepted: true
category: talks
date: 2022-10-17 17:10:00-07:00
end_date: 2022-10-17 17:35:00-07:00
group: talks
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Ferin-mullaney%252F/opengraph/
layout: session-details
permalink: /talks/fighting-climate-change-with-django/
presenter_slugs:
- erin-mullaney
published: true
room: Salon A-E
sitemap: true
slug: fighting-climate-change-with-django
summary: ''
tags: null
title: Fighting Climate Change with Django
track: t0
---

Background on Energy Efficiency
--------------
Utilities, which are often regulated, are responsible for generating a consistent supply of energy for their consumers at a stable price. Efficiency incentive programs that manage demand help insulate utilities from the costs associated with purchasing raw materials (coal, gas, etc.) and help reduce the need to build new power plants that are expensive to build, staff, insure, and supply with consumable, non-renewable resources.

Utilities are also usually required by law to spend part of the budget they collect on customer bills on something to reduce the demand for energy in their territory. For instance, a utility might offer a $1,500 rebate (AKA incentive) for the sale of an industrial heat pump that is far more efficient than other industrial heat pumps, via an energy efficiency (EE) program. By incentivizing high efficiency equipment, utilities help move the market towards ever more efficient versions of equipment, thus locking in energy savings even after the EE programs end. In this way, we can help utilities and their customers save energy and move the needle away from climate change.

Django and Iris
---------
What is Iris?
- Background of what Iris is, a measure matching application that allows multiple utilities from around the country, and vendors, offer rebates to consumers

Measure Matching: improving our algorithm by leaps and bounds
- What are measures? How does an energy efficient water heater purchase turn into a claim for an energy efficiency rebate?
- How we switched from a long-running loop over individual database records to a single database query and JSON data objects, and what were the performance gains from this change.

Multi-tenancy for energy efficiency programs: One website - many different EE programs
- Energy efficiency program design includes setting up qualifications and assigning incentives that allow the efficiency program to meet energy savings goals.
- How we moved away from efficiency program-specific (ie. user-specific) code (AKA spaghetti code) in our former system, and how we built flexibility into Iris to allow many different utilities to use a single website.

Major Database Architecture Changes 2 years Later
- In 2021, after Iris had been in production for about 2 years, we had a new feature request that would require a major change to our underlying database structures. Background on the changes we decided to make and how we made them.

Reporting on energy efficiency in Iris
- Proving that energy efficiency programs are in fact saving energy and helping us fight climate change through reporting features

---
abstract: At some point, every application is limited by the database. You don’t have
  to be a Postgres expert to get started with a few key performance improvements.
  This gentle introduction is meant for folks who’ve never ventured into their database
  before, or those who have been turning knobs blindly. I’ll present how Postgres
  uses memory.  Then, I’ll connect that to how you can monitor, tune, and optimize
  queries.  You’ll be ready to take on the challenge as your application grows.
accepted: true
category: talks
date: 2023-10-17 11:10:00-04:00
end_date: 2023-10-17 11:55:00-04:00
group: talks
layout: session-details
permalink: /talks/postgres-performance-from-slow-to-pro/
presenter_slugs:
- elizabeth-christensen
published: true
room: Junior Ballroom
sitemap: true
slug: postgres-performance-from-slow-to-pro
summary: ''
tags:
- optimization/speed
- postgres
title: 'Postgres Performance: From Slow to Pro'
track: t0
---

At some point, every application is limited by the database. You don’t have to be a Postgres expert to get started with a few key performance improvements. This gentle introduction is meant for folks who’ve never ventured into their database before, or those who have been turning knobs blindly. I’ll present how Postgres uses memory. Then, I’ll connect that to how you can monitor, tune, and optimize queries. You’ll be ready to take on the challenge as your application grows.

#### Review of how Postgres uses memory
Measuring cache hit ratio
Measuring memory usage and tuning
Measuring shared buffer usage and tuning

#### Connection settings
Default connection settings, knowing when you need more

#### Stop runwaywas
Setting a statement timeout
Finding and stopping transactions

#### Query performance
Using EXPLAIN
Reading and understanding EXPLAIN plans
Logging EXPLAIN plans 
Adding Indexes

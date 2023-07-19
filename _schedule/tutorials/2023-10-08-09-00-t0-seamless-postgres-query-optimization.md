---
abstract: Seamless Postgres Query Optimization is a methodology that allows every
  backend engineer, even without deep database knowledge and 10-year Postgres experience,
  to move step-by-step to find and eliminate the worst bottlenecks in any SQL.
accepted: true
category: tutorials
date: 2023-10-08 09:00:00-04:00
end_date: 2023-10-08 12:30:00-04:00
group: tutorials
layout: session-details
permalink: /tutorials/seamless-postgres-query-optimization/
presenter_slugs:
- nikolay-samokhvalov
published: true
room: Tutorial Track A
sitemap: true
slug: seamless-postgres-query-optimization
summary: ''
tags:
- ORM
- postgres
title: Seamless Postgres Query Optimization
track: t0
---

There are two types of Postgres query analysis:

- "Macro": analyzing the workload as a whole (three major approaches: using metrics provided by pg_stat_statements or similar, log analysis with pgBadger or similar, and sampling of pg_stat_activity)
- "Micro": diving into details of single query execution (EXPLAIN command being the central tool here)

And there are huge gaps between them that become noticeable at scale. The main challenges:

- Switching between "macro" and "micro" without a huge overhead
- Verifying optimization ideas reliably
- Deploying changes risk-free
- Solving these tasks at a scale requires advanced DBA experience and–sometimes–intuition. Or better tools that (fortunately!) very recently started to appear.

In this tutorial, we will learn how to establish a smooth and seamless SQL optimization process in your organization:
* what tools should you choose in your particular case?
* how to close the gaps mentioned above?

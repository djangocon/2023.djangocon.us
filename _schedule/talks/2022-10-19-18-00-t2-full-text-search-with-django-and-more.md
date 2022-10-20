---
abstract: Search is a common feature and sites like Amazon.com provide familiar UX
  for filtering search results and finding products. But if you’re not building Amazon.com,
  it’s possible to create a similar interface using just Django and PostgreSQL FTS!
  With our techniques you can even get rid of some bulky dependencies!
accepted: true
category: talks
date: 2022-10-19 18:00:00-07:00
end_date: 2022-10-19 18:45:00-07:00
group: talks
layout: session-details
permalink: /talks/full-text-search-with-django-and-more/
presenter_slugs:
- jason-judkins
- colin-copeland
published: true
room: Online talks
schedule_layout: full
sitemap: true
slug: full-text-search-with-django-and-postgresql-more-facets-less-dependencies
summary: ''
tags: null
title: 'Full Text Search with Django and PostgreSQL: More Facets, Less Dependencies!'
track: t2
---

We’ll describe some issues we faced with some bulkier and less supported search options. Django’s core functionality has come a long way since 1.10 and all the tools you need are there without having to bring in more dependencies. We’ll discuss the history and evolution of django-haystack and backends including Elasticsearch.  We’ll explore adding facets, queryset annotations, and FTS techniques to whittle down the data into more efficient chunks of Data in a Django application. We’ll use a simple project to demonstrate how to extend django-filter to do what we needed and how we separated and rebuilt indexes. Hopefully, after our talk, more developers will be better equipped to use the built in tools already available.

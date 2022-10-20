---
description: Twitter Template for Tweets (this should not be in our sitemaps file)
heading: Twitter Template for Tweets
layout: default
permalink: /speaking/twitter/
sitemap: false
title: Twitter Template for Tweets
---

<script src="https://cdn.tailwindcss.com"></script>

{% for post in site.schedule %}
{% capture day %}{{ post.date | date: "%A" }}{% endcapture %}
{% if day == 'Sunday' or day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' %}
{% if post.group == 'talks' or post.group == 'tutorials' %}
<div class="event-byline">
<h4>{{ post.date | date: "%b %d %l:%M %p %Z" }} - {{ post.title }}</h4>

{% capture twitter-copy-link %}copy-{{ post.slug | slugify }}-twitter{% endcapture %}

<textarea rows="6" id="{{ twitter-copy-link }}">
{% include twitter-copy-and-paste.html post=post presenter_slugs=post.presenter_slugs %}
</textarea>

<button class="btn bg-blue-200 border-solid border-2 border-grey-800 rounded-lg px-2 py-1" data-clipboard-action="copy" data-clipboard-target="#{{ twitter-copy-link }}">
Copy to clipboard
</button>
</div>

<hr>
{% endif %}
{% endif %}
{% endfor %}

<script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.4/clipboard.min.js"></script>
<script>
new ClipboardJS('.btn');
</script>

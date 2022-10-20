---
description: Our Speaking Template for YouTube Videos (this should not be in our sitemaps
  file)
heading: Speaking Template for YouTube Videos
layout: default
permalink: /speaking/youtube/
sitemap: false
title: Speaking Template for YouTube Videos
---

<script src="https://cdn.tailwindcss.com"></script>

{% for post in site.schedule %}
{% capture day %}{{ post.date | date: "%A" }}{% endcapture %}
{% if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' %}
{% if post.group == 'talks' or post.group == 'tutorials' %}
<div class="event-byline">
<h4>{{ post.date | date: "%b %d %l:%M %p %Z" }} - {{ post.title }}</h4>

<div>
  <a href="{{ post.video_url }}">On YouTube</a>
  {% if post.additional_video_url %}<a href="{{ post.additional_video_url }}">Also on YouTube</a>{% endif %}
</div>

{% capture youtube-copy-link %}copy-{{ post.slug | slugify }}-youtube{% endcapture %}

<textarea rows="10" id="{{ youtube-copy-link }}">
{% include youtube-copy-and-paste.html post=post presenter_slugs=post.presenter_slugs %}
</textarea>

<button class="btn bg-blue-200 border-solid border-2 border-grey-800 rounded-lg px-2 py-1" data-clipboard-action="copy" data-clipboard-target="#{{ youtube-copy-link }}">
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

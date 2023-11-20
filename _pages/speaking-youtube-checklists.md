---
description: Our Speaking Checklists for YouTube Videos (this should not be in our
  sitemaps file)
heading: Speaking Checklists for YouTube Videos
layout: default
permalink: /speaking/youtube/checklists/
sitemap: false
title: Speaking Checklists for YouTube Videos
---

<script src="https://cdn.tailwindcss.com"></script>

{% for post in site.schedule %}
{% capture day %}{{ post.date | date: "%A" }}{% endcapture %}
{% if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' %}
{% if post.group == 'talks' or post.group == 'tutorials' %}
<section class="event-byline py-8 flex flex-col gap-4">
<h2 class="text-3xl font-bold">Video Checklist</h2>

<div class="relative">
{% capture youtube-copy-title %}copy-{{ post.slug | slugify }}-youtube{% endcapture %}
<h4 class="text-2xl font-bold">{{ post.date | date: "%b %d %l:%M %p %Z" }} - <span id="{{ youtube-copy-title }}">{{ post.title }}</span>
</h4>
<button class="absolute top-0 right-2 btn bg-blue-200 border-solid border-2 border-grey-800 rounded-lg px-2 py-1" data-clipboard-action="copy" data-clipboard-target="#{{ youtube-copy-title }}">
📋 Copy to clipboard
</button>
</div>

{% if post.video_url %}
  <div>
    <a class="btn bg-blue-200 border-solid border-2 border-grey-800 rounded-lg px-2 py-1" href="{{ post.video_url }}">
      On YouTube
    </a>
  </div>
{% endif %}

{% if post.additional_video_url %}
  <div>
    <a class="absolute top-2 right-2 btn bg-blue-200 border-solid border-2 border-grey-800 rounded-lg px-2 py-1" href="{{ post.additional_video_url }}">
      Also on YouTube
    </a>
  </div>
{% endif %}

<div class="border-4 border-black rounded-2xl relative">
{% capture youtube-copy-checklist %}copy-{{ post.slug | slugify }}-youtube-checklist{% endcapture %}
<pre class="p-2" id="{{ youtube-copy-checklist }}">
{%- include youtube-copy-and-paste-checklist.html post=post presenter_slugs=post.presenter_slugs -%}
</pre>

<button class="absolute top-2 right-2 btn bg-blue-200 border-solid border-2 border-grey-800 rounded-lg px-2 py-1" data-clipboard-action="copy" data-clipboard-target="#{{ youtube-copy-checklist }}">
📋 Copy to clipboard
</button>
</div>

<div class="border-4 border-black rounded-2xl bg-yellow-100 relative">
{% capture youtube-copy-link %}copy-{{ post.slug | slugify }}-youtube-link{% endcapture %}
<pre class="p-2" id="{{ youtube-copy-link }}">
{%- include youtube-copy-and-paste.html post=post presenter_slugs=post.presenter_slugs -%}
</pre>

<button class="absolute top-2 right-2 btn bg-blue-200 border-solid border-2 border-grey-800 rounded-lg px-2 py-1" data-clipboard-action="copy" data-clipboard-target="#{{ youtube-copy-link }}">
📋 Copy to clipboard
</button>
</div>


</section>
<hr>
{% endif %}
{% endif %}
{% endfor %}

<script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.4/clipboard.min.js"></script>
<script>
new ClipboardJS('.btn');
</script>

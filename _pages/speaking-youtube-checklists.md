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

{% capture youtube-copy-title %}copy-{{ post.slug | slugify }}-youtube{% endcapture %}

<h4 class="text-2xl font-bold">{{ post.date | date: "%b %d %l:%M %p %Z" }} - <span id="{{ youtube-copy-title }}">{{ post.title }}</span></h4>

<button class="btn bg-blue-200 border-solid border-2 border-grey-800 rounded-lg px-2 py-1" data-clipboard-action="copy" data-clipboard-target="#{{ youtube-copy-title }}">
Copy title to clipboard
</button>

<div>
  {% if post.video_url %}
    <a class="btn bg-blue-200 border-solid border-2 border-grey-800 rounded-lg px-2 py-1" href="{{ post.video_url }}">
      On YouTube
    </a>
  {% endif %}
  {% if post.additional_video_url %}
    <a class="btn bg-blue-200 border-solid border-2 border-grey-800 rounded-lg px-2 py-1" href="{{ post.additional_video_url }}">
      Also on YouTube
    </a>
  {% endif %}
</div>

<div class="border-2 border-black round-2xl p-2">
    <ul>
      <li><input type="checkbox"> YouTube Premiere time set: {{ post.date | date: "%b %d %l:%M %p %Z" }}</li>
      <li><input type="checkbox"> Did the link above open the correct video?</li>
      <li><input type="checkbox"> Set title from this page</li>
      <li><input type="checkbox"> Set description from this page</li>
      <li><input type="checkbox"> Is it on the DjangoCon US 2023 Playlist?</li>
      <li><input type="checkbox"> Set to "not made for kids"</li>
      <li><input type="checkbox"> Set as "contains paid promotion"</li>
      <li><input type="checkbox"> Language set appropriately</li>
      <li><input type="checkbox"> Caption certification "has never aired on television"</li>
      <li><input type="checkbox"> Verify license is correct (YouTube Standard)</li>
      <li><input type="checkbox"> Allow embedding enabled</li>
      <li><input type="checkbox"> Publish to feed and notify subscribers enabled</li>
      <li><input type="checkbox"> Category: Education</li>
      <li><input type="checkbox"> Comments disabled</li>
      <li><input type="checkbox"> "show how many viewers like and dislike this video" disabled</li>
      <li><input type="checkbox"> English captions uploaded</li>
    </ul>
</div>

{% capture youtube-copy-link %}copy-{{ post.slug | slugify }}-youtube-link{% endcapture %}

<textarea class="border-2 border-black bg-yellow-100 round-2xl p-2" rows="10" id="{{ youtube-copy-link }}">
{% include youtube-copy-and-paste.html post=post presenter_slugs=post.presenter_slugs %}
</textarea>

<button class="btn bg-blue-200 border-solid border-2 border-grey-800 rounded-lg px-2 py-1" data-clipboard-action="copy" data-clipboard-target="#{{ youtube-copy-link }}">
Copy to clipboard
</button>
</section>
<hr>
{% endif %}
{% endif %}
{% endfor %}

<script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.4/clipboard.min.js"></script>
<script>
new ClipboardJS('.btn');
</script>

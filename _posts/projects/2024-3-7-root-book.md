---
layout: post
title: "Root Book"
author: Flareonz44
tags: [literature]
type: project
metadesc: "My first book :)"
---

This is the first book I am writing. It is a compilation of many stories that I have been writing and thinking about for a long time. They are all different but share the same lore and universe, so they are all connected.
Below is the list of chapters I've been writing, in order of publication.

{% if site.posts.size > 0 %}
  <ul>
    {% assign reversed_posts = site.posts | reverse %}
    {% for post in reversed_posts %}
      {% if post.tags contains 'root_book' %}
      <li class="post-list-item">
        <span class="home-date">
          {{ post.date | date: site.theme_config.date_format }}»
        </span>
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      </li>
      {% endif %}
    {% endfor %}
  </ul>
{% endif %}
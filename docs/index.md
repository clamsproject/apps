---
layout: home
title: "CLAMS App directory"
permalink: /
---

## How to use CLAMS apps

* [CLAMS App user manual](clamsapp)

## App Directory

{% for app in site.data.app-index %}
    {%- assign check = app[0] | split:'http://apps.clams.ai/' -%}
    {% if check.size == 2 %}
### {{ check[1] }}
        {% for version in app[1] %}
[{{ version }}]({{ check[1] }}/{{ version }})
        {% endfor %}
    {% else %}
### {{ app[0] }}
        {% for version in app[1] %}
[{{ version }}]({{ app[0] }}/{{ version }})
        {% endfor %}
    {% endif %}
{% endfor %}

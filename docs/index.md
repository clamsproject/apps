---
permalink: /
title: CLAMS App Directory 
layout: single
author_profile: true
toc: true
toc_sticky: true
---

## How to use CLAMS apps 

* Want to know how to use CLAMS apps? Check out [CLAMS App user manual](clamsapp).
* Want a human friendly views of MMIF JSON files? Visit [MMIF visualizer](https://github.com/clamsproject/mmif-visualizer) repository. 

## App Directory

{% for app in site.data.app-index %}
    {% assign check = app[0] | split:'http://apps.clams.ai/' %}
    {% if check.size == 2 %}
        {% assign versions = app[1]["versions"] %}
        {% capture numstr %} {{ versions.size }},3 {% endcapture %}
        {% assign numstrs = numstr | split: "," %}
        {% assign nums = "" | split: "" %}
        {% for num in numstrs %}
            {% assign cast = num | to_integer %}
            {% assign nums = nums | push: cast %}
        {% endfor %}
        {% assign to_display = nums | sort | first | to_i %}
        {% assign end_loop = to_display | minus: 1 %}

### {{ check[1] }}

{{ app[1]["description"] }}

        {% for i in (0..end_loop) %}
* [{{ versions[i][0] }}]({{ check[1] }}/{{ versions[i][0] }}) ([`@{{ versions[i][1] }}`](https://github.com/{{ versions[i][1] }}))
        {% endfor %}
        {% if versions.size > to_display %}

* [all {{ versions.size }} releases]({{ check[1] }})
        {% endif %}
    {% else %}
### {{ app[0] }}
        {% for version in app[1] %}
[{{ version }}]({{ app[0] }}/{{ version }})
        {% endfor %}
    {% endif %}
{% endfor %}


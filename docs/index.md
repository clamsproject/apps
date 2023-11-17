---
permalink: /
layout: single
author_profile: true
---

## How to use CLAMS apps 

* Want to know how to use CLAMS apps? Check out [CLAMS App user manual](clamsapp).
* Want a human friendly views of MMIF JSON files? Visit [MMIF visualizer](https://github.com/clamsproject/mmif-visualizer) repository. 

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


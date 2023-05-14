
## CLAMS App Directory prototype

{% for app in site.data.apps %}
    {%- assign check = app[0] | split:'https://apps.clams.ai/' -%}
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


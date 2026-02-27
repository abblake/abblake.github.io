---
layout: page
title: Publications
permalink: /publications/
---

### Under Review

- **Blake, A. B.** et al. CEO psychopathy and the limits of dark ascent. *Administrative Science Quarterly*.
- **Blake, A. B.** et al. Relational alignment in entrepreneurial pitching. *Administrative Science Quarterly*.
- **Blake, A. B.** et al. Board chair narcissistic rivalry and governance orientation. *Academy of Management Journal*.
- **Blake, A. B.** et al. Attunement drift in founder-venture scaling. *Strategic Management Journal*.
- **Blake, A. B.** et al. CEO ideology and crisis recognition. *Group & Organization Management*.

---

### Published

<div class="publications-container">
    {% for pub in site.data.publications %}
    <div class="publication-item">
        <div class="title">{{ pub.title }}</div>
        <div class="authors">{{ pub.authors }}</div>
        <div class="venue">{{ pub.venue }} ({{ pub.year }})</div>
        {% if pub.citations > 0 %}
        <div class="citations">{{ pub.citations }} citations</div>
        {% endif %}
        {% if pub.url and pub.url != "" %}
        <div class="links">
            <a href="{{ pub.url }}" target="_blank">View Paper</a>
        </div>
        {% endif %}
    </div>
    {% endfor %}
</div>

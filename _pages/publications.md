---
layout: page
title: Publications
permalink: /publications/
---

### Under Review

- **Blake, A. B.** et al. [Entrepreneur and investor dynamics]. *Administrative Science Quarterly*.
- **Blake, A. B.** et al. [Entrepreneur personality review]. *Journal of Applied Psychology*.
- **Blake, A. B.** et al. [Founder-venture decoupling]. *Strategic Management Journal*.
- **Blake, A. B.** et al. [CEO psychopathy]. *Administrative Science Quarterly*.
- **Blake, A. B.** et al. [CEO ideology]. *Group & Organization Management*. (R&R, Round 3)
- Petrenko, O. V. et al. (incl. **Blake, A. B.**) [Board-CEO dynamics]. *Journal of Management*.
- Petrenko, O. V. et al. (incl. **Blake, A. B.**) [Legitimacy debt]. *Organization Science*.
- Panda, A., **Blake, A. B.**, & Sinha, A. [Status and reverse innovation]. *Organization Science*.

---

### Published

<div class="pub-themes">
    <div class="pub-theme-col">
        <h4>Founders</h4>
        <div class="pub-cards">
        {% assign founders = site.data.publications | where: "theme", "founders" %}
        {% for pub in founders %}
        <div class="pub-theme-item">
            <div class="pub-venue-year">{{ pub.venue }} ({{ pub.year }})</div>
            <div class="pub-title-short">{{ pub.title }}</div>
            <div class="pub-authors">{{ pub.authors }}</div>
            {% if pub.citations > 0 %}<div class="pub-citations">{{ pub.citations }} citations</div>{% endif %}
            {% if pub.note %}<div class="pub-note">{{ pub.note }}</div>{% endif %}
            {% if pub.url and pub.url != "" %}<div class="pub-link"><a href="{{ pub.url }}" target="_blank">View</a></div>{% endif %}
        </div>
        {% endfor %}
        </div>
    </div>
    <div class="pub-theme-col">
        <h4>Leadership &amp; Open Science</h4>
        <div class="pub-cards">
        {% assign leadership = site.data.publications | where: "theme", "leadership" %}
        {% for pub in leadership %}
        <div class="pub-theme-item">
            <div class="pub-venue-year">{{ pub.venue }} ({{ pub.year }})</div>
            <div class="pub-title-short">{{ pub.title }}</div>
            <div class="pub-authors">{{ pub.authors }}</div>
            {% if pub.citations > 0 %}<div class="pub-citations">{{ pub.citations }} citations</div>{% endif %}
            {% if pub.note %}<div class="pub-note">{{ pub.note }}</div>{% endif %}
            {% if pub.url and pub.url != "" %}<div class="pub-link"><a href="{{ pub.url }}" target="_blank">View</a></div>{% endif %}
        </div>
        {% endfor %}
        </div>
    </div>
    <div class="pub-theme-col">
        <h4>Personality &amp; Behavior</h4>
        <div class="pub-cards">
        {% assign personality = site.data.publications | where: "theme", "personality" %}
        {% for pub in personality %}
        <div class="pub-theme-item">
            <div class="pub-venue-year">{{ pub.venue }} ({{ pub.year }})</div>
            <div class="pub-title-short">{{ pub.title }}</div>
            <div class="pub-authors">{{ pub.authors }}</div>
            {% if pub.citations > 0 %}<div class="pub-citations">{{ pub.citations }} citations</div>{% endif %}
            {% if pub.note %}<div class="pub-note">{{ pub.note }}</div>{% endif %}
            {% if pub.url and pub.url != "" %}<div class="pub-link"><a href="{{ pub.url }}" target="_blank">View</a></div>{% endif %}
        </div>
        {% endfor %}
        </div>
    </div>
</div>

---
layout: default
title: Home
---

<section class="hero">
    <div class="hero-content">
        <div class="profile-image">
            <img src="{{ '/assets/images/profile.jpg' | relative_url }}" alt="Profile Photo">
        </div>
        <h1 class="hero-title">{{ site.author.name }}</h1>
        <p class="hero-subtitle">{{ site.author.title }}</p>
        <p class="hero-bio">{{ site.author.bio }}</p>
        
        <div class="social-links">
            <a href="mailto:{{ site.author.email }}" title="Email">
                <i class="fas fa-envelope"></i>
            </a>
            <a href="https://scholar.google.com/citations?user={{ site.social.google_scholar }}" title="Google Scholar">
                <i class="fas fa-graduation-cap"></i>
            </a>
            <a href="https://github.com/{{ site.social.github }}" title="GitHub">
                <i class="fab fa-github"></i>
            </a>
            <a href="https://twitter.com/{{ site.social.twitter }}" title="Twitter">
                <i class="fab fa-twitter"></i>
            </a>
            <a href="https://linkedin.com/in/{{ site.social.linkedin }}" title="LinkedIn">
                <i class="fab fa-linkedin"></i>
            </a>
            <a href="{{ '/assets/cv/Blake_CV.pdf' | relative_url }}" title="CV" target="_blank">
                <i class="fas fa-file-alt"></i>
            </a>
        </div>
    </div>
    <div class="scroll-indicator">
        <i class="fas fa-chevron-down"></i>
    </div>
</section>

<nav class="floating-nav">
    <ul>
        <li><a href="#research" data-tooltip="Research"></a></li>
        <li><a href="#publications" data-tooltip="Publications"></a></li>
        <li><a href="#contact" data-tooltip="Contact"></a></li>
    </ul>
</nav>

<div class="main-content">
    <section id="research" class="section">
        <h2>Alpha Lab</h2>
        <div class="research-grid">
            <div class="research-card student-card">
                <div class="student-photo">
                    <img src="{{ '/assets/images/amrit-panda.jpg' | relative_url }}" alt="Amrit Panda">
                </div>
                <h3>Amrit Panda</h3>
                <p class="student-title">PhD Student</p>
                <p>Exploring how personality, morality and environmental ambiguity shape entrepreneurial strategy and market creation using econometric modeling, linguistic analysis, and comparative qualitative research.</p>
            </div>
            <div class="research-card student-card">
                <div class="student-photo">
                    <img src="{{ '/assets/images/mahija-ratnoo.jpg' | relative_url }}" alt="Mahija Ratnoo">
                </div>
                <h3>Mahija Ratnoo</h3>
                <p class="student-title">PhD Student</p>
                <p>Exploring the intersection of behavioral psychology and data analytics to understand how leadership traits influence organizational outcomes and strategic decision-making.</p>
            </div>
        </div>
    </section>

<section id="publications" class="section">
    <h2>Publications</h2>
    <div class="pub-themes">
        <div class="pub-theme-col">
            <h4>Founders</h4>
            <div class="pub-cards">
            {% assign founders = site.data.publications | where: "theme", "founders" %}
            {% for pub in founders %}
            <div class="pub-theme-item">
                <div class="pub-venue-year">{{ pub.venue }} ({{ pub.year }})</div>
                <div class="pub-title-short">{{ pub.title }}</div>
                {% if pub.citations > 0 %}<div class="pub-citations">{{ pub.citations }} citations</div>{% endif %}
                {% if pub.note %}<div class="pub-note">{{ pub.note }}</div>{% endif %}
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
                {% if pub.citations > 0 %}<div class="pub-citations">{{ pub.citations }} citations</div>{% endif %}
                {% if pub.note %}<div class="pub-note">{{ pub.note }}</div>{% endif %}
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
                {% if pub.citations > 0 %}<div class="pub-citations">{{ pub.citations }} citations</div>{% endif %}
                {% if pub.note %}<div class="pub-note">{{ pub.note }}</div>{% endif %}
            </div>
            {% endfor %}
            </div>
        </div>
    </div>
</section>

    <section id="contact" class="section">
        <h2>Contact</h2>
        <div class="contact-info">
            <div class="contact-item">
                <i class="fas fa-envelope"></i>
                <a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a>
            </div>
            <div class="contact-item">
                <i class="fas fa-building"></i>
                <span>{{ site.author.institution }}</span>
            </div>
            <div class="contact-item">
                <i class="fas fa-map-marker-alt"></i>
                <span>{{ site.author.location }}</span>
            </div>
        </div>
    </section>
</div>

<footer class="footer">
    <div class="container">
        <p>&copy; 2026 {{ site.author.name }}. All rights reserved.</p>
    </div>
</footer>

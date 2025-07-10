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
        </div>
    </div>
    <div class="scroll-indicator">
        <i class="fas fa-chevron-down"></i>
    </div>
</section>

<nav class="floating-nav">
    <ul>
        <li><a href="#about" data-tooltip="About"></a></li>
        <li><a href="#research" data-tooltip="Research"></a></li>
        <li><a href="#publications" data-tooltip="Publications"></a></li>
        <li><a href="#contact" data-tooltip="Contact"></a></li>
    </ul>
</nav>

<div class="main-content">
    <section id="about" class="section">
        <h2>About Me</h2>
        <p>I am an Assistant Professor of Data Science at {{ site.author.institution }}, where I conduct research at the intersection of artificial intelligence, machine learning, and computational methods. My work focuses on developing novel algorithms and methodologies that can extract meaningful insights from complex, high-dimensional data.</p>
        
        <p>I am particularly passionate about bridging the gap between theoretical foundations and practical applications, with a focus on solving real-world problems through innovative data science approaches. My research spans multiple domains including natural language processing, computer vision, and statistical learning theory.</p>
        
        <p>Beyond research, I am deeply committed to teaching and mentoring the next generation of data scientists and AI researchers. I believe in fostering inclusive environments where diverse perspectives can contribute to advancing our understanding of intelligent systems.</p>
    </section>

    <section id="research" class="section">
        <h2>Alpha Lab</h2>
        <div class="research-grid">
            <div class="research-card student-card">
                <div class="student-photo">
                    <img src="{{ '/assets/images/amrit-panda.jpg' | relative_url }}" alt="Amrit Panda">
                </div>
                <h3>Amrit Panda</h3>
                <p class="student-title">PhD Student</p>
                <p>Investigating how natural language processing and machine learning can reveal hidden patterns in entrepreneurial communication and investor decision-making processes.</p>
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
    <div class="publications-container">
        {% for pub in site.data.publications %}
        <div class="publication-item">
            <div class="title">{{ pub.title }}</div>
            <div class="authors">{{ pub.authors }}</div>
            <div class="venue">{{ pub.venue }} ({{ pub.year }})</div>
            <div class="date">{{ pub.date }}</div>
            {% if pub.citations > 0 %}
            <div class="citations">{{ pub.citations }} citations</div>
            {% endif %}
            {% if pub.url %}
            <div class="links">
                <a href="{{ pub.url }}" target="_blank">View Paper</a>
            </div>
            {% endif %}
        </div>
        {% endfor %}
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
        <p>&copy; 2025 {{ site.author.name }}. All rights reserved.</p>
    </div>
</footer>

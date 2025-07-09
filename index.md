---
layout: default
title: Home
---

<section class="hero">
    <div class="hero-content">
        <div class="profile-image">
            <img src="{{ '/assets/images/profile.jpg' | relative_url }}" alt="{{ site.author.name }}">
        </div>
        <h1 class="hero-title">{{ site.author.name }}</h1>
        <p class="hero-subtitle">{{ site.author.title }}</p>
        <p class="hero-bio">{{ site.author.bio }}</p>
        
        <div class="social-links">
            {% if site.author.email %}
            <a href="mailto:{{ site.author.email }}" title="Email">
                <i class="fas fa-envelope"></i>
            </a>
            {% endif %}
            {% if site.social.google_scholar %}
            <a href="https://scholar.google.com/citations?user={{ site.social.google_scholar }}" title="Google Scholar">
                <i class="fas fa-graduation-cap"></i>
            </a>
            {% endif %}
            {% if site.social.github %}
            <a href="https://github.com/{{ site.social.github }}" title="GitHub">
                <i class="fab fa-github"></i>
            </a>
            {% endif %}
            {% if site.social.twitter %}
            <a href="https://twitter.com/{{ site.social.twitter }}" title="Twitter">
                <i class="fab fa-twitter"></i>
            </a>
            {% endif %}
            {% if site.social.linkedin %}
            <a href="https://linkedin.com/in/{{ site.social.linkedin }}" title="LinkedIn">
                <i class="fab fa-linkedin"></i>
            </a>
            {% endif %}
            {% if site.social.orcid %}
            <a href="https://orcid.org/{{ site.social.orcid }}" title="ORCID">
                <i class="fab fa-orcid"></i>
            </a>
            {% endif %}
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
        <h2>Research Interests</h2>
        <div class="research-grid">
            <div class="research-card">
                <div class="icon">
                    <i class="fas fa-brain"></i>
                </div>
                <h3>Machine Learning</h3>
                <p>Developing novel algorithms for supervised and unsupervised learning, with a focus on deep learning architectures and optimization techniques.</p>
            </div>
            <div class="research-card">
                <div class="icon">
                    <i class="fas fa-chart-line"></i>
                </div>
                <h3>Data Science</h3>
                <p>Applying statistical methods and computational techniques to extract insights from large-scale, complex datasets across various domains.</p>
            </div>
            <div class="research-card">
                <div class="icon">
                    <i class="fas fa-robot"></i>
                </div>
                <h3>Artificial Intelligence</h3>
                <p>Researching intelligent systems that can learn, reason, and make decisions in complex environments with minimal human intervention.</p>
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
                <div class="venue">{{ pub.venue }}</div>
                <div class="date">{{ pub.date }}</div>
                <div class="links">
                    {% if pub.pdf %}
                    <a href="{{ pub.pdf }}" target="_blank">PDF</a>
                    {% endif %}
                    {% if pub.code %}
                    <a href="{{ pub.code }}" tar
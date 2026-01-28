#!/usr/bin/env python3
"""Create a visually enhanced website with icons, graphics, and better layout."""

import re

# Read the markdown file
with open('ai-comprehensive-guide.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# HTML template with enhanced visuals
html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="A comprehensive, non-technical guide to understanding AI in 2026 - tools, applications, and the future of artificial intelligence">
    <title>AI 2026: The Complete Guide to Artificial Intelligence</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">

    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>

    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Theme Toggle -->
    <button class="theme-toggle" id="themeToggle" aria-label="Toggle theme">
        <i data-lucide="sun" class="sun-icon"></i>
        <i data-lucide="moon" class="moon-icon"></i>
    </button>

    <!-- Navigation -->
    <nav class="navbar" id="navbar">
        <div class="nav-container">
            <div class="nav-logo">
                <i data-lucide="brain-circuit"></i>
                <span class="logo-text">AI 2026</span>
            </div>
            <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <ul class="nav-menu" id="navMenu">
                <li><a href="#hero" class="nav-link"><i data-lucide="home"></i> Home</a></li>
                <li><a href="#introduction" class="nav-link"><i data-lucide="sparkles"></i> Intro</a></li>
                <li><a href="#what-is-ai" class="nav-link"><i data-lucide="cpu"></i> What is AI?</a></li>
                <li><a href="#ai-tools" class="nav-link"><i data-lucide="wrench"></i> Tools</a></li>
                <li><a href="#applications" class="nav-link"><i data-lucide="rocket"></i> Use Cases</a></li>
                <li><a href="#getting-started" class="nav-link"><i data-lucide="play-circle"></i> Get Started</a></li>
            </ul>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero" id="hero">
        <div class="hero-background">
            <div class="gradient-orb orb-1"></div>
            <div class="gradient-orb orb-2"></div>
            <div class="gradient-orb orb-3"></div>
        </div>
        <div class="hero-content">
            <div class="hero-badge">
                <i data-lucide="zap"></i>
                <span>Updated for 2026</span>
            </div>
            <h1 class="hero-title">
                <span class="title-line">The Complete Guide</span>
                <span class="title-line gradient-text">to Artificial Intelligence</span>
            </h1>
            <p class="hero-subtitle">
                A comprehensive, non-technical exploration of AI fundamentals, tools, applications, and the future.
            </p>
            <div class="hero-stats">
                <div class="stat">
                    <i data-lucide="file-text"></i>
                    <div class="stat-number">13,500+</div>
                    <div class="stat-label">Words</div>
                </div>
                <div class="stat">
                    <i data-lucide="book-open"></i>
                    <div class="stat-number">13</div>
                    <div class="stat-label">Chapters</div>
                </div>
                <div class="stat">
                    <i data-lucide="clock"></i>
                    <div class="stat-number">60+</div>
                    <div class="stat-label">Min Read</div>
                </div>
            </div>
            <div class="hero-cta">
                <a href="#introduction" class="btn btn-primary">
                    <i data-lucide="book-open"></i>
                    Start Reading
                </a>
                <a href="ai-comprehensive-guide.md" class="btn btn-secondary" download>
                    <i data-lucide="download"></i>
                    Download Guide
                </a>
            </div>
        </div>
        <div class="scroll-indicator">
            <div class="mouse">
                <div class="wheel"></div>
            </div>
        </div>
    </section>

    <!-- Quick Features -->
    <section class="quick-features">
        <div class="container">
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">
                        <i data-lucide="graduation-cap"></i>
                    </div>
                    <h3>Beginner Friendly</h3>
                    <p>No technical background needed. Learn AI concepts in plain English.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">
                        <i data-lucide="trending-up"></i>
                    </div>
                    <h3>2026 Updated</h3>
                    <p>Latest trends, tools, and real-world applications from 2026.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">
                        <i data-lucide="lightbulb"></i>
                    </div>
                    <h3>Practical Guide</h3>
                    <p>Step-by-step instructions to start using AI today.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">
                        <i data-lucide="shield-check"></i>
                    </div>
                    <h3>Ethics & Safety</h3>
                    <p>Learn responsible AI use and understand limitations.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Table of Contents with Visual Icons -->
    <section class="visual-toc" id="toc">
        <div class="container">
            <div class="section-header">
                <i data-lucide="map"></i>
                <h2 class="section-title">Your Learning Journey</h2>
                <p class="section-subtitle">13 comprehensive chapters to master AI fundamentals</p>
            </div>
            <div class="toc-timeline">
                <div class="timeline-item" data-chapter="1">
                    <div class="timeline-icon">
                        <i data-lucide="sparkles"></i>
                    </div>
                    <div class="timeline-content">
                        <a href="#introduction">
                            <h3>Introduction</h3>
                            <p>Welcome to the Age of AI</p>
                        </a>
                    </div>
                </div>
                <div class="timeline-item" data-chapter="2">
                    <div class="timeline-icon">
                        <i data-lucide="brain"></i>
                    </div>
                    <div class="timeline-content">
                        <a href="#what-is-ai">
                            <h3>What is AI?</h3>
                            <p>Understanding the fundamentals</p>
                        </a>
                    </div>
                </div>
                <div class="timeline-item" data-chapter="3">
                    <div class="timeline-icon">
                        <i data-lucide="cog"></i>
                    </div>
                    <div class="timeline-content">
                        <a href="#how-ai-works">
                            <h3>How AI Works</h3>
                            <p>The basics explained simply</p>
                        </a>
                    </div>
                </div>
                <div class="timeline-item" data-chapter="4">
                    <div class="timeline-icon">
                        <i data-lucide="layers"></i>
                    </div>
                    <div class="timeline-content">
                        <a href="#types-of-ai">
                            <h3>Types of AI</h3>
                            <p>ML, Deep Learning & Generative AI</p>
                        </a>
                    </div>
                </div>
                <div class="timeline-item" data-chapter="5">
                    <div class="timeline-icon">
                        <i data-lucide="wrench"></i>
                    </div>
                    <div class="timeline-content">
                        <a href="#ai-tools">
                            <h3>AI Tools</h3>
                            <p>ChatGPT, Claude, Gemini & more</p>
                        </a>
                    </div>
                </div>
                <div class="timeline-item" data-chapter="6">
                    <div class="timeline-icon">
                        <i data-lucide="rocket"></i>
                    </div>
                    <div class="timeline-content">
                        <a href="#applications">
                            <h3>Applications</h3>
                            <p>Real-world AI in action</p>
                        </a>
                    </div>
                </div>
                <div class="timeline-item" data-chapter="7">
                    <div class="timeline-icon">
                        <i data-lucide="building-2"></i>
                    </div>
                    <div class="timeline-content">
                        <a href="#industries">
                            <h3>Industries</h3>
                            <p>Healthcare, Finance, Education</p>
                        </a>
                    </div>
                </div>
                <div class="timeline-item" data-chapter="8">
                    <div class="timeline-icon">
                        <i data-lucide="play-circle"></i>
                    </div>
                    <div class="timeline-content">
                        <a href="#getting-started">
                            <h3>Getting Started</h3>
                            <p>Your practical guide</p>
                        </a>
                    </div>
                </div>
                <div class="timeline-item" data-chapter="9">
                    <div class="timeline-icon">
                        <i data-lucide="scale"></i>
                    </div>
                    <div class="timeline-content">
                        <a href="#ethics">
                            <h3>Ethics</h3>
                            <p>Responsible AI use</p>
                        </a>
                    </div>
                </div>
                <div class="timeline-item" data-chapter="10">
                    <div class="timeline-icon">
                        <i data-lucide="alert-circle"></i>
                    </div>
                    <div class="timeline-content">
                        <a href="#limitations">
                            <h3>Limitations</h3>
                            <p>What AI cannot do</p>
                        </a>
                    </div>
                </div>
                <div class="timeline-item" data-chapter="11">
                    <div class="timeline-icon">
                        <i data-lucide="telescope"></i>
                    </div>
                    <div class="timeline-content">
                        <a href="#future">
                            <h3>The Future</h3>
                            <p>Trends and predictions</p>
                        </a>
                    </div>
                </div>
                <div class="timeline-item" data-chapter="12">
                    <div class="timeline-icon">
                        <i data-lucide="award"></i>
                    </div>
                    <div class="timeline-content">
                        <a href="#skills">
                            <h3>Skills</h3>
                            <p>Thrive in the AI era</p>
                        </a>
                    </div>
                </div>
                <div class="timeline-item" data-chapter="13">
                    <div class="timeline-icon">
                        <i data-lucide="flag"></i>
                    </div>
                    <div class="timeline-content">
                        <a href="#conclusion">
                            <h3>Conclusion</h3>
                            <p>Your AI journey begins</p>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Banner -->
    <section class="cta-banner">
        <div class="container">
            <div class="cta-content">
                <i data-lucide="zap" class="cta-icon"></i>
                <h2>Ready to Master AI?</h2>
                <p>Start your journey into artificial intelligence today</p>
                <a href="#introduction" class="btn btn-primary btn-large">
                    <i data-lucide="arrow-right"></i>
                    Begin Learning
                </a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <div class="footer-logo">
                        <i data-lucide="brain-circuit"></i>
                        <h3>AI 2026 Guide</h3>
                    </div>
                    <p>A comprehensive, non-technical exploration of artificial intelligence.</p>
                    <div class="footer-social">
                        <a href="https://github.com/friscodanconia/ai-2026-guide" target="_blank" rel="noopener">
                            <i data-lucide="github"></i>
                        </a>
                        <a href="https://aibasics.vercel.app" target="_blank" rel="noopener">
                            <i data-lucide="globe"></i>
                        </a>
                    </div>
                </div>
                <div class="footer-section">
                    <h4><i data-lucide="book-open"></i> Chapters</h4>
                    <ul>
                        <li><a href="#introduction">Introduction</a></li>
                        <li><a href="#what-is-ai">What is AI?</a></li>
                        <li><a href="#ai-tools">AI Tools</a></li>
                        <li><a href="#getting-started">Get Started</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4><i data-lucide="download"></i> Resources</h4>
                    <ul>
                        <li><a href="ai-comprehensive-guide.md" download>Download Guide</a></li>
                        <li><a href="#toc">Table of Contents</a></li>
                        <li><a href="#hero">Back to Top</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4><i data-lucide="info"></i> About</h4>
                    <p>Created through comprehensive research from 50+ authoritative AI sources.</p>
                    <p class="footer-stat">
                        <i data-lucide="calendar"></i>
                        Updated January 2026
                    </p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 AI Guide. Educational resource on artificial intelligence.</p>
            </div>
        </div>
    </footer>

    <script src="script.js"></script>
    <script>
        // Initialize Lucide icons
        lucide.createIcons();
    </script>
</body>
</html>'''

# Write the new visual HTML file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("✅ Visual website created!")
print("🎨 Added features:")
print("   - Lucide icon library")
print("   - Visual timeline for chapters")
print("   - Feature cards with icons")
print("   - Better visual hierarchy")
print("   - CTA banners")
print("   - Icon-enhanced navigation")
print("\n🌐 View at: http://localhost:8000")

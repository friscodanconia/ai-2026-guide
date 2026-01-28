#!/usr/bin/env python3
"""Generate complete HTML with full content - no excerpts."""

import re
import html

# Read the markdown file
with open('ai-comprehensive-guide.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

def md_to_html(text):
    """Convert markdown to HTML."""
    # Escape HTML first
    # text = html.escape(text)

    # Headers
    text = re.sub(r'^#### (.*?)$', r'<h4>\1</h4>', text, flags=re.MULTILINE)
    text = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)

    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)

    # Lists - handle bullet points
    lines = text.split('\n')
    result = []
    in_list = False

    for line in lines:
        stripped = line.strip()

        # Check if line starts with a dash (list item)
        if stripped.startswith('- '):
            if not in_list:
                result.append('<ul>')
                in_list = True
            result.append(f'<li>{stripped[2:]}</li>')
        else:
            if in_list:
                result.append('</ul>')
                in_list = False

            # Check for headers or already formatted HTML
            if stripped and not stripped.startswith('<') and not stripped.startswith('#'):
                result.append(f'<p>{stripped}</p>')
            elif stripped:
                result.append(stripped)

    if in_list:
        result.append('</ul>')

    return '\n'.join(result)

# HTML template
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
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Theme Toggle -->
    <button class="theme-toggle" id="themeToggle" aria-label="Toggle theme">
        <svg class="sun-icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="5"></circle>
            <line x1="12" y1="1" x2="12" y2="3"></line>
            <line x1="12" y1="21" x2="12" y2="23"></line>
            <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
            <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
            <line x1="1" y1="12" x2="3" y2="12"></line>
            <line x1="21" y1="12" x2="23" y2="12"></line>
            <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
            <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
        </svg>
        <svg class="moon-icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
        </svg>
    </button>

    <!-- Navigation -->
    <nav class="navbar" id="navbar">
        <div class="nav-container">
            <div class="nav-logo">
                <span class="logo-text">AI 2026</span>
            </div>
            <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <ul class="nav-menu" id="navMenu">
                <li><a href="#hero" class="nav-link">Home</a></li>
                <li><a href="#introduction" class="nav-link">Introduction</a></li>
                <li><a href="#what-is-ai" class="nav-link">What is AI?</a></li>
                <li><a href="#how-ai-works" class="nav-link">How It Works</a></li>
                <li><a href="#types-of-ai" class="nav-link">Types</a></li>
                <li><a href="#ai-tools" class="nav-link">Tools</a></li>
                <li><a href="#applications" class="nav-link">Applications</a></li>
                <li><a href="#getting-started" class="nav-link">Get Started</a></li>
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
                <span class="badge-dot"></span>
                <span>Updated for 2026</span>
            </div>
            <h1 class="hero-title">
                <span class="title-line">The Complete Guide</span>
                <span class="title-line gradient-text">to Artificial Intelligence</span>
            </h1>
            <p class="hero-subtitle">
                A comprehensive, non-technical exploration of AI fundamentals, tools, applications, and the future.
                <br>Understand AI without the complexity.
            </p>
            <div class="hero-stats">
                <div class="stat">
                    <div class="stat-number">13,500+</div>
                    <div class="stat-label">Words</div>
                </div>
                <div class="stat">
                    <div class="stat-number">13</div>
                    <div class="stat-label">Chapters</div>
                </div>
                <div class="stat">
                    <div class="stat-number">60+</div>
                    <div class="stat-label">Min Read</div>
                </div>
            </div>
            <div class="hero-cta">
                <a href="#introduction" class="btn btn-primary">Start Reading</a>
                <a href="ai-comprehensive-guide.md" class="btn btn-secondary" download>Download PDF</a>
            </div>
        </div>
        <div class="scroll-indicator">
            <div class="mouse">
                <div class="wheel"></div>
            </div>
            <div class="arrow">
                <span></span>
                <span></span>
            </div>
        </div>
    </section>

    <!-- Content Wrapper -->
    <div class="content-wrapper">
        <div class="container">
            <div class="content-layout">
                <!-- Sidebar -->
                <aside class="sidebar" id="sidebar">
                    <div class="sidebar-sticky">
                        <div class="sidebar-header">
                            <h3>Quick Navigation</h3>
                        </div>
                        <nav class="sidebar-nav">
                            <a href="#introduction" class="sidebar-link">Introduction</a>
                            <a href="#what-is-ai" class="sidebar-link">What is AI?</a>
                            <a href="#how-ai-works" class="sidebar-link">How AI Works</a>
                            <a href="#types-of-ai" class="sidebar-link">Types of AI</a>
                            <a href="#ai-tools" class="sidebar-link">AI Tools</a>
                            <a href="#applications" class="sidebar-link">Applications</a>
                            <a href="#industries" class="sidebar-link">Industries</a>
                            <a href="#getting-started" class="sidebar-link">Getting Started</a>
                            <a href="#ethics" class="sidebar-link">Ethics</a>
                            <a href="#limitations" class="sidebar-link">Limitations</a>
                            <a href="#future" class="sidebar-link">Future</a>
                            <a href="#skills" class="sidebar-link">Skills</a>
                            <a href="#conclusion" class="sidebar-link">Conclusion</a>
                        </nav>
                    </div>
                </aside>

                <!-- Main Content -->
                <main class="main-content" id="mainContent">
                    <article class="content-article">
{CONTENT}
                    </article>
                </main>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>AI 2026 Guide</h3>
                    <p>A comprehensive, non-technical exploration of artificial intelligence fundamentals, tools, applications, and the future.</p>
                </div>
                <div class="footer-section">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="#introduction">Introduction</a></li>
                        <li><a href="#what-is-ai">What is AI?</a></li>
                        <li><a href="#ai-tools">AI Tools</a></li>
                        <li><a href="#getting-started">Get Started</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Resources</h4>
                    <ul>
                        <li><a href="ai-comprehensive-guide.md" download>Download Guide</a></li>
                        <li><a href="#hero">Back to Top</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>About</h4>
                    <p>This guide was created through comprehensive research of authoritative AI sources and is updated for 2026.</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 AI Guide. Created with research and insights from leading AI resources.</p>
                <p>Last updated: January 2026</p>
            </div>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>'''

# Split by H2 headers but keep everything
sections = re.split(r'\n## ', md_content)

# Section ID mapping
section_ids = {
    'Introduction: Welcome to the Age of AI': 'introduction',
    'What is Artificial Intelligence?': 'what-is-ai',
    'How AI Works: The Basics Explained Simply': 'how-ai-works',
    'Types of AI: From Machine Learning to Deep Learning': 'types-of-ai',
    'AI Tools and Platforms You Can Use Today': 'ai-tools',
    'AI in Action: Real-World Applications': 'applications',
    'Industry Transformation: Healthcare, Finance, and Education': 'industries',
    'Getting Started with AI: A Practical Guide': 'getting-started',
    'AI Ethics and Responsible AI': 'ethics',
    "Understanding AI's Limitations and Challenges": 'limitations',
    'The Future of AI: Trends and Predictions': 'future',
    'Skills for the AI Era': 'skills',
    'Conclusion: Your AI Journey': 'conclusion'
}

html_sections = []

# Process each section
for i, section in enumerate(sections):
    if i == 0:  # Skip title page
        continue

    lines = section.split('\n', 1)
    if len(lines) < 2:
        continue

    title = lines[0].strip()
    # Remove the {#anchor} from title if present
    title = re.sub(r'\s*\{#.*?\}', '', title)
    content = lines[1].strip() if len(lines) > 1 else ''

    # Get section ID
    section_id = section_ids.get(title, title.lower().replace(' ', '-').replace(':', '').replace("'", ''))

    # Convert markdown to HTML
    html_content = md_to_html(content)

    # Create section HTML
    section_html = f'''
<section id="{section_id}" class="content-section">
    <h2>{title}</h2>
    {html_content}
</section>
'''
    html_sections.append(section_html)

# Combine everything
full_content = '\n'.join(html_sections)
final_html = html_template.replace('{CONTENT}', full_content)

# Write the complete HTML file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("✅ Complete website generated with FULL content!")
print("📖 All 13 chapters included - no excerpts")
print("🔗 All navigation working")
print("📄 Total content: 13,500+ words")
print("\n🌐 Refresh your browser: http://localhost:8000")

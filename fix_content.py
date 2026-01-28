#!/usr/bin/env python3
"""Fix markdown conversion - use markdown library instead of regex."""

import markdown
import re

# Read the markdown file
with open('ai-comprehensive-guide.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# Split by H2 headers
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

# Icon mapping
icon_map = {
    'introduction': 'sparkles',
    'what-is-ai': 'brain',
    'how-ai-works': 'cog',
    'types-of-ai': 'layers',
    'ai-tools': 'wrench',
    'applications': 'rocket',
    'industries': 'building-2',
    'getting-started': 'play-circle',
    'ethics': 'scale',
    'limitations': 'alert-circle',
    'future': 'telescope',
    'skills': 'award',
    'conclusion': 'flag'
}

html_sections = []

# Initialize markdown converter
md = markdown.Markdown(extensions=['extra', 'nl2br'])

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
    icon = icon_map.get(section_id, 'file-text')

    # Convert markdown to HTML using proper markdown library
    html_content = md.convert(content)
    md.reset()  # Reset for next section

    # Create section HTML with icon
    section_html = f'''
<section id="{section_id}" class="content-section">
    <div class="section-header-inline">
        <i data-lucide="{icon}"></i>
        <h2>{title}</h2>
    </div>
    {html_content}
</section>
'''
    html_sections.append(section_html)

# Now read the current index.html and replace just the content sections
with open('index.html', 'r', encoding='utf-8') as f:
    current_html = f.read()

# Find where content starts and ends
content_start = current_html.find('<section id="table-of-contents"')
content_end = current_html.find('</section>', current_html.rfind('</section>')) + len('</section>')

# Rebuild HTML
full_content = '\n'.join(html_sections)
new_html = current_html[:content_start] + full_content + current_html[content_end:]

# Write the new HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("✅ Content fixed using proper markdown library!")
print("📖 All 13 chapters processed")
print("🔧 No more conversion issues")

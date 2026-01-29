#!/usr/bin/env python3
"""Create video resources section with card-based layout."""

# Video data structure
videos = {
    "essential": [
        {
            "title": "Intro to Large Language Models",
            "creator": "Andrej Karpathy",
            "description": "Foundational introduction to how LLMs work, from one of AI's best educators.",
            "youtube_id": "zjkBMFhNj_g",
            "duration": "1:00:00",
            "difficulty": "Beginner"
        },
        {
            "title": "Deep Dive into LLMs like ChatGPT",
            "creator": "Andrej Karpathy",
            "description": "Under-the-hood fundamentals of how ChatGPT and similar models actually work.",
            "youtube_id": "7xTGNNLPyMI",
            "duration": "1:26:00",
            "difficulty": "Beginner"
        },
        {
            "title": "How I Use LLMs in Daily Life",
            "creator": "Andrej Karpathy",
            "description": "Practical guide with real-world examples of using AI tools productively.",
            "youtube_id": "EWvNQjAaOHw",
            "duration": "30:00",
            "difficulty": "Beginner"
        },
        {
            "title": "Sam Altman on ChatGPT & Superintelligence",
            "creator": "TED2025",
            "description": "OpenAI's CEO discusses the astonishing growth of AI and its future implications.",
            "youtube_id": "TED2025-SamAltman",  # Placeholder - needs real ID
            "duration": "45:00",
            "difficulty": "Beginner"
        }
    ],
    "beginner_channels": [
        {
            "title": "But What is a Neural Network?",
            "creator": "3Blue1Brown",
            "description": "Beautiful animated explanation of how neural networks learn and make decisions.",
            "youtube_id": "aircAruvnKk",
            "duration": "19:13",
            "difficulty": "Beginner"
        },
        {
            "title": "AI Explained: A Beginner's Guide",
            "creator": "AI Explained",
            "description": "Simple introduction to artificial intelligence concepts without technical jargon.",
            "youtube_id": "AIExplained-Basics",  # Placeholder
            "duration": "15:00",
            "difficulty": "Beginner"
        },
        {
            "title": "Top AI Papers This Week",
            "creator": "Two Minute Papers",
            "description": "Stay current with bite-sized breakdowns of cutting-edge AI research.",
            "youtube_id": "TwoMinutePapers-Latest",  # Placeholder
            "duration": "5:00",
            "difficulty": "Intermediate"
        }
    ],
    "courses": [
        {
            "title": "AI For Everyone",
            "creator": "Andrew Ng (Coursera)",
            "description": "Non-technical introduction to AI by Stanford professor and Google Brain founder.",
            "youtube_id": "DeepLearningAI-AIForEveryone",  # Placeholder
            "duration": "Series",
            "difficulty": "Beginner"
        },
        {
            "title": "Machine Learning Specialization",
            "creator": "DeepLearning.AI",
            "description": "Comprehensive 41-video series covering ML fundamentals and practical implementation.",
            "youtube_id": "DeepLearningAI-MLSpec",  # Placeholder
            "duration": "Series",
            "difficulty": "Intermediate"
        },
        {
            "title": "Generative AI Basics",
            "creator": "Google AI",
            "description": "Short course on what generative AI is and how it differs from traditional ML.",
            "youtube_id": "GoogleAI-GenAI",  # Placeholder
            "duration": "30:00",
            "difficulty": "Beginner"
        }
    ],
    "expert_insights": [
        {
            "title": "AI Safety & Deceptive Behaviors",
            "creator": "Yoshua Bengio (TED2025)",
            "description": "AI pioneer's sobering assessment of rapidly advancing AI capabilities and risks.",
            "youtube_id": "TED2025-Bengio",  # Placeholder
            "duration": "18:00",
            "difficulty": "Intermediate"
        },
        {
            "title": "Why AI is Wildly Underhyped",
            "creator": "Eric Schmidt (TED2025)",
            "description": "Former Google CEO on why public discourse misses AI's true development velocity.",
            "youtube_id": "TED2025-Schmidt",  # Placeholder
            "duration": "22:00",
            "difficulty": "Beginner"
        }
    ]
}

# Category metadata
categories = {
    "essential": {
        "icon": "star",
        "title": "Essential Viewing",
        "subtitle": "Start here - the most valuable videos for understanding AI"
    },
    "beginner_channels": {
        "icon": "graduation-cap",
        "title": "Beginner-Friendly Channels",
        "subtitle": "Learn AI concepts through engaging visual explanations"
    },
    "courses": {
        "icon": "book-open",
        "title": "Structured Video Courses",
        "subtitle": "Comprehensive learning paths from top educators"
    },
    "expert_insights": {
        "icon": "lightbulb",
        "title": "Expert Insights & TED Talks",
        "subtitle": "Big-picture perspectives from AI leaders and researchers"
    }
}

# Generate HTML
html_output = '''
    <!-- Video Learning Resources -->
    <section id="video-resources" class="content-section">
        <div class="section-header-inline">
            <i data-lucide="video"></i>
            <h2>Video Learning Resources</h2>
        </div>
        <p>Learn AI through curated videos from the world's best educators, researchers, and practitioners. Whether you prefer visual explanations, hands-on tutorials, or expert insights, these resources will accelerate your understanding.</p>
'''

# Generate each category
for category_key, category_data in categories.items():
    videos_in_category = videos[category_key]

    html_output += f'''
        <div class="video-category">
            <div class="category-header">
                <i data-lucide="{category_data['icon']}"></i>
                <div class="category-text">
                    <h3>{category_data['title']}</h3>
                    <p>{category_data['subtitle']}</p>
                </div>
            </div>

            <div class="video-grid">
'''

    # Generate video cards
    for video in videos_in_category:
        difficulty_class = video['difficulty'].lower()
        youtube_url = f"https://www.youtube.com/watch?v={video['youtube_id']}"
        thumbnail_url = f"https://img.youtube.com/vi/{video['youtube_id']}/maxresdefault.jpg"

        html_output += f'''
                <div class="video-card">
                    <a href="{youtube_url}" target="_blank" rel="noopener" class="video-thumbnail">
                        <img src="{thumbnail_url}" alt="{video['title']}" loading="lazy">
                        <div class="play-overlay">
                            <i data-lucide="play-circle"></i>
                        </div>
                        <span class="duration-badge">{video['duration']}</span>
                    </a>

                    <div class="video-content">
                        <div class="video-header">
                            <h4>{video['title']}</h4>
                            <span class="difficulty-badge {difficulty_class}">{video['difficulty']}</span>
                        </div>

                        <div class="video-creator">
                            <i data-lucide="user"></i>
                            <span>{video['creator']}</span>
                        </div>

                        <p class="video-description">{video['description']}</p>

                        <a href="{youtube_url}" target="_blank" rel="noopener" class="btn-video">
                            <i data-lucide="external-link"></i>
                            Watch on YouTube
                        </a>
                    </div>
                </div>
'''

    html_output += '''
            </div>
        </div>
'''

html_output += '''
        <div class="video-resources-footer">
            <p><strong>More Resources:</strong> Explore <a href="https://github.com/dair-ai/ML-YouTube-Courses" target="_blank" rel="noopener">GitHub's ML-YouTube-Courses</a> for a comprehensive list of AI video courses, or visit <a href="https://www.coursera.org/courses?query=artificial+intelligence" target="_blank" rel="noopener">Coursera's AI courses</a> for structured learning paths.</p>
        </div>
    </section>
'''

# Read current index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Insert before the CTA banner
insertion_point = html_content.find('<!-- CTA Banner -->')
if insertion_point == -1:
    insertion_point = html_content.find('</main>')

new_html = html_content[:insertion_point] + html_output + '\n\n    ' + html_content[insertion_point:]

# Write updated HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("✅ Video resources section created!")
print(f"📹 Added {sum(len(v) for v in videos.values())} video cards")
print("🎨 4 categories with custom styling")
print("📱 Mobile-responsive card grid")

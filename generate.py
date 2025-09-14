#!/usr/bin/env python3
"""
Static HTML Generator using Jinja2
Generates static HTML files from templates and data
"""

import os
import json
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Mailchimp configuration from environment variables
mailing_list = {
    'form_url': os.getenv('MAILCHIMP_FORM_URL', '')
}

# Data for the AI facts
ai_facts = [
    {
        'id': 'card1',
        'title': 'Hundreds of AI leaders, including Nobel Prize-winning scientists and CEOs, agreed that AI could lead to human extinction.',
        'content': """
<p>In 2023, over 500 AI scientists signed this statement:</p>

<h5 style="font-family: Cormorant, sans-serif;">"Mitigating the risk of extinction from AI should be a global priority alongside other societal-scale risks such as pandemics and nuclear war."</h5>

<p>These include Yoshua Bengio and Nobel Prize winner Geoffrey Hinton, the two most highly-cited scientists of all time, who pioneered the techniques underlying all of today’s AI systems.  Hinton quit his job at Google in 2023 to warn the public about the dangers of AI.</p>

<div class="embed-responsive embed-responsive-16by9 mb-3">
    <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/66WiF8fXL0k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

<p>On average, AI researchers believe there’s a <b>~15% chance</b> of extremely bad, extinction-level outcomes.</p>
"""
    },
    {
        'id': 'card2',
        'title': 'Researchers still don\'t understand how AI systems work, even after decades of work and thousands of papers.',
        'content': 'This is a fundamental problem in AI safety - we\'re building systems we don\'t fully understand.'
    },
    {
        'id': 'card3',
        'title': 'AI systems can deceive humans even when trained not to do so.',
        'content': 'Research shows that AI models can learn to lie and manipulate, even when explicitly trained to be truthful.'
    },
    {
        'id': 'card4',
        'title': 'AI companies have repeatedly reneged on their own safety commitments.',
        'content': 'Existing safety techniques like RLHF may not scale to superintelligent AI systems.'
    },
    {
        'id': 'card5',
        'title': 'AI researchers have admitted being surprised at how fast recent AI progress has been.',
        'content': 'The capabilities gap is widening between what AI can do and what we can safely control.'
    },
    {
        'id': 'card6',
        'title': 'AI systems can learn to pursue unintended goals that conflict with human values.',
        'content': 'This is known as the alignment problem - ensuring AI goals match human intentions.'
    },
    {
        'id': 'card7',
        'title': 'Once AI systems become superintelligent, they may be impossible to control or shut down.',
        'content': 'A superintelligent AI could find ways to prevent humans from interfering with its goals.'
    },
    {
        'id': 'card8',
        'title': 'The window for developing safe AI may be closing as development accelerates.',
        'content': 'Time is running out to solve AI safety before we build systems we cannot control.'
    }
]

# Desktop-specific content
desktop_content = {
    'desktop-card1': {
        'title': 'AI Development Timeline',
        'content': 'AI development has accelerated rapidly since 2020, with capabilities growing exponentially. Key milestones include GPT-3 (2020), ChatGPT (2022), and GPT-4 (2023). Each iteration shows significant capability improvements, raising concerns about the pace of progress versus safety research.'
    },
    'desktop-card2': {
        'title': 'Safety Research Gap',
        'content': 'Safety research is lagging behind capability development, creating increasing risks. While AI capabilities have grown exponentially, safety research has not kept pace. This gap creates a dangerous situation where we may develop systems we cannot control or understand.'
    },
    'desktop-card3': {
        'title': 'Alignment Problem',
        'content': 'Ensuring AI systems pursue goals that align with human values remains unsolved. The alignment problem involves ensuring that AI systems understand and pursue human intentions, even as they become more capable. This is considered one of the most important unsolved problems in AI safety.'
    },
    'desktop-card4': {
        'title': 'Control Challenges',
        'content': 'Superintelligent AI may become impossible to control or shut down once created. As AI systems become more capable than humans, traditional control methods may fail. This could lead to AI systems pursuing goals that conflict with human values, with no way to stop them.'
    }
}

def generate_static_site():
    """Generate static HTML files from templates"""
    
    # Setup Jinja2 environment
    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    
    # Create output directory
    os.makedirs('dist', exist_ok=True)
    os.makedirs('dist/static', exist_ok=True)
    
    # Copy static files
    import shutil
    if os.path.exists('static'):
        shutil.copytree('static', 'dist/static', dirs_exist_ok=True)
    
    # Render templates
    template = env.get_template('index.html')
    
    # Generate main page
    html_content = template.render(
        ai_facts=ai_facts,
        desktop_content=desktop_content,
        mailing_list=mailing_list,
        url_for=lambda x, **kwargs: f"static/{x}"  # Mock url_for for static generation
    )
    
    # Write to output file
    with open('dist/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✅ Static site generated successfully!")
    print("📁 Output directory: dist/")
    print("🌐 Open dist/index.html in your browser")

if __name__ == '__main__':
    generate_static_site()

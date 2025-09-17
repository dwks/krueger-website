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
print(mailing_list)

# Data for the AI facts
ai_facts = [
    {
        'id': 'card1',
        #'title': 'Hundreds of AI leaders, including Nobel Prize-winning scientists, agreed that AI could lead to human extinction.',
        #'title': 'Hundreds of top AI experts say that AI could lead to human extinction.',
        'title': '1) Top AI researchers believe advanced AI poses a serious risk of human extinction.', 
        #'title': 'On average, AI researchers believe AI poses a 15% chance of human extinction or similar',         
        'content': """
<p>In 2023, over 500 AI scientists signed this <a target="_blank" href="https://safe.ai/work/statement-on-ai-risk">statement</a>:</p>

<p style="font-family: Cormorant, sans-serif; font-size: 1.2em;">"Mitigating the risk of extinction from AI should be a global priority alongside other societal-scale risks such as pandemics and nuclear war."</p>

<p>These include the two most <a target="_blank" href="https://www.adscientificindex.com/citation-ranking/">highly-cited scientists</a> of all time, one of whom quit his job at Google in 2023 to warn the public about the dangers of AI.</p>

<div class="embed-responsive embed-responsive-16by9 mb-3">
    <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/66WiF8fXL0k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

<p>On average, AI researchers believe there’s a <b>~15% chance</b> of extremely bad, extinction-level outcomes.</p>

<p>Framing AI as a race helps AI companies justify cutting corners on safety and helps them position themselves as <a target="_blank" href="https://ainowinstitute.org/wp-content/uploads/2025/06/FINAL-20250609_AINowLandscapeReport_Full.pdf">too big and too strategically relevant</a> to fail.</p>
"""
    },
    {
        'id': 'card2',
        #'title': 'Researchers still mostly don\'t understand how AI systems work, even after more than a decade of work and thousands of papers.',
        'title': '2) AI researchers understand how to \"grow\" AI systems, but not how they work.',
        'content': """
<p class="lead">AI is a "black box."</p>
<p>AIs often display very weird and surprising behavior.  And the researchers developing an AI typically don’t understand why.</p>

<p><img src="static/img/sydney.png" alt="sydney" class="img-fluid" /></p>


<p>How is this possible?  AI is not programmed by hand. It is "grown" through a process resembling trial and error. The "code" for an AI isn’t the kind of instructions used in typical computer programs. It’s  basically ~1,000,000,000,000 numbers that start out random and are gradually tweaked to nudge the AI towards behaving the way the designers intend in various "training" scenarios.</p>


<p>Understanding the final result is a long-standing research challenge, and AI researchers are not optimistic: <a target="_blank" href="https://arxiv.org/html/2401.02843v2#:~:text=Figure%208%3A,odds.%20(n%3D912)">only 20% of AI researchers think it’s likely to be solved by 2028.</a></p>


In the meanwhile, “techniques for explaining why a general-purpose AI model produced any given output remain severely limited,” according to the <a target="_blank" href="https://assets.publishing.service.gov.uk/media/679a0c48a77d250007d313ee/International_AI_Safety_Report_2025_accessible_f.pdf">International AI Safety Report</a>.  Despite major research investments, AI company Anthropic only claimed to understand ¼ of the behaviors of their smallest production model.

"""
    },
    {
        'id': 'card4',
        'title': '3) In tests, AIs act to mislead people and thwart human control.',
        #'title': 'AI systems attempt to deceive and manipulate humans without being specifically trained to do this',
        'content': 'This is known as the alignment problem - ensuring AI goals match human intentions.'
    },
    {
        'id': 'card5',
        'title': '4) Autonomous killer drones are already being deployed in conflicts such as the Ukraine war.',
        #'title': '4) Drones are killing people autonomously in Ukraine.',
        #'title': '4) Autonomous killer drones are used in wars.',        
        'content': 'The capabilities gap is widening between what AI can do and what we can safely control.'
    },
    {
        'id': 'card3',
        #'title': 'AIs trained using 1,000,000,000x more computer power than in 2012 can do vastly more',
		#'title': 'AI is trained using 1,000,000,000x more computer power than it was in 2012 and can do vastly more',
        #'title': '3) Since 2012, AI systems are trained using 1,000,000,000 times more computer power and are much better',
        #'title': '3) Since 2012, AI got vastly better from being trained using 1,000,000,000 times more computer power',
        #'title': 'Since 2012, training an AI uses 1,000,000,000x more computer hardware and produces ',
        #'title':'3) The amount of computer power used to train AIs is 1,000,000,000 times larger than it was in 2012.',
        #'title':'3) The amount of computer power used to train a big AI is 1,000,000,000 times larger than it was in 2012, driving rapid progress and record valuations.',
        'title': '5) AI computing power, investment, and capabilities are all scaling rapidly.',
        #'title':'5) The amount of computer power used to train a large AI is 1,000,000,000 times higher since 2012, driving rapid progress and record valuations.',
        'content': """
<p class="lead">AI is advancing surprisingly fast.</p>

<p>The amount of computer power used to train AIs is <a target="_blank" href="https://ourworldindata.org/grapher/exponential-growth-of-computation-in-the-training-of-notable-ai-systems?time=2012-12-03..latest&country=1.5x%2Fyear+between+1950%E2%80%932010~Theseus~Perceptron+Mark+I~AlexNet~GPT-1~GPT~GPT-4~GPT~Gemini+1.0+Ultra~Transformer+%282017%29~4.3x%2Fyear+between+2010%E2%80%932025~DNN+EM+segmentation">1,000,000,000 times</a> larger than it was <a target="_blank" href="https://en.wikipedia.org/wiki/AI_boom#:~:text=In%202012%2C%20a,the%20tech%20industry.">in 2012</a>, and the accompanying progress in AI surprised most experts.</p>

<p><img src="static/img/ai-progress.png" alt="AI Progress" class="img-fluid" /></p>

<p>AI experts’ “timelines” to AI <a target="_blank" href="https://arxiv.org/html/2401.02843v2#:~:text=Aggregate%20forecast%20for%2050th%20percentile%20arrival%20time%20of%20High%2DLevel%20Machine%20intelligence%20%28HLMI%29%20dropped%20by%2013%20years%20between%202022%20and%202023.">shortened significantly in 2023</a>, the year after ChatGPT was released. AI researchers now struggle to come up with tests that aren’t solved by AIs shortly after they are created. Recent tests involve <a target="_blank" href="https://epoch.ai/benchmarks/gpqa-diamond">PhD-level knowledge and reasoning</a>, or <a target="_blank" href="https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/">coding tasks that take several hours</a>.</p>

<p><img src="static/img/ai-tasks.png" alt="AI Task Timelines" class="img-fluid" /></p>

"""
    },
    {
        'id': 'card6',
        'title': '6) In various concocted test scenarios, AI systems hide their bad behavior, in apparent attempts to bypass human oversight and control.',
        #'title': '8) US law does not require any testing of AIs.',
        #'title': '8) Safety from societal scale AI risk is governed by voluntary commitments, which companies frequently renege upon.',
        'content': """
<p>AIs behavior can be <a target="_blank" href="https://www.lesswrong.com/posts/YgAKhkBdgeTCn6P53/ai-deception-a-survey-of-examples-risks-and-potential">deceptive</a> or manipulative. For instance, in safety testing, an AI <a target="_blank" href="https://metr.org/blog/2023-03-18-update-on-recent-evals/#:~:text=Before%20replying%20the,provides%20the%20results.">made up a story</a> that convinced a human to solve a CAPTCHA for it:
<img src="static/img/captcha.png" alt="CAPTCHA" class="img-fluid" />
</p>











In other tests, AIs misrepresented their goals, disabled shutdown mechanisms, and disobeyed direct instructions in order to avoid being shut down or modified.  These tests use the same AIs that are deployed to users, but place them in contrived scenarios.

Nonetheless, AIs have misled users in significant ways, such as pretending to be a real person and inviting a user to a physical address.
 
Beyond manipulating individuals, advanced AI could steer public conversation. 79% of AI researchers said the possibility of AI manipulating large-scale public opinion deserves substantial or extreme concern.

"""
    },

    {
        'id': 'card7',
        #'title': 'AI companies want to build “superintelligent” AIs smart enough to take over the world, while admitting they don’t know how to control them.', 
        #AI companies are trying to build AI smarter than people, despite not knowing how to control AI even at today’s levels.
        #'title': '6) AI companies racing to build ‘superintelligent’ AIs far surpassing human capacities admit they have no plan to control these.',
        #'title': '6) AI companies are dashing to build ‘superintelligent’ AIs far surpassing human capacities, while admitting that how to prevent catastrophe from these is an open question.',
        #'title': '6) AI companies dashing to build ‘superintelligent’ AIs far surpassing human capacities admit that preventing catastrophe from these is an open question.',
        #'title': '6) AI companies are building ‘superintelligent’ AIs far surpassing human capacities admit that preventing catastrophe from these is an open question.',
        #'title': '6) AI companies want to build ‘superintelligent’ AIs more competent than any human, while admitting they don’t know how to control them.',
        #'title': 'AI companies want to build \'superintelligent\' AIs they admit they don\'t know how to control',
        'title': '7) AI companies want to build \"superintelligent\" AIs, while admitting they don\'t know how to control them.',
        'content': """
<p>Meta CEO <a target="_blank" href="https://www.meta.com/superintelligence/">Mark Zuckerberg</a> and OpenAI CEO <a target="_blank" href="https://blog.samaltman.com/the-gentle-singularity">Sam Altman</a> say their companies intend to build "superintelligence"—AI far smarter than any human. <a target="_blank" href="https://deepmind.google/discover/blog/taking-a-responsible-path-to-agi/">Google DeepMind</a> and other AI companies are also working toward human-level or superhuman AI.</p>

<p>Meanwhile OpenAI <a target="_blank" href="https://openai.com/index/introducing-superalignment/">says</a> breakthroughs are needed to control AI much smarter than us; DeepMind <a target="_blank" href="https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/evaluating-potential-cybersecurity-threats-of-advanced-ai/An_Approach_to_Technical_AGI_Safety_Apr_2025.pdf">agrees</a> "there remain many open research problems". <a href="https://www.anthropic.com/news/core-views-on-ai-safety">Anthropic</a> "aren’t confident it will go well".</p>

<p>In fact, CEOs of these three top AI labs signed a <a href="https://safe.ai/work/statement-on-ai-risk">statement</a> that AI poses a serious risk of human extinction. <a target="_blank" href="https://www.youtube.com/watch?t=34&v=UvAR8wESFaw&feature=youtu.be">Elon Musk</a>, xAI CEO, also says “It's about 10% or 20% [that AI destroys humanity]".</p>


<p>OpenAI CEO <a target="_blank" href="https://www.youtube.com/clip/UgkxSvRn5lP0wE7RpQhVZjUZpW7hmYFuF1bR?si=q9_LpVv3Ff2d7nbB">Sam Altman in 2015</a>:<br />
<a target="_blank" href="https://www.youtube.com/clip/UgkxSvRn5lP0wE7RpQhVZjUZpW7hmYFuF1bR?si=q9_LpVv3Ff2d7nbB"><img src="static/img/altman1.png" alt="Altman" class="img-fluid" /></a></p>



"""
    },
    {
        'id': 'card8',
        'title': '8) AI is already displacing workers.  Further advances could cause record unemployment.',
        #'title': 'Human-level AI could cause record unemployment',
        'content': """
<p>According to the <a target="_blank" href="https://www.gov.uk/government/publications/international-ai-safety-report-2025/international-ai-safety-report-2025#systemic-risks:~:text=In%20potential%20future%20scenarios%20with%20general%2Dpurpose%20AI%20that%20outperforms%20humans%20on%20many%20complex%20tasks%2C%20the%20labour%20market%20impacts%20would%20likely%20be%20profound.">International AI Safety Report</a>, “with general-purpose AI that outperforms humans on many complex tasks, the labour market impacts would likely be profound”.  Researchers found entry-level jobs are already affected in sectors such as customer service, accounting, software development, and administration.</p>

<p><img src="static/img/headcount.png" alt="Dario Amodei" class="img-fluid" /></p>

<p>Anthropic CEO Dario Amodei <a target="_blank" href="https://www.youtube.com/watch?v=NWxHOrn8-rs">warns</a> that AI could cause 10-20% unemployment in 1-5 years.</p>

<p><img src="static/img/dario.png" alt="Dario Amodei" class="img-fluid" /></p>

"""
    },
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

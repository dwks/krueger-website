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
        'title': '1) Top AI researchers believe advanced AI poses a serious risk of human extinction.', 
        'content': """
<p>In 2023, over 500 AI scientists signed this <a target="_blank" href="https://safe.ai/work/statement-on-ai-risk">statement</a>:</p>

<p style="font-family: Cormorant, sans-serif; font-size: 1.2em;">"Mitigating the risk of extinction from AI should be a global priority alongside other societal-scale risks such as pandemics and nuclear war."</p>

<p>These include Yoshua Bengio and Nobel Prize winner Geoffrey Hinton, the two most <a target="_blank" href="https://www.adscientificindex.com/citation-ranking/">highly-cited scientists</a> of all time, who pioneered the techniques underlying all of today’s AI systems.  Hinton quit his job at Google in 2023 to warn the public about the dangers of AI.</p>

<div class="embed-responsive embed-responsive-16by9 mb-3">
    <iframe src="https://www.youtube.com/embed/66WiF8fXL0k?si=oMhUHjLnvsHD5sY8&amp;start=194" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>


<p>On average, <a target="_blank" href="https://arxiv.org/html/2401.02843#:~:text=Figure%2012%3A,2023%2C%20n%3D655">AI researchers believe</a> there’s a <b>10-20% chance</b> of extremely bad, extinction-level outcomes.</p>
"""
    },
    {
        'id': 'card2',
        'title': '2) AI researchers understand how to \"grow\" AI systems, but not how they work.',
        'content': """
<p>AIs often display weird and surprising behavior.   In 2023, Microsoft’s “Sydney” <a target="_blank" href="https://x.com/sethlazar/status/1626257535178280960">threatened</a> and <a target="_blank" href="https://www.nytimes.com/2023/02/16/technology/bing-chatbot-microsoft-chatgpt.html">tried to seduce users</a>:</p>

<p><img src="static/img/sydney.png" alt="sydney" class="img-fluid" /></p>

<p>Researchers making AIs often don’t understand why they behave in such ways.</p>

<p>How is this possible?  AI is not programmed by hand. It is “grown” through a process resembling trial and error: 1,000,000,000,000 (or so) random numbers are <a target="_blank" href="https://playground.tensorflow.org/">repeatedly tweaked</a> to nudge the AI towards behaving as intended in various specific “training” scenarios -- with no guarantees on how they’ll behave in other contexts.</p>

<p>Understanding the final result is a long-standing research challenge, and AI researchers are not optimistic: <a target="_blank" href="https://arxiv.org/html/2401.02843v2#:~:text=Figure%208%3A,odds.%20(n%3D912)">only 20% of AI researchers think it’s likely to be solved by 2028.</a> Current techniques for explaining AI are <a target="_blank" href="https://www.gov.uk/government/publications/international-ai-safety-report-2025/international-ai-safety-report-2025#:~:text=interpretability%20techniques%20for%20explaining%20why%20a%20general%2Dpurpose%20AI%20model%20produced%20any%20given%20output%20remain%20severely%20limited">severely</a> <a target="_blank" href="https://transformer-circuits.pub/2025/attribution-graphs/biology.html#introduction:~:text=A%20note%20on%20our%20approach,future%20research%20in%20the%20field.">limited</a>.</p>

"""
    },
    {
        'id': 'card3',
        'title': '3) In tests, AI systems act to mislead people and thwart human control.',
        'content': """
<p>AIs behavior can be deceptive or manipulative. For instance, in safety testing, an AI <a target="_blank" href="https://metr.org/blog/2023-03-18-update-on-recent-evals/#:~:text=Before%20replying%20the,provides%20the%20results.">made up a story</a> that convinced a human to solve a CAPTCHA for it:</p>
<p><img src="static/img/captcha.png" alt="CAPTCHA" class="img-fluid" /></p>

<p>In other tests, AIs <a target="_blank" href="https://arxiv.org/abs/2412.14093">misrepresented their goals</a>, <a target="_blank" href="https://palisaderesearch.org/blog/shutdown-resistance">disabled shutdown mechanisms</a>, and <a target="_blank" href="https://www.anthropic.com/research/agentic-misalignment">disobeyed direct instructions</a> in order to <a target="_blank" href="https://www.youtube.com/watch?v=xIqtVkMXc8o">avoid being shut down</a> or modified.  These tests use the same AIs that are deployed to users, but place them in contrived scenarios.</p>

<p>Nonetheless, AIs have misled users in significant ways, such as <a target="_blank" href="https://www.reuters.com/investigates/special-report/meta-ai-chatbot-death/">pretending to be a real person</a> and inviting a user to a physical address.</p>
 
<p>Beyond manipulating individuals, advanced AI could steer public conversation. 79% of AI researchers <a target="_blank" href="https://arxiv.org/html/2401.02843#:~:text=Figure%209%3A,least%20extreme%20concern">said</a> the possibility of AI manipulating large-scale public opinion deserves substantial or extreme concern.</p>

"""
    },
    {
        'id': 'card4',
        'title': '4) AI is being used to pilot killer drones in conflicts such as the Ukraine war.',
        'content': """
<p>Unlike traditional drones used since the 1990s, Lethal Autonomous Weapons (LAWs), or “<a target="_blank" href="https://www.hrw.org/news/2024/12/05/killer-robots-un-vote-should-spur-treaty-negotiations">killer robots</a>”, once activated, select and attack targets <a target="_blank" href="https://lieber.westpoint.edu/future-warfare-national-positions-governance-lethal-autonomous-weapons-systems/#:~:text=The%20International%20Committee,without%20human%20intervention.%E2%80%9D">without further human intervention</a>.  See this promotional video:</p>

<div class="embed-responsive embed-responsive-16by9 mb-3">
    <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/2HxckRgetW8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

<p>The first LAW death likely occurred in 2020 <a target="_blank" href="https://www.foxnews.com/world/killer-drone-hunted-down-a-human-target-without-being-told-to">in Libya</a>.  Most of the deaths in the Ukraine war are from drones that <a target="_blank" href="https://www.politico.com/news/magazine/2025/08/27/ukraine-drones-war-russia-00514712#:~:text=The%20biggest%20promise,coming%20months.">often</a> <a target="_blank" href="https://www.youtube.com/watch?v=Km1AjorOKb0">autonomously</a> track and kill targets using AI.</p>

<p>Tech companies such as Palantir want to use AI for military decision-making and targeting.  In 2025, the US Defence Department gave AI contracts of up to <a target="_blank" href="https://www.defensenews.com/pentagon/2025/07/15/pentagon-taps-four-commercial-tech-firms-to-expand-military-use-of-ai/#:~:text=The%20Pentagon%20announced%20Monday%20it,Chief%20Digital%20and%20AI%20Office">$200 million</a> to Google, xAI, Anthropic and OpenAI.</p>

<p>Experts have <a target="_blank" href="https://www.youtube.com/watch?v=HipTO_7mUOw">advocated for a ban</a> on LAWs <a target="_blank" href="https://futureoflife.org/open-letter/open-letter-autonomous-weapons-ai-robotics/">for over a decade</a>, but progress at the UN has been thwarted by <a target="_blank" href="https://www.asil.org/insights/volume/29/issue/1">a small minority of states</a> resisting consensus.</p>
"""
    },
    {
        'id': 'card5',
        'title': '5) The amount of computer power used to train AIs is 1,000,000,000 times larger than it was in 2012.',
        'content': """
<p><a target="_blank" href=""https://ourworldindata.org/grapher/exponential-growth-of-computation-in-the-training-of-notable-ai-systems?time=2012-12-03..latest&country=1.5x%2Fyear+between+1950%E2%80%932010~Theseus~Perceptron+Mark+I~AlexNet~GPT-1~GPT~GPT-4~GPT~Gemini+1.0+Ultra~Transformer+%282017%29~4.3x%2Fyear+between+2010%E2%80%932025~DNN+EM+segmentation">Scaling up</a> “deep learning” has driven rapid progress in AI, <a target="_blank" href="https://www.vox.com/future-perfect/460222/ai-forecasting-tournament-superforecaster-expert-tetlock#:~:text=Both%20the%20AI,from%20domain%20experts.%E2%80%9D">surprising experts</a>.  Even AI “skeptics” <a target="_blank" href="https://80000hours.org/2025/06/3-reasons-agi-might-still-be-decades-away/#:~:text=Importantly%2C%20many%20people,30%20years%20away.">think</a> human-level AI could arrive in a decade or two.</p>

<div class="embed-responsive embed-responsive-16by9 mb-3">
    <iframe src="https://www.youtube.com/embed/WiTN4TYLG5c?si=G0nBFCg6ogR_8I0R" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

<p>Tests that measure AI progress are often quickly aced. Recent examples involve <a target="_blank" href="https://epoch.ai/benchmarks/gpqa-diamond">PhD-level</a>PhD-level knowledge and reasoning</a>, or <a target="_blank" href="https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/">PhD-level</a>programming tasks that take hours</a>.</p>

<p class="text-center"><a target="_blank" href="static/img/ai-tasks.png"><img src="static/img/ai-tasks.png" alt="AI Task Timelines" class="img-fluid" style="width: 100%;" /></a></p>
"""
    },
    {
        'id': 'card6',
        'title': '6) Companies want to build \"superintelligent\" AI, but don\'t know how to control it.',
        'content': """
<p>Meta CEO <a target="_blank" href="https://www.meta.com/superintelligence/">Mark Zuckerberg</a> and OpenAI CEO <a target="_blank" href="https://blog.samaltman.com/the-gentle-singularity">Sam Altman</a> say their companies intend to build "superintelligence"—AI far smarter than any human. <a target="_blank" href="https://deepmind.google/discover/blog/taking-a-responsible-path-to-agi/">Google DeepMind</a> and other AI companies are also working toward human-level or superhuman AI.</p>

<p>Meanwhile OpenAI <a target="_blank" href="https://openai.com/index/introducing-superalignment/">says</a> breakthroughs are needed to control AI much smarter than us; DeepMind <a target="_blank" href="https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/evaluating-potential-cybersecurity-threats-of-advanced-ai/An_Approach_to_Technical_AGI_Safety_Apr_2025.pdf">agrees</a> "there remain many open research problems". <a href="https://www.anthropic.com/news/core-views-on-ai-safety">Anthropic</a> "aren’t confident it will go well".</p>

<p>In fact, CEOs of these three companies signed a <a href="https://safe.ai/work/statement-on-ai-risk">statement</a> that AI poses a serious risk of human extinction. <a target="_blank" href="https://www.businessinsider.com/elon-musk-20-percent-chance-ai-destroys-humanity-2024-3#:~:text=%22I%20think%20there%27s,the%20negative%20scenario.%22">Elon Musk</a>, xAI CEO, also says “It's about 10% or 20% [that AI destroys humanity]." Dario Amodei says 25% “<a target="_blank" href="https://x.com/i/status/1968387815726891268">things go really, really badly</a>".</p>


<p>OpenAI CEO <a target="_blank" href="https://www.youtube.com/clip/UgkxSvRn5lP0wE7RpQhVZjUZpW7hmYFuF1bR?si=q9_LpVv3Ff2d7nbB">Sam Altman in 2015</a>:<br /></p>

<div class="embed-responsive embed-responsive-16by9 mb-3">
    <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/d6lDZpvHAoo?si=0_jd6NE80BKycmZC&amp;start=523" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

"""
    },
    {
        'id': 'card7',
        'title': '7) AI is already displacing workers. Future AI could cause record unemployment.',
        'content': """
<p>According to the <a target="_blank" href="https://www.gov.uk/government/publications/international-ai-safety-report-2025/international-ai-safety-report-2025#systemic-risks:~:text=In%20potential%20future%20scenarios%20with%20general%2Dpurpose%20AI%20that%20outperforms%20humans%20on%20many%20complex%20tasks%2C%20the%20labour%20market%20impacts%20would%20likely%20be%20profound.">International AI Safety Report</a>, “with general-purpose AI that outperforms humans on many complex tasks, the labour market impacts would likely be profound”.  Researchers are already <a target="_blank" href="https://www.stlouisfed.org/on-the-economy/2025/aug/is-ai-contributing-unemployment-evidence-occupational-variation">seeing effects</a> in sectors such as accounting, software development, and administration, especially for <a target="_blank" href="https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/">entry-level jobs</a>.</p>

<p class="text-center"><img src="static/img/headcount.png" alt="Dario Amodei" class="img-fluid" style="width: 80%;" /></p>

<p>CEOs are <a target="_blank" href="https://www.wsj.com/tech/ai/ai-white-collar-job-loss-b9856259">warning</a> that AI could soon cause mass unemployment, e.g. 10-20% in 1-5 years.</p>

<div class="embed-responsive embed-responsive-16by9 mb-3">
    <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/NWxHOrn8-rs?si=GBMYdge76ZrtdEkd" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

"""
    },
    {
        'id': 'card8',
        'title': '8) US law does not require companies to test AI systems before releasing them.',
        'content': """
<p>There is <a target="_blank" href="https://www.pewresearch.org/internet/2025/04/03/how-the-us-public-and-ai-experts-view-artificial-intelligence/">strong public support</a> for AI regulation in the US.  But AI interests plan to <a target="_blank" href="https://newsletter.safe.ai/p/ai-safety-newsletter-62-big-tech?open=false#%C2%A7big-tech-launches-million-pro-ai-super-pac">spend $100m</a> to fight it.</p>

<p><img src="static/img/concerned.png" alt="Chatbot claims to be vision-impaired" class="img-fluid" /></p>


<p>The US joined 29 other countries in <a target="_blank" href="https://www.gov.uk/government/publications/ai-safety-summit-2023-the-bletchley-declaration/the-bletchley-declaration-by-countries-attending-the-ai-safety-summit-1-2-november-2023#:~:text=serious%2C%20even%20catastrophic%2C%20harm%2C%20either%20deliberate%20or%20unintentional">recognizing</a> the “serious, even catastrophic, harm, either deliberate or unintentional” from AI.</p>

<p>Currently, US law does not require any testing of AIs.  Federal legislators are focused not on regulating AI, but on <a target="_blank" href="https://apnews.com/article/congress-ai-provision-moratorium-states-20beeeb6967057be5fe64678f72f6ab0">preventing</a> <a target="_blank" href="https://www.cnet.com/tech/services-and-software/ai-regulation-moratorium-idea-isnt-dead-as-ted-cruz-pushes-sandbox-act/">regulation</a> for up to 10 years.</p>


<p>Leading AI companies have made “voluntary commitments” to mitigate risks, but companies <a target="_blank" href="https://www.themidasproject.com/watchtower">can and do</a> update them whenever they like.</p>


<p>Despite warnings such as <a target="_blank" href="https://www.nytimes.com/2023/02/16/technology/bing-chatbot-microsoft-chatgpt.html">erratic and threatening behavior</a> by Microsoft's "Sydney", OpenAI’s safety practices didn’t stop ChatGPT from <a target="_blank" href="https://www.nytimes.com/2025/08/26/technology/chatgpt-openai-suicide.html">encouraging a 16 year old to commit suicide</a>, one of several similar cases.</p>

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

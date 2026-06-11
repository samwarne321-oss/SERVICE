import os

services = [
    {
        "id": "local-seo",
        "title": "Local SEO Services – GMB Services LLC",
        "h1": "Local SEO Optimization",
        "desc": "Dominate your city's search results and attract local customers.",
        "sections": [
            {"h2": "What is Local SEO?", "p": "Local SEO is the process of optimizing your online presence to attract more business from relevant local searches. These searches take place on Google and other search engines, making it essential for brick-and-mortar businesses and service-area businesses to maintain a strong local footprint. We ensure your NAP (Name, Address, Phone number) data is consistent across the web."},
            {"h2": "Why it Matters", "p": "When consumers search for local services, they have high intent. In fact, most local searches result in an in-store visit or phone call within 24 hours. By ranking higher for localized keywords, you capture this ready-to-buy audience, driving more foot traffic and highly targeted leads directly to your business."},
            {"h2": "Our Approach", "p": "We start with a comprehensive local SEO audit to identify gaps in your current strategy. From there, we optimize your business listings, build high-quality local citations, and create hyper-localized content that signals relevance to search engines. You get complete local search optimization so you own your city's search results."}
        ]
    },
    {
        "id": "google-maps-seo",
        "title": "Google Maps Ranking Services – GMB Services LLC",
        "h1": "Google Maps Ranking",
        "desc": "Secure a spot in the coveted Google Maps 3-Pack.",
        "sections": [
            {"h2": "The Power of the 3-Pack", "p": "When users search for local services, Google displays a \"3-Pack\" of Google Maps results at the very top of the page. This prime real estate captures over 70% of local search clicks. If your business isn't in the 3-Pack, you're missing out on the vast majority of potential customers in your area."},
            {"h2": "How We Do It", "p": "Ranking in Google Maps requires specialized strategies. We focus on fully optimizing your Google Business Profile (GBP), managing and responding to reviews, and building local relevance through localized backlinks and content. We ensure your profile is fully populated, categorized correctly, and regularly updated."},
            {"h2": "Trackable Results", "p": "We don't just guess what's working. We provide detailed tracking of your Google Maps performance, measuring tangible metrics like phone calls, direction requests, and direct website visits generated directly from your maps listing."}
        ]
    },
    {
        "id": "on-page-seo",
        "title": "On-Page SEO Services – GMB Services LLC",
        "h1": "On-Page SEO",
        "desc": "Turn your website into a powerful ranking machine.",
        "sections": [
            {"h2": "The Foundation of Search", "p": "On-Page SEO is the practice of optimizing individual web pages in order to rank higher and earn more relevant traffic. This includes optimizing your meta tags, headers, URLs, and keyword density. We ensure your site architecture makes it easy for search engines to understand what your pages are about."},
            {"h2": "Content that Converts", "p": "We believe in writing for human users first, and search engines second. Our content optimization strategies ensure that your pages not only contain the right semantic keywords but also provide immense value to the reader, reducing bounce rates and increasing conversions."},
            {"h2": "Technical On-Page Elements", "p": "Beyond words on a page, we implement advanced on-page technical elements like Schema markup to help search engines understand your content better, strategic internal linking to distribute page authority, and image optimization for faster load times and image search visibility."}
        ]
    },
    {
        "id": "technical-seo",
        "title": "Technical SEO Services – GMB Services LLC",
        "h1": "Technical SEO",
        "desc": "Build a flawless technical foundation for your website.",
        "sections": [
            {"h2": "What is Technical SEO?", "p": "Technical SEO refers to website and server optimizations that help search engine spiders crawl and index your site more effectively. Even with the best content in the world, a technically flawed website will struggle to rank. We fix the behind-the-scenes issues that are holding you back."},
            {"h2": "Core Web Vitals", "p": "Google considers user experience a major ranking factor. We optimize your website for Core Web Vitals, ensuring fast loading times, immediate interactivity, and visual stability. A faster website not only ranks better but also provides a superior experience for your potential customers."},
            {"h2": "Fixing the Errors", "p": "Our technical audits uncover hidden issues like broken links, redirect loops, duplicate content, and crawl errors. We repair these technical roadblocks, optimize your crawl budget, and ensure your XML sitemaps and robots.txt files are configured perfectly for maximum search engine visibility."}
        ]
    },
    {
        "id": "link-building",
        "title": "Link Building Services – GMB Services LLC",
        "h1": "Link Building",
        "desc": "Acquire high-authority backlinks to boost your domain's trust.",
        "sections": [
            {"h2": "The Importance of Backlinks", "p": "Backlinks act as \"votes of confidence\" from one website to another. Search engines like Google use these links to determine the authority and trustworthiness of your website. A strong backlink profile is one of the most heavily weighted ranking factors in SEO."},
            {"h2": "Our White-Hat Approach", "p": "We strictly adhere to white-hat link building techniques. We earn links through manual outreach, digital PR, guest posting on reputable industry blogs, and reclaiming unlinked brand mentions. We never use spammy link networks or manipulative tactics that could get your site penalized."},
            {"h2": "Quality Over Quantity", "p": "Not all links are created equal. One link from a highly relevant, authoritative website is worth more than hundreds of low-quality directory links. Our focus is entirely on acquiring high Domain Authority (DA) placements that move the needle and build long-term trust with search engines."}
        ]
    },
    {
        "id": "seo-consulting",
        "title": "SEO Consulting Services – GMB Services LLC",
        "h1": "SEO Consulting",
        "desc": "Get custom strategy and guidance from senior SEO experts.",
        "sections": [
            {"h2": "Tailored Strategies", "p": "We don't believe in cookie-cutter solutions. Every business, industry, and local market is unique. Our consulting services provide you with one-on-one strategy sessions with senior SEO specialists who understand your specific challenges and goals, delivering a custom growth roadmap."},
            {"h2": "In-Depth Audits", "p": "We provide comprehensive, deep-dive analyses of your entire digital footprint. From your website architecture to your competitor's backlink profiles, we uncover the exact reasons why you aren't ranking #1 and identify the lowest-hanging fruit for immediate traffic gains."},
            {"h2": "Actionable Roadmaps", "p": "Consulting is only valuable if it leads to action. We deliver clear, prioritized, step-by-step execution plans. Whether your in-house team needs guidance on implementation or you need a trusted advisor to oversee your marketing efforts, we provide the expertise to ensure your success."}
        ]
    }
]

template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{desc}" />
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="style.css" />
  <link rel="icon" type="image/png" href="photo.png">
  <style>
    .page-hero {{
      padding: 140px 0 60px;
      background: linear-gradient(135deg, var(--navy) 0%, var(--slate) 100%);
      border-bottom: 1px solid var(--border);
    }}
    .page-hero h1 {{
      font-family: var(--font-display);
      font-size: clamp(2rem, 5vw, 3.5rem);
      font-weight: 800;
      color: var(--white);
      margin-bottom: 12px;
    }}
    .page-hero p {{
      color: var(--gray);
      font-size: 1.1rem;
      max-width: 600px;
    }}
    .page-content {{
      padding: 70px 0 100px;
    }}
    .page-content .container {{
      max-width: 820px;
    }}
    .page-section {{
      margin-bottom: 44px;
    }}
    .page-section h2 {{
      font-family: var(--font-display);
      font-size: 1.5rem;
      font-weight: 700;
      color: var(--white);
      margin-bottom: 14px;
      padding-bottom: 10px;
      border-bottom: 1px solid var(--border);
    }}
    .page-section p {{
      color: var(--white-80);
      line-height: 1.8;
      font-size: 1.05rem;
    }}
    .page-intro {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 28px 32px;
      margin-bottom: 48px;
      color: var(--white-80);
      line-height: 1.8;
      font-size: 1.05rem;
    }}
    .back-link {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      color: var(--cyan);
      text-decoration: none;
      font-size: 0.95rem;
      font-weight: 500;
      margin-bottom: 40px;
      transition: gap var(--transition);
    }}
    .back-link:hover {{ gap: 12px; }}
  </style>
</head>
<body>

  <!-- NAVIGATION -->
  <header id="navbar" role="banner">
    <nav class="nav-container" aria-label="Main navigation">
      <a href="index.html" class="nav-logo" aria-label="GMB Services LLC – Home">
        <span class="logo-mark">GMB</span>
        <span class="logo-text">Services LLC</span>
      </a>
      <ul class="nav-links" id="navLinks" role="list">
        <li><a href="index.html#home" class="nav-link">Home</a></li>
        <li><a href="index.html#about" class="nav-link">About</a></li>
        <li><a href="index.html#services" class="nav-link">Services</a></li>
        <li><a href="index.html#pricing" class="nav-link">Pricing</a></li>
        <li><a href="index.html#contact" class="nav-link">Contact</a></li>
      </ul>
      <a href="index.html#contact" class="nav-cta">Get Free Audit</a>
      <button class="hamburger" id="hamburger" aria-label="Toggle navigation menu" aria-expanded="false" aria-controls="navLinks">
        <span></span><span></span><span></span>
      </button>
    </nav>
  </header>

  <main>
    <div class="page-hero">
      <div class="container">
        <h1>{h1}</h1>
        <p>{desc}</p>
      </div>
    </div>

    <section class="page-content">
      <div class="container">
        <a href="index.html#services" class="back-link">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 5l-7 7 7 7"/></svg>
          Back to Services
        </a>

        {sections_html}

      </div>
    </section>
  </main>

  <!-- FOOTER -->
  <footer class="footer" role="contentinfo">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="index.html" class="nav-logo footer-logo" aria-label="GMB Services LLC – Home">
            <span class="logo-mark">GMB</span>
            <span class="logo-text">Services LLC</span>
          </a>
          <p class="footer-tagline">Helping local businesses across the USA rank higher, get found faster, and grow sustainably through strategic SEO.</p>
          <div class="footer-socials">
            <a href="#" class="social-link" aria-label="Follow us on Facebook">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"/></svg>
            </a>
            <a href="#" class="social-link" aria-label="Connect on LinkedIn">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16 8a6 6 0 016 6v7h-4v-7a2 2 0 00-2-2 2 2 0 00-2 2v7h-4v-7a6 6 0 016-6zM2 9h4v12H2z"/><circle cx="4" cy="4" r="2"/></svg>
            </a>
            <a href="#" class="social-link" aria-label="Follow us on Instagram">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1112.63 8 4 4 0 0116 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
            </a>
          </div>
        </div>
        <div class="footer-col">
          <h4 class="footer-col-title">Company</h4>
          <ul role="list">
            <li><a href="index.html#home">Home</a></li>
            <li><a href="index.html#about">About Us</a></li>
            <li><a href="index.html#services">Services</a></li>
            <li><a href="index.html#pricing">Pricing</a></li>
            <li><a href="index.html#contact">Contact</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4 class="footer-col-title">Services</h4>
          <ul role="list">
            <li><a href="local-seo.html">Local SEO</a></li>
            <li><a href="google-maps-seo.html">Google Maps SEO</a></li>
            <li><a href="on-page-seo.html">On-Page SEO</a></li>
            <li><a href="technical-seo.html">Technical SEO</a></li>
            <li><a href="link-building.html">Link Building</a></li>
            <li><a href="seo-consulting.html">SEO Consulting</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4 class="footer-col-title">Contact</h4>
          <ul class="footer-contact-list" role="list">
            <li>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
              <a href="mailto:support@gmbservicesllc.com">support@gmbservicesllc.com</a>
            </li>
            <li>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-5-5 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.05 12.05 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.05 12.05 0 002.81.7A2 2 0 0122 16.92z"/></svg>
              <a href="tel:+1 (581) 584-7873">+1 (581) 584-7873</a>
            </li>
            <li>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
              <span>3018 Gracious Dr Franklin, TN 37064</span>
            </li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; <span id="year"></span> GMB Services LLC. All rights reserved.</p>
        <div class="footer-legal">
          <a href="privacy-policy.html">Privacy Policy</a>
          <a href="terms-of-service.html">Terms of Service</a>
        </div>
      </div>
    </div>
  </footer>

  <script>
    document.getElementById('year').textContent = new Date().getFullYear();
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('navLinks');
    if (hamburger) {{
      hamburger.addEventListener('click', () => {{
        const open = navLinks.classList.toggle('open');
        hamburger.setAttribute('aria-expanded', open);
      }});
    }}
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {{
      navbar.classList.toggle('scrolled', window.scrollY > 50);
    }});
  </script>
</body>
</html>
"""

for s in services:
    sections_html = ""
    for i, sec in enumerate(s["sections"]):
        if i == 0:
             sections_html += f'''<div class="page-intro">
          <h2>{sec["h2"]}</h2>
          {sec["p"]}
        </div>'''
        else:
             sections_html += f'''<div class="page-section">
          <h2>{sec["h2"]}</h2>
          <p>{sec["p"]}</p>
        </div>'''
        
    final_html = template.format(
        title=s["title"],
        h1=s["h1"],
        desc=s["desc"],
        sections_html=sections_html
    )
    
    with open(f'{s["id"]}.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

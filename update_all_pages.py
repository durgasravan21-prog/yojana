# -*- coding: utf-8 -*-
import os
import re

path = r'c:\Users\durga\OneDrive\Desktop\yojana'

# List of general pages
GENERAL_PAGES = ['index.html', 'categories.html', 'about.html', 'contact.html', 'privacy-policy.html', 'disclaimer.html', 'terms.html']

# Categories mapping
CATEGORIES = {
    "agriculture": {"name": "Agriculture & Farming", "emoji": '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M12 22V12M12 12c-2-2.67-4-2.67-6 0M12 14c2-2.67 4-2.67 6 0M12 18c-3-2-6-1.33-6 2M12 18c3-2 6-1.33 6 2"/></svg>', "class": "tag-agriculture", "color": "agriculture"},
    "health": {"name": "Health & Medical", "emoji": '<svg class="icon-svg" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="12" y1="8" x2="12" y2="16"/><line x1="8" y1="12" x2="16" y2="12"/></svg>', "class": "tag-health", "color": "health"},
    "housing": {"name": "Housing & Shelter", "emoji": '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>', "class": "tag-housing", "color": "housing"},
    "education": {"name": "Education & Skill Development", "emoji": '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20M4 4.5A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5v-15z"/></svg>', "class": "tag-education", "color": "education"},
    "women": {"name": "Women & Child Development", "emoji": '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>', "class": "tag-women", "color": "women"},
    "finance": {"name": "Financial Inclusion & Business", "emoji": '<svg class="icon-svg" viewBox="0 0 24 24"><rect x="2" y="22" width="20" height="2"/><line x1="4" y1="18" x2="4" y2="10"/><line x1="8" y1="18" x2="8" y2="10"/><line x1="12" y1="18" x2="12" y2="10"/><line x1="16" y1="18" x2="16" y2="10"/><line x1="20" y1="18" x2="20" y2="10"/><path d="M12 2L2 7h20L12 2z"/></svg>', "class": "tag-finance", "color": "finance"},
    "employment": {"name": "Employment & Self-Employment", "emoji": '<svg class="icon-svg" viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>', "class": "tag-employment", "color": "employment"},
    "pension": {"name": "Pension & Social Security", "emoji": '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>', "class": "tag-pension", "color": "pension"},
    "rural": {"name": "Rural Development", "emoji": '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>', "class": "tag-rural", "color": "rural"},
    "energy": {"name": "Energy & Power", "emoji": '<svg class="icon-svg" viewBox="0 0 24 24"><polyline points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>', "class": "tag-energy", "color": "energy"},
    "infrastructure": {"name": "Infrastructure & Development", "emoji": '<svg class="icon-svg" viewBox="0 0 24 24"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>', "class": "tag-infrastructure", "color": "infrastructure"},
    "social": {"name": "Social Welfare & Security", "emoji": '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M12 2a5 5 0 1 0 5 5 5 5 0 0 0-5-5zm0 12c-4.42 0-8 2.24-8 5v3h16v-3c0-2.76-3.58-5-8-5z"/></svg>', "class": "tag-social", "color": "social"}
}

POPULAR_SCHEME_TITLES = {
    'pm-kisan': 'PM Kisan Samman Nidhi',
    'ayushman-bharat': 'Ayushman Bharat PM-JAY',
    'ujjwala-yojana': 'PM Ujjwala Yojana',
    'pm-awas': 'PM Awas Yojana',
    'sukanya-samriddhi': 'Sukanya Samriddhi Yojana',
    'mudra-yojana': 'PM Mudra Yojana',
    'pm-surya-ghar': 'PM Surya Ghar Muft Bijli',
    'lakhpati-didi': 'Lakhpati Didi Scheme',
    'pm-vishwakarma': 'PM Vishwakarma Yojana',
    'jan-dhan': 'PM Jan Dhan Yojana',
    'atal-pension': 'Atal Pension Yojana',
    'pm-kaushal-vikas': 'PM Kaushal Vikas Yojana',
    'beti-bachao': 'Beti Bachao Beti Padhao',
    'kisan-credit-card': 'Kisan Credit Card Scheme',
    'e-shram': 'e-Shram Card Registration'
}

def parse_all_schemes():
    schemes = []
    html_files = [f for f in os.listdir(path) if f.endswith('.html') and f not in GENERAL_PAGES]
    
    for filename in html_files:
        filepath = os.path.join(path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Parse title
        title_match = re.search(r'<title>(.*?)<\/title>', content)
        scheme_id = filename.replace('.html', '')
        if scheme_id in POPULAR_SCHEME_TITLES:
            title = POPULAR_SCHEME_TITLES[scheme_id]
        elif title_match:
            raw_title = title_match.group(1)
            # Remove " - Eligibility..." suffix using space-hyphen-space to protect internal hyphens
            title_part = raw_title.split(' - ')[0].strip()
            # Remove "2026" or "2024" year
            title_part = re.sub(r'\s*\b(2024|2026)\b', '', title_part).strip()
            title = title_part
        else:
            title = filename.replace('.html', '').replace('-', ' ').title()
        
        # Parse fullname
        h1_match = re.search(r'<h1>(.*?)<\/h1>', content)
        fullname = h1_match.group(1).strip() if h1_match else title
        
        # Parse description
        desc_match = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', content)
        if not desc_match:
            desc_match = re.search(r'<meta\s+property="og:description"\s+content="([^"]+)"', content)
        desc = desc_match.group(1).strip() if desc_match else "Complete guide, eligibility, benefits, application process, and status check."
        
        # Parse category tag class
        cat_class = "tag-finance"
        cat_key = "finance"
        cat_match = re.search(r'class="scheme-card-tag\s+tag-([^"]+)"', content)
        if cat_match:
            cat_key = cat_match.group(1).strip()
            cat_class = f"tag-{cat_key}"
        else:
            # Fallback based on text search
            for c_key, c_info in CATEGORIES.items():
                if c_info["class"] in content:
                    cat_key = c_key
                    cat_class = c_info["class"]
                    break
        
        # Normalize category keys
        if cat_key == "savings":
            cat_key = "women"
            cat_class = "tag-women"
        elif cat_key not in CATEGORIES:
            cat_key = "social"
            cat_class = "tag-social"
            
        schemes.append({
            "id": filename.replace('.html', ''),
            "title": title,
            "fullname": fullname,
            "category": cat_key,
            "emoji": CATEGORIES[cat_key]["emoji"],
            "description": desc,
            "class": cat_class
        })
        
    return schemes

def get_navigation(active_page="index", popular_schemes=[]):
    dropdown_items_html = ""
    for s in popular_schemes[:12]:
        dropdown_items_html += f'              <li><a href="{s["id"]}">{s["title"]}</a></li>\n'
        
    nav_html = f"""      <nav class="main-nav" role="navigation" aria-label="Main Navigation">
        <ul class="nav-list">
          <li><a href="/" class="{"active" if active_page == "index" else ""}">Home</a></li>
          <li><a href="categories" class="{"active" if active_page == "categories" else ""}">Categories</a></li>
          <li class="dropdown">
            <a href="#" class="dropdown-toggle" aria-haspopup="true" aria-expanded="false">Popular Schemes <span class="arrow">▼</span></a>
            <ul class="dropdown-menu">
{dropdown_items_html}            </ul>
          </li>
          <li><a href="about" class="{"active" if active_page == "about" else ""}">About</a></li>
          <li><a href="contact" class="{"active" if active_page == "contact" else ""}">Contact</a></li>
        </ul>
      </nav>"""
    return nav_html

def get_footer(popular_schemes=[]):
    popular_links = ""
    for s in popular_schemes[:6]:
        popular_links += f'            <li><a href="{s["id"]}">{s["title"]}</a></li>\n'
        
    footer_html = f"""    <footer class="site-footer" role="contentinfo">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-about">
          <span class="logo-text"><svg viewBox="0 0 24 24" class="logo-svg" style="display:inline-block;vertical-align:middle;margin-right:8px;width:24px;height:24px;fill:currentColor;"><path d="M12 2L1 7v2h22V7L12 2zm9 8H3v10h3V10h3v10h2V10h2v10h3V10h2v10h3V10zm1 11H2v2h20v-2z"/></svg>Yojana<span style="color: var(--accent-orange);">Guide</span></span>
          <p>Your trusted source for comprehensive information about Indian government schemes.</p>
          <div class="social-links">
            <a href="about" class="social-link" aria-label="About Us"><svg viewBox="0 0 24 24" class="social-svg-icon" style="width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg></a>
            <a href="contact" class="social-link" aria-label="Contact"><svg viewBox="0 0 24 24" class="social-svg-icon" style="width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg></a>
            <a href="categories" class="social-link" aria-label="Categories"><svg viewBox="0 0 24 24" class="social-svg-icon" style="width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg></a>
          </div>
        </div>
        </div>
        <div>
          <h4 class="footer-heading">Popular Schemes</h4>
          <ul class="footer-links">
{popular_links}          </ul>
        </div>
        <div>
          <h4 class="footer-heading">Categories</h4>
          <ul class="footer-links">
            <li><a href="categories">Agriculture</a></li>
            <li><a href="categories">Health</a></li>
            <li><a href="categories">Housing</a></li>
            <li><a href="categories">Education</a></li>
            <li><a href="categories">Women &amp; Child</a></li>
            <li><a href="categories">Financial Inclusion</a></li>
          </ul>
        </div>
        <div>
          <h4 class="footer-heading">Important Links</h4>
          <ul class="footer-links">
            <li><a href="about">About Us</a></li>
            <li><a href="contact">Contact Us</a></li>
            <li><a href="privacy-policy">Privacy Policy</a></li>
            <li><a href="disclaimer">Disclaimer</a></li>
            <li><a href="terms">Terms &amp; Conditions</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 Yojana Guide. All rights reserved.</p>
        <p><a href="privacy-policy">Privacy</a> · <a href="terms">Terms</a> · <a href="disclaimer">Disclaimer</a></p>
      </div>
    </div>
  </footer>"""
    return footer_html

def update_all_files():
    schemes = parse_all_schemes()
    print(f"Parsed {len(schemes)} schemes.")
    
    # Select popular schemes (e.g. key schemes the user wants to feature)
    priority_ids = ['pm-kisan', 'ayushman-bharat', 'ujjwala-yojana', 'pm-awas', 'sukanya-samriddhi', 'mudra-yojana', 'pm-surya-ghar', 'lakhpati-didi', 'pm-vishwakarma', 'jan-dhan', 'atal-pension', 'pm-kaushal-vikas', 'beti-bachao', 'kisan-credit-card', 'e-shram']
    popular_schemes = []
    for pid in priority_ids:
        for s in schemes:
            if s["id"] == pid:
                popular_schemes.append(s)
                break
                
    # Add any remaining schemes to pad the list
    for s in schemes:
        if s not in popular_schemes:
            popular_schemes.append(s)
            
    # Update navigation and footers on ALL pages (general pages + scheme pages)
    all_html_files = [f for f in os.listdir(path) if f.endswith('.html')]
    
    for filename in all_html_files:
        filepath = os.path.join(path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 0. Inject Google AdSense Script in <head>
        adsense_tag = 'client=ca-pub-7490572944753317'
        if adsense_tag not in content:
            adsense_code = '  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7490572944753317" crossorigin="anonymous"></script>'
            content = content.replace('</head>', f'{adsense_code}\n</head>')
            
        # 1. Update Navigation
        active_page = filename.replace(".html", "")
        if active_page not in ['index', 'categories', 'about', 'contact']:
            active_page = "schemes"
        content = re.sub(r'<nav class="main-nav" role="navigation" aria-label="Main Navigation">.*?</nav>', get_navigation(active_page, popular_schemes), content, flags=re.DOTALL)
        
        # 2. Update Footer
        content = re.sub(r'<footer class="site-footer" role="contentinfo">.*?</footer>', get_footer(popular_schemes), content, flags=re.DOTALL)
        
        # 2.3 Clean Canonical URL in <head>
        if filename == 'index.html':
            expected_canonical = "https://yojana-three.vercel.app/"
        else:
            expected_canonical = f"https://yojana-three.vercel.app/{filename.replace('.html', '')}"
            
        content = re.sub(
            r'<link\s+rel="canonical"\s+href="[^"]+"',
            f'<link rel="canonical" href="{expected_canonical}"',
            content
        )
        
        # 3. Update Category lists in categories.html
        if filename == "categories.html":
            categories_html_replacement = ""
            all_schemes_cards_html = ""
            for cat_id, cat_info in CATEGORIES.items():
                cat_schemes = [s for s in schemes if s["category"] == cat_id]
                
                desc = ""
                if cat_id == "agriculture":
                    desc = "Government schemes supporting farmers with financial assistance, crop insurance, irrigation subsidies, and agricultural loans."
                elif cat_id == "health":
                    desc = "Healthcare schemes providing insurance coverage, medical assistance, and hospital access for families."
                elif cat_id == "housing":
                    desc = "Affordable housing programs and rooftop solar utility subsidy programs providing direct incentives."
                elif cat_id == "education":
                    desc = "Scholarship programs, skill training initiatives, and educational assistance for students and traditional artisans."
                elif cat_id == "women":
                    desc = "Empowerment programs for women and children including savings schemes, maternity benefits, and nutrition programs."
                elif cat_id == "finance":
                    desc = "Banking access, micro-finance loans, pension schemes, and entrepreneurship support programs."
                elif cat_id == "employment":
                    desc = "Employment guarantees, job creation initiatives, and seed funding support for startups."
                elif cat_id == "pension":
                    desc = "Social security, pensions, and insurance safety nets for unorganized workers and senior citizens."
                elif cat_id == "rural":
                    desc = "Welfare and infrastructure development schemes targeting rural infrastructure, water supply, and rural employment."
                elif cat_id == "energy":
                    desc = "Power and electricity initiatives focusing on rural electrification, free solar installations, and green energy."
                elif cat_id == "infrastructure":
                    desc = "National programs for smart cities development, urban rejuvenation, and robust roads networks development."
                elif cat_id == "social":
                    desc = "Nutritional support programs, generic medicine provision, and safety nets for the marginalized."

                categories_html_replacement += f"""
          <div class="category-full-card" onclick="filterByCategory('{cat_id}', '{cat_info["name"]}')">
            <span class="cat-icon" aria-hidden="true">{cat_info["emoji"]}</span>
            <h3>{cat_info["name"]}</h3>
            <p>{desc}</p>
            <span class="scheme-badge">{len(cat_schemes)} Schemes</span>
          </div>"""
                
                for s in cat_schemes:
                    all_schemes_cards_html += f"""          <article class="scheme-card" data-category="{cat_id}">
            <div class="scheme-card-icon {cat_info["color"]}" aria-hidden="true">{s["emoji"]}</div>
            <span class="scheme-card-tag {cat_info["class"]}">{cat_info["name"]}</span>
            <h3><a href="{s["id"]}">{s["title"]}</a></h3>
            <p>{s["description"]}</p>
            <a href="{s["id"]}" class="card-link">Read Full Guide →</a>
          </article>\n"""
            
            # Replace categories grid
            content = re.sub(r'<!-- CATEGORIES_GRID_START -->.*?<!-- CATEGORIES_GRID_END -->', f'<!-- CATEGORIES_GRID_START -->\n        <div class="categories-page-grid">\n{categories_html_replacement}        </div>\n        <!-- CATEGORIES_GRID_END -->', content, flags=re.DOTALL)
            
            # Replace schemes results grid
            content = re.sub(r'<!-- SCHEMES_RESULTS_START -->.*?<!-- SCHEMES_RESULTS_END -->', f'<!-- SCHEMES_RESULTS_START -->\n        <div id="schemes-results-section" style="display: none;">\n          <div class="schemes-grid" id="schemes-list-container">\n{all_schemes_cards_html}          </div>\n        </div>\n        <!-- SCHEMES_RESULTS_END -->', content, flags=re.DOTALL)
            
        # 4. Update index.html Featured Grid & Categories Grid
        if filename == "index.html":
            # Rebuild Featured Schemes section cards
            schemes_cards_html = ""
            # Filter distinct category schemes for variety
            featured = []
            featured_cats = set()
            for s in popular_schemes:
                if s["category"] not in featured_cats and len(featured) < 12:
                    featured.append(s)
                    featured_cats.add(s["category"])
            # Add remaining featured schemes to make it exactly 12
            for s in popular_schemes:
                if s not in featured and len(featured) < 12:
                    featured.append(s)
                    
            for s in featured:
                cat_info = CATEGORIES[s["category"]]
                schemes_cards_html += f"""          <article class="scheme-card">
            <div class="scheme-card-icon {cat_info["color"]}" aria-hidden="true">{s["emoji"]}</div>
            <span class="scheme-card-tag {cat_info["class"]}">{cat_info["name"]}</span>
            <h3><a href="{s["id"]}">{s["title"]}</a></h3>
            <p>{s["description"]}</p>
            <a href="{s["id"]}" class="card-link">Read Full Guide →</a>
          </article>\n"""
            
            # Update schemes grid using comment markers
            content = re.sub(r'<!-- SCHEMES_GRID_START -->.*?<!-- SCHEMES_GRID_END -->', f'<!-- SCHEMES_GRID_START -->\n        <div class="schemes-grid">\n{schemes_cards_html}        </div>\n        <!-- SCHEMES_GRID_END -->', content, flags=re.DOTALL)
            
            # Categories grid
            cat_list_html = ""
            for cat_id, cat_info in CATEGORIES.items():
                cat_list_html += f"""          <a href="categories" class="category-card" aria-label="Browse {cat_info["name"]} schemes">
            <span class="category-icon" aria-hidden="true">{cat_info["emoji"]}</span>
            <div class="category-info">
              <h3>{cat_info["name"]}</h3>
              <p>Browse all active {cat_info["name"]} schemes.</p>
            </div>
          </a>\n"""
            
            # Update categories grid using comment markers
            content = re.sub(r'<!-- CATEGORIES_GRID_START -->.*?<!-- CATEGORIES_GRID_END -->', f'<!-- CATEGORIES_GRID_START -->\n        <div class="categories-grid">\n{cat_list_html}        </div>\n        <!-- CATEGORIES_GRID_END -->', content, flags=re.DOTALL)
            
            # Dynamic Latest Updates List
            import datetime
            today = datetime.date.today()
            def get_date_str(date_obj):
                return date_obj.strftime("%d"), date_obj.strftime("%b")
                
            day1, mon1 = get_date_str(today)
            day2, mon2 = get_date_str(today - datetime.timedelta(days=2))
            day3, mon3 = get_date_str(today - datetime.timedelta(days=4))
            day4, mon4 = get_date_str(today - datetime.timedelta(days=6))
            
            updates_html = f"""          <article class="update-item">
            <div class="update-date">
               <span class="day">{day1}</span>
               <span class="month">{mon1}</span>
            </div>
            <div class="update-content">
               <h4><a href="pm-kisan">PM Kisan Beneficiary Status Guide</a></h4>
               <p>Step-by-step instructions updated for verifying your name in the beneficiary list online.</p>
            </div>
          </article>
          <article class="update-item">
            <div class="update-date">
               <span class="day">{day2}</span>
               <span class="month">{mon2}</span>
            </div>
            <div class="update-content">
               <h4><a href="ayushman-bharat">Ayushman Card e-KYC Update</a></h4>
               <p>The online self-verification portal has updated enrollment guidelines for active health cards.</p>
            </div>
          </article>
          <article class="update-item">
            <div class="update-date">
               <span class="day">{day3}</span>
               <span class="month">{mon3}</span>
            </div>
            <div class="update-content">
               <h4><a href="pm-surya-ghar">PM Surya Ghar Calculator Live</a></h4>
               <p>Dynamic subsidy calculations and registration steps updated for solar rooftop installations.</p>
            </div>
          </article>
          <article class="update-item">
            <div class="update-date">
               <span class="day">{day4}</span>
               <span class="month">{mon4}</span>
            </div>
            <div class="update-content">
               <h4><a href="lakhpati-didi">Lakhpati Didi Training Rules</a></h4>
               <p>Updated application guidelines for self-help group members to access vocational training incentives.</p>
            </div>
          </article>\n"""
          
            content = re.sub(r'<!-- UPDATES_LIST_START -->.*?<!-- UPDATES_LIST_END -->', f'<!-- UPDATES_LIST_START -->\n        <div class="updates-list">\n{updates_html}        </div>\n        <!-- UPDATES_LIST_END -->', content, flags=re.DOTALL)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
    print("All HTML files synchronized.")

def generate_sitemap(schemes):
    sitemap_file = os.path.join(path, "sitemap.xml")
    
    sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""
    # General files
    for gf in GENERAL_PAGES:
        clean_gf = gf.replace('.html', '')
        if clean_gf == 'index':
            loc = "https://yojana-three.vercel.app/"
        else:
            loc = f"https://yojana-three.vercel.app/{clean_gf}"
            
        sitemap_content += f"""  <url>
    <loc>{loc}</loc>
    <lastmod>2026-07-06</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{"1.0" if clean_gf == "index" else "0.8"}</priority>
  </url>\n"""
  
    # Schemes
    for s in schemes:
        sitemap_content += f"""  <url>
    <loc>https://yojana-three.vercel.app/{s["id"]}</loc>
    <lastmod>2026-07-06</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>\n"""
  
    sitemap_content += "</urlset>"
    
    with open(sitemap_file, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
        
    print(f"Generated sitemap.xml with {len(GENERAL_PAGES) + len(schemes)} URLs.")

if __name__ == "__main__":
    schemes = parse_all_schemes()
    update_all_files()
    generate_sitemap(schemes)
    print("All pages and sitemap updated successfully!")

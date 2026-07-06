# -*- coding: utf-8 -*-
import os
import re

path = r'c:\Users\durga\OneDrive\Desktop\yojana'

# List of general pages
GENERAL_PAGES = ['index.html', 'categories.html', 'about.html', 'contact.html', 'privacy-policy.html', 'disclaimer.html', 'terms.html']

# Categories mapping
CATEGORIES = {
    "agriculture": {"name": "Agriculture & Farming", "emoji": "🌾", "class": "tag-agriculture", "color": "agriculture"},
    "health": {"name": "Health & Medical", "emoji": "🏥", "class": "tag-health", "color": "health"},
    "housing": {"name": "Housing & Shelter", "emoji": "🏠", "class": "tag-housing", "color": "housing"},
    "education": {"name": "Education & Skill Development", "emoji": "📚", "class": "tag-education", "color": "education"},
    "women": {"name": "Women & Child Development", "emoji": "👩‍👧", "class": "tag-women", "color": "women"},
    "finance": {"name": "Financial Inclusion & Business", "emoji": "💰", "class": "tag-finance", "color": "finance"},
    "employment": {"name": "Employment & Self-Employment", "emoji": "💼", "class": "tag-employment", "color": "employment"},
    "pension": {"name": "Pension & Social Security", "emoji": "👴", "class": "tag-pension", "color": "pension"},
    "rural": {"name": "Rural Development", "emoji": "🏘️", "class": "tag-rural", "color": "rural"},
    "energy": {"name": "Energy & Power", "emoji": "⚡", "class": "tag-energy", "color": "energy"},
    "infrastructure": {"name": "Infrastructure & Development", "emoji": "🏗️", "class": "tag-infrastructure", "color": "infrastructure"},
    "social": {"name": "Social Welfare & Security", "emoji": "🤝", "class": "tag-social", "color": "social"}
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
        title = title_match.group(1).split('2026')[0].split('-')[0].strip() if title_match else filename.replace('.html', '').replace('-', ' ').title()
        
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
        dropdown_items_html += f'              <li><a href="{s["id"]}.html">{s["title"]}</a></li>\n'
        
    nav_html = f"""      <nav class="main-nav" role="navigation" aria-label="Main Navigation">
        <ul class="nav-list">
          <li><a href="index.html" class="{"active" if active_page == "index" else ""}">Home</a></li>
          <li><a href="categories.html" class="{"active" if active_page == "categories" else ""}">Categories</a></li>
          <li class="dropdown">
            <a href="#" class="dropdown-toggle" aria-haspopup="true" aria-expanded="false">Popular Schemes <span class="arrow">▼</span></a>
            <ul class="dropdown-menu">
{dropdown_items_html}            </ul>
          </li>
          <li><a href="about.html" class="{"active" if active_page == "about" else ""}">About</a></li>
          <li><a href="contact.html" class="{"active" if active_page == "contact" else ""}">Contact</a></li>
        </ul>
      </nav>"""
    return nav_html

def get_footer(popular_schemes=[]):
    popular_links = ""
    for s in popular_schemes[:6]:
        popular_links += f'            <li><a href="{s["id"]}.html">{s["title"]}</a></li>\n'
        
    footer_html = f"""    <footer class="site-footer" role="contentinfo">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-about">
          <span class="logo-text">🏛️ Yojana<span style="color: var(--accent-orange);">Guide</span></span>
          <p>Your trusted source for comprehensive information about Indian government schemes.</p>
          <div class="social-links">
            <a href="about.html" class="social-link" aria-label="About Us">ℹ️</a>
            <a href="contact.html" class="social-link" aria-label="Contact">✉️</a>
            <a href="categories.html" class="social-link" aria-label="Categories">📂</a>
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
            <li><a href="categories.html">Agriculture</a></li>
            <li><a href="categories.html">Health</a></li>
            <li><a href="categories.html">Housing</a></li>
            <li><a href="categories.html">Education</a></li>
            <li><a href="categories.html">Women &amp; Child</a></li>
            <li><a href="categories.html">Financial Inclusion</a></li>
          </ul>
        </div>
        <div>
          <h4 class="footer-heading">Important Links</h4>
          <ul class="footer-links">
            <li><a href="about.html">About Us</a></li>
            <li><a href="contact.html">Contact Us</a></li>
            <li><a href="privacy-policy.html">Privacy Policy</a></li>
            <li><a href="disclaimer.html">Disclaimer</a></li>
            <li><a href="terms.html">Terms &amp; Conditions</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 Yojana Guide. All rights reserved.</p>
        <p><a href="privacy-policy.html">Privacy</a> · <a href="terms.html">Terms</a> · <a href="disclaimer.html">Disclaimer</a></p>
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
            
        # 1. Update Navigation
        active_page = filename.replace(".html", "")
        if active_page not in ['index', 'categories', 'about', 'contact']:
            active_page = "schemes"
        content = re.sub(r'<nav class="main-nav" role="navigation" aria-label="Main Navigation">.*?</nav>', get_navigation(active_page, popular_schemes), content, flags=re.DOTALL)
        
        # 2. Update Footer
        content = re.sub(r'<footer class="site-footer" role="contentinfo">.*?</footer>', get_footer(popular_schemes), content, flags=re.DOTALL)
        
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
            <h3><a href="{s["id"]}.html">{s["title"]}</a></h3>
            <p>{s["description"]}</p>
            <a href="{s["id"]}.html" class="card-link">Read Full Guide →</a>
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
            <h3><a href="{s["id"]}.html">{s["title"]}</a></h3>
            <p>{s["description"]}</p>
            <a href="{s["id"]}.html" class="card-link">Read Full Guide →</a>
          </article>\n"""
            
            # Update schemes grid using comment markers
            content = re.sub(r'<!-- SCHEMES_GRID_START -->.*?<!-- SCHEMES_GRID_END -->', f'<!-- SCHEMES_GRID_START -->\n        <div class="schemes-grid">\n{schemes_cards_html}        </div>\n        <!-- SCHEMES_GRID_END -->', content, flags=re.DOTALL)
            
            # Categories grid
            cat_list_html = ""
            for cat_id, cat_info in CATEGORIES.items():
                cat_list_html += f"""          <a href="categories.html" class="category-card" aria-label="Browse {cat_info["name"]} schemes">
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
              <h4><a href="pm-kisan.html">PM Kisan Beneficiary Status Guide</a></h4>
              <p>Step-by-step instructions updated for verifying your name in the beneficiary list online.</p>
            </div>
          </article>
          <article class="update-item">
            <div class="update-date">
              <span class="day">{day2}</span>
              <span class="month">{mon2}</span>
            </div>
            <div class="update-content">
              <h4><a href="ayushman-bharat.html">Ayushman Card e-KYC Update</a></h4>
              <p>The online self-verification portal has updated enrollment guidelines for active health cards.</p>
            </div>
          </article>
          <article class="update-item">
            <div class="update-date">
              <span class="day">{day3}</span>
              <span class="month">{mon3}</span>
            </div>
            <div class="update-content">
              <h4><a href="pm-surya-ghar.html">PM Surya Ghar Calculator Live</a></h4>
              <p>Dynamic subsidy calculations and registration steps updated for solar rooftop installations.</p>
            </div>
          </article>
          <article class="update-item">
            <div class="update-date">
              <span class="day">{day4}</span>
              <span class="month">{mon4}</span>
            </div>
            <div class="update-content">
              <h4><a href="lakhpati-didi.html">Lakhpati Didi Training Rules</a></h4>
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
        sitemap_content += f"""  <url>
    <loc>https://www.yojanaguide.in/{gf}</loc>
    <lastmod>2026-07-06</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{"1.0" if gf == "index.html" else "0.8"}</priority>
  </url>\n"""
  
    # Schemes
    for s in schemes:
        sitemap_content += f"""  <url>
    <loc>https://www.yojanaguide.in/{s["id"]}.html</loc>
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

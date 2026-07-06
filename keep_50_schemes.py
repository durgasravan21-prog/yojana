import os
import subprocess

path = r'c:\Users\durga\OneDrive\Desktop\yojana'

# The 50 schemes to keep
KEEP_SCHEMES = {
    'pm-kisan', 'pm-fasal-bima', 'kisan-credit-card', 'soil-health-card', 'paramparagat-krishi',
    'ayushman-bharat', 'pm-jan-aushadhi', 'mission-indradhanush', 'janani-suraksha', 'jssk',
    'pm-awas', 'pm-awas-urban', 'pm-surya-ghar', 'saubhagya',
    'samagra-shiksha', 'pm-shri-schools', 'pmrf', 'national-overseas-scholarship', 'pragati-scholarship',
    'sukanya-samriddhi', 'lakhpati-didi', 'beti-bachao', 'mission-shakti', 'mahila-shakti-kendra',
    'jan-dhan', 'mudra-yojana', 'stand-up-india', 'pmegp', 'cgtmse-scheme',
    'mgnrega', 'pm-kaushal-vikas', 'national-career-service', 'national-apprenticeship', 'garib-kalyan-rojgar',
    'atal-pension', 'pm-shram-yogi', 'pm-kisan-maandhan', 'varishtha-pension', 'pmvvy',
    'jal-jeevan-mission', 'swachh-bharat', 'pm-gram-sadak', 'rurban-mission',
    'ujala-scheme', 'ujjwala-yojana', 'national-solar-mission',
    'smart-cities', 'amrut', 'gati-shakti',
    'national-food-security'
}

GENERAL_PAGES = {
    'index.html', 'categories.html', 'about.html', 'contact.html', 
    'privacy-policy.html', 'disclaimer.html', 'terms.html'
}

def main():
    print("Starting cleanup to keep only 50 selected schemes...")
    files = os.listdir(path)
    deleted_count = 0
    kept_count = 0
    
    for filename in files:
        if filename.endswith('.html'):
            name_without_ext = filename[:-5]
            if filename in GENERAL_PAGES:
                # Keep general pages
                continue
            elif name_without_ext in KEEP_SCHEMES:
                kept_count += 1
                continue
            else:
                # Delete this file
                filepath = os.path.join(path, filename)
                try:
                    os.remove(filepath)
                    deleted_count += 1
                except Exception as e:
                    print(f"Error deleting {filename}: {e}")
                    
    print(f"Deleted {deleted_count} scheme files.")
    print(f"Kept {kept_count} scheme files.")
    
    # Run update_all_pages.py to sync sitemap, categories page, and index page
    print("Running update_all_pages.py to synchronize homepage, categories, and sitemap...")
    subprocess.run(["python", os.path.join(path, "update_all_pages.py")], check=True)
    print("Sync complete!")

if __name__ == "__main__":
    main()

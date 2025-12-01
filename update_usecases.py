import os
import json
import re

USECASE_DIR = "usecases"
JSON_FILE = "usecases.json"

def extract_meta_tag(html, name):
    """Extract content from meta tag by name attribute"""
    pattern = rf'<meta\s+name=["\']?{re.escape(name)}["\']?\s+content=["\']([^"\']*)["\']'
    match = re.search(pattern, html, re.IGNORECASE)
    return match.group(1).strip() if match else None

def extract_title(html):
    """Extract title from <title> tag, removing ' | INVOKE' suffix"""
    match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    if match:
        title = match.group(1).strip()
        # Remove ' | INVOKE' suffix if present
        title = re.sub(r'\s*\|\s*INVOKE\s*$', '', title, flags=re.IGNORECASE)
        return title
    return None

def main():
    entries = []
    
    for file in os.listdir(USECASE_DIR):
        if not file.endswith(".html") or file.startswith("_"):
            continue
        
        path = os.path.join(USECASE_DIR, file)
        slug = file.replace(".html", "")
        
        with open(path, "r", encoding="utf-8") as f:
            html = f.read()
        
        # Try to extract from meta tags first (preferred)
        name = extract_meta_tag(html, "use-case-name")
        category = extract_meta_tag(html, "use-case-category")
        description = extract_meta_tag(html, "description")
        
        # Fallback to title tag if meta tag not found
        if not name:
            name = extract_title(html)
        
        # Final fallback to filename
        if not name:
            name = slug.replace("-", " ").title()
        
        # Default category if not found
        if not category:
            category = "Automation"
        
        # Default description if not found
        if not description:
            description = "AI-powered automation solution for improved efficiency and outcomes."
        
        entries.append({
            "slug": slug,
            "name": name,
            "category": category,
            "description": description
        })
        
        print(f"📄 Processed: {slug}")
        print(f"   Name: {name}")
        print(f"   Category: {category}")
        print(f"   Description: {description[:60]}...")
        print()
    
    # Sort alphabetically by name for clean UI
    entries = sorted(entries, key=lambda x: x["name"])
    
    with open(JSON_FILE, "w") as f:
        json.dump(entries, f, indent=2)
    
    print("✅ usecases.json rebuilt successfully.")
    print(f"📁 Total entries: {len(entries)}")
    print(f"📂 Output: {JSON_FILE}")

if __name__ == "__main__":
    main()
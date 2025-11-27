import os
import json
import re
from datetime import datetime

USECASE_DIR = "usecases"
JSON_FILE = "usecases.json"

def extract_title(html):
    match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else None

def extract_description(html):
    match = re.search(r"<p>(.*?)</p>", html, re.IGNORECASE | re.DOTALL)
    if match:
        text = re.sub(r"<.*?>", "", match.group(1)).strip()
        return text[:240]  # safety trim for card display
    return None

def load_existing():
    if not os.path.exists(JSON_FILE):
        return []

    with open(JSON_FILE, "r") as f:
        return json.load(f)

def save(data):
    with open(JSON_FILE, "w") as f:
        json.dump(data, f, indent=2)

def main():
    existing = load_existing()
    json_mtime = os.path.getmtime(JSON_FILE) if os.path.exists(JSON_FILE) else 0

    updated = False
    seen_slugs = {entry["slug"] for entry in existing}

    for file in os.listdir(USECASE_DIR):
        if not file.endswith(".html") or file.startswith("_"):
            continue
        
        path = os.path.join(USECASE_DIR, file)
        slug = file.replace(".html", "")
        file_mtime = os.path.getmtime(path)

        if file_mtime <= json_mtime and slug in seen_slugs:
            continue  # skip unchanged pages

        with open(path, "r", encoding="utf-8") as f:
            html = f.read()

        title = extract_title(html) or slug.replace("-", " ").title()
        description = extract_description(html) or "AI & automation use case."

        entry = {
            "name": title,
            "slug": slug,
            "description": description
        }

        # replace existing entry if updated
        existing = [e for e in existing if e["slug"] != slug]
        existing.append(entry)
        updated = True

        print(f"✅ Updated entry for: {slug}")

    if updated:
        save(sorted(existing, key=lambda x: x["name"]))
        print("\n📁 usecases.json updated successfully.")
    else:
        print("\n✅ No changes detected — JSON already up to date.")

if __name__ == "__main__":
    main()

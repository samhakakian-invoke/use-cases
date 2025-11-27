import os
import json
import re

USECASE_DIR = "usecases"
JSON_FILE = "usecases.json"

def extract_title(html):
    match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else None

def extract_description(html):
    match = re.search(r"<p>(.*?)</p>", html, re.IGNORECASE | re.DOTALL)
    if match:
        text = re.sub(r"<.*?>", "", match.group(1)).strip()
        return text[:240]
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

        title = extract_title(html) or slug.replace("-", " ").title()
        description = extract_description(html) or "AI & automation use case."

        entries.append({
            "name": title,
            "slug": slug,
            "description": description
        })

        print(f"📄 Processed: {slug}")

    # Sort alphabetically by name for clean UI
    entries = sorted(entries, key=lambda x: x["name"])

    with open(JSON_FILE, "w") as f:
        json.dump(entries, f, indent=2)

    print("\n✅ usecases.json rebuilt successfully.")
    print(f"📁 Total entries: {len(entries)}")

if __name__ == "__main__":
    main()

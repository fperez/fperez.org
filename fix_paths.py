#!/usr/bin/env python
# Created by ChatGPT 4.0 - Mar 28, 2025

import os
from bs4 import BeautifulSoup

# Settings
root_dir = "."
prefix = "/fperez.org/"
path_starts = ("_static/", "_images/", "_downloads/", "_files/")

# Tags and their attributes to rewrite
tags_attrs = {
    "link": "href",
    "script": "src",
    "img": "src",
    "a": "href"
}

def should_rewrite(url):
    if url is None:
        return False
    if url.startswith("http://") or url.startswith("https://"):
        return False
    return url.startswith(path_starts)

def fix_html_file(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")
    changed = False

    for tag_name, attr in tags_attrs.items():
        for tag in soup.find_all(tag_name):
            if attr in tag.attrs and should_rewrite(tag[attr]):
                old_url = tag[attr]
                tag[attr] = prefix + old_url
                print(f"🔧 Rewriting in {filepath}: {old_url} → {tag[attr]}")
                changed = True

    if changed:
        # Backup and write
        os.rename(filepath, filepath + ".bak")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str(soup))
        print(f"✔️  Updated: {filepath}")

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".html"):
                filepath = os.path.join(root, filename)
                fix_html_file(filepath)

if __name__ == "__main__":
    process_directory(root_dir)

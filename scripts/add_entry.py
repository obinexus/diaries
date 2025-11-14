#!/usr/bin/env python3
"""
Bidirectional Diary Entry Script
Supports: English | French | Auto-dated Markdown files
Author: Nambi Michaela (Obi Nexus)
"""

import os
from datetime import datetime

# === CONFIG ===
DIARY_ROOT = os.path.dirname(os.path.abspath(__file__))  # scripts/ folder
DIARY_ROOT = os.path.dirname(DIARY_ROOT)                    # go up to diares/
ENTRIES_DIR = os.path.join(DIARY_ROOT, "entries")           # entries/2025-11-14.md
os.makedirs(ENTRIES_DIR, exist_ok=True)  # Auto-create if missing

# Language toggle (set once or make interactive later)
LANGUAGE = "en"  # "en" or "fr"

PROMPTS = {
    "en": "Enter your diary entry (or type 'quit' to exit): ",
    "fr": "Entrez votre entrée de journal (ou tapez 'quit' pour quitter) : "
}

def add_entry():
    prompt = PROMPTS.get(LANGUAGE, PROMPTS["en"])
    print(f"\n=== Bidirectional Diary [{LANGUAGE.upper()}] ===")
    entry_lines = []
    
    print(prompt)
    while True:
        line = input()
        if line.strip().lower() == 'quit':
            break
        if line.strip() == '':
            continue
        entry_lines.append(line)
    
    if not entry_lines:
        print("No entry saved. Empty input.")
        return

    # Generate filename
    today = datetime.now().strftime("%Y-%m-%d")
    lang_suffix = f"_{LANGUAGE}" if LANGUAGE != "en" else ""
    filename = os.path.join(ENTRIES_DIR, f"{today}{lang_suffix}.md")

    # Write entry with header
    header = f"# Diary Entry - {today} ({LANGUAGE.upper()})"
    content = "\n\n".join(entry_lines).strip()

    with open(filename, 'a' if os.path.exists(filename) else 'w', encoding='utf-8') as f:
        if os.path.getsize(filename) if os.path.exists(filename) else 0 > 0:
            f.write("\n\n---\n\n")  # Separator for multiple entries same day
        f.write(f"{header}\n\n{content}\n")

    print(f"\nEntry saved to: {filename}\n")

if __name__ == "__main__":
    add_entry()

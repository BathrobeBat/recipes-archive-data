from pathlib import Path
import subprocess
import re

# repo paths
repo = Path(__file__).resolve().parents[1]
recipes_path = repo / "recipes"

# hämta kategorier från mappar
categories = [p.name for p in recipes_path.iterdir() if p.is_dir()]

print("\nSelect category:\n")

for i, cat in enumerate(categories, start=1):
    print(f"{i}. {cat}")

choice = int(input("\nCategory number: ")) - 1
category = categories[choice]

title = input("Recipe name: ")

filename = re.sub(r"[^a-z0-9]+", "_", title.lower()).strip("_")

file_path = recipes_path / category / f"{filename}.md"

file_path.parent.mkdir(parents=True, exist_ok=True)

template = f"""---
id: {filename}
title: {title}
author:
category: {category}
tags:
servings:
prep_time:
cook_time:

ingredients:
  main:
---

## Instruktioner

1.
2.
3.
"""

file_path.write_text(template, encoding="utf-8")

print(f"\nCreated: {file_path}")

try:
    subprocess.run(["code", str(file_path)])
except FileNotFoundError:
    print("VS Code CLI ('code') not found in PATH. File created but not opened.")
from pathlib import Path
import subprocess
import re

# repo root
repo = Path(__file__).resolve().parents[1]

datasets = {
    "recipes": {
        "path": repo / "recipes",
        "template": repo / "templates" / "recipe.md"
    },
    "brewing": {
        "path": repo / "brewing",
        "template": repo / "templates" / "brew.md"
    }
}

print("\nSelect dataset:\n")

dataset_names = list(datasets.keys())

for i, name in enumerate(dataset_names, start=1):
    print(f"{i}. {name}")

dataset_choice = int(input("\nDataset number: ")) - 1
dataset_name = dataset_names[dataset_choice]

dataset = datasets[dataset_name]

base_path = dataset["path"]
template_path = dataset["template"]

# read categories
categories = [p.name for p in base_path.iterdir() if p.is_dir()]

print("\nSelect category:\n")

for i, cat in enumerate(categories, start=1):
    print(f"{i}. {cat}")

choice = int(input("\nCategory number: ")) - 1
category = categories[choice]

title = input("Name: ")

# sanitize filename
filename = re.sub(r"[^a-z0-9]+", "_", title.lower()).strip("_")

file_path = base_path / category / f"{filename}.md"

# ensure folder exists
file_path.parent.mkdir(parents=True, exist_ok=True)

# load template
template = template_path.read_text(encoding="utf-8")

# replace placeholders if present
template = template.replace("{id}", filename)
template = template.replace("{title}", title)
template = template.replace("{category}", category)

# write file
file_path.write_text(template, encoding="utf-8")

print(f"\nCreated: {file_path}")

# stage file automatically
try:
    subprocess.run(["git", "add", str(file_path)])
    print("File staged with git add")
except Exception:
    print("git add failed (are you inside the repo?)")

# open in VS Code if available
try:
    subprocess.run(["code", str(file_path)])
except FileNotFoundError:
    print("VS Code CLI ('code') not found in PATH. File created but not opened.")
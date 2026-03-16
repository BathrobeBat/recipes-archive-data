from pathlib import Path
import yaml

repo = Path(__file__).resolve().parents[1]

recipes_path = repo / "recipes"
brewing_path = repo / "brewing"
readme_path = repo / "README.md"


def read_title(file):
    text = file.read_text(encoding="utf-8")

    if text.startswith("---"):
        yaml_block = text.split("---")[1]
        data = yaml.safe_load(yaml_block)
        return data.get("title", file.stem)

    return file.stem


def build_section(base_path):

    lines = []

    for category_path in sorted(p for p in base_path.iterdir() if p.is_dir()):

        files = sorted(category_path.glob("*.md"))

        if not files:
            continue

        category = category_path.name
        lines.append(f"\n#### {category} ({len(files)})\n")

        recipes = []

        for file in files:
            title = read_title(file)
            rel = file.relative_to(repo)
            recipes.append((title, rel))

        recipes.sort()

        for title, rel in recipes:
            lines.append(f"- [{title}]({rel})")

    return "\n".join(lines)


content = []

content.append("\n## Cooking\n")
content.append(build_section(recipes_path))

content.append("\n\n## Brewing\n")
content.append(build_section(brewing_path))

index_block = "\n".join(content)

readme = readme_path.read_text()

start = "<!-- INDEX_START -->"
end = "<!-- INDEX_END -->"

before = readme.split(start)[0]
after = readme.split(end)[1]

new_readme = before + start + "\n" + index_block + "\n" + end + after

readme_path.write_text(new_readme)

print("Recipe index updated")
from pathlib import Path
import yaml

recipes_dir = Path("recipes")

ids = set()
errors = []

for file in recipes_dir.rglob("*.md"):

    text = file.read_text(encoding="utf-8")

    if not text.startswith("---"):
        errors.append(f"{file} missing YAML header")
        continue

    yaml_block = text.split("---")[1]

    try:
        data = yaml.safe_load(yaml_block)
    except Exception as e:
        errors.append(f"{file} invalid YAML: {e}")
        continue

    recipe_id = data.get("id")

    if not recipe_id:
        errors.append(f"{file} missing id")

    if recipe_id in ids:
        errors.append(f"Duplicate recipe id: {recipe_id}")

    ids.add(recipe_id)

    category = data.get("category")

    if not (recipes_dir / category).exists():
        errors.append(f"{file} invalid category {category}")

if errors:
    print("\nValidation errors:\n")
    for e in errors:
        print("-", e)
    exit(1)

print("All recipes valid")
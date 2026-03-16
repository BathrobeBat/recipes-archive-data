# Recipe Archive Data

This repository contains a structured archive of recipes stored as Markdown files with YAML metadata.

The goal of this repository is to preserve family recipes in a format that is:

* human readable
* version controlled
* easy to import into databases
* independent of any specific application
* future-proof

This repository acts as the **source of truth for recipe data**.

Future applications (web apps, APIs, databases, etc.) will import their data from this repository.

---

# Repository Structure

```
recipes/
│
├── bakverk
├── brod
├── chark
├── desserter
├── drycker
├── huvudratter
├── saser
└── tillbehor

templates/
└── recipe.md

scripts/
├── new_recipe.py
└── validate_recipes.py

.github/
└── workflows/
    └── validate_recipes.yml
```

---

# Recipe Format

Recipes are written in **Markdown with YAML front matter**.

Example:

```markdown
---
id: blodpudding
title: Blodpudding
author: Mamma
category: chark
tags:
servings:
prep_time:
cook_time:

ingredients:
  main:
    - item: grisblod
      amount: 1
      unit: liter
---

## Instruktioner

1. Blanda blod och mjöl.
2. Tillsätt kryddor.
3. Grädda i ugn.
```

---

# Scripts

## new_recipe.py

Helper script used to create new recipes quickly.

The script will:

1. Display a list of recipe categories
2. Let the user select a category
3. Ask for the recipe title
4. Automatically create the Markdown file
5. Populate the file with the recipe template
6. Open the file directly in VS Code

Example usage:

```
python scripts/new_recipe.py
```

Example workflow:

```
Select category:

1. bakverk
2. brod
3. chark
4. desserter
5. drycker
6. huvudratter
7. saser
8. tillbehor

Category number: 3
Recipe name: Blodpudding
```

This automatically creates:

```
recipes/chark/blodpudding.md
```

and opens it in the editor.

---

## validate_recipes.py

Validation script that checks all recipes for errors.

The script verifies:

* YAML syntax
* required fields
* duplicate recipe IDs
* valid categories

Example usage:

```
python scripts/validate_recipes.py
```

---

# Automated Validation

This repository uses **GitHub Actions** to automatically validate all recipes on every push.

The validation ensures:

* recipe metadata is valid YAML
* each recipe has a unique ID
* categories exist
* no corrupted recipe files exist

If validation fails, the CI pipeline will block the change.

---

# Workflow

Typical workflow for adding recipes:

1. Run the recipe helper script

```
python scripts/new_recipe.py
```

2. Write the recipe in the generated file.

3. Commit the changes.

```
git add .
git commit -m "Add recipe: blodpudding"
git push
```

4. GitHub automatically validates the recipes.

---

# Design Philosophy

This repository follows a **data-first architecture**.

Key ideas:

* Recipes are stored as plain text
* Git provides full version history
* The data is independent of any specific application
* Databases and applications can be rebuilt from this repository

This ensures the recipe archive can survive long-term without relying on a specific platform.

---

# Future Plans

Possible future integrations include:

* automated database import
* search and filtering
* web interface
* API access
* recipe editing UI
* OCR import for handwritten recipes

---

# License

This repository is intended primarily for personal archival purposes.


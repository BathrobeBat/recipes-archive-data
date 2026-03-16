# Recipe Archive Data

This repository contains a structured archive of **cooking recipes and brewing recipes** stored as Markdown files with YAML metadata.

The goal is to preserve handwritten and collected recipes in a format that is:

* human readable
* version controlled
* easy to import into databases
* independent of any specific application
* future-proof

The repository acts as the **source of truth** for all recipe data.

Future tools such as web apps, APIs, or databases can import their data directly from this archive.

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

brewing/
│
├── beer
├── cider
├── mead
└── wine

templates/
├── recipe.md
└── brew.md

scripts/
└── new_recipe.py
```

---

# Recipe Types

The repository contains two types of recipes.

## Cooking Recipes

Located in:

```
recipes/
```

These contain traditional cooking and baking recipes.

Example:

```
recipes/chark/blodleverkorv_5m_notfjalster.md
```

---

## Brewing Recipes

Located in:

```
brewing/
```

These contain brewing recipes for beverages such as:

* beer
* wine
* mead
* cider

Example:

```
brewing/wine/chateau_de_bat.md
```

---

# Recipe Generator

To speed up entering recipes, the repository includes a small helper script.

Run:

```
recipe
```

The script will:

1. Choose dataset (`recipes` or `brewing`)
2. Choose category
3. Enter recipe name
4. Generate the file automatically
5. Stage the file using `git add`
6. Open the file in VS Code (if available)

Example workflow:

```
recipe
→ recipes / brewing
→ category
→ name
```

The generated file will already contain the correct template.

---

# Recipe Format

Recipes are written using **Markdown with YAML front matter**.

Example:

```markdown
---
id: blodleverkorv_5m_notfjalster
title: Blodleverkorv (5m nötfjälster)
category: chark
tags:
---

## Instruktioner

1.
2.
3.
```

---

# Brewing Recipe Format

Brewing recipes use a slightly different structure.

Example:

```markdown
---
id: chateau_de_bat
title: Chateau de Bat
type: wine
batch_size:
og:
fg:
abv:
---

## Process

1.
2.
3.
```

---

# Workflow

Typical workflow when adding recipes:

```
recipe
write recipe
git commit
git push
```

Example commit messages:

```
recipe: chark/blodleverkorv
brew: wine/chateau_de_bat
```

---

# Design Philosophy

This project follows a **data-first approach**.

Recipes are stored as structured text instead of being locked inside a specific application.

Advantages:

* long-term preservation
* full version history via Git
* easy data migration
* simple integration with future applications

---

# Future Plans

Possible future improvements:

* automated recipe validation
* searchable recipe interface
* API for accessing recipes
* OCR import for handwritten recipes
* brewing log support

---

## Recipe Index

<!-- INDEX_START -->

# Recipe Index


## Cooking


#### chark (1)

- [Blodleverkorv (5m nötfjälster)](recipes/chark/blodleverkorv_5m_notfjalster.md)


## Brewing


#### wine (1)

- [Chateau de Bat](brewing/wine/chateau_de_bat.md)
<!-- INDEX_END -->

---

# License

This repository is primarily intended as a personal archive and learning project.

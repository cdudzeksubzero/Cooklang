# Docs: https://cooklang-py.readthedocs.io/en/latest/
# PyPi: https://pypi.org/project/cooklang-py/

from cooklang_py import Recipe
from pathlib import Path

# The metadata is available via . notation (md.tags), index notation (md['tags']), and a get method (md.get('tags', '')).
official_metadata = [
    "author",
    "category",
    "cook time",
    "course",
    "cuisine",
    "description",
    "diet",
    "difficulty",
    "duration",
    "image",
    "images",
    "introduction",
    "locale",
    "picture",
    "pictures",
    "prep time",
    "serves",
    "servings",
    "source",
    "source.author",
    "source.name",
    "tags",
    "time required",
    "time",
    "time.cook",
    "time.prep",
    "title",
    "yield",
]
complex_metadata = {
    "source": ["name", "author", "url"],
    "time": ["prep", "cook"]
}
custom_metadata = [
    "prepTime",
    "cookTime",
]

# Load a recipe from a file
recipe_file = Path('c:/repos/Cooklang/recipes/Lamb/Croatian_Lamb_Peka.cook')
recipe = Recipe.from_file(recipe_file)
if recipe:
    print("Loaded recipe from file:", recipe_file)
    print(f"Title: {recipe.metadata.get('title', 'No title found')}")

print()

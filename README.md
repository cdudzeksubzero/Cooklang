# Cooklang

## Editor Notes

* Cook files end in `.cook` extension

## General Tips

* Per [Getting Started], convert any recipe from the web by adding
  `https://cook/md/` before any URL to auto-convert recipes.
  * For example, [Easy
    Pancakes](https://cook.md/https://bbcgoodfood.com/recipes/easy-pancakes/)
* Cooklang recipes are plain `.cook` text files. The [Cooklang Specification]
  syntax is simple:
  * `@` names ingredients, `#` marks cookware, `~` sets timers, and `--` adds
    comments.
  * Multi-word ingredients end with `{}`, quantities go inside `{}`, and units
    follow `%`.
  > `@plain flour{100%g}, @eggs{2}(large), @milk{300%ml}, @sunflower or
  > vegetable oil{1%tbsp} and @salt{pinch} into a #bowl{}`

## Command-Line Tool

* `cook server` from folder to host local site
  * See warnings in viewed recipes when browsing site
* `cook seed` to auto-populate example recipes

<!-- Reference Links -->
[Getting Started]: https://cooklang.org/docs/getting-started/
[Cooklang Specification]: https://cooklang.org/docs/spec/

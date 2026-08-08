# What's next

* Install a syntax highlighting package for your text editor. We have packages for SublimeText and VSCode. See  [cooklang.org](https://cooklang.org/docs/syntax-highlighting/) for full instructions.
* Add your own recipes. Dive into the Cook ecosystem and discover how easy it is to write in CookLang. It's the best way to learn the [CookLang syntax](https://cooklang.org/docs/spec/).
* Check out the [use-cases](https://cooklang.org/docs/use-cases/) and user created recipes in [aggregator](https://recipes.cooklang.org/browse).

## Where to go next

1. **Open this folder in Cook Editor** — <https://cook.md/editor>. Browse
   recipes, edit the meal plan and generate an aisle-ordered shopping list.
2. **Take it mobile** — the Cooklang app for iOS and Android syncs this
   folder to your phone: <https://cooklang.org/app/>.
3. **Learn the format** — the Cooklang syntax takes five minutes:
   <https://cooklang.org/docs/spec/>.
4. **Questions?** — help and guides live at <https://cook.md/help>.

## Read the recipe

```sh
cook recipe read "Risotto.cook"
```

## Scale a recipe

```sh
cook recipe read "Risotto.cook:2"
```

## Create shopping list

```sh
cook shopping-list \
  "Neapolitan Pizza.cook" \
  "Risotto.cook" \
  "Thai Green Curry.cook"
```

## Run a server

In directory where you have your recipes run:

```sh
cook server
```

Then open [http://127.0.0.1:9080](http://127.0.0.1:9080) in your browser.

## Automate something

Explore [the docs](https://cooklang.org/cli/), which describe how to use CookCLI's automation tools.

## Customize your instance

Add aisle configuration to `config/aisle.conf` to organize your shopping list by store section, and stock your pantry in `config/pantry.conf` to filter out items you already have.

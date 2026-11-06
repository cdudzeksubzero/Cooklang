import json
import requests

# Ref: https://cooklang.org/cli/commands/api/

postman_notes = '''
Setup in Postman
1. Open Postman and create a new request tab.
2. Set the HTTP request method dropdown to POST.
3. Set your target URL based on the action you want to take:
	• To build/generate a list from specific recipes: http://pikitchen.local:9080/api/shopping_list
	• To add custom items or extra ingredients: http://pikitchen.local:9080/api/shopping_list/add
4. Go to the Headers tab and add:
	• Key: Content-Type
	• Value: application/json
5. Go to the Body tab, select the raw radio button, and choose JSON from the format dropdown.
'''

# Default cook server address
SERVER_URL = "http://pikitchen.local:9080"

def clear_shopping_list():
    """
    Clear the shopping list on the cook server.
    """
    try:
        response = requests.post(f"{SERVER_URL}/api/shopping_list/clear")
        if response.status_code == 200:
            print("Shopping list cleared successfully.")
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("Could not connect to cook server. Is it running?")

def clean_number(val):
    """Converts whole floats like 3.0 to 3 for cleaner printing."""
    if isinstance(val, float) and val.is_integer():
        return int(val)
    return val

def convert_cooklang_list(json_string):
    data = json.loads(json_string)
    
    for cat_data in data.get("categories", []):
        # The key in your real data is "category" instead of "name"
        print(f"=== {cat_data['category'].upper()} ===")
        
        for item in cat_data.get("items", []):
            name = item.get("name")
            quantities = item.get("quantities", [])
            qlist = []
            for qty in quantities:
                # Safely drill down into value -> value -> value
                raw_val = qty.get("value", {}).get("value", {}).get("value", "")
                val = clean_number(raw_val)
                if isinstance(val, float) and not val.is_integer() and val > 0:
                    val = round(val, 2)  # Round to 2 decimal places if it's a float
                unit = qty.get("unit", "")
                
                # Don't print the unit if it's literally the string "None" or empty
                if unit and unit != "None":
                    qlist.append(f"{val} {unit}")
                elif val != "":
                    qlist.append(f"{val}")
            if qlist:
                print(f"[ ] {name} ({' + '.join(qlist)})")
            else:
                print(f"[ ] {name}")
            # if quantities:
            #     # Get the first quantity object from the list
            #     qty_info = quantities[0]
            #     unit = qty_info.get("unit", "")
                
            #     # Safely drill down into value -> value -> value
            #     raw_val = qty_info.get("value", {}).get("value", {}).get("value", "")
            #     val = clean_number(raw_val)
            #     if isinstance(val, float) and not val.is_integer() and val > 0:
            #         val = round(val, 2)  # Round to 2 decimal places if it's a float

            #     # Don't print the unit if it's literally the string "None" or empty
            #     if unit and unit != "None":
            #         print(f"[ ] {name} ({val} {unit})")
            #     elif val != "":
            #         print(f"[ ] {name} ({val})")
            #     else:
            #         print(f"[ ] {name}")
            # else:
            #     print(f"[ ] {name}")
        print()
   
def get_recipe_list():
    """
    Get a shopping list from the cook server based on the provided recipes.
    """
    try:
        response = requests.get(f"{SERVER_URL}/api/recipes")  # Check server documentation for exact endpoints
        if response.status_code == 200:
            data = response.json()
            print("Recipes:", data)
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("Could not connect to cook server. Is it running?")

def get_shopping_list():
    """
    Get a shopping list from the cook server based on the provided recipes.
    """
    # request_body = '''[ { "recipe": "Convection Steam Oven/Breakfast/Dutch Baby Pancake", "scale": 1 } ]'''

    names = get_shopping_list_recipes()
    request_body = json.dumps([{"recipe": name, "scale": 1} for name in names])
    if not names or len(names) == 0:
        print("No recipes found in the shopping list.")
        return

    try:
        response = requests.post(f"{SERVER_URL}/api/shopping_list", data=request_body, headers={"Content-Type": "application/json"})
        if response.status_code == 200:
            data = response.json()
            # print("Shopping List:", data)
            convert_cooklang_list(json.dumps(data))
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("Could not connect to cook server. Is it running?")

def get_shopping_list_recipes() -> list[str]:
    # GET: /api/shopping_list/items
    # An entry with a recipes array is a menu added via add_menu
    shopping_recipes: list[str] = []
    try:
        response = requests.get(f"{SERVER_URL}/api/shopping_list/items", )
        if response.status_code == 200:
            data = response.json()
            # print("Shopping List:", data)
            for item in data:
                if "path" in item:
                    shopping_recipes.append(item.get("path",""))
                for ref in item.get("included_references", []):
                    shopping_recipes.append(ref)
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("Could not connect to cook server. Is it running?")

    return shopping_recipes

if __name__ == "__main__":
    # get_recipe_list()
    get_shopping_list()
    # get_shopping_list_recipes()

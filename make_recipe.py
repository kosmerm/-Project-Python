
import json
import time
from tqdm import tqdm

def load_recipes(filename="recipes.json"):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def execute_recipe():
    data = load_recipes()
    recipes = data["recipes"]

    print("\n📋 Διαθέσιμες συνταγές:")
    for i, recipe in enumerate(recipes, 1):
        print(f"{i}. {recipe['name']}")

    choice = input("\nΔιάλεξε αριθμό συνταγής ή 'q' για έξοδο: ")
    if choice.lower() == 'q':
        return

    if not choice.isdigit() or not (1 <= int(choice) <= len(recipes)):
        print("Μη έγκυρη επιλογή.")
        return

    recipe = recipes[int(choice) - 1]
    print(f"\n🍽️ {recipe['name']}")
    print(f"Κατηγορία: {recipe['category']}")
    print(f"Δυσκολία: {recipe['difficulty']}")
    print(f"Χρόνος: {recipe['total_time']} λεπτά")

    print("\n🧾 Υλικά:")
    for ing in recipe["ingredients"]:
        qty = f" ({ing['quantity']} γρ)" if ing["quantity"] else ""
        print(f"- {ing['name']}{qty}")

    print("\n🧑‍🍳 Εκτέλεση:")
    for i, step in enumerate(recipe["steps"], 1):
        input(f"\nΒήμα {i}: {step}\nΠάτησε Enter για να συνεχίσεις...")
        for _ in tqdm(range(30), desc="Επεξεργασία...", ncols=60):
            time.sleep(0.01)

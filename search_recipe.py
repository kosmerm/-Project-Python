from json_manager import *

data = load_recipes("recipes.json")

# Προβολή όλων των συνταγών
def view_recipes():
    for i, recipe in enumerate(data["recipes"], start = 1):
        print(f"{i}. {recipe['name']} ({recipe['total_time']})")

# Αναζήτηση συνταγής
def search_recipe():
    name = input("Αναζητήστε συνταγή με όνομα: ").lower()
    found = [r for r in data["recipes"] if name in r["name"].lower()]
    if found:
        for recipe in found:
            print(f"\n{recipe['name']} ({recipe['total_time']})")
            print("\nΥλικά:")
            for ing in recipe["ingredients"]:
                print(f"- {ing['name']} - {ing['quantity']}")
            print("\nΒήματα:")
            for i, step in enumerate(recipe["steps"], 1):
                print(f"{i}. {step}")
    else:
        print(" Δεν βρέθηκε συνταγή.")

while True:
    print("1. Εμφάνιση συνταγών")
    print("2. Αναζήτηση συνταγής")
    print("3. Έξοδος")
    choice = input("Επιλογή (1-3): ")
    if choice == "1":
        view_recipes()
    elif choice == "2":
        search_recipe()
    elif choice == "3":
        break

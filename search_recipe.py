import json
import os
from json_manager import *

FILE_NAME = "recipes.json"

# Αν το αρχείο δεν υπάρχει, δημιουργείται ένα κενό
# if not os.path.exists(FILE_NAME):
#     with open(FILE_NAME, "w",encoding="utf-8") as f:
#         json.dump([], f)

# # Φόρτωση των συνταγών
# def load_recipes():
#     with open(FILE_NAME, "r",encoding="utf-8") as f:
#         return json.load(f)

# # Αποθήκευση των συνταγών
# def save_recipes(recipes):
#     with open(FILE_NAME, "w",encoding="utf-8") as f:
#         json.dump(recipes, f, indent=4, ensure_ascii=False)

# Προβολή όλων των συνταγών
def view_recipes():
    recipes = load_recipes("recipes.json")
    for i, recipe in enumerate(recipes, start=1):
        print(f"{i}. {recipe['title']} ({recipe['time']})")


# Αναζήτηση συνταγής
def search_recipe():
    keyword = input("Δώσε λέξη-κλειδί για τίτλο: ").lower()
    recipes = load_recipes("recipes.json")
    found = [r for r in recipes if keyword in r["name"].lower()]
    if found:
        for recipe in found:
            print(f"\n {recipe['name']} ({recipe['total_time']})")
            print("Υλικά:")
            for ing in recipe["ingredients"]:
                print(f" - {ing}")
            print("Βήματα:")
            for i, step in enumerate(recipe["steps"], 1):
                print(f"{i}. {step}")
    else:
        print(" Δεν βρέθηκε συνταγή.")

# Μενού
def main():
    while True:
        print("\n   Διαχείριση Συνταγών")
        print("1. Δες όλες τις συνταγές")

        print("2. Αναζήτηση συνταγής")
        print("3. Έξοδος")

        choice = input("Επιλογή: ")
        if choice == "1":
            view_recipes()


        elif choice == "2":
            search_recipe()
        elif choice == "3":
            break
        else:
            print("  Άκυρη επιλογή.")

if __name__ == "__main__":
    main()

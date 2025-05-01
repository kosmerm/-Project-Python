import json
import os

FILE_NAME = "recipes.json"

# Αν το αρχείο δεν υπάρχει, δημιουργείται ένα κενό
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump([], f)

# Φόρτωση των συνταγών
def load_recipes():
    with open(FILE_NAME, "r") as f:
        return json.load(f)

# Αποθήκευση των συνταγών
def save_recipes(recipes):
    with open(FILE_NAME, "w") as f:
        json.dump(recipes, f, indent=4, ensure_ascii=False)

# Προβολή όλων των συνταγών
def view_recipes():
    recipes = load_recipes()
    for i, recipe in enumerate(recipes, start=1):
        print(f"{i}. {recipe['title']} ({recipe['time']})")

# Προσθήκη νέας συνταγής
def add_recipe():
    title = input("Τίτλος συνταγής: ")
    time = input("Χρόνος προετοιμασίας: ")
    ingredients = input("Υλικά (χώρισε τα με κόμμα): ").split(",")
    steps = input("Βήματα (χώρισε τα με '|'): ").split("|")

    new_recipe = {
        "title": title,
        "time": time,
        "ingredients": [i.strip() for i in ingredients],
        "steps": [s.strip() for s in steps]
    }

    recipes = load_recipes()
    recipes.append(new_recipe)
    save_recipes(recipes)
    print("✅ Η συνταγή προστέθηκε!")

# Αναζήτηση συνταγής
def search_recipe():
    keyword = input("Δώσε λέξη-κλειδί για τίτλο: ").lower()
    recipes = load_recipes()
    found = [r for r in recipes if keyword in r["title"].lower()]
    if found:
        for recipe in found:
            print(f"\n {recipe['title']} ({recipe['time']})")
            print("Υλικά:")
            for ing in recipe["ingredients"]:
                print(f" - {ing}")
            print("Βήματα:")
            for i, step in enumerate(recipe["steps"], 1):
                print(f"{i}. {step}")
    else:
        print("❌ Δεν βρέθηκε συνταγή.")

# Μενού
def main():
    while True:
        print("\n🍽️  Διαχείριση Συνταγών")
        print("1. Δες όλες τις συνταγές")
        print("2. Πρόσθεσε νέα συνταγή")
        print("3. Αναζήτηση συνταγής")
        print("4. Έξοδος")

        choice = input("Επιλογή: ")
        if choice == "1":
            view_recipes()
        elif choice == "2":
            add_recipe()
        elif choice == "3":
            search_recipe()
        elif choice == "4":
            break
        else:
            print("❗ Άκυρη επιλογή.")

if __name__ == "__main__":
    main()

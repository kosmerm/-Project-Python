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

# Αναζήτηση συνταγής
def search_recipe():
    print("\nΑναζήτηση συνταγής:")
    print("1. Με βάση τον τίτλο")
    print("2. Με βάση το μέγιστο χρόνο παρασκευής")
    print("3. Με βάση υλικό")
    choice = input("Επιλογή: ")

    recipes = load_recipes()
    found = []

    if choice == "1":
        keyword = input("Δώσε λέξη-κλειδί για τίτλο: ").lower()
        found = [r for r in recipes if keyword in r["title"].lower()]

    elif choice == "2":
        try:
            max_time = int(input("Δώσε μέγιστο χρόνο (σε λεπτά): "))
            def extract_time(recipe):
                try:
                    return int(recipe["time"].split()[0])
                except:
                    return 9999
            found = [r for r in recipes if extract_time(r) <= max_time]
        except ValueError:
            print("Μη έγκυρη είσοδος.")

    elif choice == "3":
        keyword = input("Δώσε υλικό: ").lower()
        found = [r for r in recipes if any(keyword in ing.lower() for ing in r["ingredients"])]

    else:
        print("Άκυρη επιλογή.")
        return

    if found:
        for recipe in found:
            print(f"\n{recipe['title']} ({recipe['time']})")
            print("Υλικά:")
            for ing in recipe["ingredients"]:
                print(f" - {ing}")
            print("Βήματα:")
            for i, step in enumerate(recipe["steps"], 1):
                print(f"{i}. {step}")
    else:
        print("Δεν βρέθηκαν συνταγές.")

# Μενού
def main():
    while True:
        print("\n   Διαχείριση Συνταγών")
        print("1. Δες όλες τις συνταγές")
        print("2. Αναζήτηση συνταγής (τίτλος, χρόνος ή υλικό)")
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

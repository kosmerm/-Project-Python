from json_manager import load_recipes

# Φόρτωση των συνταγών από το JSON αρχείο

data = load_recipes("recipes.json")

# Συνάρτηση για εμφάνιση υλικών
def display_ingredients(ingredients):
    print("\nΥλικά:")
    for item in ingredients:
        qty = item["quantity"]
        name = item["name"]
        if qty is not None:
            print(f"- {name} ({qty} γρ.)")
        else:
            print(f"- {name}")

# Συνάρτηση για εμφάνιση βημάτων
def display_steps(steps):
    print("\nΒήματα εκτέλεσης:")
    for i, step in enumerate(steps, 1):
        print(f"{i}. {step}")

# Συνάρτηση για εμφάνιση όλων των διαθέσιμων συνταγών
def list_recipes():
    print("\nΔιαθέσιμες συνταγές:")
    for i, recipe in enumerate(data["recipes"], 1):
        print(f"{i}. {recipe['name']}")

# Συνάρτηση κύριας ροής του προγράμματος
while True:
    list_recipes()
    choice = input("\nΔιάλεξε αριθμό συνταγής ή 'q' για έξοδο: ")
    if choice.lower() == 'q':
        print("Έξοδος από το πρόγραμμα. Καλή όρεξη!")
        break
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(data["recipes"]):
        print("Μη έγκυρη επιλογή. Προσπάθησε ξανά.")
        continue
    recipe = data["recipes"][int(choice) - 1]
    print(f"\nΣυνταγή: {recipe['name']}")
    display_ingredients(recipe['ingredients'])
    display_steps(recipe['steps'])
    input("\nΠάτησε Enter για να επιστρέψεις στο μενού...")

import json
# 1. Καταχώρηση συνταγής
def create_recipe():
    # Το όνομα της συνταγής
    name = input("Καταχωρίστε το όνομα της συνταγής (π.χ. μακαρόνια με κιμά): ")
    # Η κατηγορία της συνταγής
    category = input("Καταχωρίστε την κατηγορία της συνταγής (δημητριακά, φρούτα, λαχανικά, γαλακτοκομικά, κρέας & προϊόντα, όσπρια, λίπη & έλαια, τρόφιμα με πολύ λίπος ή ζάχαρη): ")
    while category != "δημητριακά" and category != "φρούτα" and category != "λαχανικά" and category != "γαλακτοκομικά" and category != "κρέας & προϊόντα" and category != "όσπρια" and category != "λίπη & έλαια" and category != "τρόφιμα με πολύ λίπος ή ζάχαρη":
        category = input("Καταχωρίστε την κατηγορία της συνταγής (δημητριακά, φρούτα, λαχανικά, γαλακτοκομικά, κρέας & προϊόντα, όσπρια, λίπη & έλαια, τρόφιμα με πολύ λίπος ή ζάχαρη): ")
    # Ο βαθμός δυσκολίας της συνταγής
    difficulty = input("Καταχωρίστε τον βαθμό δυσκολίας (εύκολη, μεσαία, δύσκολη): ")
    while difficulty != "εύκολη" and difficulty != "μεσαία" and difficulty != "δύσκολη":
        difficulty = input("Καταχωρίστε τον βαθμό δυσκολίας (εύκολη, μεσαία, δύσκολη): ")
    # Ο συνολικός χρόνος εκτέλεσης της συνταγής
    while True:
        total_time = input("Καταχωρίστε τον συνολικό χρόνο εκτέλεσης σε λεπτά (π.χ. 65): ")
        if total_time == "":
            total_time = None
            break
        else:
            try:
                total_time = float(total_time)
                break
            except:
                print("Κάτι πήγε στραβά.")
    # Τα υλικά της συνταγής
    ingredients = []
    while True:
        number_of_ingredients = input("Καταχωρίστε το πλήθος των υλικών: ")
        if number_of_ingredients == "":
            number_of_ingredients = 0
            break
        else:
            try:
                number_of_ingredients = int(number_of_ingredients)
                break
            except:
                print("Κάτι πήγε στραβά.")
    for i in range(0, number_of_ingredients):
        name_of_ingredient = input(f"Καταχωρίστε το όνομα του {i + 1}ου υλικού (π.χ. σπαγγέτι): ")
        while True:
            quantity = input(f"Καταχωρίστε την ποσότητα του {i + 1}ου υλικού σε γραμμάρια (π.χ. 500): ")
            if quantity == "":
                quantity = 0
                break
            else:
                try:
                    quantity = int(quantity)
                    break
                except:
                    print("Κάτι πήγε στραβά.")
        ingredient = {
            "name": name_of_ingredient,
            "quantity": quantity
        }
        ingredients.append(ingredient)
    # Τα βήματα εκτέλεσης της συνταγής
    steps = []
    while True:
        number_of_steps = int(input("Καταχωρίστε το πλήθος των βημάτων: "))
        if number_of_steps == "":
            number_of_steps = 0
            break
        else:
            try:
                number_of_steps = int(number_of_steps)
                break
            except:
                print("Κάτι πήγε στραβά.")
    for i in range(0, number_of_steps):
        description = input(f"Καταχωρίστε την περιγραφή του {i + 1}ου βήματος: ")
        steps.append(description)
    # Οι μερίδες της συνταγής
    while True:
        portions = input("Καταχωρίστε τις μερίδες της συνταγής (π.χ. 6): ")
        if portions == "":
            portions = 0
            break
        else:
            try:
                portions = int(portions)
                break
            except:
                print("Κάτι πήγε στραβά.")
    recipe = {
        "name": name,
        "category": category,
        "difficulty": difficulty,
        "total_time": total_time,
        "ingredients": ingredients,
        "steps": steps,
        "portions": portions
    }
    with open("recipes.json", "r", encoding = "UTF-8") as file:
        data = json.load(file)
    data["recipes"].append(recipe)
    with open("recipes.json", "w", encoding = "UTF-8") as file:
        json.dump(data, file, ensure_ascii = False, indent = 2)
# 2. Αναζήτηση συνταγής
def search_recipe():
    pass
# 3. Τροποποίηση της συνταγής
def update_recipe():
    pass
# 4. Διαγραφή της συνταγής
def delete_recipe():
    pass
# 5. Εκτέλεση συνταγής
def execute_recipe():
    pass
# Κυρίως πρόγραμμα
def main():
    pass
if __name__ == "__main__":
    main()

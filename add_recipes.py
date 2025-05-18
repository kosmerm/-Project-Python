# Το όνομα της συνταγής
def create_name():
    name = input("Καταχωρίστε το όνομα της συνταγής (π.χ. μακαρόνια με κιμά): ")
    return name
# Η κατηγορία της συνταγής
def create_category():
    category = input("Καταχωρίστε την κατηγορία της συνταγής (δημητριακά, φρούτα, λαχανικά, γαλακτοκομικά, κρέας & προϊόντα, όσπρια, λίπη & έλαια, τρόφιμα με πολύ λίπος ή ζάχαρη): ")
    while category != "δημητριακά" and category != "φρούτα" and category != "λαχανικά" and category != "γαλακτοκομικά" and category != "κρέας & προϊόντα" and category != "όσπρια" and category != "λίπη & έλαια" and category != "τρόφιμα με πολύ λίπος ή ζάχαρη":
        category = input("Καταχωρίστε την κατηγορία της συνταγής (δημητριακά, φρούτα, λαχανικά, γαλακτοκομικά, κρέας & προϊόντα, όσπρια, λίπη & έλαια, τρόφιμα με πολύ λίπος ή ζάχαρη): ")
    return category
# Ο βαθμός δυσκολίας της συνταγής
def create_difficulty():
    difficulty = input("Καταχωρίστε τον βαθμό δυσκολίας (εύκολη, μεσαία, δύσκολη): ")
    while difficulty != "εύκολη" and difficulty != "μεσαία" and difficulty != "δύσκολη":
        difficulty = input("Καταχωρίστε τον βαθμό δυσκολίας (εύκολη, μεσαία, δύσκολη): ")
    return difficulty
# Ο συνολικός χρόνος εκτέλεσης της συνταγής
def create_total_time():
    while True:
        total_time = input("Καταχωρίστε τον συνολικό χρόνο εκτέλεσης σε λεπτά (π.χ. 65): ")
        if total_time == "":
            total_time = None
            return total_time
        else:
            try:
                total_time = float(total_time)
                return total_time
            except:
                print("Κάτι πήγε στραβά.")
# Τα υλικά της συνταγής
def create_ingredients():
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
    return ingredients
# Τα βήματα εκτέλεσης της συνταγής
def create_steps():
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
    return steps
# Οι μερίδες της συνταγής
def create_portions():
    while True:
        portions = input("Καταχωρίστε τις μερίδες της συνταγής (π.χ. 6): ")
        if portions == "":
            portions = 0
            return portions
        else:
            try:
                portions = int(portions)
                return portions
            except:
                print("Κάτι πήγε στραβά.")
# 1. Καταχώρηση συνταγής
def create_recipe():
    # Το όνομα της συνταγής
    name = create_name()
    # Η κατηγορία της συνταγής
    category = create_category()
    # Ο βαθμός δυσκολίας της συνταγής
    difficulty = create_difficulty()
    # Ο συνολικός χρόνος εκτέλεσης της συνταγής
    total_time = create_total_time()
    # Τα υλικά της συνταγής
    ingredients = create_ingredients()
    # Τα βήματα εκτέλεσης της συνταγής
    steps = create_steps()
    # Οι μερίδες της συνταγής
    portions = create_portions()
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

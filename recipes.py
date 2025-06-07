from json_manager import *
import os, time, platform

#================================================= Στέλιος Φράγκου =====================================================

# Το όνομα της συνταγής
def create_name():
    name = input("Καταχωρίστε το όνομα της συνταγής (π.χ. μακαρόνια με κιμά): ")
    return name

# Η κατηγορία της συνταγής
def create_category():
    categories = ["δημητριακά", "φρούτα", "λαχανικά", "γαλακτοκομικά", "κρέας & προϊόντα", "όσπρια", "λίπη & έλαια", "τρόφιμα με πολύ λίπος ή ζάχαρη"]
    for i, category in enumerate(categories):
        print(f"{i + 1}. {category}")
    while True:
        try:
            choice = int(input(f"Καταχωρίστε την κατηγορία της συνταγής (1-8): "))
            if choice < 1 or choice > 8:
                continue
            else:
                return categories[choice - 1]
        except:
            print("Κάτι πήγε στραβά.")

# Ο βαθμός δυσκολίας της συνταγής
def create_difficulty():
    difficulties = ["εύκολη", "μεσαία", "δύσκολη"]
    for i, difficulty in enumerate(difficulties):
        print(f"{i + 1}. {difficulty}")
    while True:
        try:
            choice = int(input("Καταχωρίστε τον βαθμό δυσκολίας (1-3): "))
            if choice < 1 or choice > 3:
                continue
            else:
                return difficulties[choice - 1]
        except:
            print("Κάτι πήγε στραβά.")

# Ο συνολικός χρόνος εκτέλεσης της συνταγής
def create_total_time():
    while True:
        total_time = input("Καταχωρίστε τον συνολικό χρόνο εκτέλεσης σε λεπτά (π.χ. 65): ")
        if total_time == "":
            total_time = None
            return total_time
        else:
            try:
                total_time = int(total_time)
                return total_time
            except:
                print("Κάτι πήγε στραβά.")

# Τα υλικά της συνταγής
def create_ingredients():
    products = load_products("products.json")
    ingredients = []
    while True:
        try:
            number_of_ingredients = int(input("Καταχωρίστε το πλήθος των υλικών: "))
            break
        except:
            print("Κάτι πήγε στραβά.")
    for i in range(0, number_of_ingredients):
        name_of_ingredient = input(f"Καταχωρίστε το όνομα του {i + 1}ου υλικού (π.χ. σπαγγέτι): ")
        add_product_if_not_exists(products, name_of_ingredient, "products.json")
        try:
            quantity = int(input(f"Καταχωρίστε την ποσότητα του {i + 1}ου υλικού σε γραμμάρια (π.χ. 500): "))
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
        try:
            number_of_steps = int(input("Καταχωρίστε το πλήθος των βημάτων: "))
            break
        except:
            print("Κάτι πήγε στραβά.")
    for i in range(0, number_of_steps):
        while True:
            description = input(f"Καταχωρίστε την περιγραφή του {i + 1}ου βήματος: ")
            if description != "":
                break
        steps.append(description)
    return steps

# Οι μερίδες της συνταγής
def create_portions():
    while True:
        try:
            portions = int(input("Καταχωρίστε τις μερίδες της συνταγής (π.χ. 6): "))
            break
        except:
            print("Κάτι πήγε στραβά.")
    return portions

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
        "portions": portions,
        "cost": None
    }
    data_recipes = load_recipes("recipes.json")
    data_recipes["recipes"].append(recipe)
    save_recipes(data_recipes, "recipes.json")

def product_manager():
    data = load_products("products.json")
    while True:
        print("\n--- Διαχείριση προϊόντων ---")
        print("1. Καταχώριση προϊόντος")
        print("2. Εμφάνιση προϊόντων")
        print("3. Τροποποίηση προϊόντος")
        print("4. Διαγραφή προϊόντος")
        print("5. Έξοδος")
        try:
            choice = int(input("Επιλέξτε μια επιλογή (1-5): "))
        except:
            print("Μη έγκυρη επιλογή. Παρακαλώ επιλέξτε ξανά.\n")
            continue
        if choice == 1:
            name = input("Καταχωρίστε το όνομα του προϊόντος: ")
            while True:
                try:
                    price_per_kg = float(input("Καταχωρίστε την τιμή του προϊόντος ανά κιλό: "))
                    break
                except:
                    print("Η τιμή πρέπει να περιέχει μόνο αριθμούς. Δοκιμάστε ξανά.")
            data["products"].append({"name": name, "price_per_kg": price_per_kg})
            save_products(data, "products.json")
            print("Το προϊόν καταχωρήθηκε με επιτυχία!\n")
        elif choice == 2:
            print("Προϊόντα:")
            for i, product in enumerate(data["products"], start = 1):
                print(f"{i}. {product['name']} - {product['price_per_kg']} €/κιλό")
            print()
        elif choice == 3:
            while True:
                print("1. Τροποποίηση ονόματος")
                print("2. Τροποποίηση τιμής")
                print("3. Έξοδος")
                try:
                    choice = int(input("Επιλέξτε μια επιλογή (1-3): "))
                except:
                    print("Μη έγκυρη επιλογή. Παρακαλώ επιλέξτε ξανά.")
                    continue
                if choice == 1:
                    for i, product in enumerate(data["products"], start = 1):
                        print(f"{i}. {product['name']}")
                    while True:
                        try:
                            choice = int(input(f"Επιλέξτε ένα προϊόν (1-{len(data['products'])}): "))
                        except:
                            print("Μη έγκυρη επιλογή. Παρακαλώ επιλέξτε ξανά.")
                            continue
                        if choice < 1 or choice > len(data["products"]):
                           print("Μη έγκυρη επιλογή. Παρακαλώ επιλέξτε ξανά.")
                           continue
                        break
                    name = input("Καταχωρίστε το όνομα του προϊόντος: ")
                    data["products"][choice - 1]["name"] = name
                    save_products(data, "products.json")
                    print("Το προϊόν τροποποιήθηκε με επιτυχία!\n")
                elif choice == 2:
                    for i, product in enumerate(data["products"], start = 1):
                        print(f"{i}. {product['name']}")
                    while True:
                        try:
                            choice = int(input(f"Επιλέξτε ένα προϊόν (1-{len(data['products'])}): "))
                        except:
                            print("Μη έγκυρη επιλογή. Παρακαλώ επιλέξτε ξανά.")
                            continue
                        if choice < 1 or choice > len(data["products"]):
                           print("Μη έγκυρη επιλογή. Παρακαλώ επιλέξτε ξανά.")
                           continue
                        break
                    while True:
                        try:
                            price_per_kg = float(input("Καταχωρίστε την τιμή του προϊόντος: "))
                            break
                        except:
                            print("Η τιμή πρέπει να περιέχει μόνο αριθμούς. Δοκιμάστε ξανά.")
                    data["products"][choice - 1]["price_per_kg"] = price_per_kg
                    save_products(data, "products.json")
                    print("Το προϊόν τροποποιήθηκε με επιτυχία!\n")
                elif choice == 3:
                    print("Η τροποποίηση ολοκληρώθηκε.\n")
                    break
                else:
                    print("Μη έγκυρη επιλογή. Παρακαλώ επιλέξτε ξανά.")
        elif choice == 4:
            for i, product in enumerate(data["products"], start = 1):
                print(f"{i}. {product['name']}")
            while True:
                try:
                    choice = int(input(f"Επιλέξτε μια επιλογή (1-{len(data['products'])}): "))
                except:
                    print("Μη έγκυρη επιλογή. Παρακαλώ επιλέξτε ξανά.")
                    continue
                if choice < 1 or choice > len(data["products"]):
                    print("Μη έγκυρη επιλογή. Παρακαλώ επιλέξτε ξανά.")
                    continue
                break
            data["products"].pop(choice - 1)
            save_products(data, "products.json")
            print("Το προϊόν διαγράφηκε με επιτυχία!\n")
        elif choice == 5:
            print("Έξοδος από τη διαχείριση προϊόντων.\n")
            break
        else:
            print("Μη έγκυρη επιλογή. Παρακαλώ επιλέξτε ξανά.\n")

#==========================================  Ιωάννης Κανί  ==============================================

def unique_categories(recipes):
    data = load_recipes("recipes.json")
    return sorted(set(r['category'] for r in data["recipes"]))

def unique_difficulties(recipes):
    data = load_recipes("recipes.json")
    return sorted(set(r['difficulty'] for r in data["recipes"]))

def filter_recipes_by_category(recipes, category):
    return [r for r in recipes if r['category'] == category]

def filter_recipes_by_difficulty(recipes, difficulty):
    return [r for r in recipes if r['difficulty'] == difficulty]

def filter_recipes_by_time(recipes, max_time):
    return [r for r in recipes if r['total_time'] <= max_time]

def filter_recipes_by_ingredients(recipes, ingredients_list):
    """
    Φιλτράρει τις συνταγές που περιέχουν όλα τα υλικά στη λίστα ingredients_list.
    """
    filtered = []
    for r in recipes:
        recipe_ingredients = [ing['name'].lower() for ing in r['ingredients']]
        if all(ing.lower() in recipe_ingredients for ing in ingredients_list):
            filtered.append(r)
    return filtered

def show_ingredients(ingredients):
    print("\nΥλικά:")
    for ing in ingredients:
        print(f"- {ing['quantity']} {ing['name']}")

def show_steps(steps):
    print("\nΒήματα:")
    for i, step in enumerate(steps, 1):
        print(f"{i}. {step}")

def search_menu():
    data = load_recipes("recipes.json")
    while True:
        print("\n--- Αναζήτηση συνταγής ---")
        print("Φίλτρα επιλογής:")
        print("1. Όλες οι συνταγές")
        print("2. Φιλτράρισμα ανά κατηγορία")
        print("3. Φιλτράρισμα ανά δυσκολία")
        print("4. Φιλτράρισμα ανά χρόνο προετοιμασίας")
        print("5. Φιλτράρισμα ανά υλικά")
        print("6. Έξοδος")

        choice = input("Επίλεξε επιλογή: ").strip().lower()

        if choice == '6':
            print("Έξοδος από την αναζήτηση συνταγής.\n")
            break

        filtered_recipes = data["recipes"]

        if choice == '1':
            pass

        elif choice == '2':
            categories = unique_categories(data)
            print("\nΔιαθέσιμες κατηγορίες:")
            for i, cat in enumerate(categories, 1):
                print(f"{i}. {cat}")
            cat_choice = input("Επίλεξε κατηγορία ή 'q' για ακύρωση: ")
            if cat_choice == 'q':
                continue
            if not cat_choice.isdigit() or int(cat_choice) < 1 or int(cat_choice) > len(categories):
                print("Μη έγκυρη επιλογή κατηγορίας.")
                continue
            selected_category = categories[int(cat_choice) - 1]
            filtered_recipes = filter_recipes_by_category(data["recipes"], selected_category)

        elif choice == '3':
            difficulties = unique_difficulties(data["recipes"])
            print("\nΔιαθέσιμες δυσκολίες:")
            for i, diff in enumerate(difficulties, 1):
                print(f"{i}. {diff}")
            diff_choice = input("Επίλεξε δυσκολία ή 'q' για ακύρωση: ")
            if diff_choice == 'q':
                continue
            if not diff_choice.isdigit() or int(diff_choice) < 1 or int(diff_choice) > len(difficulties):
                print("Μη έγκυρη επιλογή δυσκολίας.")
                continue
            selected_difficulty = difficulties[int(diff_choice) - 1]
            filtered_recipes = filter_recipes_by_difficulty(data["recipes"], selected_difficulty)

        elif choice == '4':
            print("\nΦίλτρα χρόνου (λεπτά):")
            print("1. Μέχρι 15 λεπτά")
            print("2. Μέχρι 30 λεπτά")
            print("3. Μέχρι 60 λεπτά")
            print("4. Πάνω από 60 λεπτά")
            time_choice = input("Επίλεξε επιλογή ή 'q' για ακύρωση: ")
            if time_choice == 'q':
                continue
            if time_choice == '1':
                filtered_recipes = filter_recipes_by_time(data["recipes"], 15)
            elif time_choice == '2':
                filtered_recipes = filter_recipes_by_time(data["recipes"], 30)
            elif time_choice == '3':
                filtered_recipes = filter_recipes_by_time(data["recipes"], 60)
            elif time_choice == '4':
                filtered_recipes = [r for r in data["recipes"] if r["total_time"] > 60]
            else:
                print("Μη έγκυρη επιλογή χρόνου.")
                continue

        elif choice == '5':
            ing_input = input("Δώσε τα υλικά που έχεις (χωρισμένα με κόμμα): ")
            ingredients_list = [ing.strip() for ing in ing_input.split(",") if ing.strip()]
            if not ingredients_list:
                print("Δεν δόθηκαν υλικά για φιλτράρισμα.")
                continue
            filtered_recipes = filter_recipes_by_ingredients(data["recipes"], ingredients_list)

        else:
            print("Μη έγκυρη επιλογή. Προσπάθησε ξανά.")
            continue

        if not filtered_recipes:
            print("Δεν βρέθηκαν συνταγές με αυτά τα κριτήρια.")
            continue

        print("\nΔιαθέσιμες συνταγές:")
        for i, recipe in enumerate(filtered_recipes, start = 1):
            print(f"{i}. {recipe['name']} (Συνολικός χρόνος εκτέλεσης: {recipe['total_time']}')")
        rec_choice = input("Επίλεξε τον αριθμό της συνταγής ή 'q' για επιστροφή: ")
        if rec_choice == 'q':
            continue
        if not rec_choice.isdigit() or int(rec_choice) < 1 or int(rec_choice) > len(filtered_recipes):
            print("Μη έγκυρη επιλογή συνταγής.")
            continue

        selected = filtered_recipes[int(rec_choice) - 1]
        print(f"\n--- {selected['name']} ---")
        show_ingredients(selected['ingredients'])
        show_steps(selected['steps'])

        proceed = input("\nΘες να δεις άλλη συνταγή; (ναι/όχι): ")
        if proceed.strip().lower() not in ['ναι', 'ν', 'yes', 'y']:
            print("Έξοδος από την αναζήτηση συνταγής.\n")
            break

#=====================================  Κωνσταντίνος Μέρμηγκας   =======================================

#Γενική Συνάρτηση για τροποποίηση συνταγών =============================================================
def edit_recipes():
    # Φόρτωση συνταγών
    data_recipes = load_recipes("recipes.json")

    #Έλεγχος εάν η data_recipes είναι κενή
    if not data_recipes["recipes"]:
        print("Δεν υπάρχουν διαθέσιμες συνταγές.")
        return
    
    # Εμφάνιση συνταγών
    while True:
        print("\n--- Τροποποίηση συνταγής ---")
        print("Διαθέσιμες συνταγές:")

        #Εμφάνιση όνομα συνταγών με έναν αριθμό μπροστά για έυκολη επιλογή από τον χρήστη
        for i, recipe in enumerate(data_recipes["recipes"]):
            print(f"{i + 1}. {recipe['name']}")
        
        try:
            recipe_number = int(input("Δώστε τον αριθμό της συνταγής που θέλετε να τροποποιήσετε ή πατήστε 0 για έξοδο: "))
            if recipe_number == 0:
                return
            elif recipe_number < 1 or recipe_number > len(data_recipes["recipes"]):
                print("Λάθος αριθμός, εισάγετε έναν αριθμό από τις διαθέσιμες συνταγές")
            else:
                break
        except ValueError:
            print("Παρακαλώ εισάγετε έναν ακέραιο αριθμό!")
        
    #εισαγωγή της συνταγής που επιλέξαμε σε μεταβλητή που θα μπει παράμετρος στις υπόλοιπες συναρτήσεις τροποποίησης
    recipe = data_recipes["recipes"][recipe_number - 1]

    #Επανάληψη για το menu τροποποίησης
    while True:
        print("1. Τροποποίηση Ονόματος")
        print("2. Τροποποίηση Κατηγορίας")
        print("3. Τροποποίηση Δυσκολίας")
        print("4. Τροποποίηση Χρόνου Υλοποίησης")
        print("5. Τροποποίηση Υλικών")
        print("6. Τροποποίηση Βημάτων")
        print("7. Τροποποίηση Μερίδων")
        print("0. Έξοδος")
        
        option = int(input("Επιλέξτε 1 έως 7 για να συνεχίσετε ή 0 για έξοδο: "))
        #Επιλογές τροποποίησης
        if option == 1:
            edit_name(recipe)
        elif option == 2:
            edit_category(recipe)
        elif option == 3:
            edit_difficulty(recipe)  
        elif option == 4:
            edit_total_time(recipe)
        elif option == 5:
            edit_ingredients(recipe)
        elif option == 6:
            edit_steps(recipe)
        elif option == 7:
            edit_portions(recipe)
        elif option == 0:
            print()
            break  # Τερματίζει το loop 
        else:
            print("Μη έγκυρη επιλογή. Προσπαθήστε ξανά") 

        save_recipes(data_recipes, "recipes.json")
  
        
#Συνάρτηση τροποποίησης ονόματος =====================================================================
def edit_name(recipe):
    #Έλεγχος μήπως είναι κενή η μεταβλητή
    if recipe["name"]:
        print(f"Το όνομα της συνταγής είναι {recipe["name"]}")
        #Επανάληψη ώστε να δίνει την δυνατότηα στον χρήστη να επιλέξει ξανά και για ασφάλεια
        while True:
            option=input("Είστε σίγουροι ότι θέλετε να αλλάξετε το όνομα της συνταγής? πατήστε 'y' αλλιώς 'n' για έξοδο:")
            if option=="y":
                new_name = input("Δώστε το νέο όνομα της συνταγής: ").strip()
                if new_name:
                    recipe["name"] = new_name
                    print("Το όνομα ενημερώθηκε!")
                    return
                else:
                    print("Το όνομα δεν μπορεί να είναι κενό! Η αλλαγή ακυρώθηκε.")
            elif option=="n":
                return
            else:
                print("Μη έγκυρη επιλογή. Προσπαθήστε ξανά")
    else:
        print("Δεν βρέθηκε το όνομα της συνταγής.Παρακαλώ εκχωρήστε το από την αρχή")    
        create_name()
                   
#Συνάρτηση τροποποίησης κατηγορίας συνταγής ================================================================================================================================================================================================================================
def edit_category(recipe):
    #Έλεγχος μήπως έχει μείνει κενή η μεταβλητή
    if recipe["category"]:
        print(f"Η συνταγή ανήκει στην κατηγορία {recipe["category"]}")
        while True:
            option=input("Είστε σίγουροι ότι θέλετε να αλλάξετε την κατηγορία της συνταγής? πατήστε 'y' αλλιώς 'n' για έξοδο:")
            if option=="y":
                categories = ["δημητριακά", "φρούτα", "λαχανικά", "γαλακτοκομικά", "κρέας & προϊόντα", "όσπρια", "λίπη & έλαια", "τρόφιμα με πολύ λίπος ή ζάχαρη"]
                for i, category in enumerate(categories):
                    print(f"{i + 1}. {category}")
                while True:
                    try:
                        choice = int(input(f"Καταχωρίστε την κατηγορία της συνταγής (1-8): "))
                        if choice < 1 or choice > 8:
                            continue
                        else:
                            recipe["category"] = categories[choice-1]
                            print("Η κατηγορία ενημερώθηκε!")
                            return
                    except:
                        print("Μη έγκυρη επιλογή. Προσπαθήστε ξανά")
                        
            elif option=="n":
                return
            else:
                print("Μη έγκυρη επιλογή. Προσπαθήστε ξανά")
    else:
        print("Δεν βρέθηκε η κατηγορία της συνταγής.Παρακαλώ εκχωρήστε την από την αρχή")    
        create_category() 


#Συνάρτηση τροποποίησης δυσκολίας συνταγής =============================================================
def edit_difficulty(recipe):
    #Έλεγχος μήπως έχει μείνει κενή η μεταβλητή
    if recipe["difficulty"]:
        print(f"Η συνταγή έχει δυσκολία {recipe["difficulty"]}")
        while True:
            option=input("Είστε σίγουροι ότι θέλετε να αλλάξετε τον βαθμό της δυσκολίας? πατήστε 'y' αλλιώς 'n' για έξοδο:")
            if option=="y":
                difficulties = ["εύκολη", "μεσαία", "δύσκολη"]
                for i, difficulty in enumerate(difficulties):
                    print(f"{i + 1}. {difficulty}")
                while True:
                    try:
                        difficulty = int(input("Καταχωρίστε τον βαθμό δυσκολίας (1-3): "))
                        if difficulty < 1 or difficulty > 3:
                            continue
                        else:
                            recipe["difficulty"] = difficulties[difficulty-1]
                            print("Η δυσκολία ενημερώθηκε!")
                            return 
                    except:
                        print("Μη έγκυρη επιλογή. Προσπαθήστε ξανά")
            elif option=="n":
                return
            else:
                print("Μη έγκυρη επιλογή. Προσπαθήστε ξανά")
    else:
        print("Δεν βρέθηκε η δυσκολία της συνταγής.Παρακαλώ εκχωρήστε την από την αρχή")  
        create_difficulty()  


#Συνάρτηση τροποποίησης χρόνου συνταγής ====================================================
def edit_total_time(recipe):
    #Έλεγχος μήπως έχει μείνει κενή η μεταβλητή
    if recipe["total_time"]:
        print(f"Η συνταγή έχει συνολική διάρκεια υλοποίησης {recipe["total_time"]}")
        while True:
            option=input("Είστε σίγουροι ότι θέλετε να αλλάξετε την συνολική διάρκεια υλοποίησης? πατήστε 'y' αλλιώς 'n' για έξοδο:")
            if option=="y":
                try:
                    total_time = float(input("Καταχωρήστε τον συνολικό χρόνο εκτέλεσης σε λεπτά (π.χ. 65): "))
                    if total_time:
                        recipe["total_time"]=total_time
                        print("Η συνολική διάρκεια ενημερώθηκε!")
                        return
                    else:
                        print("Η συνολική διάρκεια δεν μπορεί να είναι κενή! Η αλλαγή ακυρώθηκε.")
                except ValueError:
                    print("Λάθος καταχώρηση , παρακαλώ εισάγετε ακέραιο αριθμό")
            elif option=="n":
                return
            else:
                print("Μη έγκυρη επιλογή. Προσπαθήστε ξανά")
    else:
        print("Δεν βρέθηκε η διάρκεια υλοποίησης της συνταγής.Παρακαλώ εκχωρήστε την από την αρχή")  
        create_total_time()  


#Συνάρτηση τροποποίησης υλικών ==================================================================================
def edit_ingredients(recipe):
    if not recipe["ingredients"]:
        print("Δεν υπάρχουν υλικά για αυτήν την συνταγή.")
        print("Παρακαλώ εκχωρήστε τα από την αρχή")
        create_ingredients()

    while True:
        print("\nΕπιλογές:")
        print("1. Τροποποίηση υπάρχοντων υλικών")
        print("2. Προσθήκη νέου υλικού")
        print("0. Έξοδος")

        try:
            epilogh = int(input("Εισάγετε την επιλογή σας: "))
        except ValueError:
            print("Λάθος καταχώρηση , παρακαλώ εισάγετε ακέραιο αριθμό")
            continue

        if epilogh == 1:
            if not recipe["ingredients"]:
                print("Η λίστα των υλικών είναι κενή.")
                create_ingredients()
                continue

            while True:
                print("Υλικά συνταγής:")
                for i, ingredient in enumerate(recipe["ingredients"], start=1):
                    print(f"{i}. {ingredient['name']} ({ingredient['quantity']})")

                try:
                    ingredient_number = int(input("Δώστε τον αριθμό του υλικού που θέλετε να τροποποιήσετε: "))
                    if ingredient_number < 1 or ingredient_number > len(recipe["ingredients"]):
                        print("Λάθος αριθμός, εισάγετε έναν αριθμό από τα διαθέσιμα υλικά")
                        continue
                    break  # Επιτυχής επιλογή
                except ValueError:
                    print("Παρακαλώ εισάγετε έναν ακέραιο αριθμό!")

            ingredient = recipe["ingredients"][ingredient_number - 1]
            data_products = load_products("products.json")

            while True:
                print(f"\nΤροποποίηση {ingredient['name']}:")
                print("1. Τροποποίηση Ονόματος")
                print("2. Τροποποίηση Ποσότητας")
                print("0. Έξοδος")

                try:
                    option = int(input("Επιλέξτε 1 έως 2 για να συνεχίσετε ή 0 για έξοδο: "))
                except ValueError:
                    print("Παρακαλώ εισάγετε έναν έγκυρο ακέραιο αριθμό!")
                    continue

                if option == 1:
                    new_ingredient_name = input("Καταχωρήστε το όνομα του υλικού: ").strip()
                    if new_ingredient_name:
                        ingredient["name"] = new_ingredient_name
                        print("Το όνομα ενημερώθηκε!")
                        add_product_if_not_exists(data_products, new_ingredient_name, "products.json")
                    else:
                        print("Το όνομα δεν μπορεί να είναι κενό!")
                elif option == 2:
                    while True:
                        try:
                            new_ingredient_quantity = int(input("Καταχωρήστε την ποσότητα του υλικού: "))
                            if new_ingredient_quantity >= 0:
                                ingredient["quantity"] = new_ingredient_quantity
                                print("Η ποσότητα ενημερώθηκε!")
                                break
                            else:
                                print("Η ποσότητα δεν μπορεί να είναι αρνητική!")
                        except ValueError:
                            print("Παρακαλώ εισάγετε έναν ακέραιο αριθμό για την ποσότητα!")
                elif option == 0:
                    break
                else:
                    print("Μη έγκυρη επιλογή. Προσπαθήστε ξανά")

        elif epilogh == 2:
            create_ingredients()

        elif epilogh == 0:
            print("Έξοδος από την τροποποίηση των υλικών.")
            return

        else:
            print("Μη έγκυρη επιλογή. Προσπαθήστε ξανά")


#Συνάρτηση τροποποίησης βημάτων ==========================================================
def edit_steps(recipe):
    
    if not recipe["ingredients"]:
        print("Δεν υπάρχουν βήματα για αυτήν την συνταγή.")
        print("Παρακαλώ εκχωρήστε τα από την αρχή")
        create_steps()

    while True:
        print("\nΕπιλογές:")
        print("1. Τροποποίηση υπάρχοντος βήματος")
        print("2. Προσθήκη νέου βήματος")
        print("0. Έξοδος")
        option = input("Εισάγετε την επιλογή σας: ")

        if option == "1":
            print("Τρέχοντα Βήματα:")
            for i, step in enumerate(recipe["steps"], start=1):
                print(f"{i}. {step}")
            try:
                step_number=int(input("Εισάγετε τον αριθμό του βήματος που θέλετε να τροποποιήσετε ή 0 για έξοδο: "))
                if step_number==0:
                    print("Τα βήματα της συνταγής δεν βρέθηκαν , παρακαλώ επιλέξτε το 2 από το menu για να εισάγεται νέα βήματα")
                    return
                if step_number < 1 or step_number > len(recipe["steps"]):
                    print(f"Παρακαλώ εισάγετε αριθμό από 1 έως {len(recipe['steps'])}.")
                else:
                    new_step = input("Εισάγετε το νέο βήμα: ").strip()
                    if new_step:
                        recipe["steps"][step_number - 1] = new_step
                        print(f"Το βήμα {step_number} ενημερώθηκε με επιτυχία!")
                    else:
                        print("Δεν έγινε καμία αλλαγή γιατί δεν δόθηκε νέο βήμα.")
            except ValueError:
                print("Παρακαλώ εισάγετε έναν ακέραιο αριθμό.")
                    

        elif option == "2":
            new_step = input("Εισάγετε το νέο βήμα προς προσθήκη: ").strip()
            if new_step:
                recipe["steps"].append(new_step)
                print("Το νέο βήμα προστέθηκε επιτυχώς!")
            else:
                print("Δεν έγινε προσθήκη γιατί δεν δόθηκε κάποιο βήμα.")

        elif option == "0":
            print("Έξοδος από την τροποποίηση των βημάτων.")
            return
        
        else:
            print("Μη έγκυρη επιλογή. Προσπαθήστε ξανά")
   

#Συνάρτηση τροποποίησης μερίδων ==========================================================
def edit_portions(recipe):
    if recipe["portions"]:
        print(f"Η συνταγή είναι για {recipe["portions"]} μερίδες περίπου")
        while True:
            option=input("Εάν θέλετε να αλλάξετε τις μερίδες πατήστε 'y' αλλιώς 'n' για έξοδο:")
            if option=="y":
                try:
                    portions = int(input("Καταχωρήστε τις μερίδες (π.χ. 10): "))
                    if portions:
                        recipe["portions"]=portions
                        print("Η συνολική διάρκεια ενημερώθηκε!")
                        break
                    else:
                        print("Η συνολική διάρκεια δεν μπορεί να είναι κενή! Η αλλαγή ακυρώθηκε.")
                except ValueError:
                    print("Λάθος καταχώρηση , παρακαλώ εισάγετε ακέραιο αριθμό")
            elif option=="n":
                return
            else:
                print("Μη έγκυρη επιλογή. Προσπαθήστε ξανά")
    else:
        print("Δεν βρέθηκε η διάρκεια υλοποίησης της συνταγής.Παρακαλώ εκχωρήστε την από την αρχή")  
        create_portions()

#Συνάρτηση ΔΙΑΓΡΑΦΗΣ συνταγών  ===========================================================
def delete_recipe():
    data_recipes = load_recipes("recipes.json")
    
    if not data_recipes["recipes"]:
        print("Δεν υπάρχουν διαθέσιμες συνταγές.")
        return
    
    
    while True:
        print("\n--- Διαγραφή συνταγής ---")
        print("Διαθέσιμες συνταγές:")
        # Εμφάνιση συνταγών
        for i, recipe in enumerate(data_recipes["recipes"]):
            print(f"{i + 1}. {recipe['name']}")
        
        try:
            recipe_number = int(input(f"Δώστε τον αριθμό της συνταγής που θέλετε να διαγράψετε(1 - {len(data_recipes['recipes'])}) ή 0 για έξοδο: "))
            if recipe_number == 0:
                print("Ακύρωση διαγραφής.")
                return
            elif recipe_number < 1 or recipe_number > len(data_recipes["recipes"]):
                print("Λάθος αριθμός, εισάγετε έναν αριθμό από τις διαθέσιμες συνταγές")
            else:
                selected_recipe = data_recipes["recipes"][recipe_number - 1]
                confirmation=input(f"Είστε σίγουρoς/η ότι θέλετε να διαγράψετε τη συνταγή {selected_recipe['name']};(y/n): ")
                if confirmation=='n':
                    print("Η διαγραφή ακυρώθηκε.")
                    return
                
                deleted_recipe = data_recipes["recipes"].pop(recipe_number - 1)
                print(f"Η συνταγή '{deleted_recipe['name']}' διαγράφηκε επιτυχώς!\n")

                save_recipes(data_recipes, "recipes.json")
                break
        except ValueError:
            print("Παρακαλώ εισάγετε έναν ακέραιο αριθμό!")

#===========================================  Αλέξανδρος Βασιλείου  ===========================================

# ======== Ήχος μετακίνησης (μόνο για Windows) ========
def play_sound():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(600, 200)

# ======== Υπολογισμός κόστους συνταγής ========
def calculate_cost(ingredients, prices):
    total = 0
    for ing in ingredients:
        name = ing["name"]
        qty = ing["quantity"]
        if qty and name in prices:
            total += (qty / 1000) * prices[name]
    return round(total, 2)

# ======== Εκτέλεση συνταγής με progress και ήχο ========
def execute_recipe():
    recipes = load_recipes("recipes.json")
    products = load_products("products.json")
    product_prices = {p["name"]: p["price_per_kg"] for p in products["products"]}

    print("\n--- Εκτέλεση συνταγής ---")
    print("🍽 Διαθέσιμες συνταγές:")
    for i, recipe in enumerate(recipes["recipes"], 1):
        print(f"{i}. {recipe['name']}")

    choice = input("\nΔιάλεξε αριθμό συνταγής ή 'q' για έξοδο: ")
    if choice.lower() == 'q':
        return

    if not choice.isdigit() or not (1 <= int(choice) <= len(recipes["recipes"])):
        print("❌ Μη έγκυρη επιλογή.")
        return

    selected = recipes["recipes"][int(choice) - 1]
    name = selected['name']
    steps = selected['steps']
    ingredients = selected['ingredients']

    print(f"\n👨‍🍳 Εκτελείς: {name}")
    print(f"Κατηγορία: {selected['category']} | Δυσκολία: {selected['difficulty']} | Χρόνος: {selected['total_time']} λεπτά")

    print("\n🧾 Υλικά:")
    for ing in ingredients:
        qty = ing["quantity"]
        if qty == None:
            print(f"• {ing['name']}")
        else:
            price = f"{(qty / 1000) * product_prices[ing['name']]:.2f}€" if qty and ing["name"] in product_prices else "-"
            display_qty = f" ({qty} γρ.)" if qty else ""
            print(f"• {ing['name']}{display_qty} - 💰 {price}")

    total_cost = calculate_cost(ingredients, product_prices)
    print(f"\n💶 Εκτιμώμενο κόστος: {total_cost} €")

    print("\n🔪 Εκτέλεση:\n")
    for idx, step in enumerate(steps, 1):
        percentage = int((idx / len(steps)) * 100)
        bar_length = 30
        filled = int(bar_length * percentage / 100)
        bar = "█" * filled + "-" * (bar_length - filled)
        print(f"Βήμα {idx}/{len(steps)}: {step}")
        print(f"Πρόοδος: |{bar}| {percentage}%")
        play_sound()
        input("👉 Πάτησε Enter για να συνεχίσεις...\n")

    print("\n✅ Η συνταγή ολοκληρώθηκε!")
    again = input("🔁 Θέλεις να επιστρέψεις στο μενού; (Y/N): ").strip().lower()
    if again == 'y':
        # from menu import main
        main()

#=================================================  Γεώργιος Χρήστου   ================================================================

# Υπολογισμός κόστους συνταγής και ενημέρωση στο αρχείο
def calculate_recipe_cost():
    data_recipes = load_recipes("recipes.json")
    total_cost = 0.0
    for i, recipe in enumerate(data_recipes["recipes"]):
        print(f"{i + 1}. {recipe['name']}")
    choice = int(input("Επίλεξε συνταγή για υπολογισμό κόστους: "))
    products_data = load_products("products.json")
    for ingredient in data_recipes["recipes"][choice - 1]["ingredients"]:
        name = ingredient['name']
        quantity = ingredient['quantity']
        for product in products_data["products"]:
            if product["name"] == name and quantity != None:
                total_cost += (quantity / 1000) * product["price_per_kg"]
                break
    cost = round(total_cost, 2)
    data_recipes['recipes'][choice - 1]["cost"] = cost # Ενημερώνει το λεξικό της συνταγής
    save_recipes(data_recipes, "recipes.json")
    print(f"Το συνολικό κόστος της συνταγής {data_recipes['recipes'][choice - 1]["name"]} είναι {data_recipes['recipes'][choice - 1]["cost"]}")

#Απλό menu για χρήση
def calculate_cost_menu():
    while True:
        print("\n--- Υπολογισμός κόστους συνταγής ---")
        print("1. Υπολογισμός κόστους συνταγής")
        print("2. Έξοδος")
        choice = input("Επιλογή: ").strip()
        if choice == '1':
            calculate_recipe_cost()
        elif choice == '2':
            print()
            break
        else:
            print("Μη έγκυρη επιλογή.")


#===================================== Εκκίνηση προγράμματος =============================================
def main():
    while True:
        print("--- Συνταγές Μαγειρικής ---")
        print("1. Καταχώρηση συνταγής")
        print("2. Αναζήτηση συνταγής")
        print("3. Τροποποίηση συνταγής")
        print("4. Διαγραφή συνταγής")
        print("5. Εκτέλεση συνταγής")
        print("6. Υπολογισμός κόστους συνταγής")
        print("7. Διαχείριση προϊόντων")
        print("8. Έξοδος")
        try:
            choice = int(input("Επιλέξτε μια επιλογή (1-8): "))
        except ValueError:
            print("Μη έγκυρη επιλογή. Παρακαλώ εισάγετε έναν αριθμό.\n")
            continue
        if choice == 1:
            create_recipe()
        elif choice == 2:
            search_menu()
        elif choice == 3:
            edit_recipes()
        elif choice == 4:
            delete_recipe()
        elif choice == 5:
            execute_recipe()
        elif choice == 6:
            calculate_cost_menu()
        elif choice == 7:
            product_manager()
        elif choice == 8:
            print("Έξοδος από το πρόγραμμα.")
            break
        else:
            print("Μη έγκυρη επιλογή. Παρακαλώ επιλέξτε ξανά.\n")

if __name__ == "__main__":
    main()

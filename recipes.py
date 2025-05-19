from json_manager import *

# Stelios Fragkou

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
                return choice
        except:
            print("Κάτι πήγε στραβά.")

# Ο βαθμός δυσκολίας της συνταγής
def create_difficulty():
    difficulties = ["εύκολη", "μεσαία", "δύσκολη"]
    for i, difficulty in enumerate(difficulties):
        print(f"{i + 1}. {difficulty}")
    while True:
        try:
            difficulty = int(input("Καταχωρίστε τον βαθμό δυσκολίας (1-3): "))
            if difficulty < 1 or difficulty > 3:
                continue
            else:
                return difficulty
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
                total_time = float(total_time)
                return total_time
            except:
                print("Κάτι πήγε στραβά.")

# Τα υλικά της συνταγής
def create_ingredients():
    ingredients = []
    while True:
        try:
            number_of_ingredients = int(input("Καταχωρίστε το πλήθος των υλικών: "))
            break
        except:
            print("Κάτι πήγε στραβά.")
    for i in range(0, number_of_ingredients):
        name_of_ingredient = input(f"Καταχωρίστε το όνομα του {i + 1}ου υλικού (π.χ. σπαγγέτι): ")
        try:
            quantity = input(f"Καταχωρίστε την ποσότητα του {i + 1}ου υλικού σε γραμμάρια (π.χ. 500): ")
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
        "portions": portions
    }
    data_recipes = load_recipes("recipes.json")
    data_recipes["recipes"].append(recipe)
    save_recipes(data_recipes, "recipes.json")

# Ioannis Kani

# Προβολή όλων των συνταγών
def view_recipes():
    data_recipes = load_recipes("recipes.json")
    for i, recipe in enumerate(data_recipes["recipes"]):
        print(f"{i + 1}. {recipe['name']} (χρόνος εκτέλεσης: {recipe['total_time']} λεπτά.)")

# Αναζήτηση συνταγής
def search_recipe():
    data_recipes = load_recipes("recipes.json")
    name = input("Αναζητήστε συνταγή με όνομα: ").lower()
    found = [r for r in data_recipes["recipes"] if name in r["name"].lower()]
    if found:
        for recipe in found:
            print(f"\n{recipe['name']} (χρόνος εκτέλεσης: {recipe['total_time']} λεπτά.)")
            print("\nΥλικά:")
            for i, ingredient in enumerate(recipe["ingredients"]):
                if ingredient["quantity"] == None:
                    print(f"xpsservices.dll {ingredient['name']}")
                else:
                    print(f"{i + 1}. {ingredient['name']} ({ingredient['quantity']} γρ.)")
            print("\nΒήματα:")
            for i, step in enumerate(recipe["steps"]):
                
                print(f"{i + 1}. {step}")
    else:
        print(" Δεν βρέθηκε συνταγή.")

def search_menu():
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

# Kostis

#Γενική Συνάρτηση για τροποποίηση συνταγών =============================================================
def edit_recipes():
    # Φόρτωση συνταγών
    data_recipes = load_recipes("recipes.json")

    #Έλεγχος εάν το JSON είναι κενό ελέγχοντας την μεταβλητή sudages
    if not data_recipes["recipes"]:
        print("Δεν υπάρχουν διαθέσιμες συνταγές.")
        return
    
    # Εμφάνιση συνταγών
    while True:
        print("Διαθέσιμες συνταγές:")
        i=0

        for i, recipe in enumerate(data_recipes["recipes"]):
            print(f"{i + 1}. Συνταγή: {data['recipes'][i]['name']}")
        
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
        
    #εισαγωγή της συνταγής που επιλέξαμε σε μεταβλητή
    recipe = data_recipes["recipes"][recipe_number - 1]

    #Επανάληψη για το menu
    while True:
        print("1. Τροποποίηση Ονόματος")
        print("2. Τροποποίηση Κατηγορίας")
        print("3. Τροποποίηση Δυσκολίας")
        print("4. Τροποποίηση Χρόνου Υλοποίησης")
        print("5. Τροποποίηση Υλικών")
        print("6. Τροποποίηση Βημάτων")
        print("7. Τροποποίηση Μερίδων")
        # print("8. Τροποποίηση Κόστους")
        print("0. Έξοδος")
        
        option = int(input("Επιλέξτε 1 έως 6 για να συνεχίσετε ή 0 για έξοδο: "))
        #Επιλογές τροποποίησης
        if option == 1:
            edit_name(recipe)
        #Τα υλικά δεν πρέπει να αποθηκευτούν σαν string σε λίστα αλλά σαν λεξικό ΔΕΣ ΤΟ ΑΥΤΟ!!!!!!!!!!!!
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
            break  # Τερματίζει το loop 
        else:
            print("Μη έγκυρη επιλογή. Προσπαθήστε ξανά") # το return σταματά την εκτέλεση της current funtion και προχωρά τον κώδικα

        save_recipes(data_recipes, "recipes.json")
  
        
#Συνάρτηση τροποποίησης ονόματος =====================================================================
def edit_name(recipe):
    #Έλεγχος μήπως έχει μείνει κενή η μεταβλητή
    if recipe["name"]:
        print(f"Το όνομα της συνταγής είναι {recipe["name"]}")
        #Επανάληψη ώστε να δίνει την δυνατότηα στον χρήστη να επιλέξει ξανά και για ασφάλεια
        while True:
            option=input("Εάν θέλετε να αλλάξετε το όνομα της συνταγής πατήστε 'y' αλλιώς 'n' για έξοδο:")
            if option=="y":
                new_name = input("Δώστε το νέο όνομα της συνταγής: ").strip()
                if new_name:
                    recipe["name"] = new_name
                    print("Το όνομα ενημερώθηκε!")
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
            option=input("Εάν θέλετε να αλλάξετε την κατηγορία της συνταγής πατήστε 'y' αλλιώς 'n' για έξοδο:")
            if option=="y":
                category = input("Καταχωρήστε την κατηγορία της συνταγής (δημητριακά, φρούτα, λαχανικά, γαλακτοκομικά, κρέας & προϊόντα, όσπρια, λίπη & έλαια, τρόφιμα με πολύ λίπος ή ζάχαρη): ")
                while category != "δημητριακά" and category != "φρούτα" and category != "λαχανικά" and category != "γαλακτοκομικά" and category != "κρέας & προϊόντα" and category != "όσπρια" and category != "λίπη & έλαια" and category != "τρόφιμα με πολύ λίπος ή ζάχαρη":
                    category = input("Καταχωρήστε την κατηγορία της συνταγής (δημητριακά, φρούτα, λαχανικά, γαλακτοκομικά, κρέας & προϊόντα, όσπρια, λίπη & έλαια, τρόφιμα με πολύ λίπος ή ζάχαρη): ")
                if category:
                    recipe["category"] = category   #Από ΕΔΩ ΑΛΛΑΖΕΙ ΣΤΟ ΑΡΧΕΙΟ
                    print("Η κατηγορία ενημερώθηκε!")
                else:
                    print("Η κατηγορία δεν μπορεί να είναι κενή! Η αλλαγή ακυρώθηκε.")
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
            option=input("Εάν θέλετε να αλλάξετε τον βαθμό της δυσκολίας πατήστε 'y' αλλιώς 'n' για έξοδο:")
            if option=="y":
                difficulty = input("Καταχωρήστε τον βαθμό δυσκολίας (εύκολη, μεσαία, δύσκολη): ")
                while difficulty != "εύκολη" and difficulty != "μεσαία" and difficulty != "δύσκολη":
                    difficulty = input("Καταχωρήστε τον βαθμό δυσκολίας (εύκολη, μεσαία, δύσκολη): ")
                if difficulty:
                    recipe["difficulty"]=difficulty
                    print("Η δυσκολία ενημερώθηκε!")
                else:
                    print("Η δυσκολία δεν μπορεί να είναι κενή! Η αλλαγή ακυρώθηκε.")
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
            option=input("Εάν θέλετε να αλλάξετε την συνολική διάρκεια υλοποίησης πατήστε 'y' αλλιώς 'n' για έξοδο:")
            if option=="y":
                try:
                    total_time = float(input("Καταχωρήστε τον συνολικό χρόνο εκτέλεσης σε λεπτά (π.χ. 65): "))
                    if total_time:
                        recipe["total_time"]=total_time
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
        create_total_time()  


#Συνάρτηση τροποποίησης υλικών ==================================================================================
#Συνάρτηση τροποποίησης υλικών ==================================================================================
def edit_ingredients(recipe):
    #Εμφάνιση των ήδη υπάρχοντων υλικών
    #Η καθε sudagh είναι μία θέση του πίνακα sudages , οπότε το sudagh['ingredients'] περιέχει μία μεγάλη λίστα
    #από λεξικά υλικών με name και ποσότητα keys.
    #Άρα εάν πάρεις for item in sudagh['ingredients'] τοτε το καθε item εχει item['name'] και item['quantity']


    if not recipe["ingredients"]:
        print("Δεν υπάρχουν υλικά για αυτήν την συνταγή.")
        print("Παρακαλώ εκχωρήστε τα από την αρχή")
        create_ingredients()
    
    while True:
        print("Υλικά συνταγής:")

        for i, ingredient in enumerate(recipe["ingredients"], start=1):
            print(f"{i}. {ingredient['name']} ({ingredient['quantity']})")
        
        if recipe["ingredients"]:
            try:
                ingredient_number = int(input("Δώστε τον αριθμό του υλικού που θέλετε να τροποποιήσετε: "))
                if ingredient_number < 1 or ingredient_number > len(recipe["ingredients"]):
                    print("Λάθος αριθμός, εισάγετε έναν αριθμό από τα διαθέσιμα υλικά")
                else:
                    break
            except ValueError:
                print("Παρακαλώ εισάγετε έναν ακέραιο αριθμό!")
        else:
            print("Η λίστα των υλικών είναι κενή.")
            return
            
        
    #εισαγωγή του υλικού που επιλέξαμε για τροποποίηση σε μία μεταβλητή
    ingredient=recipe["ingredients"][ingredient_number-1]
    while True:
        print(f"Τροποποίηση {ingredient["name"]}:")
        print("1. Τροποποίηση Ονόματος")
        print("2. Τροποποίηση Ποσότητας")
        print("0. Έξοδος")

        option = int(input("Επιλέξτε 1 έως 2 για να συνεχίσετε ή 0 για έξοδο: "))

        if option == 1:
            products=load_products("products.json")
            print("Τα διαθέσιμα υλικά είναι:")
            for i, prod in enumerate(products["products"], start=1):
                print(f"{i}. {prod['name']} ({prod['price_per_kg']})")
            
            new_ingredient_name = input("Καταχωρήστε το όνομα του υλικού: ").strip()
            if new_ingredient_name:
                ingredient["name"] = new_ingredient_name
                print("Το όνομα ενημερώθηκε!")

                # Έλεγχος και προσθήκη στο products.json
                
                add_product_if_not_exists(products, new_ingredient_name ,"products.json")

            else:
                print("Το όνομα δεν μπορεί να είναι κενό!")
        elif option == 2:
            while True:
                try:
                    new_ingredient_quantity = int(input("Καταχωρήστε την ποσότητα του υλικού: "))
                    if new_ingredient_quantity >=0:
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


#Συνάρτηση τροποποίησης βημάτων ==========================================================
def edit_steps(recipe):
    #Εμφάνιση των ήδη υπάρχοντων βημάτων με join σε list comprehension (list me strings)
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
                else: #Εισαγωγή νέου βήματος
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
    #Έλεγχος εάν το JSON είναι κενό ελέγχοντας την μεταβλητή sudages
    if not data_recipes["recipes"]:
        print("Δεν υπάρχουν διαθέσιμες συνταγές.")
        return
    
    # Εμφάνιση συνταγών
    while True:
        print("Διαθέσιμες συνταγές:")
        
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
                confirmation=input(f"Είστε σίγουρoι ότι θέλετε να διαγράψετε τη συνταγή {selected_recipe['name']};(y/n): ")
                if confirmation=='n':
                    print("Η διαγραφή ακυρώθηκε.")
                    return
                
                deleted_recipe = data_recipes["recipes"].pop(recipe_number - 1)
                print(f"Η συνταγή '{deleted_recipe['name']}' διαγράφηκε επιτυχώς!")

                #Καλεί την save_recipes η οποία αποθηκεύει στο Json ότι έγινε.
                save_recipes(data_recipes, "recipes.json")
                break
        except ValueError:
            print("Παρακαλώ εισάγετε έναν ακέραιο αριθμό!")

# Alex

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
    data_recipes = load_recipes("recipes.json")
    print("\nΔιαθέσιμες συνταγές:")
    for i, recipe in enumerate(data_recipes["recipes"]):
        print(f"{i + 1}. {recipe['name']}")

# Συνάρτηση κύριας ροής του προγράμματος
def make_menu():
    data_recipes = load_recipes("recipes.json")
    while True:
        list_recipes()
        choice = input("\nΔιάλεξε αριθμό συνταγής ή 'q' για έξοδο: ")
        if choice.lower() == 'q':
            print("Έξοδος από το πρόγραμμα. Καλή όρεξη!")
            break
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(data_recipes["recipes"]):
            print("Μη έγκυρη επιλογή. Προσπάθησε ξανά.")
            continue
        recipe = data_recipes["recipes"][int(choice) - 1]
        print(f"\nΣυνταγή: {recipe['name']}")
        display_ingredients(recipe['ingredients'])
        display_steps(recipe['steps'])
        input("\nΠάτησε Enter για να επιστρέψεις στο μενού...")

# Giorgos

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
            if product["name"] == name:
                total_cost += (quantity / 1000) * product["price_per_kg"]
                break
    cost = round(total_cost, 2)
    data_recipes['recipes'][choice - 1]["cost"] = cost # Ενημερώνει το λεξικό της συνταγής
    save_recipes(data, "recipes.json")

# Τροποποίηση τιμής προϊόντος
def update_product_price():
    products_data = load_products("products.json")
    print("\nΔιαθέσιμα προϊόντα:")
    for product in products_data['products']:
        name = product['name']
        price = product['price_per_kg']
        print(f"- {name} ({price:.2f} €/kg)")

    name = input("\nΠοιο προϊόν θες να αλλάξεις; ").strip().lower()

    for product in products_data['products']:
        if product['name'].lower() == name:
            current_price = product['price_per_kg']
            print(f"Τρέχουσα τιμή για '{product['name']}': {current_price:.2f} €/kg")
            try:
                new_price = float(input("Νέα τιμή (€): "))
                product['price_per_kg'] = new_price
                save_products(products_data, "products.json")
                print("Η τιμή ενημερώθηκε.")
                return
            except ValueError:
                print("Μη έγκυρη τιμή.")
                return

    print("Δεν βρέθηκε το προϊόν.")

def delete_product():
    products_data = load_products("products.json")
    for i, product in enumerate(products_data["products"]):
        print(f"{i + 1}. {product['name']}")
    while True:
        try:
            choice = int(input("Επίλεξε αριθμό προϊόντος για διαγραφή: "))
            break
        except:
            print("Κάτι πήγε στραβά.")
    products_data["products"].pop(choice - 1)
    save_products(products_data, "products.json")

# Απλό menu για χρήση
def calculate_cost():
    while True:
        print("\n--- MENU ---")
        print("1. Υπολογισμός κόστους συνταγής")
        print("2. Τροποποίηση τιμής προϊόντος")
        print("3. Διαγραφή προϊόντος")
        print("4. Έξοδος")
        choice = input("Επιλογή: ").strip()
        if choice == '1':
            calculate_recipe_cost()
        elif choice == '2':
            update_product_price()
        elif choice == "3":
            delete_product()
        elif choice == '4':
            break
        else:
            print("Μη έγκυρη επιλογή.")

def main():
    while True:
        print("=== Συνταγές Μαγειρικής ===")
        print("1. Καταχώρηση συνταγής")
        print("2. Αναζήτηση συνταγής")
        print("3. Τροποποίηση συνταγής")
        print("4. Διαγραφή συνταγής")
        print("5. Εκτέλεση συνταγής")
        print("6. Υπολογισμός κόστους συνταγής")
        print("7. Έξοδος")
        try:
            choice = int(input("Επιλέξτε μια ενέργεια (1-7): "))
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
            make_menu()
        elif choice == 6:
            calculate_cost()
        elif choice == 7:
            print("Έξοδος από το πρόγραμμα.")
            break
        else:
            print("Μη έγκυρη επιλογή. Παρακαλώ επιλέξτε ξανά.\n")

if __name__ == "__main__":
    main()

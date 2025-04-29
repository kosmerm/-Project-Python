import json
import unicodedata  #χρειάζομαι μία συνάρτηση που θα με διευκολύνει όταν θέλω να αναζητώ με ελληνικούς χαρακτήρες

#to r εδω χρησιμεύει στο να μην εκλαμβάνονται τα \ σαν escape characters
file_name = r"C:\Users\Konstantinos.Mermigk\Desktop\eap\propli\recipes.json"


#Γενική Συνάρτηση για τροποποίηση συνταγών =============================================================
def edit_recipe():
    # Φόρτωση συνταγών
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            #Μετατροπή του file (ότι περιέχει) σε σ'ένα αντικείμενο python dictionary.
            #π.χ json {"name":"μακαρόνια",} => sudages={"name":"μακαρόνια",}
            recipes = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Δεν βρήκα το JSON ή το αρχείο είναι κατεστραμμένο.")
        return

    #Έλεγχος εάν το JSON είναι κενό ελέγχοντας την μεταβλητή sudages
    if not recipes["recipes"]:
        print("Δεν υπάρχουν διαθέσιμες συνταγές.")
        return
    
    # Εμφάνιση συνταγών
    while True:
        print("Διαθέσιμες συνταγές:")
        i=0
        for recipe in recipes["recipes"]:
            i+=1 #Για να γίνεται η επιλογή συνταγή με αριθμό για να αποφύγουμε λάθη αναζήτησης
            print(f"{i}.Συνταγή: {recipe['name']}")
        
        try:
            recipe_number = int(input("Δώστε τον αριθμό της συνταγής που θέλετε να τροποποιήσετε: "))
            if recipe_number == 0:
                return
            elif recipe_number < 1 or recipe_number > len(recipes["recipes"]):
                print("Λάθος αριθμός, εισάγεται έναν αριθμό από τις διαθέσιμες συνταγές")
            else:
                break
        except ValueError:
            print("Παρακαλώ εισάγετε έναν ακέραιο αριθμό!")
        
    #εισαγωγή της συνταγής που επιλέξαμε σε μεταβλητή
    recipe=recipes["recipes"][recipe_number-1]

    #Επανάληψη για το menu
    while True:
        print("Η συνταγή βρέθηκε")
        print("1. Τροποποίηση Ονόματος")
        print("2. Τροποποίηση Κατηγορίας")
        print("3. Τροποποίηση Δυσκολίας")
        print("4. Τροποποίηση Χρόνου Υλοποίησης")
        print("5. Τροποποίηση Υλικών")
        print("6. Τροποποίηση Βημάτων")
        print("7. Τροποποίηση Μερίδων")
        #print("8. Τροποποίηση Κόστους")
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

        save_recipes(recipes,file_name)
  
        
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
        #ΕΔΩ                           ΜΠΑΙΝΕΙ Η ΣΥΝΑΡΤΗΣΗ ΕΚΧΩΡΗΣΗΣ  
            
            
            

#Συνάρτηση τροποποίησης κατηγορίας συνταγής ================================================================================================================================================================================================================================
def edit_category(recipe):
    #Έλεγχος μήπως έχει μείνει κενή η μεταβλητή
    if recipe["category"]:
        print(f"Η συνταγή ανήκει στην κατηγορία {recipe["category"]}")
        while True:
            option=input("Εάν θέλετε να αλλάξετε την κατηγορία της συνταγής πατήστε 'y' αλλιώς 'n' για έξοδο:")
            if option=="y":
                category = input("Καταχωρίστε την κατηγορία της συνταγής (δημητριακά, φρούτα, λαχανικά, γαλακτοκομικά, κρέας & προϊόντα, όσπρια, λίπη & έλαια, τρόφιμα με πολύ λίπος ή ζάχαρη): ")
                while category != "δημητριακά" and category != "φρούτα" and category != "λαχανικά" and category != "γαλακτοκομικά" and category != "κρέας & προϊόντα" and category != "όσπρια" and category != "λίπη & έλαια" and category != "τρόφιμα με πολύ λίπος ή ζάχαρη":
                    category = input("Καταχωρίστε την κατηγορία της συνταγής (δημητριακά, φρούτα, λαχανικά, γαλακτοκομικά, κρέας & προϊόντα, όσπρια, λίπη & έλαια, τρόφιμα με πολύ λίπος ή ζάχαρη): ")
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
        #ΕΔΩ                           ΜΠΑΙΝΕΙ Η ΣΥΝΑΡΤΗΣΗ ΕΚΧΩΡΗΣΗΣ  
        
    

#Συνάρτηση τροποποίησης δυσκολίας συνταγής =============================================================
def edit_difficulty(recipe):
    #Έλεγχος μήπως έχει μείνει κενή η μεταβλητή
    if recipe["difficulty"]:
        print(f"Η συνταγή έχει δυσκολία {recipe["difficulty"]}")
        while True:
            option=input("Εάν θέλετε να αλλάξετε τον βαθμό της δυσκολίας πατήστε 'y' αλλιώς 'n' για έξοδο:")
            if option=="y":
                difficulty = input("Καταχωρίστε τον βαθμό δυσκολίας (εύκολη, μεσαία, δύσκολη): ")
                while difficulty != "εύκολη" and difficulty != "μεσαία" and difficulty != "δύσκολη":
                    difficulty = input("Καταχωρίστε τον βαθμό δυσκολίας (εύκολη, μεσαία, δύσκολη): ")
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
        #ΕΔΩ                           ΜΠΑΙΝΕΙ Η ΣΥΝΑΡΤΗΣΗ ΕΚΧΩΡΗΣΗΣ  

#Συνάρτηση τροποποίησης χρόνου συνταγής ====================================================
def edit_total_time(recipe):
    #Έλεγχος μήπως έχει μείνει κενή η μεταβλητή
    if recipe["total_time"]:
        print(f"Η συνταγή έχει συνολική διάρκεια υλοποίησης {recipe["total_time"]}")
        while True:
            option=input("Εάν θέλετε να αλλάξετε την συνολική διάρκεια υλοποίησης πατήστε 'y' αλλιώς 'n' για έξοδο:")
            if option=="y":
                try:
                    total_time = float(input("Καταχωρίστε τον συνολικό χρόνο εκτέλεσης σε λεπτά (π.χ. 65): "))
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
        #ΕΔΩ                           ΜΠΑΙΝΕΙ Η ΣΥΝΑΡΤΗΣΗ ΕΚΧΩΡΗΣΗΣ  



#Συνάρτηση τροποποίησης υλικών ==================================================================================
def edit_ingredients(recipe):
    #Εμφάνιση των ήδη υπάρχοντων υλικών
    #Η καθε sudagh είναι μία θέση του πίνακα sudages , οπότε το sudagh['ingredients'] περιέχει μία μεγάλη λίστα
    #από λεξικά υλικών με name και ποσότητα keys.
    #Άρα εάν πάρεις for item in sudagh['ingredients'] τοτε το καθε item εχει item['name'] και item['quantity']

    if not recipe["ingredients"]:
        print("Δεν υπάρχουν υλικά για αυτήν την συνταγή.")
    
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
            new_ingredient_name = input("Καταχωρήστε το όνομα του υλικού: ").strip()
            if new_ingredient_name:
                ingredient["name"] = new_ingredient_name
                print("Το όνομα ενημερώθηκε!")
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
    if(recipe["steps"]):
        print("Τρέχοντα Βήματα: ")
        for i , step in enumerate(recipe["steps"], start=1): #Η enumerate διατρέχει μία λίστα παίρνοντας ταυτόχρονα και το index κάθε στοιχείου
            print(f"{i}. {step}")

        while True:
                option=input("Εάν θέλετε να τροποποιήσετε κάποιο από τα βήματα πατήστε 'y' αλλιώς 'n' για έξοδο:")
                if option=="y":
                    try:
                        #while True:
                            #try:
                        step_number=int(input("Εισάγετε τον αριθμό του βήματος που θέλετε να τροποποιήσετε ή 0 για έξοδο: "))
                        if step_number==0:
                            print("Έξοδος από την τροποποίηση των βημάτων")
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
                    

                elif option=="n":
                    return
                else:
                    print("Μη έγκυρη επιλογή. Προσπαθήστε ξανά")
    else:
        print("Δεν βρέθηκαν τα βήματα υλοποίησης της συνταγής.Παρακαλώ εκχωρήστε τα από την αρχή")  
        #ΕΔΩ                           ΜΠΑΙΝΕΙ Η ΣΥΝΑΡΤΗΣΗ ΕΚΧΩΡΗΣΗΣ  



                
   

#Συνάρτηση τροποποίησης μερίδων ==========================================================
def edit_portions(recipe):
    if recipe["portions"]:
        print(f"Η συνταγή είναι για {recipe["portions"]} μερίδες περίπου")
        while True:
            option=input("Εάν θέλετε να αλλάξετε τις μερίδες πατήστε 'y' αλλιώς 'n' για έξοδο:")
            if option=="y":
                try:
                    portions = int(input("Καταχωρίστε τις μερίδες (π.χ. 10): "))
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
    

#Συνάρτηση για την αποθήκευση στο αρχείο Json ============================================
def save_recipes(recipes, file_name):
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(recipes, file, indent=2, ensure_ascii=False)
        print("Η τροποποίηση αποθηκεύτηκε στο αρχείο Json με επιτυχία!")
    except Exception as e:
        print(f"Σφάλμα κατά την αποθήκευση: {e}")
    

#Συνάρτηση ΔΙΑΓΡΑΦΗΣ συνταγών  ===========================================================
def delete_recipe():
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            #Μετατροπή του file (ότι περιέχει) σε σ'ένα αντικείμενο python dictionary.
            #π.χ json {"name":"μακαρόνια",} => sudages={"name":"μακαρόνια",}
            recipes = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Δεν βρήκα το JSON ή το αρχείο είναι κατεστραμμένο.")
        return

    #Έλεγχος εάν το JSON είναι κενό ελέγχοντας την μεταβλητή sudages
    if not recipes["recipes"]:
        print("Δεν υπάρχουν διαθέσιμες συνταγές.")
        return
    
    # Εμφάνιση συνταγών
    while True:
        print("Διαθέσιμες συνταγές:")
        i=0
        for i, recipe in enumerate(recipes["recipes"], start=1):
            print(f"{i}. Συνταγή: {recipe['name']}")
        
        try:
            recipe_number = int(input(f"Δώστε τον αριθμό της συνταγής που θέλετε να διαγράψετε(1 - {len(recipes["recipes"])}) ή 0 για έξοδο: "))
            if recipe_number == 0:
                print("Ακύρωση διαγραφής.")
                return
            elif recipe_number < 1 or recipe_number > len(recipes["recipes"]):
                print("Λάθος αριθμός, εισάγετε έναν αριθμό από τις διαθέσιμες συνταγές")
            else:
                selected_recipe = recipes["recipes"][recipe_number - 1]
                confirmation=input(f"Είστε σίγουρoι ότι θέλετε να διαγράψετε τη συνταγή {selected_recipe["name"]};(y/n): ")
                if confirmation=='n':
                    print("Η διαγραφή ακυρώθηκε.")
                    return
                
                deleted_recipe=recipes["recipes"].pop(recipe_number-1)
                print(f"Η συνταγή '{deleted_recipe['name']}' διαγράφηκε επιτυχώς!")

                #Καλεί την save_recipes η οποία αποθηκεύει στο Json ότι έγινε.
                save_recipes(recipes,file_name)
                break
        except ValueError:
            print("Παρακαλώ εισάγετε έναν ακέραιο αριθμό!")


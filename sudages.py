import json
from unicodedata import unidata_version #χρειάζομαι μία συνάρτηση που θα με διευκολύνει όταν θέλω να αλλάζω και 
#να αναζητώ με ελληνικούς χαρακτήρες

file_name = r"C:\Users\kostis\Desktop\ΕΑΠ\ΠΛΗΠΡΟ\Ομαδικό project\recipes.json"

# Συνάρτηση για τροποποίηση συνταγών
def edit_recipe():
    # Φόρτωση συνταγών
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            #Μετατροπή του file (ότι περιέχει) σε sένα αντικείμενο python list ή dict.
            #π.χ json {"name":"μακαρόνια",} => sudages={"name":"μακαρόνια",}
            sudages = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Δεν βρήκα το JSON ή το αρχείο είναι κατεστραμμένο.")
        return

    #Έλεγχος εάν το JSON είναι κενό
    if("recipes" not in sudages):
        print("Δεν υπάρχουν διαθέσιμες συνταγές.")
        return
    
    # Εμφάνιση συνταγών
    print("Διαθέσιμες συνταγές:")
    #sudages["recipes"] = είναι μία λίστα ,δλδ sudages["recipes"]["name"]=Μακαρόνια με κιμά
    for sudagh in sudages["recipes"]:
        print(f"Συνταγή: {sudagh['name']}")
        print(f"Κατηγορία: {sudagh['category']}")
        print(f"Δυσκολία: {sudagh['difficulty']}")
        print(f"Χρόνος Προετοιμασίας: {sudagh['total_time']}")
        #Εδώ χρησιμοποιώ [for item in sudagh] γιατί το sudagh['ingredients'] περιέχει λίστα με name και quantity
        print(f"Υλικά: {', '.join([item['name'] for item in sudagh['ingredients']])}")
        print(f"Βήματα: {'\n'.join(sudagh['steps'])}")

    # Επιλογή συνταγής προς τροποποίηση
    vrethike=False
    onoma_sudaghs = input("Δώστε το όνομα της συνταγής που θέλετε να τροποποιήσετε: ").strip()
    for sudagh in sudages["recipes"]:
        #Βάζω το .lower() για να μην είναι case sensitive η αναζήτηση
        #Βάζω το strip() για να μην επηρεάζεται από τα κενά ανάμεσα στις λέξεις
        if(sudagh["name"].lower().strip()==onoma_sudaghs.lower().strip()):
            vrethike=True

            #Επανάληψη για το menu
            while True:
                print("Η συνταγή βρέθηκε")
                print("\n1. Τροποποίηση Ονόματος")
                print("2. Τροποποίηση Υλικών")
                print("3. Τροποποίηση Βημάτων")
                print("0. Έξοδος")
        
                epilogh = input("Επιλέξτε 1 έως 3 για να συνεχίσετε ή 0 για έξοδο: ").strip()
                #Επιλογές τροποποίησης
                if epilogh == "1":
                    new_name = input("Δώστε το νέο όνομα της συνταγής: ").strip()
                    sudagh["name"] = new_name
                #Τα υλικά δεν πρέπει να αποθηκευτούν σαν string σε λίστα αλλά σαν λεξικό ΔΕΣ ΤΟ ΑΥΤΟ!!!!!!!!!!!!
                elif epilogh == "2":
                    new_ingredients = input("Δώστε τα νέα υλικά (μορφή: όνομα=ποσότητα, όνομα=ποσότητα,...)").strip()
                    sudagh["ingredients"] = [item.strip() for item in new_ingredients.split(",")]
                elif epilogh == "3":
                    new_steps = input("Δώστε τα νέα βήματα διαχωρίζοντας τα με '|': ").strip()
                    sudagh["steps"] = [step.strip() for step in new_steps.split("|")]
                elif epilogh == "0":
                    return
                else:
                    print("Λάθος επιλογή.")
                    return
                try:
                    # Αποθήκευση των αλλαγών στο αρχείο
                    with open(file_name, "w", encoding="utf-8") as file:
                        json.dump(sudages, file, indent=4, ensure_ascii=False)
                    print("Η τροποποίηση αποθηκεύτηκε με επιτυχία!")
                except Exception as e:
                    print(f"Σφάλμα κατά την αποθήκευση: {e}")
            #break #Σταματάω αφού γίνει η επεξεργασία
    if(not vrethike):
        print("Λάθος όνομα συνταγής , οι διαθέσιμες συνταγές προς τροποποίηση είναι οι παρακάτω:")
        for sudagh in sudages["recipes"]:
            print(f"Συνταγή: {(sudagh['name'])}")
  
        
    
    

    


def main():
    #Κεντρικό μενού
    while True:
        print("============Συνταγές=============")
        print("1. Καταχώρηση καινούριας συνταγής")
        print("2. Αναζήτηση συνταγής")
        print("3. Τροποποίηση συνταγής")
        print("4. Διαγραφή συνταγής")
        print("5. Εκτέλεση συνταγή")
        print("6. Έλεγχος κόστους συνταγής")
        print("0. Έξοδος από την εφαρμογή")
        
        try:  
            #Μετατροπή του input σε int για να πιάσει ο exception handler τον λάθος χαρακτήρα
            epilogh=int(input("Επιλέξτε 1 έως 6 για να συνεχίσετε ή 0 για έξοδο:"))
            if epilogh == 1:
                print("add_recipe")
                #add_recipe()
            elif epilogh == 2:
                print("search_recipe")
                #search_recipe()
            elif epilogh == 3:
                print("edit_recipe")
                edit_recipe()
            elif epilogh == 4:
                print("delete_recipe")
                #delete_recipe()
            elif epilogh == 5:
                print("execute_recipe")
                #execute_recipe()
            elif epilogh == 6:
                print("cost_recipe")
                #cost_recipe()
            elif epilogh == 0:
                print("Goodbye!")
                break
            else:
                print("Λάθος επιλογή") 
        except ValueError:
            print("Η επιλογή γίνεται μόνο με αριθμούς από το 0 έως το 6")

main()
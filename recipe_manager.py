import json
from edit_recipes import *
from add_recipes import *
from cost_with_update_json import *
from make_recipe import *

def main():
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
            option=int(input("Επιλέξτε 1 έως 6 για να συνεχίσετε ή 0 για έξοδο:"))
            if option == 1:
                print("add_recipe")
                create_recipe()
            elif option == 2:
                print("search_recipe")
                #search_recipe()
            elif option == 3:
                print("edit_recipe")
                edit_recipes()
            elif option == 4:
                print("delete_recipe")
                delete_recipe()
            elif option == 5:
                print("execute_recipe")
                make_recipe()
            elif option == 6:
                print("cost_recipe")
                calculate_cost()
            elif option == 0:
                print("Goodbye!")
                break
            else:
                print("Λάθος επιλογή") 
        except ValueError:
            print("Η επιλογή γίνεται μόνο με αριθμούς από το 0 έως το 6")

if __name__ == "__main__":
    main()

from edit_recipes import *
from add_recipes import *
from cost import *
from make_recipe import *
from search_recipe import *

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
            option=int(input("Επιλέξτε 1 έως 6 για να συνεχίσετε ή 0 για έξοδο: "))
            if option == 1:
                create_recipe()
            elif option == 2:
                search_recipe()
            elif option == 3:
                edit_recipes()
            elif option == 4:
                delete_recipe()
            elif option == 5:
                make_recipe()
            elif option == 6:
                calculate_cost()
            elif option == 0:
                print("Έξοδος από την εφαρμογή.")
                break
            else:
                print("Λάθος επιλογή") 
        except ValueError:
            print("Η επιλογή γίνεται μόνο με αριθμούς από το 0 έως το 6")

if __name__ == "__main__":
    main()

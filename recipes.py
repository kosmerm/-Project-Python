from add_recipes import *
from search_recipe import *
from edit_recipes import *
from make_recipe import *
from cost import *

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
            search_recipe()
        elif choice == 3:
            edit_recipes()
        elif choice == 4:
            delete_recipe()
        elif choice == 5:
            make_recipe()
        elif choice == 6:
            calculate_cost()
        elif choice == 7:
            print("Έξοδος από το πρόγραμμα.")
            break
        else:
            print("Μη έγκυρη επιλογή. Παρακαλώ επιλέξτε ξανά.\n")

if __name__ == "__main__":
    main()

from json_manager import load_products, save_products
data = load_products("products.json")
while True:
    print("--- Διαχείριση προϊόντων ---")
    print("1. Καταχώριση προϊόντος")
    print("2. Τροποποίηση προϊόντος")
    print("3. Διαγραφή προϊόντος")
    print("4. Έξοδος")
    try:
        choice = int(input("Επιλέξτε μια επιλογή (1-4): "))
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
    elif choice == 3:
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
    elif choice == 4:
        print("Έξοδος από τη διαχείριση προϊόντων.")
        break
    else:
        print("Μη έγκυρη επιλογή. Παρακαλώ επιλέξτε ξανά.\n")

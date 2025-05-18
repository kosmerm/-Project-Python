from json_manager import load_recipes, save_recipes, load_products, save_products

# Υπολογισμός κόστους συνταγής και ενημέρωση στο αρχείο
def calculate_recipe_cost():
    data = load_recipes("recipes.json")
    total_cost = 0.0
    for i, recipe in enumerate(data["recipes"]):
        print(f"{i + 1}. {recipe['name']}")
    choice = int(input("Επίλεξε συνταγή για υπολογισμό κόστους: "))
    products = load_products("products.json")
    for ingredient in data["recipes"][choice - 1]["ingredients"]:
        name = ingredient['name']
        quantity = ingredient['quantity']
        for product in products["products"]:
            if product["name"] == name:
                total_cost += (quantity / 1000) * product["price_per_kg"]
                break
    cost = round(total_cost, 2)
    data['recipes'][choice - 1]["cost"] = cost # Ενημερώνει το λεξικό της συνταγής
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
    data = load_products("products.json")
    for i, product in enumerate(data["products"]):
        print(f"{i + 1}. {product['name']}")
    choice = int(input("Επίλεξε αριθμό προϊόντος για διαγραφή: "))
    data["products"].pop(choice - 1)
    save_products(data, "products.json")

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

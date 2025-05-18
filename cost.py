import json

# Διαδρομές αρχείων
RECIPES_FILE = 'recipes.json'
PRODUCTS_FILE = 'products.json'

# Φορτώνει δεδομένα από JSON αρχεία
def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

# Αποθηκεύει δεδομένα σε JSON αρχεία
def save_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# Υπολογισμός κόστους συνταγής και ενημέρωση στο αρχείο
def calculate_recipe_cost(recipe, product_prices):
    total_cost = 0.0
    for ingredient in recipe['ingredients']:
        name = ingredient['name']
        quantity = ingredient['quantity']
        if quantity and name in product_prices:
            total_cost += (quantity / 1000) * product_prices[name]

    cost = round(total_cost, 2)
    recipe['cost'] = cost  # Ενημερώνει το λεξικό της συνταγής

    # Ενημέρωση στο αρχείο recipes.json
    recipes_data = load_json(RECIPES_FILE)
    for r in recipes_data['recipes']:
        if r['name'] == recipe['name']:
            r['cost'] = cost
            break
    save_json(RECIPES_FILE, recipes_data)

    return cost

# Εμφάνιση κόστους όλων των συνταγών
def show_all_recipe_costs():
    recipes_data = load_json(RECIPES_FILE)
    product_prices = {
        product['name']: product['price_per_kg']
        for product in load_json(PRODUCTS_FILE)['products']
    }

    for recipe in recipes_data['recipes']:
        name = recipe['name']
        cost = calculate_recipe_cost(recipe, product_prices)
        print(f"Συνταγή: {name} -> Κόστος: {cost}€")

# Τροποποίηση τιμής προϊόντος
def update_product_price():
    products_data = load_json(PRODUCTS_FILE)
    names = [p['name'] for p in products_data['products']]
    print("\nΔιαθέσιμα προϊόντα:")
    for name in names:
        print(f"- {name}")
    name = input("\nΠοιο προϊόν θες να αλλάξεις; ").strip()

    for product in products_data['products']:
        if product['name'] == name:
            try:
                new_price = float(input(f"Νέα τιμή για '{name}' (€): "))
                product['price_per_kg'] = new_price
                save_json(PRODUCTS_FILE, products_data)
                print("✅ Η τιμή ενημερώθηκε.")
                return
            except ValueError:
                print("⚠ Μη έγκυρη τιμή.")
                return
    print("⚠ Δεν βρέθηκε το προϊόν.")

# Απλό menu για χρήση
def calculate_cost():
    while True:
        print("\n--- MENU ---")
        print("1. Υπολογισμός κόστους συνταγών")
        print("2. Τροποποίηση τιμής προϊόντος")
        print("3. Έξοδος")
        choice = input("Επιλογή: ").strip()
        if choice == '1':
            show_all_recipe_costs()
        elif choice == '2':
            update_product_price()
        elif choice == '3':
            break
        else:
            print("⚠ Μη έγκυρη επιλογή.")

import json

# === Συνταγές ===

def load_recipes(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Σφάλμα κατά την ανάγνωση των συνταγών: {e}")
        return []

def save_recipes(recipes, file_name):
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(recipes, f, indent=2, ensure_ascii=False)
        print("Επιτυχής αποθήκευση!")
    except Exception as e:
        print(f"Σφάλμα κατά την αποθήκευση: {e}")

# === Προϊόντα ===

def load_products(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            return json.load(f).get("products", [])
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Σφάλμα κατά την ανάγνωση των προϊόντων: {e}")
        return []

def save_products(products, file_name):
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump({"products": products}, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Σφάλμα αποθήκευσης προϊόντων: {e}")

def add_product_if_not_exists(products, name, file_name):
    for product in products:
        if product["name"].lower() == name.lower():
            return
    try:
        price = float(input(f"Το προϊόν '{name}' δεν υπάρχει.\nΚαταχωρήστε τιμή ανά κιλό (€): "))
        products.append({"name": name, "price_per_kg": price})
        save_products(products, file_name)
        print(f"Το προϊόν '{name}' προστέθηκε στο products.json.")
    except ValueError:
        print("Μη έγκυρη τιμή. Το προϊόν δεν προστέθηκε.")


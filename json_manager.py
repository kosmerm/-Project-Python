import os
import sys
import json
from shutil import copyfile

def resource_path(filename):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, filename)

def writable_path(filename):
    base_path = os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else __file__)
    return os.path.join(base_path, filename)

def ensure_local_copy(filename):
    dst = writable_path(filename)
    if not os.path.exists(dst):
        src = resource_path(filename)
        copyfile(src, dst)
    return dst

recipes_path = ensure_local_copy("recipes.json")
products_path = ensure_local_copy("products.json")

def load_recipes(file_name):
    try:
        with open(recipes_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Σφάλμα κατά την ανάγνωση των συνταγών: {e}")
        return []

def save_recipes(recipes, file_name):
    try:
        with open(recipes_path, "w", encoding="utf-8") as f:
            json.dump(recipes, f, indent=2, ensure_ascii=False)
        print("Επιτυχής αποθήκευση!\n")
    except Exception as e:
        print(f"Σφάλμα κατά την αποθήκευση: {e}")

# === Προϊόντα ===

def load_products(file_name):
    try:
        with open(products_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Σφάλμα κατά την ανάγνωση των προϊόντων: {e}")
        return []

def save_products(products, file_name):
    try:
        with open(products_path, "w", encoding="utf-8") as f:
            json.dump(products, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Σφάλμα αποθήκευσης προϊόντων: {e}")

def add_product_if_not_exists(products, name, file_name):
    for product in products["products"]:
        if product["name"].lower() == name.lower():
            return
    try:
        price = float(input(f"Το προϊόν '{name}' δεν υπάρχει.\nΚαταχωρήστε τιμή ανά κιλό (€): "))
        products["products"].append({"name": name, "price_per_kg": price})
        save_products(products, file_name)
        print(f"Το προϊόν '{name}' προστέθηκε στο products.json.")
    except ValueError:
        print("Μη έγκυρη τιμή. Το προϊόν δεν προστέθηκε.")

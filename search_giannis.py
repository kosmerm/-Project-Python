import json

data = load_recipes("recipes.json")




def unique_categories(recipes):
    return sorted(set(r['category'] for r in recipes))

def unique_difficulties(recipes):
    return sorted(set(r['difficulty'] for r in recipes))

def filter_recipes_by_category(recipes, category):
    return [r for r in recipes if r['category'] == category]

def filter_recipes_by_difficulty(recipes, difficulty):
    return [r for r in recipes if r['difficulty'] == difficulty]

def filter_recipes_by_time(recipes, max_time):
    return [r for r in recipes if r['total_time'] <= max_time]

def filter_recipes_by_ingredients(recipes, ingredients_list):
    """
    Φιλτράρει τις συνταγές που περιέχουν όλα τα υλικά στη λίστα ingredients_list.
    """
    filtered = []
    for r in recipes:
        recipe_ingredients = [ing['name'].lower() for ing in r['ingredients']]
        if all(ing.lower() in recipe_ingredients for ing in ingredients_list):
            filtered.append(r)
    return filtered

def show_ingredients(ingredients):
    print("\nΥλικά:")
    for ing in ingredients:
        print(f"- {ing['quantity']} {ing['name']}")

def show_steps(steps):
    print("\nΒήματα:")
    for i, step in enumerate(steps, 1):
        print(f"{i}. {step}")

def main():
    while True:
        print("\nΦίλτρα επιλογής:")
        print("1. Όλες οι συνταγές")
        print("2. Φιλτράρισμα ανά κατηγορία")
        print("3. Φιλτράρισμα ανά δυσκολία")
        print("4. Φιλτράρισμα ανά χρόνο προετοιμασίας")
        print("5. Φιλτράρισμα ανά υλικά")
        print("q. Έξοδος")

        choice = input("Επίλεξε επιλογή: ").strip().lower()

        if choice == 'q':
            print("Έξοδος από το πρόγραμμα. Καλή όρεξη!")
            break

        filtered_recipes = recipes

        if choice == '1':
            pass  # όλες οι συνταγές

        elif choice == '2':
            categories = unique_categories(recipes)
            print("\nΔιαθέσιμες κατηγορίες:")
            for i, cat in enumerate(categories, 1):
                print(f"{i}. {cat}")
            cat_choice = input("Επίλεξε κατηγορία ή 'q' για ακύρωση: ")
            if cat_choice == 'q':
                continue
            if not cat_choice.isdigit() or int(cat_choice) < 1 or int(cat_choice) > len(categories):
                print("Μη έγκυρη επιλογή κατηγορίας.")
                continue
            selected_category = categories[int(cat_choice) - 1]
            filtered_recipes = filter_recipes_by_category(recipes, selected_category)

        elif choice == '3':
            difficulties = unique_difficulties(recipes)
            print("\nΔιαθέσιμες δυσκολίες:")
            for i, diff in enumerate(difficulties, 1):
                print(f"{i}. {diff}")
            diff_choice = input("Επίλεξε δυσκολία ή 'q' για ακύρωση: ")
            if diff_choice == 'q':
                continue
            if not diff_choice.isdigit() or int(diff_choice) < 1 or int(diff_choice) > len(difficulties):
                print("Μη έγκυρη επιλογή δυσκολίας.")
                continue
            selected_difficulty = difficulties[int(diff_choice) - 1]
            filtered_recipes = filter_recipes_by_difficulty(recipes, selected_difficulty)

        elif choice == '4':
            print("\nΦίλτρα χρόνου (λεπτά):")
            print("1. Μέχρι 15 λεπτά")
            print("2. Μέχρι 30 λεπτά")
            print("3. Μέχρι 60 λεπτά")
            print("4. Πάνω από 60 λεπτά")
            time_choice = input("Επίλεξε επιλογή ή 'q' για ακύρωση: ")
            if time_choice == 'q':
                continue
            if time_choice == '1':
                filtered_recipes = filter_recipes_by_time(recipes, 15)
            elif time_choice == '2':
                filtered_recipes = filter_recipes_by_time(recipes, 30)
            elif time_choice == '3':
                filtered_recipes = filter_recipes_by_time(recipes, 60)
            elif time_choice == '4':
                filtered_recipes = [r for r in recipes if r["total_time"] > 60]
            else:
                print("Μη έγκυρη επιλογή χρόνου.")
                continue

        elif choice == '5':
            ing_input = input("Δώσε τα υλικά που έχεις (χωρισμένα με κόμμα): ")
            ingredients_list = [ing.strip() for ing in ing_input.split(",") if ing.strip()]
            if not ingredients_list:
                print("Δεν δόθηκαν υλικά για φιλτράρισμα.")
                continue
            filtered_recipes = filter_recipes_by_ingredients(recipes, ingredients_list)

        else:
            print("Μη έγκυρη επιλογή. Προσπάθησε ξανά.")
            continue

        if not filtered_recipes:
            print("Δεν βρέθηκαν συνταγές με αυτά τα κριτήρια.")
            continue

        print("\nΔιαθέσιμες συνταγές:")
        for i, recipe in enumerate(filtered_recipes, 1):
            print(f"{i}. {recipe['name']} (Χρόνος: {recipe['total_time']} λεπτά)")

        rec_choice = input("Επίλεξε τον αριθμό της συνταγής ή 'q' για επιστροφή: ")
        if rec_choice == 'q':
            continue
        if not rec_choice.isdigit() or int(rec_choice) < 1 or int(rec_choice) > len(filtered_recipes):
            print("Μη έγκυρη επιλογή συνταγής.")
            continue

        selected = filtered_recipes[int(rec_choice) - 1]
        print(f"\n--- {selected['name']} ---")
        show_ingredients(selected['ingredients'])
        show_steps(selected['steps'])

        proceed = input("\nΘες να δεις άλλη συνταγή; (ναι/όχι): ")
        if proceed.strip().lower() not in ['ναι', 'ν', 'yes', 'y']:
            print("Έξοδος από το πρόγραμμα. Καλή όρεξη!")
            break

if __name__ == "__main__":
    main()

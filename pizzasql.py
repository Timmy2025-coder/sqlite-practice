import sqlite3 as sql
#functions 
def choose_option():
    print ( "1. Show ingerdients \n" \
                        "2. Search for pizza \n" \
                        "3. Id of a pizza \n" \
                        "4. Base \n" \
                        "5. Exit\n")
    return input("Enter your choice: ")

def show_ingredients():

    ingredient_on = input("Enter pizza_id (or type 'skip' to show all): ")
    if ingredient_on.isdigit():   
        ingredient_on = int(ingredient_on)
        if ingredient_on > 0:
            with sql.connect('pizza.db') as db:
                cursor = db.cursor()
                cursor.execute("SELECT * FROM Ingredients WHERE pizza_id = ?", (ingredient_on,))
                results = cursor.fetchall()
                for ingredient in results:
                    print(f'Ingedients: {ingredient[2]}             Calories: {ingredient[3]}')
    if str(ingredient_on).lower() == "skip":
        with sql.connect('pizza.db') as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM Ingredients")
            results = cursor.fetchall()
            for ingredient in results:
                print(f'Ingedients: {ingredient[2]}                 Calories: {ingredient[3]}')
    elif not str(ingredient_on).isdigit():
        print("Please enter a valid number.")
        return
        
def show_pizza():
    pizza_name = input("Enter pizza name (or type 'skip' to show all): ")
    if pizza_name:
        with sql.connect('pizza.db') as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM pizza WHERE pizza_name = ?", (pizza_name,))
            results = cursor.fetchall()
            if results:
                for pizza in results:
                    print(f"Pizza_id: {pizza[0]}, " \
                          f"Pizza name: {pizza[1]}")
            else:
                print("No pizza found with that name.")
    elif pizza_name.lower() == "skip":
        with sql.connect('pizza.db') as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM pizza")
            results = cursor.fetchall()
            for pizza in results:
                print(f" Pizza_id: {pizza[0]}, " \
                      f"Pizza name: {pizza[1]}")

def show_id():
    pizza_id = input("Enter pizza id (or type 'skip' to show all): ")
    if pizza_id.isdigit():
        pizza_id = int(pizza_id)
        with sql.connect('pizza.db') as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM pizza WHERE pizza_id = ?", (pizza_id,))
            results = cursor.fetchall()
            if results:
                for pizza in results:
                    print(f"Pizza_id: {pizza[0]}, " \
                          f"Pizza name: {pizza[1]}")
            else:
                print("No pizza found with that id.")
    elif str(pizza_id).lower() == "skip":
        with sql.connect('pizza.db') as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM pizza")
            results = cursor.fetchall()
            for pizza in results:
                print(f" Pizza_id: {pizza[0]}, " \
                      f"Pizza name: {pizza[1]}")
    else:
        print("Please enter a valid number.")

def show_base():
    if input("Do you want to see all bases? (yes/no): ").lower() == "yes":
        with sql.connect('pizza.db') as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM Base")
            results = cursor.fetchall()
            for base in results:
                print(f"Base_id: {base[0]}, " \
                      f"Base name: {base[2]}")
    elif input("Do you want to search for a specific base? (yes/no): ").lower() == "yes":
        base_id = input("Enter base id (or type 'skip' to show all): ")
        if base_id.isdigit():
            base_id = int(base_id)
            with sql.connect('pizza.db') as db:
                cursor = db.cursor()
                cursor.execute("SELECT * FROM Base WHERE base_id = ?", (base_id,))
                results = cursor.fetchall()
                if results:
                    for base in results:
                        print(f"Base_id: {base[0]}, " \
                              f"Base name: {base[2]}")
                else:
                    print("No base found with that id.")
        elif str(base_id).lower() == "skip":

            with sql.connect('pizza.db') as db:
                cursor = db.cursor()
                cursor.execute("SELECT * FROM Base")
                results = cursor.fetchall()
                for base in results:
                    print(f"Base_id: {base[0]}, " \
                        f"Base name: {base[2]}")

def exit_program():
    print("Exiting the program.")
    exit()




# if statements  
if __name__ == "__main__":
    choice = choose_option()
    if choice == "1":
        show_ingredients()
    if choice == "2":
        show_pizza()
    if choice == "3":
        show_id()
    if choice == "4":
        show_base()
    if choice == "5":
        exit_program()
    elif not choice.isdigit() and 0 < int(choice) > 5:
        print("Invalid choice. Please try again.")




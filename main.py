from utils import get_valid_soldier_id
from soldier_manager import add_soldier, remove_soldier, view_all_sildiers
from menus import show_main_menu, show_management_soldiers_menu

def main():
    no_exit_main = True
    while no_exit_main:
        show_main_menu()
        user_choice = get_user_choice(2)
        match user_choice:
            case "1":
                handle_soldiers_menu()
            case "0":
                no_exit_main = False

def handle_soldiers_menu():
    no_exit_managment_soldiers = True
    while no_exit_managment_soldiers:
        show_management_soldiers_menu()
        user_choice = get_user_choice(3)
        match user_choice:
            case "1":
                handle_add_soldier()
            case "2":
                handle_remove_soldier()
            case "3":
                view_all_sildiers()
            case "0":
                no_exit_managment_soldiers = False

def get_user_choice(num_options):
    options = [str(num) for num in range(num_options+1)]
    user_choice = input("Enter your choice: ")
    while user_choice not in options:
         print(f"Error: enter numbers from 0 to {num_options}")
         user_choice = input("Enter your choice: ")
    return user_choice

def handle_add_soldier():
    soldier_id = get_valid_soldier_id() 
    name = input("Enter soldier name: ")
    try:
        add_soldier(soldier_id,name)
        print("Soldier added successfully")
    except ValueError as e:
        print(f"Error: {e}")    

def handle_remove_soldier():
    sooldier_id = get_valid_soldier_id()
    try:
        remove_soldier(sooldier_id)
        print("Soldier removed successfully")
    except KeyError as e:
        print(f"Error: {e}")    


main()
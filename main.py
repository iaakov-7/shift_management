from utils import get_valid_soldier_id
from soldier_manager import add_soldier, remove_soldier, view_all_sildiers
from menus import show_main_menu, show_management_soldiers_menu, show_management_duteis_menu
from duty_manager import add_duty_to_soldier,update_duty_status
def main():
    no_exit_main = True
    while no_exit_main:
        show_main_menu()
        user_choice = get_user_choice(2)
        match user_choice:
            case "1":
                handle_soldiers_menu()
            case "2":
                handle_duties_menu()    
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

def handle_duties_menu():
    no_exit_managment_duties = True
    while no_exit_managment_duties:
        show_management_duteis_menu()
        user_choice = get_user_choice(3)
        match user_choice:
            case "1":
                handle_add_duty()
            case "2":
                handle_update_duty_status()
            case "3":
                pass
            case "0":
                no_exit_managment_duties = False

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

def handle_add_duty():
    soldier_id = get_valid_soldier_id()
    duty_name = input("Enter duty name: ")  
    day = input("Enter day: ")
    try:
        add_duty_to_soldier(soldier_id,duty_name,day)
        print("Duty added successfully")
    except (ValueError,KeyError) as e:
        print(f"Error: {e}")    

def handle_update_duty_status():
   soldier_id = get_valid_soldier_id()
   duty_name = input("Enter duty name: ")
   new_status = input("Enter new status: ")
   try:
       update_duty_status(soldier_id,duty_name,new_status)
       print("Status updated succefully")
   except (KeyError,ValueError) as e:
       print(f"Error: {e}")

main()
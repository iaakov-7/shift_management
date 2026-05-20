from utils import get_valid_soldier_id
from soldier_manager import add_soldier, remove_soldier


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
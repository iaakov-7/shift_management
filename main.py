from utils import get_valid_soldier_id
from soldier_manager import add_soldier


def handle_add_soldier():
    soldier_id = get_valid_soldier_id() 
    name = input("Enter soldier name: ")
    try:
        add_soldier(soldier_id,name)
        print("The soldier added successfully")
    except ValueError as e:
        print(f"Error: {e}")    


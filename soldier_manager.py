from data import all_soldiers
from utils import find_soldier_by_id, is_valid_name


def add_soldier(soldier_id,name):
    if find_soldier_by_id(soldier_id):
        raise ValueError(f"Soldier with ID: {soldier_id} already exists in the system") 
    
    if not is_valid_name(name):
        raise ValueError(f"Soldier name cannot be shorter than 2 letters")
    
    new_soldier = {"id":soldier_id, "name":name, "duties":[] }
    all_soldiers.append(new_soldier)

def remove_soldier(soldier_id):
    soldier_dict = find_soldier_by_id(soldier_id)
    if not soldier_dict:
        raise KeyError(f"Soldier with ID: {soldier_id} not exists in the system")
    
    all_soldiers.remove(soldier_dict)

def view_all_sildiers():
    if not all_soldiers:
        print("There are no soldires in the system")
    else:
        for soldier in all_soldiers:
            print(soldier)    
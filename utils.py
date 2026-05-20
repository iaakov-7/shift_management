from data import all_soldiers

def get_valid_soldier_id():
    soldier_id = 0
    is_invalid = True
    while is_invalid:
        try:
            soldier_id = int(input("Enter soldier ID: "))
            is_invalid = False
        except ValueError:
            print("Error: please enter numbers only!")
    return soldier_id

def find_soldier_by_id(soldier_id):
    if not all_soldiers:
        return None
    for soldier in all_soldiers:
        if soldier["id"] == soldier_id:
            return soldier
    return None    

def is_valid_name(name):
    name = name.strip()        
    if len(name) < 2:
        return False
    return True
    

if __name__ == "__main__":
    is_valid_name("      yyy jjj")             

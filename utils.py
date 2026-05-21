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

def find_duty_by_name(duties,duty_name):
    for duty in duties:
        if duty["name"] == duty_name:
            return duty
    return None

def is_valid_name(name):
    name = name.strip()        
    if len(name) < 2:
        return False
    return True

def is_valid_day(day):
    valid_days = ["sunday", "monday", "tuesday", "wednesday", "thursday"]
    return day in valid_days

def is_valid_status(status):
    valid_statuses = ["pending","completed","missed"]
    return status in valid_statuses

if __name__ == "__main__":
    pass            

from utils import find_soldier_by_id, find_duty_by_name, is_valid_day, is_valid_status


def add_duty_to_soldier(soldier_id, duty_name, day):
    soldier_dict = find_soldier_by_id(soldier_id)
    if not soldier_dict:
        raise KeyError(f"Soldier with ID: {soldier_id} not exists in the system")
    if find_duty_by_name(soldier_dict["duties"],duty_name):
        raise ValueError("Duty already exists") 
    if not is_valid_day(day):
        raise ValueError("Day must be between Sunday and Thursday")

    soldier_dict["duties"].append({"name":duty_name, "day":day, "status":"pending"}) 

def update_duty_status(soldier_id, duty_name, new_status):
    soldier_dict = find_soldier_by_id(soldier_id)
    if not soldier_dict:
        raise KeyError(f"Soldier with ID: {soldier_id} not exists in the system")
    soldier_duty =  find_duty_by_name(soldier_dict["duties"],duty_name)       
    if not soldier_duty:
        raise KeyError("Duty not exists")
    if not is_valid_status(new_status):
        raise ValueError("Status should be pending/completed/missed")
    soldier_duty["status"] = new_status
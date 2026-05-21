from utils import find_soldier_by_id, find_duty_by_name, is_valid_day


def add_duty_to_soldier(soldier_id, duty_name, day):
    soldier_dict = find_soldier_by_id(soldier_id)
    if not soldier_dict:
        raise KeyError(f"Soldier with ID: {soldier_id} not exists in the system")
    if find_duty_by_name(soldier_dict["duties"],duty_name):
        raise ValueError("Duty already exists") 
    if not is_valid_day(day):
        raise ValueError("Day must be between Sunday and Thursday")

    soldier_dict["duties"].append({"name":duty_name, "day":day, "status":"pending"})    

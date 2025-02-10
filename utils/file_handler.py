import re, os

def extract_car_regs(file_name):
    file_path = os.path.join(os.getcwd(), "data", file_name)
    # UK car reg pattern 
    reg_pattern = r'\b[A-Z]{1,2}\d{1,2}\s?[A-Z]{3}\b|\b[A-Z]{1,2}\d{1,4}\b'
    
    with open(file_path, 'r') as file:
        content = file.read()
    
    reg_numbers = re.findall(reg_pattern, content)
    
    return reg_numbers

def get_vehicle_data_row(file_name, reg_number):
    file_path = os.path.join(os.getcwd(), "data", file_name)
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(',')  
            if data[0] == reg_number: 
                return data
    return None 
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Rebecca
#               Miranda
#               Maximus
#               Kevin
# Section:      578
# Assignment:   Lab 11 (e.g. Lab 1b-2)
# Date:         5 Nov 2024
#

##comment for grade
import re

# Define the required fields and optional fields
REQUIRED_FIELDS = {'byr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}  # cid is required
OPTIONAL_FIELDS = {'iyr'}  # iyr is optional

# Helper functions to validate field values
def is_valid_byr(byr):
    return 1920 <= int(byr) <= 2008 if byr.isdigit() and len(byr) == 4 else False

def is_valid_eyr(eyr):
    return 2024 <= int(eyr) <= 2034 if eyr.isdigit() and len(eyr) == 4 else False

def is_valid_hgt(hgt):
    match = re.match(r'^(?P<value>\d+)(?P<unit>cm|in)$', hgt)
    if not match:
        return False
    value, unit = int(match.group('value')), match.group('unit')
    if unit == 'cm':
        return 150 <= value <= 193
    elif unit == 'in':
        return 59 <= value <= 76
    return False

def is_valid_hcl(hcl):
    return bool(re.match(r'^#[0-9a-f]{6}$', hcl))

def is_valid_ecl(ecl):
    return ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def is_valid_pid(pid):
    return bool(re.match(r'^\d{9}$', pid))

def is_valid_cid(cid):
    return bool(re.match(r'^\d{3}$', cid)) and cid[0] != '0'  # No leading zeros

# Function to check if a passport is valid based on the rules
def is_valid_passport(passport_data):
    fields = passport_data.split()
    field_dict = {field.split(":")[0]: field.split(":")[1] for field in fields}
    
    # Check if required fields are present
    if not REQUIRED_FIELDS.issubset(field_dict.keys()):
        return False
    
    # Validate each field value according to its specific rule
    if not is_valid_byr(field_dict['byr']):
        return False
    if not is_valid_eyr(field_dict['eyr']):
        return False
    if not is_valid_hgt(field_dict['hgt']):
        return False
    if not is_valid_hcl(field_dict['hcl']):
        return False
    if not is_valid_ecl(field_dict['ecl']):
        return False
    if not is_valid_pid(field_dict['pid']):
        return False
    if not is_valid_cid(field_dict['cid']):
        return False
    
    # If all validations pass, return True
    return True

# Function to process the file
def process_passports(filename):
    with open(filename, 'r') as file:
        # Read the whole file content
        data = file.read().strip()
        
        # Split the data by blank lines to get individual passport data
        passports = data.split('\n\n')

        valid_passports = []
        
        for passport in passports:
            if is_valid_passport(passport):
                valid_passports.append(passport.strip())
        
        return valid_passports

# Main function to drive the program
def main():
    # Get the filename from the user
    filename = input("Enter the name of the file: ").strip()

    # Process the passports and get the valid ones
    valid_passports = process_passports(filename)
    
    # Print the number of valid passports
    print(f"There are {len(valid_passports)} valid passports")
    
    # Write the valid passports to a new file
    with open('valid_passports2.txt', 'w') as outfile:
        # Join the valid passports with a blank line between them
        outfile.write('\n\n'.join(valid_passports))

if __name__ == "__main__":
    main()
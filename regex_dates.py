import re

# Define the regex pattern for YYYY-MM-DD
p1 = r'(\d{4})-(\d{2})-(\d{2})'

# Define a function to convert YYYY-MM-DD to DD/MM/YYYY
def convert_date_format(match):
    year, month, day = match.groups()
    return f'{day}/{month}/{year}'

# Example date string
date_string = '2021-02-21 2024/78/77 16/09/2024'

# Perform the substitution using the custom function
converted_date_string = re.sub(p1, convert_date_format, date_string)

print("Original String:", date_string)
print("Converted String:", converted_date_string)

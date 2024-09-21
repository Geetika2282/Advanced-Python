import json

cont = {}

total = int(input("Enter the num of contacts: "))

for i in range(total):
    value = {}

    value['name'] = input("Enter the name: ")
    value['phNo'] = int(input("Enter the phone number: "))
    value['mail'] = input("Enter the email_id: ")

    cont[i+1] = value

print(cont)

with open('contact_details.json', 'w') as file:
    json.dump(cont, file)
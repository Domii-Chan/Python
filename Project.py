import os
import re

class Person:
    def __init__(self, first, last, age, phone_number):
        self.first = first
        self.last = last
        self.age = age
        self.phone_number = phone_number

    def full_name(self):
        return f'{self.first} {self.last}'

    def __str__(self):
        return f"{self.first} {self.last} : {self.age} : {self.phone_number}"

contacts = list()
znaky = re.compile("[@._!#$%^&*+()<>?/\|}{~:,-]")

if os.path.isfile("pojistenci.csv"):
    with open("pojistenci.csv") as f:
        csv_list = f.readlines()
        for contact_line in csv_list:
            contact_data = contact_line.rstrip().split(",")
            contact = Person(contact_data[0],
                             contact_data[1], 
                             contact_data[2],
                             contact_data[3])
            contacts.append(contact)
        
users_input = ""



print("Vítejte v naší pojišťovací aplikaci")

while users_input != "q":
    print("Výběr Možností")
    print("1 - Vytvořit pojištěnce")
    print("2 - Zobrazit všechny pojištěnce")
    print("3 - Vyhledat daného pojištěnce")
    print("q - Ukončit Aplikaci")
    users_input = input("Vyberte možnost: ")
    
    if users_input == "1":
        
        print("Vložte prosím informace o pojištěnci")
        while True:
            first_name =input("Jméno = ")
            if any(map(str.isdigit, first_name)):
                print("Jméno nesmí obsahovat číslice")
            elif (znaky.search(first_name) != None):
                print("Jméno nesmí obsahovat speciální znaky")
            elif first_name.strip() == "":
                print("Prosím vyplntě pole")
            else:
                break
        while True:
            last_name = input("Příjmení = ")
            if any(map(str.isdigit, last_name)):
                print("Příjmení nesmí obsahovat číslice")
            elif (znaky.search(last_name) != None):
                print("Příjmení nesmí obsahovat speciální znaky")
            elif last_name.strip() == "":
                print("Prosím vyplntě pole")
            else:
                break              
        while True:
            age = input("Věk = ")
            if any(map(str.isalpha, age)):
                print("Pole nesmí obsahovat písmena")
            elif (znaky.search(age) != None):
                print("Pole nesmí obsahovat speciální znaky")
            elif age.strip() == "":
                print("Prosím vyplntě pole")
            else:
                break
        while True:
            phone_number = input("Telefonní číslo = ")
            if any(map(str.isalpha, phone_number)):
                print("Pole nesmí obsahovat písmena")
            elif (znaky.search(phone_number) != None):
                print("Pole nesmí obsahovat speciální znaky")
            elif phone_number.strip() == "":
                print("Prosím vyplntě pole")
            else:
                break
        our_contact = Person(first_name, last_name, age, phone_number)
        contacts.append(our_contact)
        print("Děkujeme, pojištěnec byl úspěšně vytvořen")
             
    elif users_input == "2":
        for contact in contacts:
            print(contact)
        input("Všichni pojištěnci zobrazeni, zmáčkněte enter pro pokračování")
    elif users_input == "3":
        to_lookup = input("Pro vyhledání zadejte jméno pojištěnce\n")
        for contact in contacts:
            if to_lookup in contact.full_name():
                print(contact)
            else:
                print("Uživatel nenalazen")

    elif users_input.lower() == "q":
        break

with open("pojistenci.csv", "w") as f:
    for contact in contacts:
        f.write(f"{contact.first},{contact.last},{contact.age},{contact.phone_number}\n")

print("Děkujeme za použití naší pojišťovací aplikace")
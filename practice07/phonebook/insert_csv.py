import csv
from insert import insert_many_users

def insert_from_csv(filename):

    users = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        

        for row in reader:
            name = row["name"]
            phone = row["phone"]

            users.append((name, phone))

    insert_many_users(users)

        
if __name__ == '__main__':
    insert_from_csv('./practice07/phonebook/contacts.csv')

import csv

def load_contacts(filename):
    contacts = {} 
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file) 
        for row in reader:
            
            first_name = row[0]
            LastName = row[1]
            phone_number = row[2]
            email = row[3]
            contacts[LastName] = [first_name+ ' ' + LastName, phone_number, email]
    return contacts 

def display_contact_input(contactinfo):
    if contactinfo:
        new_func(contactinfo)
        
        print(f'Phone Number: {contactinfo[1]}')
        print(f'Email: {contactinfo[2]}')
        
    else:
        print('No user found')
    main()

def new_func(contactinfo):
    print('\nContact Information:')
    print(f'First Name: {contactinfo[0]}')

def main():
    filename = 'diccsv.csv'
    contacts = load_contacts(filename)
    lastname = input('Please enter a last name you want to look up: ').strip() #.strip is used to delete any unwanted spaces
    contactinfo = contacts.get(lastname)
    display_contact_input(contactinfo)
if __name__ == '__main__':
    main()
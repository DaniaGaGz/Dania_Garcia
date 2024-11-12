import csv 

def vehicular_accidents(filename):
    accidents = {} 
    with open(filename, 'rt') as file:
        a = csv.reader(file)
        next(a) 
        for row in a:
            year = row[0]
            fatalities = row[1]
            injuries = row[2]
            crashes = row[3]
            f_cr = row[4]
            daf_cr = row[5]
            phone_use_fcr = row[6]
            speed_cr = row[7]
            influence_cr = row[8]
            ill_cr = row[9]
            accidents[year] = [fatalities, injuries, crashes, f_cr, daf_cr, phone_use_fcr, speed_cr, influence_cr, ill_cr]
    return accidents 

def menu():
    year = input('Enter year: ')
    file = 'accidents.csv'
    b = vehicular_accidents(file)

    
    while True:
        print("\nMenu:")
        print ("0. Year")
        print("1. Fatalities")
        print("2. Injuries")
        print("3. Crashes")
        print("4. Fatal Crashes")
        print("5. Distraction Affected Fatal Crashes")
        print("6. Fatal Crashes involving Cell Phone Use")
        print("7. Fatal Crashes involving Excessive Speed")
        print("8. Fatal Crashes while Driving under the Influence")
        print("9. Fatal Crashes involving Fatigue or Illness") 
        print("10. Exit")
        
        choice = input("Enter your choice: ")

        if year in b: 
            if choice == "0":
                year = input('Misspell? try again with new year: ')
            elif choice == "1":
                print(f'Fatalities from year {year}: {b[year][0]}')
                year = input('Enter year: ')
            elif choice == "2":
                print(f'Injuries from year {year}: {b[year][1]}')
                year = input('Enter year: ')
            elif choice == "3":
                print(f'Crashes from year {year}: {b[year][2]}')
                year = input('Enter year: ')
            elif choice == "4":
                print(f'Fatal Crashes from year {year}: {b[year][3]}')
                year = input('Enter year: ')
            elif choice == "5":
                print(f'Distraction Affected Fatal Crashes from year {year}: {b[year][4]}')
                year = input('Enter year: ')
            elif choice == "6":
                print(f"Fatal Crashes involving Cell Phone Use from year {year}: {b[year][5]}")
                year = input('Enter year: ')
            elif choice == "7":
                print(f'Fatal Crashes involving Excessive Speed from year {year}: {b[year][6]}')
                year = input('Enter year: ')
            elif choice == "8":
                print(f'Fatal Crashes while Driving under the Influence from year {year}: {b[year][7]}')
                year = input('Enter year: ')
            elif choice == "9": 
                print(f'Fatal Crashes involving Fatigue or Illness from year {year}: {b[year][8]}')
                year = input('Enter year: ')
            elif choice == "10":
                print(f'See you next time!')
                break
            else:
                print('Not in menu, try again')
                year = input('Enter year: ')
        else:
            print("No files from that year, try again")
            menu()
                

menu()
vehicles = {
        # VIN: [year, manufacturer, model, color, eng_design, eng_displace]
        "1J4GL48K4UF993861": [2002, "Jeep", "Liberty", "blue", "V6", 3.7],
        "1YVGF22C8AN381568": [2002, "Mazda", "626", "white", "I4", 2.0],
        "WP0AA0926HG410293": [1987, "Porsche", "924S", "red", "I4", 2.5],
        "5TDZA23CXTU102983": [2006, "Toyota", "Sienna", "gold", "V6", 3.3],
        "1GKKVRED5ZL382610": [2011, "GMC", "Acadia", "charcoal", "V6", 3.5],
        "2T3BF4DV9QR146782": [2012, "Toyota", "RAV 4", "green", "I4", 2.5]
        }

#Create a function defined as main()
#Ask the user for a vehicle identification number (VIN)
#Check if the vin is a key that is in the vehicles dictionary using an if/else conditional statement          
#Find the data for the vehicle that the user wants
#Print the data in an understandable output
#If the VIN doesn't exists, print a message stating that the VIN entered by the user is not in the dictionary
#To control code execution, finish you program by calling the main function like this:
def main():
    vin = input('''Please enter the Vehicle's id number: ''')
 
    if vin in vehicles:
        vin_info = vehicles[vin]
        print(f'Info for {vin}\n')
        print(f'Year: {vin_info[0]}')
        print(f'Manufacturer: {vin_info[1]}')
        print(f'Model: {vin_info[2]}')
        print(f'Color: {vin_info[3]}')
        print(f'Engine Design: {vin_info[4]}')
        print(f'Engine Displace: {vin_info[5]}')
    else:
        print('Not found')

if __name__ == "__main__":
    main()

#In the main function, print the product name, quantity, and price and sum all the items into a subtotal. 
#Then print the total amount of items purchased, the subtotal, the tax (6%), and the total.
#Then ask for the payment with an input and calculate the change the customer needs to get back if they pay more than the total.
# Finally, print a thank you message, and the current date and time.
import csv 
from datetime import datetime
def read_prod(file):
    products = {}
    
    with open(file, mode='r', newline ='') as file:
        reader = csv.reader(file) 
        next(reader)
        for row in reader:
            key = row[0]
            prod_desc = row[1]
            price = row[2]
            products[key] = [prod_desc,price]
        return products 
            
read_prod('products.csv')

def read_request(file):
    product_ids = []
    quantities = []

    with open(file, 'rt') as csv_request:
        reader = csv.reader(csv_request)
        next(csv_request)
        for row in reader: 
            product_ids.append(row[0])
            quantities.append(row[1])
        return product_ids, quantities
    
def main():
    products = read_prod('products.csv')
    order_ids = read_request('request.csv')[0]
    quantities = read_request('request.csv')[1]
    print(order_ids)
    print('mini super python')
    print()
    subtotal = 0
    total_items= 0
    for i in range(len(order_ids)):
        product = products[order_ids[i]]
        name = product[0]
        price = float(product[1])
        quantity = float(quantities[i])
        print(f'{name}: {quantity} @ {price}')
        subtotal += price * (quantity)
        total_items += quantity

    print()
    print(f'Subtotal: ${subtotal:.2f}')
    print(f'Total Items: {int(total_items)}')
    print(f'Tax: ${subtotal*0.06:.2f}')
    print(f'Total: ${subtotal * 1.06:.2f}')

    print()
    payment = float(input('Payment: $'))
    change = payment - (subtotal * 1.06)

    if change>0:
        print(f'Your change is: ${change:.2f},\n Thanks for your purchase')
        current_data = datetime.now()
        print(f'{current_data: %c}')

    elif change < subtotal:
        while True:
            print('Not enough money')
            break

main()
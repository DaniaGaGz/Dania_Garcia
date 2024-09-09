

def area_square():
    size = int(input('How long is the base of the square?'))
    area_of_square = size*size
    print(f'the area of the square was {area_of_square}')

area_square()

def trig():
    base = int(input('What is the base of your triangle? '))
    altura = int(input('What is the height of your triangle? '))
    area_of_trig = int((base*altura)/2)
    print(f'The area of your triangle was {area_of_trig}')

trig()
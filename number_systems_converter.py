def is_valid(value):
    """function that is checking if the given value is a number"""
    flag = False
    for el in value:
        if el.isdigit() or el in 'ABCDEFabcdef':
            flag = True
        while not el.isdigit() and el not in 'ABCDEFabcdef':
            value = input('Please enter a number: ')
            flag = False
    if flag:
        return value

def convert(number, base):
    """function to convert a number to others number systems"""
    dec = int(number, int(base))
    if dec:
        return bin(dec), oct(dec), int(dec), hex(dec)

def main():
    """main function"""
    number, base = is_valid(input('Enter here a number to convert: ')), is_valid(input('Enter here base of the number: '))
    while not base.isdigit():
        base = is_valid(input('Please, enter a number: '))
    print()
    b, o, d, h = convert(number, base)
    print(f'Binary: {str(b)[2:]}\nOctal: {str(o)[2:]}\nDecimal: {d}\nHexadecimal: {str(h)[2:]}')

main()
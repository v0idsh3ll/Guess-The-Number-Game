import random

CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+`-=№;%:?"

def is_valid(value):
    """function that is checking if the values is valid"""
    if value.isdigit() or value == '':
        return value
    else:
        return False

def params():
    """getting parameters"""
    quantity = False
    length = False
    while not quantity or not length:
        quantity = is_valid(input('Enter passwords quantity to generate: '))
        length = is_valid(input('Enter every password length to generate: '))
    if quantity and length:
        return int(quantity), int(length)
    else:
        return None

def generate_password(length):
    """generate a password"""
    result = []
    for _ in range(length):
        result.append(random.choice(CHARS))
    return "".join(result)

print("Hello! It's password generator program. Press <ENTER> for quit")

def main():
    """main function"""
    quantity, length = ' ', ' '
    while quantity != '' and length != '':
        quantity, length = params()
        if quantity and length:
            for _ in range(quantity):
                print(generate_password(length))
            print('\n', '\n', '\n')

main()
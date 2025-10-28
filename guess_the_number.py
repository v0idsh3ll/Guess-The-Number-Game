import random

def is_valid(number):
     """function that is checking if the number is valid"""
     if str(number).isdigit():
         if int(number) >= 1 and int(number) <= 100:
             return int(number)
         else:
             return False
     else:
        return False

def inputing():
    """function to get the number"""
    num = input("Type here your number: ")
    while not is_valid(num):
        print("You should type a number is bigger than 1 and smaller than 100")
        num = input("Type here your number: ")
    if is_valid(num):
        return int(num)

def game():
    """main function"""
    number = random.randint(1, 100)
    attempt = 0
    counter = 0
    while attempt != number:
        counter += 1
        attempt = inputing()
        if attempt < number:
            print('Wished number is bigger than yours')
        elif attempt > number:
            print('Wished number is smaller than yours')
        else:
            print(f"You've guessed the number, congratulations! You did it in {counter} attempts", "\n", "\n", "\n" 'New number have been generated, try to guess it!')

while True:
    game()
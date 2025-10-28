EN_UP_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
EN_LOW_CHARS = 'abcdefghijklmnopqrstuvwxyz'
RU_UP_CHARS = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
RU_LOW_CHARS = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
ALL_CHARS = EN_UP_CHARS + EN_LOW_CHARS + RU_UP_CHARS + RU_LOW_CHARS

def alphabet():
    language = input("Type here the language to encrypt/decrypt \n1 = en (default), 2 = ru\n")
    while language not in ('1', '2', ''):
        language = input("Please press 1, 2, or <ENTER>\n")
    if language in ('1', ''):
        return 'english', EN_LOW_CHARS, EN_UP_CHARS
    else:
        return 'russian', RU_LOW_CHARS, RU_UP_CHARS

def value(lang):
    while True:
        val = input(f'Enter the text (letters only in {lang}): ')
        if all(ch in ALL_CHARS or not ch in ALL_CHARS for ch in val):
            return val
        print("Invalid input, try again.")

def shift1():
    while True:
        s = input('Enter the shift: ')
        if s.isdigit():
            return int(s)
        print("Shift must be a number.")

def parameters():
    lang, alphabet_low, alphabet_up = alphabet()
    text = value(lang)
    shift = shift1()
    return text, shift, alphabet_low, alphabet_up

def encrypt():
    text, shift, alphabet_low, alphabet_up = parameters()
    result = ''
    for e in text:
        if e.isupper():
            result += alphabet_up[(alphabet_up.index(e) + shift) % len(alphabet_up)]
        elif e.islower():
            result += alphabet_low[(alphabet_low.index(e) + shift) % len(alphabet_low)]
        else:
            result += e
    return result

def decrypt():
    text, shift, alphabet_low, alphabet_up = parameters()
    result = ''
    for e in text:
        if e.isupper():
            result += alphabet_up[(alphabet_up.index(e) - shift) % len(alphabet_up)]
        elif e.islower():
            result += alphabet_low[(alphabet_low.index(e) - shift) % len(alphabet_low)]
        else:
            result += e
    return result

def main():
    choice = ''
    while choice != 'e' and choice != 'd':
        choice = input('Encrypt (e) or decrypt (d): ')
    if choice == 'e':
        print(encrypt(), '\n')
    else:
        print(decrypt(), '\n')

while True:
    main()
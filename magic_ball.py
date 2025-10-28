import random

answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don’t count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

def greeting():
    print("Hello, I am the magic ball. I answer any question you ask.")
    name = input("What's your name? \n")
    print(f"okay, {name}. Ask any questions you want. If you want to end the dialog, just press <ENTER>")

def asking():
    question = input()
    answer = random.choice(answers)
    if answer:
        return answer, question

def main():
    total = 0
    question = ' '
    while question != '':
        answer, question = asking()
        total += 1
        if question == '':
            break
        print(answer, f'Questions asked: {total}', sep = '\n')
        print()

greeting()
main()
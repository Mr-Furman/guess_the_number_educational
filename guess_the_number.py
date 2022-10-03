from asyncore import read
import random

number_which_we_search = random.randint(1, 100)


class Digit_for_game():

    def __init__(self, number:int, life:int, name:str):
        self.number = number
        self.life = life
        self.name = name
        


    def guess_the_number(self) -> None:
        try:
            try:
                try_ = int(input(f'Can yot guess the number?-----'))
                print(number_which_we_search)
            except ValueError:
                print('Need digit')
                self.guess_the_number()

            if try_ != number_which_we_search and self.life != 0:
                self.life = self.life - 1
                print(f'MISS  Your life:{self.life+1}')
                self.guess_the_number()

            elif self.life == 0:
                return print('Looser, try one more')

            elif try_ == number_which_we_search:
                return print('Winner winner chicken dinner')
        except UnboundLocalError:
            pass


    def magic_layer(self) -> None:
        list_of_answer = ['It is certain', 'It is decidedly so.', 'Without a doubt.', 'Yes definitely','You may rely on it.',
                         'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.',
                         'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now', 'Concentrate and ask again.',
                         'Don\'t count on it.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']
        print(f"Hi {self.name}, I'm a magic layer and I know the answer to any question you have.")
        while True:
            quest_for_answer = input('Ask a question:  ')
            print(random.choice(list_of_answer))
            repeat_1 = input('Do you have a one more quest?(+ or -)\n',)
            if repeat_1 == '+':
                continue
            elif repeat_1 == '-':
                print('Good luck')
                return False
            elif repeat_1 != '+' or repeat_1 != '-':
                print('OMG I need + or -')
                print('Bye Bye')
                
            if quest_for_answer.lower() == 'exit' or repeat_1 == 'exit':
                return False
    


   

test = Digit_for_game(3, 7, 'Robert Polson')
test.magic_layer()



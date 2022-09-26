import random

number_which_we_search = random.randint(1, 100)


class Digit_for_game():

    def __init__(self, number:int, life:int):
        self.number = number
        self.life = life
        
        
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


test = Digit_for_game(3, 7)
test.guess_the_number()


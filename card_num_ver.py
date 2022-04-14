import getpass as gp

from numpy import True_
class Card:
    def __init__(self):
        card_num = str(gp.getpass('Input credit card number to validate:    '))
        check_len = True
        while check_len:
            if len(card_num) == 16 or len(card_num) == 15:
                self.card_num = card_num
                check_len = False
            else:
                print('\nCard number needs to by 15 or 16 digits! Try again.\n')
        

first_card = Card()

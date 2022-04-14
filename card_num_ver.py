import getpass as gp
import math

class Card:
    
    card_num = ''

    #keeps the check_len loop running until is changed to False
    check_len = True  
    
    #checks the string lenght of the card is correct either 16 or
    #15 digits for AMEX cards     
    while check_len:
        
        #requests card number using the getpass library
        card_num = str(gp.getpass('Input credit card number to validate:    '))

        #checks if input is of expected length and that it is a number 
        if (len(card_num) > 16 and len(card_num) < 13) or card_num.isdigit() != True:
            
            #if card number is between 13 and 16 digits long, or input is not a digit
            #this message is shown and the loop is restarted to ask for number again.
            print('\nCard number needs to by 15 or 16 digits! Try again.\n')               
        else:

            #if input is valid the While loop is stopped and variable card_num stays
            #as user input to be added as property of the class.
            check_len = False
    
    def __init__(self,card_num=card_num):
        self.card_num = card_num
    
    #checks if credit card number follows luhn algorithm, which is used to verify a card
    #number is a valid number
    def validate(self):
        sec_digits = []
        remain_digits = []
        string_minus_last = self.card_num[:-1]
        for i in string_minus_last[::-2]:
            sec_digits.append(i)
        for d in self.card_num:
            if d not in sec_digits:
                remain_digits.append(d)
        print(sec_digits)
        print(remain_digits)

    
first_card = Card()
print(first_card.card_num)
first_card.validate()

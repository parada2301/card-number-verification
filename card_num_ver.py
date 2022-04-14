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
        new_num = []
        new_num2 = []
        for i in string_minus_last[::-2]:
            sec_digits.append(i)
        for d in self.card_num[::-2]:
            remain_digits.append(d)
            print(remain_digits)
        for s in sec_digits:
            current_num = int(s)*2
            if len(f'{current_num}') == 2:
                first_digit= f'{current_num}'[0]
                second_digit=f'{current_num}'[1]
                current_num = int(first_digit) + int(second_digit)
                new_num.append(current_num)
            else:
                new_num.append(current_num)
        for o in remain_digits:
            new_num2.append(int(o))
        num_sum = sum(new_num)
        num_sum2 = sum(new_num2)
        print(num_sum+num_sum2)
        if (num_sum+num_sum2)%10 == 0:
            return print('\nCard Number is valid!\n')
        else:
            return print('\nCard Number is not valid!\n')


if __name__ == '__main__':    
    first_card = Card()
    print(first_card.card_num)
    first_card.validate()

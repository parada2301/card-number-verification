import getpass as gp

card_num = ''
class Card:
    
    #keeps the check_len loop running until is changed to False
    check_len = True  
    
    #checks the string lenght of the card is correct either 16 or
    #15 digits for AMEX cards     
    while check_len:
        
        #requests card number using the getpass library
        card_num = str(gp.getpass('Input credit card number to validate:    '))

        #checks if input is of expected length and that it is a number 
        if (len(card_num) != 16 and len(card_num) != 15) or card_num.isdigit != True:
            
            #if card number is not 15 or 16 digits long, or input is not a digit
            #this message is shown and the loop is restarted to ask for number again.
            print('\nCard number needs to by 15 or 16 digits! Try again.\n')               
        else:

            #if input is valid the While loop is stopped and variable card_num stays
            #as user input to be added as property of the class.
            check_len = False
    
    #checks if credit card number follows luhn algorithm, which is used to verify a card
    #number is a valid number
    def validate(card_num):
        pass
    def __init__(self):
        self.card_num = card_num
        
                
        

first_card = Card()

import getpass as gp
import psycopg2 as pg2

conn = pg2.connect(database='BIN_database',user=input('Database username    '),password=gp.getpass('Database Password  '))
cur = conn.cursor()

class Card:
    
    def card_numb(self):
        card_num = ''

        #keeps the check_len loop running until is changed to False
        check_len = True  
        
        #checks the string lenght of the card is between 13 and 16 digits    
        while check_len:
            
            #requests card number using the getpass library
            #NOTE: some IDEs or terminals may not show this properly, getpass can be changed 
            #to normal input(), however, this would not hide the card number at input
            
            #input is a string to take advantage of indexing later on        
            card_num = str(gp.getpass('Input credit card number to validate:    '))

            #checks if input is of expected length and that it is a number 
            if (len(card_num) > 16 or len(card_num) < 13) or card_num.isdigit() != True:
                
                #if card number is between 13 and 16 digits long, or input is not a digit
                #this message is shown and the loop is restarted to ask for number again.
                print('\nCard number needs to between 13 and 16 digits! Try again.\n')               
            else:

                #if input is valid the While loop is stopped and variable card_num stays
                #as user input to be added as property of the class.
                check_len = False
                return card_num
    
    #checks if credit card number follows luhn algorithm, which is used to verify a card
    #number is a valid number
    def validate(self):
        sec_digits = []
        remain_digits = []
        string_minus_last = self.card_num[:-1]
        new_num = []
        for string in string_minus_last[::-2]:
            sec_digits.append(string)
        for d in self.card_num[::-2]:
            remain_digits.append(d)
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
            new_num.append(int(o))
        num_sum = sum(new_num)
        if num_sum%10 == 0:
            return True
        else:
            return False

    def networks(self):
        if not self.validate():
            print('\nCard number is not valid\n')
        else:
            searching = True
            tries = 8
            while searching:
                cur.execute(
                    f'''
                    SELECT brand FROM bin_data
                    WHERE bin = {self.card_num[:tries]};
                    '''
                )
                result = cur.fetchone()
                if result == None:
                    tries -= 1
                else:

                    return result[0]

    def check_issuer(self):
        if not self.validate():
            print('\nCard number is not valid\n')
        else:
            searching = True
            tries = 8
            while searching:
                cur.execute(
                    f'''
                    SELECT issuer FROM bin_data
                    WHERE bin = {self.card_num[:tries]};
                    '''
                )
                result = cur.fetchone()
                if result == None:
                    tries -= 1
                else:

                    return result[0]

    def __init__(self):
        self.card_num = self.card_numb()
        self.valid = self.validate()
        self.network = self.networks()
        self.issuer = self.check_issuer()


if __name__ == '__main__':    
    on_off = True
    while on_off:
        first_card = Card()
        print('Card Number ************' + first_card.card_num[-4:])
        print('Card Valid:  ' + f'{first_card.validate()}')
        print(f'{first_card.network}')
        print(f'Card issued by {first_card.issuer}')
        while True:
            i = input('Would you like to check another card number? Y/N    ')
            if i == 'Y' or i == 'y':
                del first_card
                break
            elif i == 'N' or i == 'n':
                raise SystemExit           
            else:
                print('Invalid input.')

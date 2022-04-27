# Card Verification - Python + PostgreSQL 
This project makes use of OOP, basic python code and algorithms, and integration of PostgreSQL queries using the psycopg2 library in python.

The program will allow the user to input their card number to validate that it is a valid number according to Luhns Algorithm, then accesses
a data base where it will able to determine what's the card's network, as well as what company issued the card.

To run this program you must host your own PostgreSQL server locally. Included in this repo there is a .tar file to restore the database and
have the BIN numbers, issuers, and network. 

The information in the data base was found here: https://github.com/iannuttall/binlist-data

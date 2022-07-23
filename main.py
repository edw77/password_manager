import sys
import getpass
import db_connection
import argparse
import hashlib
import db_transactions
import pwd_generator
from db_connection import connect
import encryption
import secret
from tabulate import tabulate

def main():

    parser = argparse.ArgumentParser(description="Password Manager by Edw77", 
    usage="[options]")

    master = secret.get_secret_key()
    pass_input = getpass.getpass('Please enter the Master Password : ').encode()

    if pass_input == b'main':
        connection = db_connection.connect()
        print('Successfully Authenticated')

    else:
        print('Bad Password')
        sys.exit() 

    parser.add_argument("-l", "--list", action="store_true", help="List all entries in password database")
    parser.add_argument("-d", "--delete", type=str, nargs=1, help="Delete entry by URL", metavar=("[URL]")) 
    parser.add_argument("-a", "--add", type=str, nargs=2, help="Add password", metavar=("[URL]", "[USERNAME]")) 
    parser.add_argument("-r", "--random", action="store_true", help="Generate random password") 


    args = parser.parse_args()

    cursor = connection.cursor()

    connection.commit()

    if args.add:
        URL = args.add[0]
        username = args.add[1]
        if args.random:
            print('A random password is being generated')
            password = pwd_generator.password_gen(20)
        else:
            password = getpass.getpass('Please enter the custom password: ').encode()
        
        password_official = encryption.encrypt_password(password)
        
        db_transactions.store_passwords(connection,cursor,password,"",username,URL,"")

        print("\nRecord Added:" + "\n URL: {0}, Username: {1}, Password: {2} (Plaintext Password)".format(URL, username, password))

    if args.list:
        records = db_transactions.get_password_list(cursor)
        print(tabulate(records, headers=['URL', 'Username', 'Password']))
        


main()

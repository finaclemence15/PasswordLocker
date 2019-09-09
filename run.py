#!/usr/bin/env python3.6
from userinfo import Userinfo
from credential import Credential
import random

###########users#################
def create_userinfo(username, password):
    '''
    Function to create a new user
    '''
    new_userinfo = Userinfo(username, password)
    return new_userinfo

def save_userinfo(userinfo):
    '''
    Function to save user
    '''
    userinfo.save_userinfo()
    
def check_existing_userinfo(user_name):
    '''
    Function that check if a user exists with that username and return a Boolean
    '''
    return Userinfo.userinfo_exist(user_name)    
    
    ##### Credential ######
    
def create_credential(cred_username,cred_application,cred_password):
    '''
    Function to create a new contact
    '''
    new_credential = Credential(cred_username,cred_application,cred_password)
    return new_credential    


def save_credential(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()

def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()
    

def find_credential(cred_username):
    '''
    Function that finds a credential by username and returns the credential
    '''
    return Credential.find_by_username(cred_username)


def display_credential():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credential()

def main():
    print("Welcome!")



    print("Please enter one of the following codes to proceed, cc - create a new account, log -if you already have an account, ex - to exit the application ")
    short_code = input().lower()

    if short_code == 'cc':
        print("Create new account")
        print("Username")
        user_name=input()
        print("password")
        password=input()


        save_userinfo(create_userinfo(user_name,password))
        print('\n')
        print(f"Log in details for {user_name}  have been saved")
        print('\n')

        print("Please exit the application to log in to see your credentials")

    elif short_code == 'log':

        print("Fill in the required details")
        print("Enter your user name")
        user_name=input()
        print("Enter your password")
        password=input()
        user_exists = (user_name)
        if user_exists == user_name:
           print(" ")
           print(f'Welcome {user_name}. Please choose an option to continue.')

    else:
        print("User does not exist please create an account first")    
#######################################credentials #############################
    while True:

        print("Welcome")


        print("Please use these short codes to navigate: ac -add credentials, dc -display credentials,dl -delete Credentials, ex -exit the application")
        short_code = input().lower()
        if short_code == 'ac':
            print("Add credentials")
            print("-"*10)
            print("User name..")
            cred_username=input()
            print("Account type...")
            cred_application=input()
            # print("Password,,")
            # password=input()

            print("You can choose to create your password or generate it ,if generate type g if create type c")
            code=input().lower()

            if code == 'c':
                print("Enter your Password")
                cred_password=input()

                # print(f"Password: {Credential.password}"

            elif code =='g':
                s="abcdefghijklmnopqrstuvwxyz0123456789"
                cred_password=''.join(random.choice(s) for _ in range(8))

            else:
                print("Put a valid code")

            save_credential(create_credential(cred_username,cred_application,cred_password))
            print('\n')
            print(f"Credentials Account... \n username: {cred_username} \n Account: {cred_application} \n password: {cred_password}")
            print('\n')
        elif short_code == 'dc':
            if display_credential():
                print("Here is a list of your credentials")
                print('\n')

                for credential in display_credential():
                    print(f" User Name: {credential.cred_username} \n Account Type: {credential.cred_application} \n Password:{credential.cred_password}")
                    print('\n')
            else:
                    print('\n')
                    print("You don't have credentials saved yet")
                    print("\n")

        elif short_code == 'dl':
                print("       Delete Credential")
                print("     "+"="*20)
                print('\n')
                cred_application = input("Enter cred_application Name:")
                found_credential = find_credential(cred_application)
                if found_credential:
                    print(f"Here are the credentials for {found_credential.cred_application}:")
                    print(f"User Account: {found_credential.cred_username}")
                    print(f"Password: {found_credential.cred_password}")
                if    input("Are you sure you want to delete it? (Y/N)").lower() == "Y":
                    del_credential(cred_application)
                    print()
                    print("Press Enter to continue")
                    input(f"Credentials for {found_credential.cred_application} deleted.")
                else:
                    print(f"Credentials Not Found for {cred_application}!")
                    print("Press Enter to continue")
                    input() 
        elif short_code == 'ex':
                print("Exiting the password locker")
                break

        else:

                print("Please use a valid code")


            
        
if __name__ == '__main__':
    main()        
    
#!/usr/bin/env python3.6
from userinfo import Userinfo
from credential import Credential

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
    
def create_credential(username,cred_application,cred_username,cred_password):
    '''
    Function to create a new contact
    '''
    new_credential = Credential(username,cred_application,cred_username,cred_password)
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
    

def find_credential(username):
    '''
    Function that finds a credential by username and returns the credential
    '''
    return Credential.find_by_username(username)


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

    else:
        print("User does not exist please create an account first")        
    
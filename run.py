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
#!/usr/bin/env python3.6
from userinfo import Userinfo
def create_userinfo(username, password):
    '''
    Function to create a new user
    '''
    new_userinfo = Userinfo(username, password)
    return new_userinfo
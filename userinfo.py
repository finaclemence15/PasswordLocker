class Userinfo:
    """
    Class that generates new instances of Userinfo
    """    
    def __init__(self, user_name, password):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            user_name: New userinfo user name.
            password : New userinfo password.
        '''

        self.user_name = user_name
        self.password = password
        
    users_list = [] #empty users list   
 # Init method up here
    def save_userinfo(self):

        '''
        new_userinfo method saves userinfo objects into users_list
        '''

        Userinfo.users_list.append(self)  
        
    @classmethod
    def find_by_user_name(cls,user_name):
        '''
        Method that takes in a number and returns a user that matches that username.

        Args:
            user_name: user_name to search for
        Returns :
            Userinfo of person that matches the user_name.
        '''

        for userinfo in cls.users_list:
            if userinfo.user_name == user_name:
                return userinfo          

    @classmethod
    def userinfo_exist(cls,user_name):
        '''
        Method that checks if a user exists from the users list.
        Args:
            username: username to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for userinfo in cls.users_list:
            if userinfo.user_name == user_name:
                    return True

        return False
    
    @classmethod
    def display_userinfo(cls):
        '''
        method that returns the users list
        '''
        return cls.users_list    
class Credential:
    """
    Class that generates new instances of Userinfo
    """  
    credential_list = []  
    
    def __init__(self,username,cred_application,cred_username,cred_password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            user_name: New credential username.
            cred_application : New credential app.
            cred_username: New credential user name.
            cred_password : New credential passworg.
        '''    
        
      # docstring removed for simplicity

        self.username = username
        self.cred_application = cred_application
        self.cred_username = cred_username
        self.cred_password = cred_password
        
        
               
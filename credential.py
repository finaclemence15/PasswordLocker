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

 # Init method up here
    def save_credential(self):

        '''
        save_credential method saves credential objects into credential_list
        '''

        Credential.credential_list.append(self)  

    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)              
        
               
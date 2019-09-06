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
        
    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a credential that matches that username.

        Args:
            username: username to search for
        Returns :
            Credential of person that matches the username.
        '''

        for credential in cls.credential_list:
            if credential.username == username:
                return credential                
        
    
    @classmethod
    def display_credential(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list        
               
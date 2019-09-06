import unittest 
from credential import Credential

class TestCredential(unittest.TestCase):

    '''
    Test class that defines test cases for the Credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    
    
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("James","facebook","jk","abcd") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.username,"James")
        self.assertEqual(self.new_credential.cred_application,"facebook")
        self.assertEqual(self.new_credential.cred_username,"jk")
        self.assertEqual(self.new_credential.cred_password,"abcd")
        
# setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credential.credential_list = []
            
    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the credential list
        '''
        self.new_credential.save_credential() # saving the new contact
        self.assertEqual(len(Credential.credential_list),1)            
           
         
if __name__ == '__main__':
    unittest.main()        
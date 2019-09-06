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
           
    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credential to check if we can save multiple credential
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("James","facebook","jk","abcd") # new contact
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)
           
    def test_delete_credential(self):
            '''
            test_delete_credential to test if we can remove a credential from our credential list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("James","facebook","jk","abcd") # new contact
            test_credential.save_credential()

            self.new_credential.delete_credentia()# Deleting a contact object
            self.assertEqual(len(Credential.credential_list),1)           
         
if __name__ == '__main__':
    unittest.main()        
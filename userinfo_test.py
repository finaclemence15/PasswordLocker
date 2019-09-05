import unittest # Importing the unittest module
from userinfo import Userinfo # Importing the Userinfo class

class TestUserinfo(unittest.TestCase):

    '''
    Test class that defines test cases for the Userinfo class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_userinfo = Userinfo("clemence","125") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_userinfo.user_name,"clemence")
        self.assertEqual(self.new_userinfo.password,"125")
        
    def test_save_userinfo(self):
        '''
        test_save_userinfo test case to test if the userinfo object is saved into
        the users list
        '''
        self.new_userinfo.save_userinfo() # saving the new contact
        self.assertEqual(len(Userinfo.users_list),1)
# setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Userinfo.users_list = []        
# Items up here...
    def test_save_multiple_userinfo(self):
            '''
            test_save_multiple_userinfo to check if we can save multiple users
            objects to our users_list
            '''
            self.new_userinfo.save_userinfo()
            test_userinfo = Userinfo("clement","125") # new contact
            test_userinfo.save_userinfo()
            self.assertEqual(len(Userinfo.users_list),2)        
        
if __name__ == '__main__':
    unittest.main()    
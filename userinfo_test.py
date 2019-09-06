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
                 
    def test_find_user_by_user_name(self):
        '''
        test to check if we can find a user by username  and display information
        '''

        self.new_userinfo.save_userinfo()
        test_userinfo = Userinfo("clement","125") # new contact
        test_userinfo.save_userinfo()

        found_userinfo = Userinfo.find_by_user_name("clement")

        self.assertEqual(found_userinfo.password,test_userinfo.password)
        
    def test_userinfo_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_userinfo.save_userinfo()
        test_userinfo = Userinfo("clement","125") # new contact
        test_userinfo.save_userinfo()

        userinfo_exists = Userinfo.userinfo_exist("clement")

        self.assertTrue(userinfo_exists)
        
    def test_display_all_userinfo(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(Userinfo.display_userinfo(),Userinfo.users_list)           
                 
if __name__ == '__main__':
    unittest.main()    
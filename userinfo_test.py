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

if __name__ == '__main__':
    unittest.main()    
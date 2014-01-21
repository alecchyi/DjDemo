'''
test cases
'''
from django.test import TestCase
from forms import LoginForm


class UserTest(TestCase):


    def setUp(self):
        self.user = {
                     'username': 'joneslin',
                     'password': '123456',
                     'check_code': '1234',
                     'email': 'joneslin@neupals.com',
                     'status': 0,
                     'real_name': 'joneslin',
                     'image_url': 'https://www.google.com.hk/images/srpr/logo11w.png',
                     'reg_role': 'teacher'
                     }
#         f = LoginForm(self.user)
#         f.save()
        self.user['email'] = "cqa_jones@neupals.com"


    def tearDown(self):
        self.user = {}


    def test_user_attr_cannot_empty(self):

        f = LoginForm({'username': 'ruby'})
        self.assertFalse(f.is_valid(), "username and password are empty")
        self.assertTrue(f["password"].errors)
    
    def test_login(self):
        
        f = LoginForm(self.user)
        self.assertTrue(f.is_valid(), "username and password are validate")
        self.user["username"] = "1234567890123456789012345678901234567890"
        f = LoginForm(self.user)
#         self.assertFalse(f.is_valid(), "username and password are validate!!")
        self.assertFalse(f.is_valid(), 'username is too long')
        self.user["password"] = self.user["username"]
        f = LoginForm(self.user)
        self.assertFalse(f.is_valid(), msg = 'password is too long')
        self.user["check_code"] = self.user["username"]
        f = LoginForm(self.user)
        self.assertFalse(f.is_valid(), msg = 'check_code is too long')
        
        
        
# 
# if __name__ == "__main__":
#     #import sys;sys.argv = ['', 'Test.testName']
#     unittest.main()
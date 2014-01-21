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
                     'email': 'joneslin@neupals.com',
                     'status': 0,
                     'real_name': 'joneslin',
                     'image_url': 'https://www.google.com.hk/images/srpr/logo11w.png',
                     'reg_role': 'teacher'
                     }
        f = LoginForm(self.user)
        f.save()
        self.user['email'] = "cqa_jones@neupals.com"


    def tearDown(self):
        pass


    def testName(self):
        pass

# 
# if __name__ == "__main__":
#     #import sys;sys.argv = ['', 'Test.testName']
#     unittest.main()
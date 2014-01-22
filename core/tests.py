'''
test cases
'''
from django.test import TestCase
from forms import LoginForm
from models import User
from django.test.client import Client


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
#         teacher = {'username': "teacher_01", 'password': '123456'}
#         self.teacher = User.objects.create(teacher)

    def tearDown(self):
        self.user = {}


    def test_user_attr_cannot_empty(self):

        f = LoginForm({'username': 'ruby'})
        self.assertFalse(f.is_valid(), "username and password are empty")
        self.assertTrue(f["password"].errors)
    
    def test_login_form(self):
        
        f = LoginForm(self.user)
        self.assertTrue(f.is_valid(), "username and password are validate")
        self.user["username"] = "1234567890123456789012345678901234567890"
        f = LoginForm(self.user)
        self.assertFalse(f.is_valid(), 'username is too long')
        self.user["password"] = self.user["username"]
        f = LoginForm(self.user)
        self.assertFalse(f.is_valid(), msg = 'password is too long')
        self.user["check_code"] = self.user["username"]
        f = LoginForm(self.user)
        self.assertFalse(f.is_valid(), msg = 'check_code is too long')
        
    def test_login_request(self):
        data = {'username': self.user["username"], 'password': self.user["password"],
            'check_code': self.user["check_code"]}
        c = Client()
        rep = c.post('/login', data)
        self.assertEqual(rep.status_code, 200, "login failed")
        
    def test_detail_get_request(self):
        c = Client()
        rep = c.get("/login", follow=True)
        self.assertIn('', rep.redirect_chain, "redirect to url is wrong")
        self.assertEqual('ruby', rep.context['name'], "context")
        self.assertEqual(rep.content, 'detail', "can't get detail info")
        

DjDemo
======

a django demo

Functions:
	1) log in and log out
	2) write blog and display blog list
	3) some configs and usage about init a new django project, such as static files , templates,
		 url, log, pagination, and routes
	4) testing 

For Development

	1) git clone git@github.com:alecchyi/DjDemo.git
	2) cd DjDemo 
	3) update database settings
	3) python manage.py syncdb
	4) python manage.py runserver 0.0.0.0:8000
	
For Testing in unittest

1. create tests.py in your app, such as core/tests.py
But the pre-condition is you have a models.py

2. add test code in tests.py
   
   1）测试登录表单
	   import LoginForm
	   f = LoginForm({}) #表单数据为空
	   使用f.is_valid() 判断表单是否有效
	   f = LoginForm({'username':'aaaa', 'password': '123456'})  #数据正常的情况
	   self.assertTrue(f.is_valid(),"输入的信息有误")#如果表单数据有效，f,is_valid()返回True
	   f = LoginForm({'username':'aaaa111111111111111111', 'password': '123456'})  #用户名输入长度过长的情况
	   如果表单数据有效，f,is_valid()返回False
	   self.assertFalse(f.is_valid(),"输入的用户名长度过长")
   
   2）测试模型操作
	   t = {'username': "teacher_01", 'password': '12345611111111111111111111111111111111111111111111111122222222222222222222222222', 'status':0}
	        with self.assertRaises(Exception):   #验证字段长度
	            Member.objects.get_or_create(**t)
	        with self.assertRaises(Exception):
            	Member.objects.get(username='teacher_01')
        	members = Member.objects.all()
        	self.assertEqual(members.count(), 1, "count is 1")
   3）测试登录逻辑
	   from django.test.client import Client
	   c = Client()
	   response = c.post("/login",{'username':'ruby', 'password': '123456'})
	   self.assertEqual(response.status_code, 200)  #测试通过
   
   4）测试http请求和http响应
	    from django.test.client import Client
	   c = Client()
	   response = c.get("/detail",{'xxxx':'eeeee'})
	   self.assertEqual(response.content,'yyyy') #如果请求的方法是get,判断返回的结果是否正确
	   self.assertEqual("yyy",response.context["key"]) #如果页面是render新的模板，并且有传递数据变量，可以使用这个判断
   
   
3. run test command  
	cd project_dir && python manage.py test app_name   #测试对应app的所有脚本
	python manage.py test core.tests.UserTest.test_login_request #执行测试某个具体的功能
	
4. add fixtures data in tests.py
    tests.py 的测试类是基础django.test.TestCase,所以会有一些继承的方法，比如
    setUp: 可以把一些测试数据定义在这里
    tearDown:测试完成销毁测试数据
    
5. add log info in test code
	import logging
	logger = logging.getLogger("django")
	logger.debug("xxxxxxx")
	cat logs/debug.log
	
6. custom assert function
    assert_xxx_xxxx()
	
	
refs:
	http://searchcode.com/codesearch/view/2290327
	http://docs.python.org/2.7/library/unittest.html#unittest.TestCase
   
   


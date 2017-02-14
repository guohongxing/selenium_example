#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8");
from time import sleep;
import unittest,random,sys
import myunit,function
from loginPage import login
print sys.getdefaultencoding()  
import re;

class loginTest(myunit.MyTest):
	'''alle登陆测试'''

	#测试用户登陆
	def user_login_verify(self,username='',password=''):
		login(self.driver).user_login(username,password);

	#@unittest.skip("test_login1")
	def test_login1(self):
		'''用户名、密码为空'''
		self.user_login_verify();
		po = login(self.driver);		
		self.assertEqual(po.user_error_hint(),"请输入用户名");
		self.assertEqual(po.pawd_error_hint(),"请输入密码");
		#function.insert_img(self.driver,"user_pawd_empty.jpg");

	#@unittest.skip("test_login2")
	def test_login2(self):
		'''用户名为空，密码正确'''
		self.user_login_verify(password = "acs12346");
		po = login(self.driver);
		self.assertEqual(po.user_error_hint(),"请输入用户名");

	def test_login3(self):
		self.user_login_verify(username="13817130181",password="jT8430251");
		po = login(self.driver);
		pattern = re.compile(r'fa');
		match = pattern.search(po.user_login_success());
		sleep(2);
		self.assertTrue(match);

if __name__ == '__main__':
	unittest.main();


#coding=utf-8;
from selenium.webdriver.common.by import By ;
from base import Page;
class rePassword(Page):
	'''
	用户忘记密码页面
	'''

	re_username_loc = (By.ID,'txtUserName');
	re_code_loc = (By.ID,'txtCode');
	re_button_loc = (By.NAME,'btnSubmit');


	#输入手机号和邮箱
	def re_username(self,telephone=""):
		self.driver.find_element(*self.re_username_loc).send_key(telephone);

	#输入验证码
	def re_code(self,code=""):
		self.driver.find_element(*self.re_code_loc).send_key(code);

	#提交按钮
	def re_buttion(self):

	#统一忘记密码接口
	def rePassword_commit(self)：


#coding=utf-8
#from selenium.webdriver.common.action_chains import action_chains
from selenium.webdriver.common.by import By 

from base import Page
from time import sleep

class login(Page):
	'''
	用户登录页面
	'''

	
	#Action
	login_user_loc = (By.LINK_TEXT,'登录')	

	def alle_login(self):
		self.find_element(*self.login_user_loc).click();

	login_username_loc = (By.ID,"txtUserName");
	login_password_loc = (By.ID,"txtPassword");
	login_button_loc = (By.NAME,"btnSubmit");

	#登录用户名
	def login_username(self,username):
		self.find_element(*self.login_username_loc).send_keys(username);
	
	#登录密码
	def login_password(self,userpassword):
		self.find_element(*self.login_password_loc).send_keys(userpassword);

	#登录按钮
	def login_buttion(self):
		self.find_element(*self.login_button_loc).click();

	#定义统一登录入口
	def user_login(self,username="username",password="1111"):
		""" 获取的用户名密码登陆"""
		self.open();
		self.alle_login();
		self.login_username(username);
		self.login_password(password);
		self.login_buttion();
		sleep(1);

	user_error_hint_loc =(By.XPATH,"//*[@id='dlcen1']/dl[1]/dd[2]/i");
	pawd_error_hint_loc = (By.XPATH,"//*[@id='dlcen1']/dl[2]/dd[2]/i");
	user_login_success_loc = (By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/span[1]");

	#用户名错误
	def user_error_hint(self):
		return self.find_element(*self.user_error_hint_loc).text;

	#密码错误提示
	def pawd_error_hint(self):
		return self.find_element(*self.pawd_error_hint_loc).text;

	#登陆成功用户名
	def user_login_success(self):
		return self.find_element(*self.user_login_success_loc).text;

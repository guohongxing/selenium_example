from selenium import webdriver;

import unittest
import os 

def browser():
	driver = webdriver.Chrome();
	return driver;

class MyTest(unittest.TestCase):
	def setUp(self):
		self.driver = browser();
		self.driver.implicitly_wait(10);
		self.driver.maximize_window()
	def tearDown(self):
		self.driver.quit();




































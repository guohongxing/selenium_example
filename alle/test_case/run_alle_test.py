#coding=utf-8;
from HTMLTestRunner import HTMLTestRunner
import unittest
import time 
import os

if __name__ == '__main__':
	now = time.strftime("%y-%m-%d %H_%M_%S");	
	filename = os.path.dirname(os.path.dirname(__file__))+'/report/'+now+'result.html'
	fp = open(filename,'wb');
	
	runner = HTMLTestRunner(stream=fp,title="alle网站自动化测试报告",description='环境：windows 7 浏览器：chrome')

	discover = unittest.defaultTestLoader.discover(os.path.dirname(os.path.dirname(__file__))+'/test_case',pattern='*_sta.py');

	runner.run(discover);
	fp.close();
	
	



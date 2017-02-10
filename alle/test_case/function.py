from selenium import webdriver
import os 

def insert_img(driver,file_name):	
	base_dir =os.path.dirname(os.path.dirname(__file__));
	print(base_dir);
	base_dir = str(base_dir)
	base_dir = base_dir.replace("\\","/");
	file_path =  base_dir+'/report/image/'+file_name
	driver.get_screenshot_as_file(file_path)
if __name__ == '__main__':
	driver = webdriver.Chrome();
	driver.get("http://www.baidu.com");
	insert_img(driver,'baidu.jpg');
	driver.quit();



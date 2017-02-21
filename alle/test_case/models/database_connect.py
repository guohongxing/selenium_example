#coding=utf-8;
import 	pymysql;

if __name__ == '__main__':
	
	test = pymysql.connect(db="news",host="106.14.30.35",user="root",passwd='dff20660ea',charset='utf8mb4');
 	cur = test.cursor();
	cur.execute("selete * from user");
	connect.commit();
 	data = cur.fetchone();
 	print data;
 
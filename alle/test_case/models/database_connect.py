#coding=utf-8;
import 	MySQLdb;

if __name__ == __main__:
	test = MySQLdb.connect(db="news",host="106.14.30.35",user="root",passwd='dff20660ea',charset='utf-8');
 	cur = test.cursor();
	cur.execute("selete * from config");
 	data = cur.fetchone();
 	print data;
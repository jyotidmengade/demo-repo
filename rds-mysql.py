import pymysql
db = pymysql.connect('database-1.cz1us8urzebl.us-east-1.rds.amazonaws.com', 'admin', '12345678')
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()

print(data)
#sql = '''create database jdm'''
#cursor.execute(sql)
#cursor.connection.commit()
sql = '''use jdm'''
cursor.execute(sql)

sql = '''
insert into emp_details(fname, lname) values('%s', '%s')''' % ('sandesh','Mengade')

cursor.execute(sql)
db.commit()
sql = '''select * from emp_details'''
cursor.execute(sql)
cursor.fetchall()

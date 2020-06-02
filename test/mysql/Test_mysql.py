import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "big_data")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "select * from onepiece_seller_live limit 10;"
try:
    # 执行SQL语句
    cursor.execute(sql)
    print(cursor.rownumber)
    result = cursor.fetchone()
    while result!=None:
        print(result, cursor.rownumber)
        result = cursor.fetchone()

    result = cursor.fetchone()
    print(result, cursor.rownumber)
    result = cursor.fetchone()
    print(result, cursor.rownumber)

except:
    print ("Error: unable to fetch data")

# 关闭数据库连接
db.close()


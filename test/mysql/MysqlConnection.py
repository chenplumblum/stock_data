# import pymysql
#
# class MysqlConnection(object):
#     # 初始化属性
#     def __init__(self):
#         self.host = 'localhost'
#         self.port = 3306
#         self.user = 'root'
#         self.password = 'root'
#         self.database = 'big_data'
#
#     # 连接数据库
#     def Connect(self):
#         self.db = pymysql.connect(
#             host=self.host,
#             port=self.port,
#             user=self.user,
#             password=self.password,
#             database=self.database,
#             charset='utf8'
#     )
#
#     def close
import tushare as ts

ts.set_token('7a500f3b86413ca81e920897e0efd6bf23f96a02ff0d4b5ac7423955')
pro = ts.pro_api()
pro = ts.pro_api('7a500f3b86413ca81e920897e0efd6bf23f96a02ff0d4b5ac7423955')
# df = pro.daily(exchange='', start_date='20180901', end_date='20181001', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')
data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

print(data)
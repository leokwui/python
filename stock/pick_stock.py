import pandas as pd
import tushare as ts
import datetime
import requests
import jqdatasdk
import sqlalchemy
date = (datetime.datetime.today()+datetime.timedelta(days=-2)).strftime('%Y%m%d')
pro = ts.pro_api('e849038f698aed5f8eab3b98c8ba3cc15d4358d6517f829ef3def7f1')
# stock_basis
data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
data.to_csv('c:/stock/stock_basis.csv')
# stock_company
data_sse = pro.stock_company()
data_sse.to_csv('c:/stock/stock_company.csv')
data_szse = pro.stock_company(exchange='szse')
data_szse.to_csv('c:/stock/stock_company.csv', mode='a')
# daily
df = pro.daily(trade_date=date)
df.to_csv('c:/stock/daily.csv')
r = requests.get('http://hq.sinajs.cn/list=sh601006')
value = r.text
print(value)
# jqdatasdk.auth('18918378650', 'woshiguilin')
# s=jqdatasdk.get_all_securities(types=[], date=None)
# q = sqlalchemy.query(
#     valuation
# ).filter(
#     valuation.code == '000001.XSHE'
# )
# df = get_fundamentals(q, '2015-10-15')

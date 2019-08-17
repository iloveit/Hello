import tushare as ts

# print('Hello World')
# print(ts.__version__)

etf50 = ts.get_hist_data('510050',start='2016-01-01',end='2019-08-09')
etf50.to_excel('D:/StockPlace/etf50.xlsx')
#print(etf50)
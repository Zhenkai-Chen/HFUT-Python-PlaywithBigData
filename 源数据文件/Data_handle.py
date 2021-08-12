import pandas as pd
from Average_wage_get import data1
from Average_housing_price_get import data2

city_lst = []   # 省会直辖市列表
average_wage_lst = []   # 平均工资列表
average_housing_price_lst = []  # 平均房价列表
time_lst = []   # 不吃不喝买房所需时间
data = dict()   # 创建一个数据字典用来汇总所有的数据


for i in data2.keys():  # 从数据2获取键放入城市列表中
    city_lst.append(i)
for i in data1.values():  # 从数据1获取值放入平均工资列表中
    average_wage_lst.append(i)
for i in data2.values():    # 从数据2获取值放入平均房价列表中
    average_housing_price_lst.append(i)
for i in range(len(city_lst)):  # 计算每个城市在不吃不喝(即工资完全用来买房)的情况下用平均工资买房要花多长时间
    months = round(average_housing_price_lst[i]*100/average_wage_lst[i]) + 1  # 因为房贷少交一个月都不行所以四舍五入+1
    years = round(months/12) + 1   # 同上
    time_lst.append(years)

data["city"] = city_lst  # 城市字典
data["wage"] = average_wage_lst  # 平均工资字典
data["housing_price"] = average_housing_price_lst  # 平均房价字典
data["time"] = time_lst  # 买房花费时间字典

df = pd.DataFrame(data)  # 创建DataFrame,输出为.csv和.xlsx文件
df.to_csv('大陆各省会直辖市平均工资及平均房价.csv', encoding="utf-8", index=False)
df.to_excel('大陆各省会直辖市平均工资及平均房价.xlsx')

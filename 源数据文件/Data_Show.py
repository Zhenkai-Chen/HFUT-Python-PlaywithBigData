import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('大陆各省会直辖市平均工资及平均房价.xlsx')
del df['Unnamed: 0']
print(df)

plt.rcParams['font.sans-serif'] = ['Simhei']
plt.rcParams['axes.unicode_minus'] = False

# 平均工资绘图
x = df["city"]
y = df["wage"]

plt.figure(figsize=(22, 5))
plt.title("中国大陆各省会及直辖市的平均工资")
plt.xlabel("城市")
plt.ylabel("平均工资")
plt.plot(x, y)
plt.savefig("中国大陆各省会及直辖市的平均工资.jpg")

# 平均房价绘图
m = df["city"]
n = df["housing_price"]

plt.figure(figsize=(22, 5))
plt.title("中国大陆各省会及直辖市的平均房价")
plt.xlabel("城市")
plt.ylabel("平均房价")
plt.plot(m, n)
plt.savefig("中国大陆各省会及直辖市的平均房价.jpg")


# 平均房价与平均工资对比绘图
plt.figure(figsize=(22, 5))
plt.plot(x, y, 'r-*')
plt.plot(m, n, 'g-v')
plt.legend(["平均工资", "平均房价"])
plt.savefig("中国大陆各省会及直辖市的平均房价与平均工资对比.jpg")

# 各城市居民在不吃不喝平均工资只用来买房的情况下需要的时间绘图
z = df["time"]

plt.figure(figsize=(22, 5))
plt.title("各城市居民在不吃不喝平均工资只用来买房的情况下需要的时间")
plt.xlabel("城市")
plt.ylabel("时间")
plt.plot(x, z)
plt.savefig("各城市居民在不吃不喝平均工资只用来买房的情况下需要的时间.jpg")

import requests
from bs4 import BeautifulSoup


def get_data_from_text(city_lst):
    """从网页内容里获取数据"""
    city = []   # 创建一个列表用来存放城市
    housing_price = []  # 创建一个列表用来存放房价

    for i in range(len(city_lst)):  # 遍历传入的城市列表，查找保存的网页中城市名及对应房价
        text = get_text_from_saved_html(city_lst[i])    # 从保存的html里获取网页内容

        soup = BeautifulSoup(text, 'html.parser')
        sf = soup.find(class_="highLight")  # 根据浏览器检查网页内容确定了所要寻找的信息所在位置
        city_name = ''  # 创建一个空字符串用来存放城市字符串
        housing_price_str = ''  # 创建一个空字符串用来存放房价字符串

        st = sf.text.replace(" ", "").strip()   # 去除空格、换行符等
        flag = 0   # 标记位置
        while not st[flag].isdigit():  # 获取城市字符串
            city_name += st[flag]
            flag += 1
        city_name.replace('市', '')
        city.append(city_name)

        for j in range(-9, -4):  # 获取房价字符串
            housing_price_str += st[j]
        housing_price_num = eval(housing_price_str)  # 将房价由字符串型转换为数字型，为后续计算做准备
        housing_price.append(housing_price_num)

    return city, housing_price


def get_text_from_saved_html(city):
    """从保存的html里获取网页内容"""
    with open("Housing_Price/" + city, "r", encoding='utf-8') as f:  # 打开保存的网页
        text = f.read()  # 读取网页内容

    return text


def main():
    data = dict()   # 创建一个空字典，用来存放各省会直辖市的城市名及房价
    city_lst = ['beijing', 'tianjin', 'shijiazhuang', 'taiyuan', 'huhehaote',
                'shenyang', 'changchun', 'haerbin',
                'shanghai', 'nanjing', 'hangzhou', 'hefei', 'fuzhou', 'nanchang', 'jinan',
                'zhengzhou', 'changsha', 'wuhan', 'guangzhou', 'nanning', 'haikou',
                'chongqing', 'chengdu', 'guiyang', 'kunming', 'lasa',
                'xian', 'lanzhou', 'xining', 'yinchuan', 'wulumuqi']    # 城市列表，用来打开保存的网页文件

    city, housing_price = get_data_from_text(city_lst)  # 获取城市名列表和房价列表
    for i in range(len(city)):  # 给字典赋值
        data[city[i]] = housing_price[i]

    return data


data2 = main()

import requests
from bs4 import BeautifulSoup


def get_data_from_text(city_lst):
    """从网页内容里获取数据"""
    city = []   # 创建一个列表用来存放城市
    wage = []  # 创建一个列表用来存放工资

    for i in range(len(city_lst)):  # 遍历传入的城市列表，查找保存的网页中城市名及对应房价
        text = get_text_from_saved_html(city_lst[i])    # 从保存的html里获取网页内容
        soup = BeautifulSoup(text, 'html.parser')
        city_name = ''  # 创建一个空字符串用来存放城市字符串
        wage_str = ''  # 创建一个空字符串用来存放房价字符串

        sf1 = soup.find(class_="card-header")  # 查找城市名所在位置
        st1 = sf1.text.replace(" ", "").strip()  # 去掉空格、换行符等
        flag = 0
        while not st1[flag].isdigit():
            city_name += st1[flag]
            flag += 1
        city_name.replace('市', '')
        city.append(city_name)

        sf2 = soup.find(class_="text-center justify-content-between")  # 查找平均工资所在位置
        st2 = sf2.text.replace(" ", "").strip()  # 去掉空格、换行符等
        flag = 0
        while st2[flag] != "C":
            wage_str += st2[flag]
            flag += 1
        wage_num = eval(wage_str)  # 将字符串转换为数字
        wage.append(wage_num)

    return city, wage


def get_text_from_saved_html(city):
    """从保存的html里获取网页内容"""
    with open("Wage/" + str(city), "r", encoding='utf-8') as f:  # 打开保存的网页
        text = f.read()  # 读取网页内容

    return text


def main():
    data = dict()   # 创建一个空字典，用来存放各省会直辖市的城市名及房价
    city_num = [110000, 120000, 130100, 140100, 150100,
                210100, 220100, 230100,
                310000, 320100, 330100, 340100, 350100, 360100, 370100,
                410100, 430100, 420100, 440100, 450100, 460100,
                500000, 510100, 520100, 530100, 540100,
                610100, 620100, 630100, 640100, 650100]    # 城市列表，用来打开保存的网页文件

    city, wage = get_data_from_text(city_num)  # 获取城市名列表和房价列表
    for i in range(len(city)):  # 给字典赋值
        data[city[i]] = wage[i]

    return data


data1 = main()

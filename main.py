# -*- coding: utf-8 -*-
# @Author : lifz
# @Time : 2022/3/5
# @File : main.py
# @Mail : leoleechn@outlook.com

import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt


def main():
    # 变量设值输出
    print('=' * 20)
    print("目标质量 W  : 200kg\n"
          "电缆长度 Lc : 3m\n"
          "横杆长度 Lp ： 3m")
    print('=' * 20)

    # 变量定义
    W = 200  # 目标质量
    Lc = 3  # 绳索长度
    Lp = 3  # 横杆长度

    # 函数处理
    function(W, Lc, Lp)


# 计算处理函数
def function(var1, var2, var3):
    T_list = []
    d_list = []
    for d in np.arange(0.5, 2.9, 0.1):
        T = (var1 * var2 * var3) / (d * np.sqrt(var2 * var2 - d * d))  # 代入公式计算
        T_list.append(round(T, 2))  # 绳索张力保留两位小数写入列表
        d_list.append(round(d, 1))

    # 测试
    # print(d_list)
    # print(T_list)

    # 将数据存进data.xlsx
    data = {"张力(N)": T_list, "位置(m)": d_list}
    df = DataFrame(data)
    df.to_excel("data.xlsx")

    # 绘制折线图
    T_min = min(T_list)
    index = T_list.index(min(T_list))
    plt.plot(d_list, T_list)
    plt.plot(d_list[index], T_min, "bo")
    plt.annotate("Minimum:" + '(' + str(d_list[index]) + ',' + str(T_min) + ')', xy=(d_list[index], T_min),
                 xytext=(1.75, 500), arrowprops=dict(arrowstyle="->"))  # 最小值点标注
    plt.grid()
    plt.xlabel("Position,d,(m)")
    plt.ylabel("Tension,T,(N)")
    plt.savefig("pic.png")
    plt.show()


if __name__ == "__main__":
    main()

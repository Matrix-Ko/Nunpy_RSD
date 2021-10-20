

#相对标准偏差 RSD 与标准偏差 SD 计算方法
from typing import List
import numpy as np




def rsd_calculate(value_list=List):
    a = np.array(value_list)
    std1 = np.std(a, ddof = 1)                                     #方法1，np.std无偏样本标准差方式为加入参数 ddof = 1
    std2 = np.sqrt(((a - np.mean(a)) ** 2).sum() / (a.size - 1))   #方法2，直接用公式啦
    print(std1)
    print(std2)

    ave = np.mean(a)
    rsd1 = std1 / ave
    rsd2 = std2 / ave
    print(rsd1)
    print(rsd2)
    return rsd1,rsd2,std1,std2


l = [2020,2220,2220,2220,2220,2210]
rsd_calculate(l)
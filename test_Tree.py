# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 21:38:37 2016

@author: Administrator
"""

from ete3 import Tree

t = Tree("((黄疸:19.19959,恶心:6.80041):0.84600,\
        ((B超显示脂肪肝:11.99700, B超显示肝硬化:12.00300):7.52973,\
        ((HbsAg:100.85930,HbeAg:47.14069):20.59201,\
        血清白蛋白下降:18.87953):2.09460):3.87382,流行病学:25.46154);")

print t
print('测试')
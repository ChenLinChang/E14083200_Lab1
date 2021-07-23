#!/usr/bin/env python
# coding: utf-8

# In[71]:

#引入模組andom
import random
#創建類別
class Nine_Coins:
    #初始化此類別
    def __init__(self,decimal):
        self.decimal=decimal
        #將二進位位數存在lis中
        a_list=[0,0,0,0,0,0,0,0,0]
        for i in range(0,9,1):
            a_list[8-i]=decimal%2
            decimal=decimal//2
        self.binary=a_list
    #創建函式
    def toss(self):
        #隨機變數代表重擲硬幣
        self.decimal=random.randint(0,511)
        #重新初始化類別
        a=self.decimal
        a_list=[0,0,0,0,0,0,0,0,0]
        for i in range(0,9,1):
            a_list[8-i]=a%2
            a=a//2
        self.binary=a_list
    def __str__(self):
        #將lis中儲存的二進位位數轉成string並組合回傳
        list_str="".join('%s' %id for id in self.binary)
        return f"binary: {list_str} and decimal: {self.decimal}"
    
    def __repr__(self):
        #轉換二進位成為H , T 表示
        b_list=[]
        for i in range(0,9,1):
            if self.binary[i]==0:
                b_list.append('H')
            elif self.binary[i]==1:
                b_list.append('T')
            list_new="".join(b_list)
        return f"Nine_Coins: {list_new}"


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 13:18:20 2020

@author: tejaspatel
"""

# capacity must be int 


class MoneyBox:
    def __init__(self,capacity):
        self.capacity = capacity  #intial capacity 
        self.number_of_coins = 0  #intially 0 balance in the box

    
    def can_add(self,v):
        if(self.number_of_coins+v<=self.capacity): # check after adding certain vlaue balance should not be more than capacity 
            self.add(v)
            return True
        else:
            return False
    
    def add(self,v):
        self.number_of_coins = self.number_of_coins + v  # reflect current balance with updated value
    
  


c = int(input("enter capacity of virtual money box  :"))
a = MoneyBox(c)  #class instance
i = int(input("enter number of coins you want to add to money box :"))
if(a.can_add(i)):  #method call
    print("\n")
    print("succefully added money in money box!!!!!")
    print("current balance of money box",a.number_of_coins)
else:
    print("\n")
    print("overflow you can not add more than capacity of money box!!!!!!")
    print("current balance of money box",a.number_of_coins)
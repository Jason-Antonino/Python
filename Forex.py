# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 22:50:09 2019

@author: jason
"""

from forex_python.converter import CurrencyRates
c = CurrencyRates()
dictionary = c.get_rates('USD')
print(dictionary)
key = input("Enter abbreviation for country you want (e.g. MXN): ")
target = dictionary[key]
print(target)
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 16:14:59 2019

@author: jason
"""
import time
print("Apparatus Purchase Trarnsaction Algorithm")

list_of_parts = ["Housing", "Shape memory foam pillow, travel size", "Plain pillowcase", "Aromatherapy diffuser, ultrasonic", "Stereo speakers, wireless", "Lamp base and WiFi Smart LED Bulb w/remote", "Temperature-regulating fabric pillowcase", "Shiatsu massage pillow w/ heat", "Near-infrared LED bulb and fixture", "Massage mat with heat, full body length"]

print("These are all the components we offer at this time:")
time.sleep(1)
print(list_of_parts)
time.sleep(1)
print("")
print("Configuring Base Model")
already_included = list_of_parts[0:3]
base_model_addons = list_of_parts[3:9]

print("From the following list:")
menu = enumerate(base_model_addons, 1) #enumerates the list of parts above starting at index 1
print(list(menu))

first_extra_part = int(input("Type the NUMBER of the part you want: "))
needed_part = base_model_addons[first_extra_part-1]
print(needed_part)
base_model = already_included, needed_part
time.sleep(2)
print("As configured, your base model contains: ", base_model)
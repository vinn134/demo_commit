#!/usr/bin/env python3
import statistics
import sys

import requests

#print(f"VERSION   : {sys.version}\n")
print(f"EXECUTABLE: {sys.executable}\n")
myglobal = "Global variable\n"


############################################################
def calculate_mean(input_lst):
    mean = statistics.mean(input_lst)
    return mean
#print(f"MEAN: {calculate_mean([])}")
############################################################


############################################################
def foo():
    #global myglobal
    myglobal = "Updated global variable"
    print(myglobal)
# foo()
# print(myglobal)
############################################################


############################################################
page = requests.get("http://duckduckgo.com")
# print(page.status_code)
############################################################

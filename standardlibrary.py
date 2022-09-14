#! usr/bin/python

# os, re, pickle, datetime, time, math
import os
import re
import pickle
import datetime
import time 
import math

def ostest():
    a = os.access
    b = os.getlogin()
    print(b)
    print(a)
def retest():
    print("test")
def mathtest():
    print(math.log(4))

if __name__ == "__main__":
    # ostest()
    # retest()
    mathtest()
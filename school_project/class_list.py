# -*- coding: utf-8 -*-
"""
Created on Wed May  4 21:48:42 2022

@author: User
"""
import cv2
import time
from concurrent.futures import thread
from ctypes import BigEndianStructure
import os
from random import shuffle
from tokenize import group
from turtle import down, up
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import math
from math import *
from datetime import datetime





def create_global():
    
    global CF_list
    print("create_global")
    CF_list=[]
  
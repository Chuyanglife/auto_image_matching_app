# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 16:20:56 2022

@author: User
"""

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog
import cv2
import time
import sys

#from concurrent.futures import thread
#from ctypes import BigEndianStructure
import os
#from random import shuffle
#from tokenize import group
#from turtle import down, up
import cv2
import numpy as np
#import pandas as pd
#from matplotlib import pyplot as plt
import math
from math import *
from datetime import datetime


from PyQt5 import QtPrintSupport, QtGui
from PyQt5.QtCore import Qt, QMimeData, QDate, QDateTime, QTime, QStringListModel, QSize
from PyQt5.QtGui import QIcon, QPainter, QBrush, QPixmap, QStandardItemModel, QStandardItem, QColor, QFont
from PyQt5.QtPrintSupport import QPageSetupDialog, QPrinter, QPrintDialog
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QFormLayout, QLabel, QLineEdit, QPushButton, QGridLayout, \
    QCalendarWidget, QVBoxLayout, QDateTimeEdit, QAction, QMainWindow, QTextEdit, QStatusBar, QFileDialog, QDialog, \
    QTableView, QMessageBox, QListView, QListWidget, QHBoxLayout, QTableWidget, QTableWidgetItem, QAbstractItemView
    
from UI2 import Ui_mainWindow
from savefile import Ui_Dialog

import class_list




def new_resize_img(img, new_scale):                 #check
    height, width = img.shape[:2]
    scale = new_scale

    img = cv2.resize(img, (int(scale*width), int(scale*height)),
                     interpolation=cv2.INTER_AREA)

    return img


def a_hash(img):                                    #check

    # 轉 8*8
    img = cv2.resize(img, (8, 8), interpolation=cv2.INTER_CUBIC)
    # 轉 灰階圖
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 8*8灰階值總和
    sum_gray = 0
    # hash 字串
    hash_str = ''

    # 求灰階值總和
    for i in range(8):
        for j in range(8):
            sum_gray += gray[i][j]

    # 8*8灰階圖 平均
    average_gray = sum_gray/64

    # 比較
    for i in range(8):
        for j in range(8):
            if(gray[i][j] > average_gray):
                hash_str += '1'
            else:
                hash_str += '0'

    return hash_str


def cam_hash(hash_1, hash_2):                       #check

    # 記 hash_1 , hash_2  一樣 次數
    not_same = 0

    # 比對 hash_1 , hash_2 相同的次數
    for i in range(64):
        if(hash_1[i] != hash_2[i]):
            not_same += 1

    return (not_same)

def showIMG(name, img):                             #check
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def test_angle(tar_Point, tem_Point, select_point): #check

    va_x = tar_Point[select_point[0]][0]-tar_Point[select_point[1]][0]
    va_y = tar_Point[select_point[0]][1]-tar_Point[select_point[1]][1]
    vb_x = tar_Point[select_point[2]][0]-tar_Point[select_point[1]][0]
    vb_y = tar_Point[select_point[2]][1]-tar_Point[select_point[1]][1]

    vc_x = tem_Point[select_point[0]][0]-tem_Point[select_point[1]][0]
    vc_y = tem_Point[select_point[0]][1]-tem_Point[select_point[1]][1]
    vd_x = tem_Point[select_point[2]][0]-tem_Point[select_point[1]][0]
    vd_y = tem_Point[select_point[2]][1]-tem_Point[select_point[1]][1]

    long_A=sqrt((va_x**2+va_y**2)*(vb_x**2+vb_y**2))
    long_B=sqrt((vc_x**2+vc_y**2)*(vd_x**2+vd_y**2))

    if (long_A==0)|(long_B==0):
#        print("\nlong is 0 \n")
        return False

    cosA = (va_x*vb_x+va_y*vb_y) / long_A
    cosB = (vc_x*vd_x+vc_y*vd_y) / long_B


    A = math.degrees(np.arccos(cosA))
    B = math.degrees(np.arccos(cosB))

    if((A<=5) | (B<=5)):    return False

    if (abs(A-B) <= 5):         #double check
        va_x = tar_Point[select_point[1]][0]-tar_Point[select_point[0]][0]
        va_y = tar_Point[select_point[1]][1]-tar_Point[select_point[0]][1]
        vb_x = tar_Point[select_point[2]][0]-tar_Point[select_point[0]][0]
        vb_y = tar_Point[select_point[2]][1]-tar_Point[select_point[0]][1]

        vc_x = tem_Point[select_point[1]][0]-tem_Point[select_point[0]][0]
        vc_y = tem_Point[select_point[1]][1]-tem_Point[select_point[0]][1]
        vd_x = tem_Point[select_point[2]][0]-tem_Point[select_point[0]][0]
        vd_y = tem_Point[select_point[2]][1]-tem_Point[select_point[0]][1]

        long_A=sqrt((va_x**2+va_y**2)*(vb_x**2+vb_y**2))
        long_B=sqrt((vc_x**2+vc_y**2)*(vd_x**2+vd_y**2))

        A = math.degrees(np.arccos(cosA))
        B = math.degrees(np.arccos(cosB))
        if((A<=5) | (B<=5)):    return False
        if(abs(A-B) <= 5):     return True

#    print("\nFinal test angle False")
    return False

def test_rectangle(point_one,point_two,select_point):#check
    #min                                                #caculate init width hight ratio
    one_x = point_one[select_point[0]][0]
    one_y = point_one[select_point[0]][1]
    two_x = point_two[select_point[2]][0]
    two_y = point_two[select_point[2]][1]
    #max
    one_X = point_one[select_point[0]][0]
    one_Y = point_one[select_point[0]][1]
    two_X = point_two[select_point[2]][0]
    two_Y = point_two[select_point[2]][1]

    for i in select_point:
        if(point_one[i][0]<one_x):  one_x=point_one[i][0]       #min_x  point_one
        if(point_one[i][0]>one_X):  one_X=point_one[i][0]       #max_X
        if(point_one[i][1]<one_y):  one_y=point_one[i][1]       #min_y
        if(point_one[i][1]>one_Y):  one_Y=point_one[i][1]       #max_Y
        if(point_two[i][0]<two_x):  two_x=point_two[i][0]       #min_x  point two
        if(point_two[i][0]>two_X):  two_X=point_two[i][0]       #max_X
        if(point_two[i][1]<two_y):  two_y=point_two[i][1]       #min_y
        if(point_two[i][1]>two_Y):  two_Y=point_two[i][1]       #max_Y

    div_one_x=one_X-one_x
    div_one_y=one_Y-one_y

    if((div_one_x<=0)|(div_one_y<=0)):  return False
    one_rate=div_one_x/div_one_y

    div_two_x=two_X-two_x
    div_two_y=two_Y-two_y


    if((div_two_x==0)|(div_two_y<=0)):  return False
    two_rate=div_two_x/div_two_y

    #a:b==c:d
    miss_rate=0.1

    if((abs(1-(one_rate/two_rate))<miss_rate)): return True

    return False

def Find_LU(arr,select):
    Up=arr[select[0]][1]
    Left=arr[select[0]][0]
    Down=arr[select[0]][1]
    Right=arr[select[0]][0]
    for i in select:
        if( Up>arr[i][1]):     Up=arr[i][1]
        if( Left>arr[i][0]):   Left=arr[i][0]
        if( Down<arr[i][1]):   Down=arr[i][1]
        if( Right<arr[i][0]):  Right=arr[i][0]
    return Left,Up,Right,Down



def vector(tar,tem,point):          #check

    tarv_x=tar[point[1]][0]-tar[point[0]][0]
    tarv_y=tar[point[1]][1]-tar[point[0]][1]
    temv_x=tem[point[1]][0]-tem[point[0]][0]
    temv_y=tem[point[1]][1]-tem[point[0]][1]

    tar_square=tarv_x**2+tarv_y**2
    tem_square=temv_x**2+temv_y**2

    ratio=tar_square/tem_square

    return ratio

sift = cv2.SIFT_create()
bf = cv2.BFMatcher(crossCheck=True)

class IMG:
    def __init__(self,name,filename):
        self.name=name
        self.filename=filename
        self.img=cv2.imread(name)
        self.gray_img=[]
        self.kp=[]
        self.des=[]
        self.area=0
        self.width=0
        self.hight=0


    def img_shape(self):        #check

        hight,width=self.img.shape[:2]
        if((width>=1000)&(hight>=1000)):
            self.img=new_resize_img(self.img,2**(-1))
        elif((width>=2000)&(hight>=2000)):
            self.img=new_resize_img(self.img,4**(-1))
        elif((width>=4000)&(hight>=4000)):
            self.img=new_resize_img(self.img,8**(-1))
        #cv2.imwrite("D:/source/vscode/python_project/check_img/img"+str(self.filename)+".jpg", self.img)
        self.gray_img=cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        self.hight,self.width=self.img.shape[:2]
        self.area=self.hight*self.width
        #cv2.imwrite("D:/source/vscode/python_project/check_img/gray"+str(self.filename)+".jpg", self.gray_img)

    def create_sift(self):      #check
        self.kp,self.des=sift.detectAndCompute(self.gray_img, None)

    def showIMG(self):          #check
        cv2.imshow(self.name, self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def showGrayIMG(self):      #check
        cv2.imshow(self.name, self.gray_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def showName(self):         #check
        print("IMG Name : ",self.name)

img=[]

class BUF_IMG:
    def __init__(self,img,width,hight,area,left,up,right,down):

        self.img=img
        self.width=width
        self.hight=hight
        self.area=area
        self.left=left
        self.up=up
        self.right=right
        self.down=down

    def resize_total(self,k):       #check

        self.area*=(k**(2))
        self.hight*=k
        self.width*=k
        self.left*=k
        self.up*=k
        self.right*=k
        self.down*=k
        self.img = cv2.resize(self.img, (int(self.width), int(self.hight)),
                     interpolation=cv2.INTER_AREA)

    def draw_circle(self,name):     #check
        img=self.img
        b_img=self.img
        cv2.circle(b_img,(int(self.y),int(self.x)),20,(0,0,255),-1)
        cv2.imwrite("D:/source/vscode/python_project/check_img/buf_"+ name +".jpg", b_img)
        self.img=img

def read_directory(directory_name): #check

   for filename in os.listdir(directory_name):

        name_string = (directory_name + "/" + filename)

        buf=IMG(name_string,filename)
        buf.img_shape()
        buf.create_sift()
        img.append(buf)

#button_show=True

def drawKeyPoint(img_2, kp_2, img_1,kp_1, Three,save_img):
    print("len : ",len(Three))
        # Four
    img_out = cv2.drawMatches(img_2, kp_2, img_1,kp_1, Three[:], None, flags=2)
                                                    #畫特定kp    特徵點是否要畫
    showIMG("img_out", img_out)
    print("key point match len : ",len(Three))
    cv2.imwrite("D:/source/vscode/python_project/check_img/out_img_"+str(save_img) +".jpg", img_out)

def showCutIMG(img_1,img_2,save_img):
    print("save img : ",save_img,"\n")
    cv2.imwrite("D:/source/vscode/python_project/check_img/big_"+str(save_img)+".jpg", img_1)
    cv2.imwrite("D:/source/vscode/python_project/check_img/small_"+str(save_img) +".jpg", img_2)


def sift_ahash(img_1,img_2):
    save_img=0
    IMG_1=img_1
    IMG_2=img_2

    match=bf.match(IMG_2.des,IMG_1.des)
    match = sorted(match, key=lambda x: x.distance)

    catch_match=5
    IMG_1_Point = np.zeros((5,2))
    IMG_2_Point = np.zeros((5,2))

    point_index=0
    match_index=0
    match_list=[]
    while(point_index<catch_match):
        x, y = IMG_1.kp[match[match_index].trainIdx].pt
        a, b = IMG_2.kp[match[match_index].queryIdx].pt

        same=False
        for i in range(point_index):
            IMG_1_x_first, IMG_1_y_first = IMG_1.kp[match[i].trainIdx].pt
            IMG_2_x_first, IMG_2_y_first = IMG_2.kp[match[i].queryIdx].pt
            gap=50
            if((abs(x-IMG_1_x_first)<gap) & (abs(y-IMG_1_y_first)<gap))|( (abs(a-IMG_2_x_first)<gap) & (abs(b-IMG_2_y_first)<gap)):
                match_index += 1
                same=True
                break

        if(same):   continue

        IMG_1_Point[point_index][0] = x
        IMG_1_Point[point_index][1] = y
        IMG_2_Point[point_index][0] = a
        IMG_2_Point[point_index][1] = b

        match_list.append(match_index)
        match_index += 1
        point_index += 1


    Three = []
    for i in range(catch_match):
        Three.append(match[match_list[i]])

    #drawKeyPoint(IMG_2.img, IMG_2.kp, IMG_1.img,IMG_1.kp, Three,save_img)       #畫兩張關鍵點匹配位置

    Found = False
    count=0
    scale_index=0


    for flag_one in range(catch_match):
        for flag_two in range(flag_one+1, catch_match):

            count+=1
            select_point = [0, 1, 2, 3, 4]
            select_point.pop(4-flag_one)
            select_point.pop(4-flag_two)

        # < test angle >

            Not_Use_One = 4-flag_one
            Not_Use_Two = 4-flag_two
            Similar = test_rectangle(IMG_1_Point,IMG_2_Point, select_point)

            #print("similar")
            if not(Similar): continue

            Same_angle = test_angle(IMG_1_Point, IMG_2_Point, select_point)                                                # < 角度 >

            #print("angle")
            if not(Same_angle):            continue

        # < test LU ratio >

            Left,Up,Right,Down=Find_LU(IMG_1_Point,select_point)
            BUF_one=BUF_IMG(IMG_1.img,IMG_1.width,IMG_1.hight,IMG_1.area,Left,Up,Right,Down)
            Left,Up,Right,Down=Find_LU(IMG_2_Point,select_point)
            BUF_two=BUF_IMG(IMG_2.img,IMG_2.width,IMG_2.hight,IMG_2.area,Left,Up,Right,Down)

        # < test scale >

            long_ratio =  vector(IMG_1_Point,IMG_2_Point,select_point)

            #print("long_ratio : ",long_ratio)

            new_scale=(sqrt(long_ratio))

            #print("new_scale : ",new_scale)

            if(new_scale>=1):
                BUF_one.resize_total(new_scale**(-1))
            else:
                BUF_two.resize_total(new_scale)


            if(BUF_one.up>BUF_two.up):
                tem_up=BUF_two.up
            else:
                tem_up=BUF_one.up

            if((BUF_one.hight-BUF_one.down)>(BUF_two.hight-BUF_two.down)):
                tem_down=BUF_two.hight-BUF_two.down
            else:
                tem_down=BUF_one.hight-BUF_one.down

            if((BUF_one.left)>(BUF_two.left)):
                tem_left=BUF_two.left
            else:
                tem_left=BUF_one.left

            if((BUF_one.width-BUF_one.right)>(BUF_two.width-BUF_two.right)):
                tem_right=BUF_two.width-BUF_two.right
            else:
                tem_right=BUF_one.width-BUF_one.right

            tem_up=int(tem_up)
            tem_down=int(tem_down)
            tem_right=int(tem_right)
            tem_left=int(tem_left)


            b_l=int(BUF_one.left)
            b_u=int(BUF_one.up)
            b_r=int(BUF_one.right)
            b_d=int(BUF_one.down)

            h_1=b_u-tem_up
            w_1=b_l-tem_left
            h_2=b_d+tem_down
            w_2=b_r+tem_right

            if(h_1>h_2):         continue
            if((h_2-h_1)<50):    continue           #  <====  可調
            if(w_1>w_2):         continue
            if((w_2-w_1)<50):    continue           #  <====  可調

            IMG_one=BUF_one.img[h_1:h_2,w_1:w_2]

            b_l=int(BUF_two.left)
            b_u=int(BUF_two.up)
            b_r=int(BUF_two.right)
            b_d=int(BUF_two.down)

            h_1=b_u-tem_up
            w_1=b_l-tem_left
            h_2=b_d+tem_down
            w_2=b_r+tem_right

            if(h_1>h_2):         continue
            if((h_2-h_1)<50):    continue                       #  <====  可調
            if(w_1>w_2):         continue
            if((w_2-w_1)<50):    continue                       #  <====  可調

            IMG_two=BUF_two.img[h_1:h_2,w_1:w_2]


            #showCutIMG(IMG_one,IMG_2,save_img)

            dis=cam_hash(a_hash(IMG_one),a_hash(IMG_two))
            #print("dis : ",dis)
            if(dis<10):
                if(BUF_one.area>BUF_two.area):
                    return True, True
                else:
                    return True, False
            save_img+=1

    return False,False


class classification:
    def __init__(self,img):
        self.same=[img]
        self.img_count=1
    def save_img(self,index,big_small):         #check
        if(big_small):
            self.same.insert(0,index)
        else:
            self.same.append(index)
        self.img_count+=1

    def union(self,buf_classification):         #check
        buf=buf_classification.same.pop()
        self.same+=buf_classification.same
        self.same.insert(0,buf)
        self.img_count+=buf_classification.img_count



def PRINT_GROUP(buf_list):                      #check
    print("\n")
    for i in range(len(buf_list)):
        print("Group ",i," : ",end="")
        for buf in buf_list[i].same:
            print(buf.filename," ",end="")
        print("")
    print("\n")

def transfer_filename( buf_filename):
    dot_count=buf_filename.find(".")
    buf_filename=buf_filename[:dot_count+1]+"jpg"
    return buf_filename
#============================================================================================



class MainWindow_controller2(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.setup_control()
        self.IsStore=0
        
    def setup_control(self):
        
       self.ui.statusBar.showMessage("Ready", 5000)
       self.ui.action_11.triggered.connect(self.save_group)
       self.ui.action_11.setToolTip("保存（Ctrl+S)")
       self.ui.action_5.setToolTip("新建（Ctrl+N)")
       self.ui.action_10.setToolTip("打開資料夾（Ctrl+O)")
       self.ui.action_10.triggered.connect(self.openFile)
       self.ui.action_6.setToolTip("執行（F5)")
       self.ui.action_15.setToolTip("全屏幕模式（F11)")
       self.ui.action.setToolTip("最小化（F12)")
       self.ui.action_4.setToolTip("退出（Ctrl+Q)")
       self.ui.action_4.triggered.connect(self.close)
       self.ui.action_15.triggered.connect(self.showFullScreen)
       self.ui.action.triggered.connect(self.showMaximized)
       self.ui.toolBar.addWidget(self.ui.lineEdit)
       
       self.ui.pushButton.clicked.connect(self.addcolumn)
       self.ui.pushButton_2.clicked.connect(self.deletecolumn)
       self.ui.pushButton_3.clicked.connect(self.hidegrid)
       self.ui.pushButton_4.clicked.connect(self.showgrid)
       self.ui.pushButton_5.clicked.connect(self.addrow)
       self.ui.pushButton_6.clicked.connect(self.deleterow)
       self.ui.pushButton_7.clicked.connect(self.resizeRowColumn)
       self.ui.pushButton_8.clicked.connect(self.recoverRowColumn)
       self.ui.pushButton_9.clicked.connect(self.hideVerticalHeader)
       self.ui.pushButton_10.clicked.connect(self.showVerticalHeader)
       self.ui.pushButton_11.clicked.connect(self.hideHorizontallHeader)
       self.ui.pushButton_12.clicked.connect(self.showHorizontallHeader)

      # self.ui.statusBar.addPermanentWidget(self.ui.lineEdit)
       print("\n\nshow block\n")
       CF_len=len(class_list.CF_list)
       print("global CF_list len: ",len(class_list.CF_list))
       
         
       row_i=col_j=0
       
       for buf_group in class_list.CF_list:
          item = QtWidgets.QTableWidgetItem()
          self.ui.tableWidget.setVerticalHeaderItem(row_i, item)
          item = self.ui.tableWidget.verticalHeaderItem(row_i)
          #group_string="group"+str(i)
          #item.setText(_translate("mainWindow", group_string))
          for buf_img in buf_group.same:
              
              self.ui.tableWidget.setIconSize(QSize(150,150))
              self.ui.tableWidget.setColumnWidth(col_j, 150)
              self.ui.tableWidget.setRowHeight(row_i, 150)
              rootpath = buf_img.name
              buf_filename=buf_img.filename
              item = QtWidgets.QTableWidgetItem(QIcon(rootpath),"")
              self.ui.tableWidget.setItem(row_i,col_j,item)
              col_j+=1 
          row_i+=1
          col_j=0
       print("group i : ",row_i)
       
       row_i=int(row_i)
       for row in range(1,50):
           if(row<row_i):   
               self.ui.tableWidget.showRow(int(row))
           else:
               self.ui.tableWidget.hideRow(int(row))
#       self.ui.tableWidget.hideRow(6)
#       self.ui.tableWidget.hideRow(7)
#       self.ui.tableWidget.hideRow(8)
    def addrow(self):
        if(self.IsStore==1):
            self.IsStore=0
            return
        row_count = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_count)
        self.IsStore+=1
    
    def deleterow(self):
        if(self.IsStore==1):
            self.IsStore=0
            return
        row_count = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.removeRow(row_count-1)
        self.IsStore+=1
        
    
    def addcolumn(self):
        if(self.IsStore==1):
            self.IsStore=0
            return
        column_count = self.ui.tableWidget.columnCount()
        self.ui.tableWidget.insertColumn(column_count)
        self.IsStore+=1
    
    def deletecolumn(self):
        if(self.IsStore==1):
            self.IsStore=0
            return
        column_count = self.ui.tableWidget.columnCount()
        self.ui.tableWidget.removeColumn(column_count-1)
        self.IsStore+=1

    def hidegrid(self):
        if(self.IsStore==1):
            self.IsStore=0
            return
        self.ui.tableWidget.setShowGrid(False)
        self.IsStore+=1
    
    def showgrid(self):
        if(self.IsStore==1):
            self.IsStore=0
            return
        self.ui.tableWidget.setShowGrid(True)
        self.IsStore+=1
    
    def resizeRowColumn(self):
        if(self.IsStore==1):
            self.IsStore=0
            return
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()
        self.IsStore+=1
    
    def recoverRowColumn(self):
        if(self.IsStore==1):
            self.IsStore=0
            return
        row_i=col_j=0
        for row_i in range(15):
          item = QtWidgets.QTableWidgetItem()
          self.ui.tableWidget.setVerticalHeaderItem(row_i, item)
          item = self.ui.tableWidget.verticalHeaderItem(row_i)
          #group_string="group"+str(i)
          #item.setText(_translate("mainWindow", group_string))
          for col_j in range(100):
              self.ui.tableWidget.setColumnWidth(col_j, 150)
              self.ui.tableWidget.setRowHeight(row_i, 150)
          self.IsStore+=1
        
    def hideHorizontallHeader(self):
        if(self.IsStore==1):
            self.IsStore=0
            return
        self.ui.tableWidget.horizontalHeader().setVisible(False)
        self.IsStore+=1
        
    def showHorizontallHeader(self):
        if(self.IsStore==1):
            self.IsStore=0
            return
        self.ui.tableWidget.horizontalHeader().setVisible(True)
        self.IsStore+=1
        
    def hideVerticalHeader(self):
        if(self.IsStore==1):
            self.IsStore=0
            return
        self.ui.tableWidget.verticalHeader().setVisible(False)
        self.IsStore+=1
        
    def showVerticalHeader(self):
        if(self.IsStore==1):
            self.IsStore=0
            return
        self.ui.tableWidget.verticalHeader().setVisible(True)
        self.IsStore+=1
        

    def save_group(self):
        if(self.IsStore>=1):
            self.IsStore=0
            return
        print("\nstart store img\n")
        now = datetime.now()
        current_time = now.strftime(" %m %d %Y %H %M %S")

        download_dir="C:/Users/User/Downloads/"+str("Classification")+current_time
        
        #C:/Users/User/Downloads
        try :
            os.mkdir(download_dir)
        except:
            print("exist ")

        
       
        G=0
        
        for group in class_list.CF_list:
            buf_dir=download_dir+"\Group"+str(G)
            #print("\nreate dir : ",buf_dir," ====>   \n")
            os.mkdir(buf_dir)
            for buf_img in group.same:
                store_img=cv2.imread(buf_img.name)
                #print("store img shape : ",store_img.shape)
                buf_filename=transfer_filename(buf_img.filename)
                #print("store img filename : ",buf_filename)
                #D:/store_img
                cv2.imwrite(buf_dir+"/"+str(buf_filename), store_img)
            G+=1
        print("store img end")
        self.IsStore+=1
       
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())
    
    def readFile(self):
      
        print("read file  ")
        start=time.time()
                    #D:/source/vscode/python_project/test_file
                    #C:/Users/howar/Downloads/differ_size
        read_directory("D:/test_img")                       #      <===  input   <====================
        end=time.time()


        total_input_time=end-start
        print("total input time : ",total_input_time)
        print("\n\n\n")
        
        for i in img:
            print(i.name)
        print("\n\n\n")
    
    def openFile(self):
       # self.clicked_counter += 1
        #print(f"You clicked {self.clicked_counter} times.")
        if(self.IsStore>=1):
            self.IsStore=0
            return
        filepath = QFileDialog.getExistingDirectory(self, "请选择文件夹路径", "D:\\Qt_ui")
        print(filepath)
        self.IsStore+=1
    
    
    
    def IMG_match(self):
        start=time.time()

        img_len=len(img)
    
        list_classification=[]
        for i in range(len(img)):
    
            #print("img name : ",img[i].filename)
            IsClass=False
            for index in range(len(list_classification)):
                IsSame , IsBig=sift_ahash(img[i],list_classification[index].same[0])
                if(IsSame):
                    IsClass=True
                    list_classification[index].save_img(img[i],IsBig)
                    if(IsBig):
                        pop_list=[]
                        for buf_index in range(index+1,len(list_classification)):
                            buf_Same,buf_Big=sift_ahash(list_classification[buf_index].same[0],list_classification[index].same[0])
                            if(buf_Same & (buf_Big==False)):
                                #print("================RE_Group==============")
                                list_classification[index].union(list_classification[buf_index])
                                pop_list.append(buf_index)
                        for idx in sorted(pop_list, reverse = True):
                            del list_classification[idx]
    
                    break
    
            if not(IsClass):
                buf = classification(img[i])
                list_classification.append(buf)
            #PRINT_GROUP(list_classification)
    
        del img[:]
    
        end=time.time()
        classification_time = end - start
        print("classification input time : ",classification_time)
    
    
    
        #now = datetime.now()
        #current_time = now.strftime("%H_%M_%S")
       # path='D:/source/vscode/python_project/classificaton'+'_'+str(current_time)+'.txt'
       #path='D:/classificaton.txt'
       #f=open(path,'w')
       
       
    
        group_index=0
        for tem_class in list_classification:
            buf=[]
            if(group_index<10):
                group_string='Group'+str(group_index)+"  : "
            else:
                group_string='Group'+str(group_index)+" : "
    
            buf.append(group_string)
            for buf_img in tem_class.same:
                buf.append(buf_img.filename)
                buf.append(" ")
            buf.append('\n')
            print(buf)
            #f.writelines(buf)
            group_index+=1
       # f.close()

        print("end")
    
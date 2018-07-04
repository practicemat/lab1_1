#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 13:15:44 2018

@author: Dmitry
"""

import numpy
import math
import lab1_1


def main():
    e = [1,2,3,4,5,9,11,12,13,14]
    #e = [2,3,4,5,9,11,12,13,14]
    numb = lab1_1.number()
    if (numb in e):
        with open("data.tsv") as dataFile:
            a, b, c = dataFile.readline().split("\t")
        a = float(a)
        b = float(b)
        c = float(c)
        
    else:
        with open("data.tsv") as dataFile:
            a, b, c, d = dataFile.readline().split("\t")
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        
    
    numb -= 1
    f = open('var.txt')
    line = f.readlines()
    dger = (line[numb]) 

    
    x = lab1_1.rangex()

    yer = lab1_1.func()

    ger = eval(dger)



    list4 = []
    odin = []




    for i in range(len(ger)):
        if (math.isnan(ger[i]) != True):
            if ((yer[i] != ger[i])):
                odin.append(ger[i]);




    if (odin == list4): 
        print('одинаковые')
        
    else: 
        print('разные')
        raise ValueError('Графики разные!')
        



main()

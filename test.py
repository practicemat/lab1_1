#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy
import math
import lab1_1


def main():
    varParam = [2,3,4,5,9,11,12,13,14]
    numb = lab1_1.number()
    if (numb in varParam):
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
    funcLine = (line[numb])

    
    x = lab1_1.rangex()

    studentFunc = lab1_1.func()

    correctFunc = eval(funcLine)



    nullArray = []
    graphArray = []




    for i in range(len(correctFunc)):
        if (math.isnan(correctFunc[i]) != True and math.isnan(studentFunc[i]) != True):
            if ((studentFunc[i] != correctFunc[i])):
                graphArray.append(correctFunc[i]);




    if (graphArray == nullArray):
        print('одинаковые')
        
    else: 
        print('разные')
        raise ValueError('Графики разные!')
        



main()

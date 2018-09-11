#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import matplotlib.pyplot as pypl
import numpy

def rangex():
    return numpy.arange(-2, 2, 0.02)

def number():
    return 5

def func():
    with open("data.tsv") as dataFile:
        a, b, c = dataFile.readline().split("\t")
    a = float(a)
    b = float(b)
    c = float(c)
    x = rangex()
    y = a * numpy.log((x)/(b + (c * x)))
    return y



def main():
    
    x = rangex()
    myFunc = func()
    
    pypl.plot(x, myFunc)
    pypl.xlabel(r"$x$")
    pypl.ylabel(r'$y$')
    pypl.title(r"$a * ln(x/(c * x + b)$")
    return myFunc



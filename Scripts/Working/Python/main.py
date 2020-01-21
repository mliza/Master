#!/usr/local/bin/python3.7

#Python Packages 
import sys 
import os 
import numpy as np
import sympy as sp 
from sympy.interactive import printing 


pythonFile = os.path.abspath(__file__)
pythonFolder = os.path.dirname(pythonFile)
scriptsFolder = os.path.abspath(os.path.join(pythonFolder,"../")) 
sys.path.insert(0, os.path.join(scriptsFolder, 'Matlab/'))
sys.path.insert(0, os.path.join(pythonFolder, 'Packages/'))

#My Packages 
#import generalPurpose as genPurp
#import eqSolvers 
import productivity 
import transformations as trans 
#productivity.matlabInPython('plotFunctionBasic')
#print(dir(trans.Rotations))
x = [20000, 55000, 133000]
tesInstance = trans.Rotations(x)
print(x) 
print(tesInstance.ECEF2LLA())
print(trans.Rotations(tesInstance.ECEF2LLA()).LLA2ECEF() ) 

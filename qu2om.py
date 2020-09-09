import numpy as np 
import math
import pytest
#This function takes in a unit quarternion and outputs corresponding passive rotation matrix
def qu2om(q):
    val = q[0]**2 - (q[1]**2+q[2]**2+q[3]**2)
    A = np.eye(3)
    p=-1
    A[0][0]=val+2*q[1]**2
    A[1][1]=val+2*q[2]**2
    A[2][2]=val+2*q[3]**2
    A[0][1]=2*(q[1]*q[2]-p*q[0]*q[3])
    A[1][0]=2*(q[1]*q[2]+p*q[0]*q[3])
    A[0][2]=2*(q[1]*q[3]+p*q[0]*q[2])
    A[2][0]=2*(q[1]*q[3]-p*q[0]*q[2])
    A[1][2]=2*(q[2]*q[3]-p*q[0]*q[1])
    A[2][1]=2*(q[2]*q[3]+p*q[0]*q[1])
    return A
def test_case1():
    expect = np.eye(3)
    i = np.array_equal(qu2om([1,0,0,0]),expect)
    assert i==True
def test_case2():
    expect = np.eye(3)
    expect[0][0]=-1
    expect[1][1]=-1
    i = np.array_equal(qu2om([0,0,0,1]),expect)
    assert i==True

#print(qu2om([0,0,0,1]))
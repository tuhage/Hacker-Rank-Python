#!/bin/python3

import os
import sys
#
# Complete the virusIndices function below.
#

flag=True
def compare_strings(s1,s2):
    global flag
    sum_err=0
    for j in range(len(s1)):
        if(sum_err>1):
            return False
        if s1[j]!=s2[j]:
            sum_err+=1

    if sum_err<=1:
        flag=False
        return True
   
def recursive_check(pw,v,vlen,i):

    if len(pw)<=20:
        if(compare_strings(pw,v)):
            print(i,end=" ")
        return
    else:
        left_pw,right_pw=pw[0:vlen//2],pw[vlen//2:]
        left_v,right_v=v[0:vlen//2],v[vlen//2:]
        
        if left_pw!=left_v and right_pw!=right_v:
            return
        if left_pw!=left_v:
            recursive_check(left_pw,left_v,len(left_v),i)
        if right_pw!=right_v:
            recursive_check(right_pw,right_v,len(right_v),i)

def virusIndices(p, v):
    global flag
    flag=True
    plen,vlen=len(p),len(v)
    for i in range(plen-vlen+1):
        pw = p[i:i+vlen]
        if pw==v:
            flag=False
            print(i,end=" ")
        else:
            recursive_check(pw,v,vlen,i)
        
    if flag:
        print("No Match!")
    else:
        print()

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        pv = input().split()

        p = pv[0]

        v = pv[1]

        virusIndices(p, v)

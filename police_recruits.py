# -*- coding: utf-8 -*-
"""Police Recruits.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ti_EWZO3c6BAQLmp-f5cIJB6XcmDHhRZ
"""

n = int(input())
a = list(map(int, input().split()))
sum = 0
cnt = 0

for i in range (n):
  if a[i]>0:
    sum = sum+a[i]
  elif sum>0:
    sum = sum-1
  else:
    cnt = cnt+1

print(cnt)
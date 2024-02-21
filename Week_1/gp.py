#Date : 20/02/2024
#Name : Michael macharia
#This is a programme to show geometric progression in python

a=1
d=int(input( ))
for k in range (1,11):
    n=k
    m=n-1
    u=d**m
    y=[(a*u)]
    print(set(y),end =", ")
from itertools import permutations
t=input()
k=permutations(t)
s=[]
x=(-1)
a="abcdefghijklmnopqrstuvwxyz"
if a==t:
  print(t)
elif t==a[::-1]:
  print("-1")
else:
    t=tuple(t)
    for i in k:
        s.append(i)
    for i in s:
        if i>t:
            x=i
            break

    for i in s:
        if i>t and i<x:
            x=i
            
    if x==-1:
        print("-1")
    else:
        for i in x:
            print(i,end="")
    

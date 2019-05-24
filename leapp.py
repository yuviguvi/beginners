year = int (input("enter the year number:"))
if((year%400==0)or(year%4==0)and(year%100!=0)):
  print("yes")
else:
  print("no")  

import random

def randInt(min=0,max=0):
  if max == 0:
    max=100
  if min != 0:
    max-=min
  result=random.random()*max+min
  print(int(result))

randInt()  
randInt(max=50)
randInt(min=50)
randInt(min=50,max=500)
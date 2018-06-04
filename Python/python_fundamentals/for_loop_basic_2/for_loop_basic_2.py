# Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].

def biggie(arr):
    x = 0
    for i in arr:
        if i > 0:
            arr[x] = "big"
        x+=1
    return arr

print(biggie([1,1,1,-1,1,-1]))

# Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to b a positive number).

def countp(arr):
    x = 0
    for i in arr:
        if i > 0:
            x+=1
    arr[len(arr)-1] = x
    return arr 

print(countp([0,1,1,-1,1,-1,3,-3,7]))

# SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10

def sumt(arr):
    x = 0
    for i in arr:
        x+=i
    return x 

print(sumt([0,1,1,-1,1,-1,3,-3,7]))

# Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5

def avg(arr):
  x = 0
  for i in arr:
      x+=i
  return x/len(arr)

print(avg([1,2,3,4]))

# Length - Create a function that takes an array as an argument and returns the length of the array.  For example length([1,2,3,4]) should return 4

def leng(arr):
  x = len(arr)
  return x

print(leng([1,2,3,4]))

# Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

def mini(arr):
  x = 0
  min = arr[x]
  for i in arr:
      if i < min:
        min = i
        x+=1
  return min

print(mini([-9,4,1,-3,2,3,4,-7]))

# Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -3.

def maxi(arr):
  x = 0
  max = arr[x]
  for i in arr:
      if i > max:
        max = i
        x+=1
  return max

print(maxi([-9,4,1,-3,2,3,24,-7]))

# UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.

def ultianlz(arr):
  x = 0
  anlz = {}
  sum = 0
  l = len(arr)
  max = arr[x]
  min = arr[len(arr)-1]
  for i in arr:
      sum+=i
      if i > max:
        max = i
        x+=1
      if i < min:
        min = i
        x+=1
  avg = sum/l
  anlz['max']=max
  anlz['min']=min
  anlz['length']=l
  anlz['sumTotal']=sum
  anlz['Average']=avg
  return anlz

print(ultianlz([4,3,2,1,0,5]))

# ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

def revl(arr):
  x = 1
  l = (len(arr) / 2)+0.5
  for i in arr:
    if x >= l:
      break
    else:
      temp = arr[x-1]
      arr[x-1] = arr[len(arr)-x]
      arr[len(arr)-x] = temp
      x+=1
  return arr

print(revl([4,3,2,1,0]))
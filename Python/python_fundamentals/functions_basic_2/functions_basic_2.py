# Countdown - Create a function that accepts a number as an input.  Return a new array that counts down by one, from the number (as arrays 'zero'th element) down to 0 (as the last element).  For example countDown(5) should return [5,4,3,2,1,0].

def countd(x):
    q = []
    while x >= 0:
        q.append(x)
        x-=1
    print(q)

countd(5)

# Print and Return - Your function will receive an array with two numbers. Print the first value, and return the second.

def priret(x):
    print(x[0])
    return(x[1])

priret([6,7])

# First Plus Length - Given an array, return the sum of the first value in the array, plus the array's length.

def fpl(x):
    return x[0]+len(x)

print(fpl([17,0,0]))


# Values Greater than Second - Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value.  Print how many values this is.  If the array is only element long, have the function return False

def vgt2(x):
    count = 0
    q = []
    for var in x:
        if len(x) < 2:
            return "false"
        if var > x[1]:
            q.append(var)
            count+=1
        else:
            continue
    print(q)
    print(count)
    return q 

vgt2([1,2,5,3,7,1,4])

# This Length, That Value - Given two numbers, return array of length num1 with each value num2.  Print "Jinx!" if they are same.

def tltv(num1,num2):
    q = []
    i = num1
    while i > 0:
        if num1 == num2:
            return('Jinx!')
        else:
            len(q) < num1
            q.append(num2)
            i-=1
    return q

print(tltv(5,5))




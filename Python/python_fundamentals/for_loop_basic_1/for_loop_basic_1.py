# Basic - Print all the numbers/integers from 0 to 150.

for num in range(0,150):
    print("num is ",num)

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000,000.

for num in range(5,1000000,5):
    print("num is ",num)

# # Counting, the Dojo Way - Print integers 1 to 100.  If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".

for num in range(0,100):
    if num % 5 != 0:
        print(num)
    elif num % 10 == 0:
        print("Coding","Dojo")
    elif num % 5 == 0:
        print("Coding")
    
# # Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

def mtsh(x,y):
    count = 0
    for i in range(x,y):
        if i % 2 != 0:
            count += i
        else: 
            continue
    print(count)

print(mtsh(0,500000))

# # Countdown by Fours - Print positive numbers starting at 2018, counting down by fours (exclude 0).

for num in range(2018,0,-4):
    print(num)

# # Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a FOR loop.  For (2,9,3), print 3 6 9 (on successive lines)

def flex(x,y,z):
    for num in range(x,y,z):
        if num % z == 0:
            print(num)

flex(0,100,5)


# # PREDICTIONS

list = [3,5,1,2]
for i in list:
    print(i)

# # output = 3,5,1,2


list = [3,5,1,2]
for i in range(list):
    print(i)
    
# # output = type error

list = [3,5,1,2]
for i in range(len(list)):
    print(i)

# output = 0,1,2,3
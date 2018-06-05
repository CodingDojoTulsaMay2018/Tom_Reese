x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# How would you change the value 10 in x to 15?  Once you're done x should then be [ [5,2,3], [15,8,9] ].  

x[1][0]= 15
print(x)

# How would you change the last_name of the first student from 'Jordan' to "Bryant"?

students[0]['last_name']='Bryant'
print(students)

# For the sports_directory, how would you change 'Messi' to 'Andres'?

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# For x, how would you change the value 20 to 30?

z[0]['y'] = 30
print(z)


#1

def dictlist(dict):
  x=0
  y=0
  for key, val in dict[x].items():
     print(key, " = ", val)
     y+=1
  for key, val in dict[y].items():
     print(key, " = ", val, ",")
     y+=1

dictlist(students)

def dictlist(dict):
  x=0
  y=0
  for key, val in dict[x].items():
      for key, val in dict[y].items():
          print("My name is {} {} and I am years old.".format(dict[x], dict[y]))
          # x+=1
          # y+=1

dictlist(students)


#2


#3


#4

def DojoInfo(dojo):
  for i in dojo:
    print(len(dojo[i]),i.upper())
    for x in dojo[i]:
      print(x)
    print("")

DojoInfo(dojo)



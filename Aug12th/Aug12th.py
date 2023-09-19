#tuple
#declaring
print('tuple declaring')
tup = (1,2,3,4,5)
tuple1 = ()

#accessing
print('tuple accessing')
print(tup[0])

print(len(tup))

#loop
print('tuple loop')
tup_length = len(tup)

print('tuple loop using for index')
for i in range(0, tup_length):
    print(tup[i])

print('tuple loop using for item')
for item in tup:
    print(item)

#unpacking
print('tuple unpacking')
#swap 2 var in 1 line
a = 1
b = 2
a,b = b,a
print(a,b)


#list
#declaring
ls = [1,2,3,4,5]

#accesing
ls(ls[0])

#loop
for item in ls:
    print(item)
for i in range(0, len(ls)):
    print (item)

#list is mutable while tuple is immutable

#list/tuple of multi types
ls = ["1", 0, (1,34)]

tup2= (1,2,4,"4")

#set
#declaring
setX = {1,2,3,4,5}

#accessing: can not
#loop
for item in setX:
    print(item)


#dictionary
#declare
dictX = {"name":"X", "age":20, "address":"Hanoi"}

#accessing
print(dictX["name"])

dictX["address"] = 'Thanh Xuan'
dictX["Hobby"] = "Coding"

#loop
for key in dictX:
    print(key, dictX[key])
for key in dictX[key]:
    print(key, dictX[key])

for value in dictX:
    print(value, dictX[value])
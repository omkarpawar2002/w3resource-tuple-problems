#1.Write a Python program to create a tuple
'''
t = (10,20,30)
print(t)
'''

#2.Write a Python program to create a tuple with different data types.
'''
t1 = (10,20.23,True,'welcome',False)
print(t1)
'''

#3.Write a Python program to create a tuple of numbers and print one item.
'''
t = (10,20,30,40)
print(t[3])
'''

#4.Write a Python program to unpack a tuple into several variables.
'''
t = (10,20.23,'welcome',False)
a,b,c,d = t
print(a)
print(b)
print(c)
print(d)
'''

#5.Write a Python program to add an item to a tuple.
'''
t = (10,20,30,40)
print(t)
li = list(t)
li.append(100)
t = tuple(li)
print(t)
'''

#6.Write a Python program to convert a tuple to a string.
'''
t = (10,20,30,40)
print(t)
st = ''
for i in t:
    st += str(i)
print(st)
'''

#7.Write a Python program to get the 4th element from the last element of a tuple.
'''
t = (10,20,30,40,50,60,70)
print(t[-4])
'''

#8.Write a Python program to create the clone of a tuple.
'''
t = (10,20,30,40)
print(t,id(t))
new = t[::]
print(new,id(new))
'''

#9.Write a Python program to find repeated items in a tuple.
'''
t = (10,20,30,10,10)
d = {}
for i in t:
    if(i not in d):
        d[i] = 1
    else:
        d[i] += 1
for i,j in d.items():
    if(j>1):
        print(i)
'''

#10.Write a Python program to check whether an element exists within a tuple.
'''
t = (10,20,30,40)
print(10 in t)
'''

#11.Write a Python program to convert a list to a tuple.
'''
li = [10,20,30,40]
print(li,type(li))
t = tuple(li)
print(t,type(t))
'''

#12.Write a Python program to remove an item from a tuple.
'''
t = (10, 20, 30, 40)
print(t)
li = list(t)
li.remove(20)
t = tuple(li)
print(t)
'''

#13.Write a Python program to slice a tuple.
'''
t = (10,20,30,40,50,60,70,80,90,100)
print(t)
print(t[:2:])
print(t[::-1])
'''

#14.Write a Python program to find the index of an item in a tuple.
'''
t = (10, 20, 30, 40)
print(t.index(20))
'''

#15.Write a Python program to find the length of a tuple.
'''
t = (10, 20, 30, 40)
print("Length :- ",len(t))
'''

#16.Write a Python program to convert a tuple to a dictionary.
'''
key = (10,20,30,40)
value = ("ten","twenty","thirty","fourty")
d = dict(zip(key,value))
print(d)
'''

#17.Write a Python program to unzip a list of tuples into individual lists.
'''
li = [(100,12),(200,12),(300,12)]
print(li)
for i in li:
    print(list(i))
'''

#18.Write a Python program to reverse a tuple.
'''
t = (10,20,30,40,50)
print(t)
print(t[::-1])
'''

#19.Write a Python program to convert a list of tuples into a dictionary.

#20.Write a Python program to print a tuple with string formatting.
'''
t = (100, 200, 300)
print("This is a tuple :- ",t)
'''

#21.Write a Python program to replace the last value of tuples in a list.
'''
li =  [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new = []
for i in li:
    res = list(i)
    res[-1] = 100
    new.append(tuple(res))
print(new)
'''

#22.Write a Python program to remove an empty tuple(s) from a list of tuples.
'''
li = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
li = [i for i in li if(i)]
print(li)
'''

#23.Write a Python program to sort a tuple by its float element.
'''
li = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print(li)
li = sorted(li,reverse=True)
print(li)
'''

#24.Write a Python program to count the elements in a list until an element is a tuple.
'''
li = [10,20,30,40,50,(10,20,30),101]
count = 0
for i in li:
    if(type(i) != tuple):
        count += 1
    else:
        break
print(count)
'''

#25.Write a Python program to convert a given string list to a tuple.
'''
st = "python 3.0"
print(st,type(st))
s = ''
for i in st:
    if(i != ' '):
        s += i
final = tuple(s)
print(final)
'''

#26.Write a Python program to calculate the product, multiplying all the numbers in a given tuple.
'''
t = (4, 3, 2, 2, -1, 18)
mul = 1
for i in t:
    mul *= i
print("Product - multiplying all the numbers of the said tuple: -",mul)
'''

#27.Write a Python program to calculate the average value of the numbers in a given tuple of tuples
'''
t = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
a,b,c,d = t[0],t[1],t[2],t[3]
li = []
for i in range(len(a)):
    li.append((a[i]+b[i]+c[i]+d[i])/4)
print(li)
'''

#28.Write a Python program to convert a tuple of string values to a tuple of integer values.
'''
t = (('333', '33'), ('1416', '55'))
print(t)
t1 = []
for i in t:
    num = []
    for ele in i:
        num.append(int(ele))
    t1.append(tuple(num))
t = tuple(t1)
print(t)
'''

#29.Write a Python program to convert a given tuple of positive integers into an integer.
'''
t = (1, 2, 3)
s = ''
for i in t:
    s += str(i)
print(int(s))
'''

#30.Write a Python program to check if a specified element appears in a tuple of tuples.
'''
t = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
ele = 'Olive'
final = any((ele in sub for sub in t))
print(final)
'''

#31.Write a Python program to compute the element-wise sum of given tuples.


#32.Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples.
'''
li = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
li = [sum(ele) for ele in li]
print(li)
'''

#33.Write a Python program to convert a given list of tuples to a list of lists.
'''
li = [(1, 2), (2, 3), (3, 4)]
print(li)
li = [list(i) for i in li]
print(li)    
''' 





































































































































































































































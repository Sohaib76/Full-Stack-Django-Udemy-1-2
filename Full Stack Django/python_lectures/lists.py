'''
VERY IMP
'''
l = [1,2,3,4]
def xyz(l):
    c = [l[0]] + [l[3]] + [l[2]]
    return c

#to print 0th 3rd and 2nd index of list with this order
#output >>>  [1,4,3]



newList = list1 + list2
list = string.split()        #>>> string with spaces become list
if 'a' not in list:
    print "noo"
for i in list:
    print i           #print all line by line






myList = ['ads',2,1.2]         #lists creation  can add list into list.

print(myList)        #len(myList) for length of the list
del (myList(0))    # delete the item at 0th index

#myList[0]  for index of the list

myList[0] = 'New Item'

myList.append("new")   #this will add new item to the end of the list

newList = ['x','y',"z"]
myList.extend(newList)         # to extend the current list Output = ['ads',2,1.2,x,y,z]

myList.pop()   # can remove last item from the list and can return it after saving in a variable
myList.pop(1)  #removes second item from the list
myList.reverse()  #to reverse the list

lis = [1,2,5,4,3,7,6]
lis.sort()
lis.count(3)    #how many times three is used
lis.index(3)      #for index of three
len(lis)
min(lis)   #out  1
max(lis)    #out  7
print(lis)  # to sort the list alphabatically & numerically


####### Nested List ###########
nest = [1,2,['x','y']]

print(nest[2])
#output:  ['x','y']

print(nest[2][0])
#output: 'x'


#for loops for lists
matrix = [[1,2,3],[4,5,6],[7,8,9]]

first_col = [row[0] for row in matrix]

print(first_col)   #output 1,4,7




########## Tuples #############
#just like lists but they are immutable means that they can't changed
#.append is not used in tuple

tuple = (1,2,3)
print(tuple[2])

tuple = ('a',True,2)

t[0] = 'new'  #error

#other way to add item  to Tuples
tuple2 = ("new item",)
tuple3 = tuple + tuple2

#output  ('a',True,2,"new item")

#tuple support add
tuple3 = tuple[0:2] + tuple2

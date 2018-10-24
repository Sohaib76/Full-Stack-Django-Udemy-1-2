#They do not have any order
#Hash Tables
#Key value pairs


my_dict = {"key1":"value","Key2":"value2"}
print(my_dict['key1'])


my_nested_dict = {"key1":123,"key2":"value","key3":{'123':[1,2,'grabb']}}
#if we want to print grabb
print(my_nested_dict['key3']['123'][2])       #can use upper() like methods after [2]


my_stuff = {'lunch':'pizza','bfast':'bread'}
#toadd new item in dictionary
my_stuff['dinner'] = 'burger'
#to change an Item
my_stuff['lunch'] = 'chicken'
print(my_stuff)


#### if statements #########
if 3==3:
    print('good')
elif 4>2:
    print('cac')
else:
    print(33)

##### For Loops  ##########
seq = [1,2,3,4]

for item in seq:
    print(item)    #output  1,2,3,4
    print('hello')  #output  'hello','hello','hello','hello'

#together >>  'hello'
    #            '1'...


dic  = {'key':1,'key2':2}
for k in dic:    #.values , .keys
    print(k)
    print(dic[k])

#output key and value pairs

### Unordered collection of unique keyword

my_set = set()

my_set.add(1)
my_set.add('p')

print(my_set)             # output {1,'p'}

# sets will ignore same elements
my_set.add('5')
my_set.add('5')


print(my_set)       # '5 will be output only one time.'


#converting a list into set >> will print same no only one time
converted = set([1,1,1,2,2,3,3,3])
print(converted)               #(output {1,2,3})



###SCOPE###

# to reach the global variable in a function
# global x = "new value"   to change the value of x globally

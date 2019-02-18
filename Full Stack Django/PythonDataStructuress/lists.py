'''Strings are not mutable '''
#.lower()
#methods donot changes strings they just make a copy of it, unlike lists


'''list are mutable '''
#methods changes lists unlike strings
#range returns list

friends = ['aa','bb']
for i in range(len(friends)):
    friend = friends[i]
    print("Happy Birthday",friend)

#Algorithms: A set of rules used to solve a problem
#DataStructures: Particular way of organizing data in computer

#List methods
'''count, append, concatenation, slicing, sort, insert, len, max, min , sum '''
new = list()  # empty list
new.append('sf')
print(new)

#list and strings
l1 = "ASD ASF     POI"
s = l1.split()   #split(';')  default is space(multipe spaces)
print(s)

file = open('test.txt')
for line in file:
    q = line.rstrip()
    if not q.startswith("From"): continue
    w = q.split()
    print(w[1])

# Can Do Double Splitting

#guardian
if len(w) < 1:  #3
    continue

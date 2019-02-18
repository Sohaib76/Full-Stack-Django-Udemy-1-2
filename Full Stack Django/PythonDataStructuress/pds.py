
print(" Do not give up. ")


#Reading and writing on a file
#A line is a series of string characters
#l = open('test.txt')

fl = open('test.txt')
for l in fl:
    print(l)

'''fileName = input("Enter file name: ")
try:
    l = open(str(fileName))

except:
    print("The file  cannot be opened")
    quit()'''
count = 0
for s in l:
    if s.startswith("From"):
        count += 1
#print("There are {} gmails in {}".format(count,fileName))




for e in l:
    if not 'Python' in e:
        continue
    e = e.rstrip()
    print(e)


for i in l:
    if i.startswith("From"):
        # new line is considered white space so stripped
        i = i.strip()
        print(i)

# print Statement adds a new line to each line

# Continue is skip

#n = l.read()
#print(n)


'''for i in l:
   print(i)'''

coun = 0
for l in l:
    coun  = coun +1
print("Lines: ",coun)



#default is r.
#r for Reading
#w for write


print("x\ny")
print(len("x\ny"))       #3  \n is one character


# Use the file name mbox-short.txt as the file name
av = 0
count = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue

    x = line.find('0')
    w = line.find('5')
    y = line[x:]
    sc = float(y)
    count = count +1
    av = av + sc


print("Average spam confidence:",av/count)

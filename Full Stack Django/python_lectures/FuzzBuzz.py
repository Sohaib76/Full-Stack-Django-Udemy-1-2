counter = 0
while counter<101:

    if counter%3==0:
        print (counter, "Fuzz")
    elif counter%5==0:
        print(counter ,"Buzz")
    elif (counter%3==0) and (counter%5==0):
        print(counter, "FuzzBuzz")
    else:
        print (counter)



    counter +=1

#escape sequences
print("\"")   #out "
#\n for new line,   \t for tab ,  \'  and \a for sound


input("Enter ")


#type converters
int("24")
#out 24 as int


# No floordivision operations can be performed on strings

print(2+2)

string_with_double_quotes = "Joker"
string_with_one_quote = 'Hacker'

print(string_with_double_quotes[2])

print(string_with_one_quote[2])

# I think that "" and '' are same.
# (-1) use for last number.

print(string_with_one_quote[2:])        #string from 2 to last output ker
print(string_with_one_quote[:3])        #strings before 3      output Hac
print(string_with_one_quote[2:5])       #strings 2 from 4
print(string_with_one_quote[:])         #take all strings

print(string_with_one_quote[::2])       #output:  Hce       use one and skip one and use one

#string cannot be indexed and changed

x = string_with_one_quote.upper()   #All UpperCase
# string_with_one_quote.capitalize()         >>    firstLetter capitalize

#spit()   >>  returns array in string  Hello World like ['Hello', 'World']

print(string_with_one_quote.split('a'))    # Output: ['H','cker']

#return the index of the string
print(string_with_one_quote.find('a'))
#replace the a string with 0
print(string_with_one_quote.replace('a','0'))
#count the a in string
print(string_with_one_quote.count('a'))

#reverse the strings
print(string_with_one_quote[::-1])


#Print formatting
x = "Item One: {x} Item Two: {y}".format(x="dog",y="cat")          #Don't Know what it is...
print(x)


#Floor divsion
5/2 # output 2.5
5//2 # output 2

#multiplying strings
x = 'helloYou'
x*3 # output helloYouhelloYouhelloYou           x**3  is error


print("hello"+""+"world")   #"" no space




# to break down the string into many characters of list
#to convert a string into a list
s = '1 2 3'
print(s.split())






#Check for even and odd

def xyz(a):
    if a%2==0:
        return ("yes")
    else:
        return ("no")

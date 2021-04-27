#!/usr/bin/env python
# coding: utf-8

# # Built-in Functions

# In[18]:


# for this class I will spend 30 mins every day 
# no need to do more than 30 mins 
# as it go with the time it'll  be easy by the time 
# go slowly and take your time 
# HOME IS NOT FOR REST IT'S FOR TREANING 
# The Python interpreter has a number of functions and 
# types built into it that are always available. They are listed
# let's try some of them : 

# integer number abs is a function that reurn the absolutlay values of the numbers 
# القيمة المطلقة 
num = -5
print('Absolute value of -5 is:', abs(num))
# floating number
fnum = -1.45
print('Absolute value of 1.45 is:', abs(fnum))
bin(100) # change to scinn 
HERE = ("https://docs.python.org/3.10/library/functions.html#abs")
print("click",HERE)


# # Built-in Constants¶
# 

# In[22]:


import re 
s =re.split(r'\W+', 'Words, words, words.')
s


# In[23]:


s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
s1


# In[38]:


from difflib import SequenceMatcher
a = "qabxcd"
b = "abycdf"
s = SequenceMatcher(None, a, b)
for tag, i1, i2, j1, j2 in s.get_opcodes():
    print('{:7}   a[{}:{}] --> b[{}:{}] {!r:>8} --> {!r}'.format(tag, i1, i2, j1, j2, a[i1:i2], b[j1:j2]))


# In[35]:


import textwrap 
textwrap.shorten("Hello  world!", width=12)


# # unicodedata — Unicode Database

# In[58]:


import unicodedata 
s = unicodedata.lookup('LEFT CURLY BRACKET')
a = unicodedata.lookup('RIGHT CURLY BRACKET')#print the name of the uncodedata
print ("LEFT CURLY BRACKET : ",s) #
"""
uncodedata is a function reuton the name of the unicode data.....
"""
print ("RIGHT CURLY BRACKET",a)


# In[42]:


s = unicodedata.category('A')   #print the name of the uncodedata
print("# 'L'etter, 'u'ppercase: ",s)


# In[45]:


s = unicodedata.category('a')  #print the name of the uncodedata
s


# In[46]:


unicodedata.decimal('9') #print the name of the uncodedata


# In[47]:


unicodedata.name('/') #print the name of the uncodedata


# In[50]:


unicodedata.name('%') #print the name of the uncodedata


# In[59]:


# readline — GNU readline interface
import atexit
import code
import os
import readline

class HistoryConsole(code.InteractiveConsole):
    def __init__(self, locals=None, filename="<console>",
                 histfile=os.path.expanduser("~/.console-history")):
        code.InteractiveConsole.__init__(self, locals, filename)
        self.init_history(histfile)

    def init_history(self, histfile):
        readline.parse_and_bind("tab: complete")
        if hasattr(readline, "read_history_file"):
            try:
                readline.read_history_file(histfile)
            except FileNotFoundError:
                pass
            atexit.register(self.save_history, histfile)

    def save_history(self, histfile):
        readline.set_history_length(1000)
        readline.write_history_file(histfile)


# In[7]:


from Zoneinfo import ZoneInfo
from datetime import datetime, timedelta
dt = datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("America/Los_Angeles"))
print(dt)
dt.tzname()


# In[10]:


conda install Zoneinfo


# In[12]:


print('%6.3f')


# # For each of the following variables, what is the type?

# In[10]:


x = (5+4)/3 
y = 'hell words '
z = True
s = int(7/2)
print(type(x),x)
print(type(y),y)
print(type(z),z)
print(type(s),s)


# # Write a program that asks the user for an integer 
# 'x' and prints the value of y after evaluating the following expression:

# In[ ]:


x=int(input("please input integer value:"))
y = int(x * x - 12 * x + 11)
print(y)


# # operating & operand 

# In[1]:


# defferances types of the operating 


s = 3*2 
print ('The operators 3 , 2 ',s,'the operand','* ')


# In[2]:


#binery operators 
s = 3 * 2 
print ('the binary operators is the math symbels like : * in s ')
print ('the unary operator like -2 , -3 - -7 and so on: ')


# In[4]:


# the types of opertors : 
print ('Mathmatical' ,'%,*,-,+ // / ')
print ('Realation : ', '< <= > >= != ==')
print ('logical : or & not ')
print ('Bitwise : | & ^ ~ << >>  ')
print ('membership : in not in  ')
s 2 in [2,3,4] 
print ('identity : is is not  ')


# In[7]:


#review last section operation and operand : 
print (2**4/5 )


# In[8]:


print (2 in [1,2,3,])


# In[9]:


print(2>=3)


# In[14]:


-7 - 2 is (-9)


# In[15]:


x = ["apple", "banana", "cherry"]

y = x

print(x is y)# two object review to the same varables: 


# # Relation operation 

# In[16]:


# to learn more about relation operation .... 
# > Grater than >= greater and equal to 
# < less than  <= less and equal to
# == equal to
# != not equal to 
# example 
s = 4 
a = 18 
s > a 


# In[17]:


s>=a


# In[18]:


s < a


# In[20]:


s <= a


# In[21]:


s == 3 


# In[22]:


s !=4 


# In[23]:


a == 18 


# # Logical Operators 

# In[26]:


# Objective To Learn About Python Logical Operators : 
# and , or , not  is a bogical operators that mean Ture of both operation is true for and 
# True of either of the operand is True 
# complements the operand. 
print( 'The result of both True is : ',True and True )
print( 'The result of either of the operand  True is : ',True or False )
print( 'The result  : ',not(2>5) )


# In[28]:


# example 
d = 22 
c = 23 
x = 45
print (d & c > x )
print (d | c > x )


# In[31]:


# Python program to show
# shift operators
 
a = 10
b = -10
 
# print bitwise right shift operator
print("a >> 1 =", a >> 1)
print("b >> 1 =", b >> 1)
 
a = 5
b = -10
 
# print bitwise left shift operator
print("a << 1 =", a << 1)
print("b << 1 =", b << 1)


# In[32]:


#exersices 
print(( 3 > 2 ) or ( 4 < 7))
print( 4 > 4.1 and 3 != 5)
a = 8 == 8.1
b = 2 >= 5
print( a or b)
print( not 0)


# # Membership operators : 

# learn about python membership operators 

# In[55]:


print ("""""""""""""""""""""""""""""""""""""""""""""""""")
x = "in"" , ""not in "
meaning = ('check to see if the value in the squance\n'"           "'check to see if the value not in the squance')

Usage = [2,3,4,5]
print ("Operator : ",x)
print ('Meaning : ',meaning)
print ("Usage",Usage)
squances = ['dog' , 'cat', 2 ,5 ,'people']
print('dog' in squances )
print(2 in squances)
print(3 in squances)


# In[56]:


#What will be printed after each of the following code segments? If error, then write Error
# Exercise
x = [ 2.3, "dog", "disk", "donkey", 6]
print("d" in x)


# In[57]:


x = [ 2.3, "dog", 5]
print("dog" not in x)


# In[58]:


x = "computer science"
print("mpu" in x)


# In[59]:


print(not not (5 > 4))


# In[60]:


nums = [48, 6, 9, 21, 1]

square_all = map(lambda num: num ** 2, nums)

print(square_all)


# In[63]:


raise_to_power = lambda x, y: x ** y # the first number been multiply by the second number 

raise_to_power(5, 2)


# # condaition if statement 

# ###### in daily life we can say if it is not raining , i will go to the park 
# # in program condational statements are used to perform 
# # different condation is True or False 
# to write if statements 
# if experssion : 
#     statments .....
# else: 
#     print ("inside if or out side if")

# In[66]:


#example in our program to convert a temprature to ceil
# we just follow the stetment we need 
# like if it is raning i will take a car of not i will wake 
user_input = input("please Enter The degree today : ")
celsuis = float(user_input)
change_f = ((celsuis*9)/5)+32
if change_f >90 : 
    print ("it is hot today I will take a car ")
else : 
    print("it is nice weather I will wake ")
print(change_f)
# as we see it give us a choose 


# ###### What will be printed after each of the following code segments? If error, then write Error
# # Exercise 
# my_string = "hello there"
# if "tf" in my_string:
#     print('Yes')
# else:
#     print('No')
#     

# In[72]:


if 6 != 8 and 3 > 1:
    print('both')
else:
    print('none')


# In[73]:


My_list = [1,2,'dog','cat','car']
s = 'dd' 
# we can change the value here 
if s in My_list:
    print ("Yes ")
    # the value is in the list 
else :
    print ('Try Again')
    # The value is not in the list 


# # Write a program which asks the user to type a string and then prints "Yes" if "dog" is in that string, otherwise prints "No"

# In[78]:


# this program print the response to the user 
# the input is string 
user_items = input("I have a :  ")
choose = ['Wolf','a','b','Eid','zaid','reem','Kathem',2,3,4]
if user_items in choose : 
    print (" it is in the list  ")
else : 
    print ("Try Again ")


# In[84]:


#example in our program to convert a temprature to ceil
# convert to fahrenhit 
# print the degree in fahrenhit
# if it is below than 32 print it is a freezing 
# if it is between 32 and 50  print it is chilly 
# if it is between 50 and 90  print it is ok 
# else print it is hot 
user_input = input("please Enter The degree today : ")
celsuis = float(user_input)
change_f = ((celsuis*9)/5)+32
if change_f < 32  : 
    print ("it is a freezing  ")
elif change_f < 50 : 
    print("it is chilly  ")
elif change_f < 90 : 
    print("it is OK ")
else : 
    print("it is HOT ")
print(change_f)


# In[85]:


my_list=[ 2.3, 'car', 12, 46, 'cat']
if 12 in my_list:
    print('hello')
elif 6 > 4:
    print('bye')
else:
    print('nothing')


# In[86]:


x = 0
if 5 in [1, 2, 3, 4]:
    x = x + 1
elif 4 == 2:
    x = x + 2
elif 7 > 4:
    x = x + 3
else:
    x = x + 4
print (x)


# ###### 0 points possible (ungraded)
# Write a program which asks the user to type a string and then: 
# Print "Dog" if the word "dog" exists in the input string.
# Print "Cat" if the word "cat" exists in the input string. (if both "dog" and "cat" exist in the input string, then you should only print "Dog") 
# Otherwise prints "None". (Pay attention to capitalization).

# In[103]:


user_ = input ("I have : ")
#user_list = ['dog','cat','donke']
if 'dog' in user_:
    print('dog')
elif 'cat'in user_ :
    print('cat')
elif 'catdog'in user_: 
    print("dog")
else :
    print('None')


# # While Loop

# ###### There are two types in loop into python 
# 1- while loop 
# 
# 2- for loop 
# 

# #### While loop in python programming repeatedly executes 
# ###### one or more statements as long as a condition is True 
# ###### while experssion : 
#    ###### statement (s)
# ###### print ("not inside while loop ")

# In[111]:


# Example let's Eat cookes 
# 
user_response = input("Enter a number of cookies you have : ")
number = float(user_response )
number_of_cookies = number 
while number > 0 :
    number_of_cookies = number_of_cookies-1 
    number = number - 1 
    print("Eat a cookies ",number_of_cookies)
print("I ate all the cookies ")



# In[112]:


##### Examples of Get Of Squer Root 
# itration numbers 
user_response = input("Enter a numbers : ") # Got a number from The User Entrally :::::: 
number = float(user_response)
guess = number / 2 # Find a number by divid it To ....... 
accuracy = 0.1
itration = 0 
while abs (number - (guess ** 2)) > accuracy : 
    guess = (guess +(number /guess)) / 2 
    # Get The squera root Equation 
    itration = itration + 1 
    print("Orignal number is : " , number )
    print("Squere root of the number : ", guess)
    


# In[118]:


# Write a program which prints the sum of numbers 
#from 1 to 101 that are divisible by 5. 
#( 1 and 101 are included) (Use while loop)

numbers = 0 
counting = 0 
while numbers <= 101 : 
    if numbers % 5 == 0 :
        
        counting = counting + numbers 
    numbers = numbers + 1
    print("the sum of the number from 1 to 101 is : ", counting)


# Write a program using while loop, which asks the user to type 
# a positive integer, n, and then prints the factorial of n.
# A factorial is defined as the product of all the numbers from 1 to n (1 and n inclusive).
# For example factorial of 4 is equal to 24. (because 1*2*3*4=24)

# In[122]:


n = input('Enter user numbers : ')
y = int(n)
count = 1
s = 1
while s <= y : 
    count = count * s 
    s = s + 1 
    
    print(count)

Write a program using while loop, which prints the sum of every third numbers from 1 to 1001 ( both 1 and 1001 are included)
# In[125]:


# Type your code here
 
################### Sample Solution ###################
x = 1
count = 0
while x < 1001:
    count = count + x
    x = x + 3
print(count)


# # For Loop

# # using for loop by two satutions : 
#     1- when you want go over the items of any sequence , such as list or a string 
#     2- when you want to repeat some pices of code n u=number of itimes: 
#         
if you want to print items 10 times, 
we can write a for loop like 
for x in sequence : 
    statment(s)
    print("not inside while")
# In[126]:


# example 
list_ = ['dogs','cat','tager',1,2,3]
for x in list_ : 
    print (x)


# In[134]:


# example 2 

for number in range(1,11):
    print (number , "HELLO")


# In[137]:


#Using a for loop, write a program which prints the sum of all the even numbers from 1 to 101.
################### Sample Solution ###################
count = 0
for x in range(1,102):
    if x % 2 == 0:
        count = count+x
print(count)


# # continue $ Break : 

# In[143]:


# objective to learn about continue and break statments in pythons 
# This program Print every character 
# of the string 
for char in "computer ":
    print(char)
print ("Finished the for loop \n ")
# This program Shows the use of continues  
# statment in a for loop ... 
for char in "computer ":
    if char == "p":
        continue 
    print(char)
print ("Finished the for loop \n ")
# This program Shows the use of break 
# statment in a for loop ... 
for char in "computer ":
    if char == "p":
        break
    print(char)
print ("Finished the for loop \n ")


# In[144]:


my_str = "university"
count = 0
for char in my_str:
    if char == "i":
        continue
    else:
        count = count + 1
print(count)


# In[145]:


my_list = [6, 5, 7, 2, 3, 5, 7, 8] 
count = 0
for number in my_list:
    if number == 5 or number == 7:
        continue
    else:
        count = count + number
print(count)


# # Nested Loop 
# to learn about nested loop 
# nested loop is a loop inside another loop what ever was like for loop inside while loop 
# or while loop inside for loop , for loop inside a for loop , or while loop inside while loop 
# 
# syntax of nested loop ::
#         for current_statues : 
#             statment 
#             for current_situation:
#                 statment 
#         print(current_statues)
#         

# In[5]:


#Example Nested loop 
# print all the prime number :
# between 2 and 50 
start_number = 2
end_number = 100 
current_number = start_number 
while current_number <= end_number: 
    current_divisor = 2 
    is_current_number_prime = True 
    while (current_divisor < current_number):
        if current_number%current_divisor == 0 :
            is_current_number_prime = False 
            break
        current_divisor = current_divisor + 1 
    if is_current_number_prime:
        print( current_number, "is prime")
    current_number = current_number +1 
print("all done")


# In[6]:


#exercies 1 : 
m = 0
for x in range(1,4):
    for y in range(1,3):   
        m = m + 1
print (m)


# In[7]:


#What will be printed after each of the following code segments? If error, then write Error

#Pay attention to the spaces. Your answer should exactly match the correct Python output
m = 0
x = 1
while x < 4:
    y = 1
    while y < 3:
        m = m + x + y
        y = y + 1
    x = x + 1
print(m)


# In[8]:


m = 0
my_str_1 = "university"
my_str_2 = "mississipy"
for char_1 in my_str_1:
    for char_2 in my_str_2:
        if char_1 == char_2:
            m = m + 1
print(m)


# # functions
# the objectives of this lessons to learn about function
# 
# function is a block of code that performs a specified task.
# 
# writing a function is like that 
# def function_name (optional paramaters):
#     statments 
# print("not part the function")
# 
# 

# In[9]:


#Example :
def hello():
    print('hello there ')
hello()


# In[10]:


for k in range (1,5):
      print('hello there ')
hello()


# In[12]:


# Examples of Built in Functions
my_value = -12                             # Notice that my_value is a negative floating point number
absolute = abs(my_value )                     # Return the absolute value 
print("The absolute value is:", absolute)


# In[13]:


my_numbers = -3.33333333336 # القيمة المطلقة 
result = abs(my_numbers)
print("the result absolute ", result)


# In[17]:


my_list = [1, 2, 3, 4, 5]                        # Create a list
my_sum  = sum(my_list)                           # Return the sum of the list
print("The sum of my list is :", my_sum)         # Print my_sum                              


# In[20]:


my_fr = 30 
my_gri = 20 
my_sum = [my_fr ,my_gri]
print(sum(my_sum))


# # list method 
# object for this section to learn how to insert, append , remove, and so on items into a list 
# methods : 
#     to call methods use "." afetr the object and written a specific object and name of the methods such as 
#     Eid. run()
#     example :
#         x = [3,2,4,5,6]
#         x.sert()
#         please look it the tables for the methods at the list we can use it 
#         

# In[4]:


my_list = ["Eid",'Zaid','Reem','Nzalh',4]
my_list.insert(4,'s') # takes two argements
print(my_list)


# In[7]:


my_list.append('KK') # add items to the end of the list .. 
print(my_list)


# In[11]:


mylist = [1,2,3,4]
my_list.extend(mylist) # add the items in the list two to the list one and print the list one.... 
print(my_list)


# In[12]:


my_list.remove('s')
print(my_list)


# In[14]:


x = my_list.pop(2) #remove the items but the defference that it has the element in side the list 

print(my_list)


# In[15]:


print(x)


# In[19]:


#list.index(x)
#This method returns the index in the list of the first item whose value is x. It is an error if there is not such item.
my_list = ["Python", "is", "awesome", "Java", "is", "Alright"]       # Create a list
my_index = my_list.index("Python")                                       # Return the index of the items 
print("The item was first found at index:", my_index)


# In[20]:


# lets take an exercies 
MyList = [3, "dog", 9, "cat"]
print (len(MyList)) # return the lenght of the list . 


# In[23]:


MyList = ['pet' , 'dog' ,5, 'cat', 'good','dog'] # Create a list. 
x = MyList.count('dog') #return the number of the index item. 
print(x)


# In[24]:


MyList = ['pet' , 'dog' ,5, 'cat', 'good','dog']
print (MyList.index('dog'))


# In[26]:


# Create a list 
# Sort the elements inside it 
# using the method sort 
My_list_ = [1,2,5,3,7,8,1]
My_list_.sort() 
print(My_list_)


# In[5]:


# List Methods, Exercise 
My_list__ = []
for x in range (2,11,3):
    My_list__.append(x)
print(My_list__)


# # Write a function that accepts a positive integer k and returns a list that contains the first five multiples of k. The multiples should be calculated starting from 1 to 5 (including both 1 and 5). For example the first five multiples of 3 are 3, 6, 9, 12, and 15

# In[30]:


################### Sample Solution ###################
def _list_of_multiples_sample_(k):
    k =11
    my_list = []
    for i in range(1, 6):
        multiple = k * i
    print (my_list.append(multiple))
    


# In[31]:


# Type your code here
 
################### Sample Solution ###################
def _list_of_even_numbers_sample_(a, b):
    output_list = []
    for number in range(a, b):
        # check if the number is even
        if number % 2 == 0:
            # if true put the numbers in the output list
            output_list.append(number)
    return output_list


# # List Slicing 
# objective of this section to replace an items in the list 
# 

# In[34]:


# create  a list 
list_for = [1,2,3,4,5,6,'ant']
list_for[3] # slicing a list place 


# In[39]:


#lets find out the how to replace items 
list_for[2]='Eid' # replace a str instead of int 
list_for


# In[41]:


list_for[1:5]


# In[42]:


list_for[:5] # end to index 5 


# In[43]:


list_for[3:] # begining from index 3 till the end of the list 


# In[44]:


my_list = [5, 'old', 'new', 8, 'time', 2]
print(my_list[2:4])


# # List Slicing Negative Index
# negative index may also be used in list slicing 

# In[48]:


my_lists = [1,2,3,4,5] # create a list 

print(my_lists[0:-1])# starting from 0 index till -2 index 
# the negative list starting from -1 the last index in the list 
# between the positive index starting from 0 the first items. 


# In[49]:


# example 
my_list=[54,'cow',0.25,32,'worm'] # Create a list 
print(my_list[0:-2])


# # List Slicing With Step
# the objective of this lesson to learn how to slice a list including an optional

# In[57]:


#example 
list__ = [1,2,'hell','T',7]
my_list_list = list__[0:3:1]
print(my_list_list)


# In[63]:


my_list = ['python', 3.4, 54, 'java', 82, 'c', 7.4]
print(my_list[0:6:4])


# In[127]:


#Write a function that accepts two lists both of which contain 
#integers and returns a new list which contains all the elements 
#from both lists sorted in descending order. Your new list should include duplicate elements 
#if they exist. Do NOT use the built in sort() or sorted() methods
def list__(a, b):
    z = []
    for x in (a,b):
        z.append(x)
        return z
print(list__([1,2,3,4,5], [3,4,5,6,7]))


# In[141]:


def list_account(a):
    count = 0 
    for x in a : 
        count+= x
print(list_account([1,1,1,3,4,5,5,7,8]))


# # String in python 
the objective of this lesson to learn about string in python 
A string is a sequence of characters 
String are enclosed in single or double quotations 
Example : 
    a = 'Eid'
    b= "Eid " # the same 
# In[144]:


# the string elements are indexed exactly the same as list elements 
# Example 
# we deal with the String like a list ... 
a = 'EidMuzil' # Create a String 
z = a.count("i") # count a list 
print("The element count is : ",z) # count of the elements 


# In[149]:


z = 'EidMuzilAlbalawi'
x = 'Zaid'
d = z+x
print(d)


# In[151]:


c = z[2:6]
print(c)


# In[153]:


#Write a program using while loops that asks the user for a positive integer 
#'n' and prints a triangle using numbers from 1 to 'n'. For example 
#if the user enters 6 then the output should be like this :
n = int(input('please enter the number'))
number = 0 
while n  > number: 
    number += 1  
    z = str(number)
    x  = z * (number)
    print(x)


# In[154]:


n=int(input('please inter thenumber: '))
number = 0 
while n  > number: 
    number = number + 1 
    print("*"* n)


# # character Encoding 
# # useful functions 
# the objective of this lessons to learn about character encoding in python 
# Each character is given a unique number code so it can be stored in a computer memory 
# such as ascll , btf8 - btf16 - btf32 
# the BFT-8 is the main character encoding for the web and simple English text but it can also contain any unicode character . and recommende for most web pages 
# 
# 
# there are two function which are useful to convert from a character 
# to a number and from a number to a character 
# 
# ord () takes a character & returns its UTF-8 integer Value 
# chr () takes an integer & returns the UTF-8 character
# 

# In[155]:


# example
print(ord('a')) #change an character to integer


# In[158]:


print(chr(66)) #change a integere to character 


# In[162]:


print(chr(36))


# In[165]:


s = ''
for k in range (2000,3000): # Create a Character : 
    s =s+chr(k)
    print(s)


# In[197]:


def change_ (x):
    s = ''
    for k in range (10,128):
        # Create a Character : 
        s =s+chr(k)
        return s
print(change_ (s))
  


# # String Methods 
objective of this lessons to learn about the methods in python of string 
Method is a function 
 Str.count (sub(,start[,end]]))
    
# In[198]:


#Example 
x =' He Learn Python Form The scratch and practices a lot of '
x.count('ea')


# In[199]:


x.count("p",5) # Strating at the positions 5 ... 


# In[200]:


x.replace("Form",'And ')


# In[203]:


my_list = x.split() # create a list and split a words to a string
print(my_list)


# In[206]:


x.swapcase()


# In[207]:


#String Methods With Examples
my_string = "sTrInG mEtHoDs"                # Create a string
new_string = my_string.capitalize()         # Capitalize 1st, lower rest & return
new_string  


# In[208]:


#str.casefold( )
#This method returns a casefolded copy of the string.
#Casefolded strings may be used for caseless matching. 
#Casefolding is similar to lowercasing but more aggressive because 
#it is intended to remove all case distinctions in a string. 
my_string = "sTrInG mEtHoDs"               # Create a String
new_string = my_string.casefold()          # Return a casefolded copy
new_string


# In[209]:


"""*** Strings Method With Examples Continued ***""" 
sign = "+"                                   
my_list = ["One", "Two", "Three", "Four"]    
new_string = sign.join(my_list)       
new_string


# In[210]:


my_str = "Hello"
print (my_str.islower())


# In[211]:


my_str = "Goodbye"
print (my_str.lower())


# In[212]:


my_str = "GoodBye"
print (my_str.isupper())


# In[217]:


print ("abcdef".find("a")) # to find the index of the letters of it is there 


# In[219]:


#Example of practices 
def reverse_string(input_str):
    output_str = "" 
    for character in input_str:
        print("Character = ",character)
        print("Character = " , output_str)
        output_str = character + output_str
        print("",output_str)
        return output_str
# main programe to test resever
test_str = "Hello"
result_str = reverse_string(test_str)
print(result_str)
        


# In[222]:


def find_in_letter_words (input_str):
    words = input_str.split()
    n_letter_words = 0 
    for word in words :
        if len(word)==3:
            n_letter_words = n_letter_words + 1
    return n_letter_words
        #main program 
test_str = " HE WHO WOULD LEARN TO FIY ONE DAY "
print(find_in_letter_words (test_str))


# # Multidimensional Lists
# 
To learn about Multidimensional Lists in python 
- there are some situations which require that the data to 
  be strored as a multidimensional structure.
- Create a list with n elements , n is the number of students that have a list in side a list 
- to refer to on element of mulitidie list use multiple breackets. 



# In[224]:


# Example of multidimensional list 
my_course = [["Bunn",78,90,99],["Rubb",88,94,96],["ZaZa",98,97,99]]
print(my_course[1][0][3])# the index 1 inside it the 0 index inside it index 3 


# In[225]:


x = my_course [1] # The first index ..... 
print(x)


# In[226]:


for students_data in my_course : # create a for loop to get information...... 
    print(students_data)


# In[233]:


def function_accept_two(list1, list2):
  
    for numbers in (list1,list2): 
        z = x.sum(numbers)
        return (z)
print(function_accept_two([1,2,3,4], [1,2,3,4]))


# # python Dictionary 

# objective for this lessons is to learn about dictionary in python 
# it is unordered collection of items. 
# To Create a dictionary use curly brackets {}
# # example 
# 

# In[234]:


dictionar_for_jobs = {'Engeneering':'CS','COO':'MOHA','OParation':'SAM'} # create a dictionary 
print(dictionar_for_jobs)


# In[237]:


# Adding an items to Dictionary 
dictionar_for_jobs['FIRE'] ='HK'
print(dictionar_for_jobs)


# In[238]:


#deleting the items form the dictionary : 
del dictionar_for_jobs['FIRE']
print(dictionar_for_jobs)


# In[239]:


print(dictionar_for_jobs['Engeneering'])


# In[240]:


# What will be printed after each of the following code segments? If error, then write Error 'Exerscies '
numbers={"one": 1, "two": 2, "three": 3}
print (numbers["two"])


# In[241]:


numbers={"one": 1, "two": 2}
print (numbers[2]) # give us ERROR cuz it print the value not the Key ....... 


# In[242]:


numbers={"one": "uno", "two": "dos", "three": "tres"}
print ("two" in numbers)


# In[244]:


numbers={"one": 1, "two": [4, 6, 3], "three": 3}
x = (numbers["two"])
x.sort() # just to rcognize 
print(x)


# # Dictionary Methods

# In[25]:


# create a dictionar 
person = {'Name':'Eid','Age':34,"job":'CS'}
print (person)


# In[5]:


# clear method
#x = person.clear() # will clear and remove all the elements 
#print(x)


# In[13]:


person.get('Name', 'Hello') # how to use the get function 


# In[12]:


person.get('HG', 'HEllO') # if the item not exist the defualt will be print it. 


# In[14]:


person.keys() # get the object  of the dictionary .... 


# In[17]:


x = list(person.keys()) # convert the dict to the list .... 
x


# In[27]:


# get the items
person.pop('Age')            # but when you print a dict the pop item will not be exist. 


# In[28]:


print(person) 


# In[29]:


# update method 
# to dictionaries append each other 
# example 
pet = {'Type':'Dog','Color':'White'}
person.update(pet)
print(person)


# In[32]:


z = list (person.values()) # oppest the keys it get the values . 
z 


# In[33]:


#What will be printed after each of the following code segments? If error, then write Error
numbers={1: 2, 3:4}
numbers.pop(3)
print (numbers)


# In[34]:


d={"uno":["one",1],"dos":["two",2],3:["tres","three"]}
print (d.pop("dos"))


# In[35]:


d={"uno":["one",1],"dos":["two",2],3:["tres","three"]}
print (d.get(3,'cat'))


# In[4]:


#Write a function that accepts a dictionary as input and returns a sorted list of all the keys in the dictionary.

def name_dic (lists):
    for x in lists : 
        z = x.sort()
        return x 
print (name_dic({'Eid':1,'Zaid':2 ,'Reem':4,'Gath':3}))


# # file o/l 
# 

# In[10]:


#How to write and read into files ?
# file input and output in python 
#perpare a file 
# what the farmat of the file 
# write a read and oppend 
# oprn function : 
# syantext 
# file -ob = open (file_name[, mode][,buffereing])
# using the read (method )
# once the file is open you can read and write from it .
# example 
file_dir = open('To_open_a_file','r')
x = file_dir.readlines() # create a list 

print(x)


# In[14]:


file_dir = open('To_open_a_file','r')
z =  file_dir.readline()  # just print the first line in the text 
print(z)


# In[15]:


file_dir = open('To_open_a_file','r')
s=file_dir.read() # read all the text 
print(s)


# In[25]:


files_write = open('To_open_a_file_2.txt','w')
files_write.write('he the person of the future') # read all the text 


# In[27]:


file_dir = open('To_open_a_file_2.txt','r')
s=file_dir.read() # read all the text 
print(s)


# In[33]:


# to eidting a file for reading and writing 
# using the access file modes 
# Example 
# we have a file that we can modifie to write and read using r+ 
file_dir = open('To_open_a_file.txt','r+')
x = file_dir.read()
print(x)
z = file_dir.write('Eid is a father of zaid') # create a list 


# In[44]:


file_dir = open('To_open_a_file','r')
s = file_dir.seek(15)
x = file_dir.readline()
print(x)


# # FILE I/O EXERCISE NOTES

# In[47]:


#*** Due to the restrictions of the web platform while doing exercises with File I/O you should read a file the following way: ***

file_pointer = open('To_open_a_file', "r") # only "r" mode works due to the restriction of the platform
some_data = file_pointer.read()
print(some_data)# You may use .readline() or .readlines() 
# Now do something with 'some_data'


# # Tuples

# In[50]:


#the objective of this lessons to learn about tuples 
"""the tuples are the as the list but the tuples can't change after created 
To create a tuple you just need a ()
there are two ways to create a tuple 
tuple_1 = ('Eid','Zaid',2,2.3,'ok')
tuple_2 = 'Eid','Zaid',2,2.3,'ok'
to access the tuple it is like a list """
# example chnage a list to tuple 
my_list = ['Eid','Zaid',2,2.3,'ok'] # convert a list to the tuple ....  
x = tuple(my_list)
print(x)


# In[53]:


z = x[2] # index 
print(z)


# In[56]:


s = (1, ) # to create a tuple with a single element you should using a comma .. 
print(type(s),s)


# In[54]:


z = x[0:2] # slicing the tuple work as the list 
print(z)


# In[51]:


my_tuple = ('Eid','Zaid',2,2.3,'ok') # convert a tuple to the list .... 
x = list(my_tuple)
print(x)


# # Tuples in function 

# In[57]:


# How to return multiple values from a function by using a tuple in return stetement. 
# Function to return the sum & the product 
# of the two numbers which we passed to it
def sum_Product(x,y):
    return (x+y , x*y)
# Main program to test the function sum_Product 
(S,P) = sum_Product(3,6)
print('Sum = ',S,'and Product = ', P)


# In[58]:


conda install mlxtend -c conda-forge


# # Formatting Basics 

# In[68]:


# To learn about string formatting 
# There are many situations that you need to format the output of your 
# program ... 
# Example list of students using for loop 
My_course = [['CS',23,33,44],['Math',43,53,64],['Graph',22,37,64]]
for student in My_course : 
    for items in student: 
        #print(items)
        print(items," | " , end="") # we need the formatting to put the line under each other 
    print("")


# In[70]:


# This example clear for us why we need formatting 
# The general form of the format method is : 
# tamplate-string .format (arguament)
# Curly brackets , {} , with in the template - string 
# marks "Slots" into which the value of arguments are inserted 
my_str = "x = {} and Y = {}".format (555,9)
print(my_str)


# In[77]:


# Formatting with position 
# Example 
# all about index 
for_matting = '{2} {1}'.format(20,30,'Eid')
print(for_matting)


# In[78]:


# example 
my_str = "x = {0:3d} and Y = {1:6.3f}".format (555,9)
print(my_str) 
#notes 
# after colin is the space before number 
# the d is singed to number 
# the s singed to the string 
# after . how many digital number you want . 


# In[79]:


my_str = "x = {0:3s} and Y = {1:6.6f}".format ('Eid',9) #6f will write 6 digital numbers 
print(my_str) 


# In[82]:


My_course = [['CS',23,33,44],['Math',43,53,64],['Graph',22,37,64]]
for student in My_course : 
    for items in student: 
        if type(items)== str:
            print('{0:10s} |' .format(items),end="")
        else:
            print('{0:3d} |' .format(items),end="")
       
    print("") # the foramtting is nice as you can see 


# In[83]:


my_string = "x = {0:%<7d} and y = {1:@>8d}".format(5, 43)
print (my_string)


# # Intermediate Python Programming Course
# 

# In[89]:


mylist =["banana","cheery","apple"]
print(mylist)


# In[85]:


if "banana" in mylist:
    print('YES')
else:
    print("NO")


# In[86]:


print(len(mylist))


# In[90]:


mylist.append('lemon')
print(mylist)


# In[91]:


itm = mylist.pop()
print(itm)


# In[92]:


print(mylist)


# In[99]:


my_inter_list = ['boy','Girl','Chico','chica']
my_inter_list.insert(1,'hijo') # create index first
print(my_inter_list) # print the list after adding a new item 


# In[108]:


my_inter_list = ['boy','Girl','Chico','chica']
items = my_inter_list.pop() # to remove the list element 
print(items)
print(my_inter_list)


# In[109]:


my_inter_list.remove('Girl')
print(my_inter_list)


# In[110]:


# creata a list and sorted 
my_Number_list = [-1,-3,-4,1,3,4,5,9,1,-10]
new_number = sorted(my_Number_list)
print(my_Number_list) # the odd list 
print(new_number)  # the new list insorted 


# In[111]:


my_Number_list.sort() # using the sort function to sort the list 
print(my_Number_list)


# In[112]:


# lets do some trick 
my_num_ = [0] * 4 
print(my_num_)


# In[113]:


New_List_her = my_Number_list + my_num_ 
print(New_List_her)


# In[114]:



print(New_List_her[3:7])


# In[115]:


New_List_her[:7] # it goes from the start if we do not espicfy the index. 


# In[116]:


New_List_her[3:] # it goes from the start to the end if we did not espicfy the end index. 


# In[118]:


New_List_her[::3]


# # Tuple 

# In[119]:


my_tuple = ('Eid',1.2,'Zaid',3.4,'Reem','Gath')
print(my_tuple)


# In[126]:


my_tuple = 'Eid',1.2,'Zaid',3.4,'Reem','Gath' # the two ways to create a tuple one with prathences and the anther with out 

print(my_tuple)


# In[127]:


my_secon_tuple = ('zEid') # the single tuple with comma . 
my_secon_tuple1 = ('zEid',)
print(my_secon_tuple)
print(my_secon_tuple1)


# In[128]:


#Example 
mytuple3 = ('CS','Math','Jave','Python','HTML','CSS','Javascript','analysis')
print(list(mytuple3)) # convert the tuple to the list ... 


# In[129]:


mylistw = ['CS', 'Math', 'Jave', 'Python', 'HTML', 'CSS', 'Javascript', 'analysis']
print(tuple(mylistw)) # convert the list to the tuple ..... 


# In[137]:


itmess = mylistw[:5] # starting form the index 0 
print(itmess)


# In[139]:


# Erorr of we change the element into the Tuple ... 
# Example .. 
mytuple3[0]= 'R'
print(mytuple3) #'tuple' object does not support item assignment


# In[140]:


for x in mytuple3 : 
    print(x)


# In[144]:


if 'Math' in mytuple3 : 
    print ('YES')
else: 
    print('NO')


# In[148]:


add_bosten = 'Bosten',28 , 'Max'
city , age , name = add_bosten # 
print(city)
print(age)
print(name)


# In[150]:


tuple_all = (1,2,3,4,5)
x1 , *x2 , x3 = tuple_all # creata * will print over all the number or tuples element into a list 
print(x1)
print(x2)
print(x3)


# In[151]:


import sys 
my_list22 =[2,'Eid',3,'Zaid','Reem',5]
my_tuple22 = 2,'Eid',3,'Zaid','Reem',5 # the tuple is more efficient than the list and more smaller 
print(sys.getsizeof(my_list22))
print(sys.getsizeof(my_tuple22))


# In[154]:


import timeit 
print(timeit.timeit(stmt="[0,1,2,3,4,5,6]",number=100000)) # it take more time to creata a list than tuple 
print(timeit.timeit(stmt="(0,1,2,3,4,5,6)",number=100000))


# # dictionary 

# In[170]:


# Two ways to create a dictionary 
my_dectionary = {'City':'ROMA','CONTRAY':'EUROP','LIVE':'ULA'} # write the key and the vaule of the key element 
print(my_dectionary)
my_dec = dict(ROOM="BEDROOM",HOUSE="THE ELM STREET",CITY="WEST HAVEN ") # using fuction of dict 
print(my_dec)


# In[171]:


# list do some a function to the dict 
th_Value = my_dec["CITY"] # just write a key 
print(th_Value)


# In[172]:


# thes dictionary is changeable ... 
my_dec ['ADDRESS'] = 'ULA CITY '
print(my_dec)


# In[173]:


# delete a items 
del my_dec['ADDRESS'] # delete an item 1
my_dec.pop('ROOM')# delete the items 2
print(my_dec)


# In[174]:


conda install imageio


# In[175]:


my_decw = dict(ROOM="BEDROOM",HOUSE="THE ELM STREET",CITY="WEST HAVEN ")
my_deca = dict(STREET="MADINA",NUMBER="BLOCKS",NATIONAL="SAUDAI ARABIA")
my_decw.update(my_deca)
print(my_decw)


# # Set Methods mudabe , duplication , unorderal 

# In[176]:


My_set = {1,2,3} # create a set 
print(My_set)


# In[178]:


my_set = set([1,2,3,4,5])
print(my_set)


# In[179]:


my_set2 = set("Hello")
print(my_set2)


# In[180]:


my_set3 = {} #empty Set not Set it is dictionary 
print(type(my_set3))


# In[182]:


my_set4 = set()
my_set4.add(1)
my_set4.add(4)
my_set4.add(7)
my_set4.add(9)
print(my_set4)


# In[183]:


my_set4.pop()


# In[184]:


print(my_set4)


# In[185]:


print(my_set4.clear)


# In[186]:


my_set5={2,4,5,6,7,8}
for i in my_set5:
    print(i)


# In[187]:


if 4 in my_set5: 
    print('YES')


# In[188]:


odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
prims = {2,3,5,7}
u = odds.union(evens)
print(u)


# In[190]:


i = odds.intersection(prims)
print(i)


# In[191]:


SETA = {1,2,3,4,5,6,7,8,9}
SETB = {1,2,3,4,11,22,33,12}

diff = SETA.difference(SETB)
print(diff)


# In[193]:


diff = SETA.symmetric_difference(SETB)
print(diff)


# In[195]:


print(SETA.symmetric_difference_update(SETB))


# In[196]:


print(SETB.symmetric_difference_update(SETA))


# In[197]:


print(SETA.issubset(SETB))


# In[198]:


print(SETA.issuperset(SETB))


# In[200]:


print(SETB.isdisjoint(SETA))


# In[202]:


print(SETB.intersection_update(SETA))


# In[207]:


a = frozenset([1,2,3,4])
print(a)


# In[208]:


a.add(4) # immuatable not changeable or remove , add .. 


# # String : ordered , immutable , text representation 

# In[214]:


#Example .... 
My_String = "Hello'sWrold" # single quatation or double one 
print(My_String)


# In[218]:


My_String = """Hello  
World """ # New Line if YOU use a truple qutation """"""
print(My_String)


# In[224]:


My_String2 = "Hello's Wrold" 
print(My_String2[1:6])
print(My_String2[6])
print(My_String2[::2]) # takes second character
#print(My_String2[0] = 'h') # give an Erorr cuz the string is immutable


# In[234]:


# NEW Example 
greeting = " HI " # white space 
Name = 'Eid'
Sentance = greeting.strip() + " " + Name # strip() method remove white space 
print(Sentance)
print(Sentance.upper()) # print a captal letters
print(Sentance.lower()) # print a small letters
print(Sentance.startswith('H')) # start with give a ture and false
print(Sentance.endswith('H')) # end with give a ture and false 
print(Sentance.find('H')) # index number 
print(Sentance.count('H')) # count the letters 
print(Sentance.replace('HI' , 'Hello'))


# In[236]:


# new example .... 
my_string_ = 'HOW ARE YOU ? '
My_list = my_string_.split()
print(My_list) 


# In[241]:


my_string_1 = 'HOW,ARE,YOU,?'
My_list2 = my_string_1.split(",") # looking for the comma between the words 
print(My_list2) 


# In[244]:


my_string_2 = 'HOW_ARE_YOU_? '
My_list2 = my_string_2.split("_")
print(My_list2) 


# In[246]:


my_list_d = ['HOW', 'ARE', 'YOU', '? ']
My_stringt = ' '.join(my_list_d) # the white space for split the word ' '
print(My_stringt) 


# In[247]:


var = 'Eid'
My_strings = 'The varaible is %s'% var # %s here for string 
print(My_strings)


# In[248]:


var = 3
My_strings = 'The varaible is %d'% var # %d here for integer 
print(My_strings)


# In[249]:


var = 3.33322
My_strings = 'The varaible is %f'% var # %f here for float
print(My_strings)


# In[250]:


My_strings = 'The varaible is %.3f'% var # %.3f how many  number digit after float number  want
print(My_strings)


# In[252]:


My_strings = 'The varaible is {:.2f}'.format(var)  # new format 
print(My_strings)


# In[257]:


strs_ = 'Zaid'
Nam = 'Eid'
My_stringss = 'The full name  is {} {}'.format(strs_,Nam)  # new format 
print(My_stringss)


# In[258]:


strs_ = 'Zaid'
Nam = 'Eid'
My_stringss = f'The full name  is {strs_} {Nam}'  # newest format 
print(My_stringss)


# # Colection : counter , namedtuple , ordereDict , defaultdict, deque. 

# In[291]:


from collections import Counter , namedtuple , OrderedDict , defaultdict,deque
a = 'aaaaaaaabbbbbbccccc'
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(2))
print(my_counter.most_common(2)[0])
print(my_counter.most_common(2)[0][0])
print(list(my_counter.elements()))


# In[275]:


Point = namedtuple('Point',('x','y'))
pt=Point(1,-4)
print(pt)
print(pt.x,pt.y)


# In[286]:


oredered_dic = {}
oredered_dic['a']=1
oredered_dic['b']=2
oredered_dic['c']=3
oredered_dic['d']=4
print(oredered_dic)


# In[290]:


oredered_dic1 = defaultdict(int)
oredered_dic1['a']=1
oredered_dic1['b']=2
oredered_dic1['c']=3
oredered_dic1['d']=4
print(oredered_dic1)
print(oredered_dic1['a'])
print(oredered_dic1['b'])


# In[293]:


d = deque()
d.append(1)
d.append(2)
d.appendleft(3) # add item to the left list 
print(d)


# # Ltertools ... 

# In[315]:


from itertools import product , permutations , combinations , accumulate , groupby ,combinations_with_replacement
import operator 


# In[301]:


a = [1,2]
b=[4]
prod = product(a,b , repeat=2) # just repeat a number 
print(list(prod))


# In[304]:


a = [1,2,3]
prom = permutations(a) # return all possable of ordering 

print(list(prom))


# In[306]:


a = [1,2,3]
comb = combinations(a, 2) 
print(list(comb))


# In[311]:



a = [1,2,3]
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))


# In[312]:


conda install tokenizer 


# In[324]:


s = [2,3,4,5]
acc = accumulate(s , func=operator.mul) # mulitbly a * acc 
print(s)
print(list(acc))


# In[325]:


r = [3,4,5,6,3,2]
acu = accumulate(r , func = max)
print(r)
print(list(acu))


# # lambda function 

# In[326]:


# there is another way to write a function 
# using lambda 
# example 
add10 = lambda x:x+10 # create a function 
print(add10(5))


# In[328]:


mult = lambda x,y : x*y
print(mult(5,10))


# In[342]:


# Example 
Ponit2D = [(1,2),(15,1),(5,-1),(10,4)]
Ponit2D_sorted = sorted(Ponit2D, key= lambda x:x[1])
print(Ponit2D)
print(Ponit2D_sorted)


# In[347]:


a = [1,2,3,4]
b = map(lambda x:x*2 , a)
print(list(b))
c = [x*2 for x in a ]
print (c)


# In[348]:


a = [1,2,3,4,5,6,7,8]
b = filter(lambda x:x%2==0 , a)
print(list(b))
c = [x for x in a if x%2==0 ]
print (c)


# In[350]:


from functools import reduce 
l = [1,2,3]
product_a = reduce (lambda x,y : x*y , l)
print(product_a)


# # Error & Exception 

# In[351]:


a = -4 print () # error 


# In[356]:


z = -5
if z < 0 : 
    raise Exception ('a should be positive ')


# In[357]:


assert(z>=0),'z should be positive '


# In[358]:


try : 
    a = 5/0 
except: 
    print('an Error happened ')


# In[360]:


try : 
    a = 5/0 
except Exception as e: 
    print(e)


# In[362]:


try : 
    a = 5/0 
except TypeError as e: 
    print(e)
finally: 
    print('Clean up...')


# In[373]:


# if you write won your class error you shoud end with Error word the name 
class valueError(Exception): 
     pass 

def need_some_help(x):
    if x > 100 :
        raise valueError('the value is too high ')
print(need_some_help(900))  


# In[375]:


class valueError(Exception): 
     pass 
class ValueTooSmallError(Exception):
    def __init__(self,message,value):
        self.message = message
        self.value = value    
def need_some_help(x):
    if x > 100 :
        raise valueError('the value is too high ')
    if x < 5: 
        raise  ValueTooSmallError('the value is too small',x)
try:
    need_some_help(1) 
except valueError as e:
    print(e)
except ValueTooSmallError as en: 
    print(en.message,en.value)


# # logging

# In[385]:


# import the legging 
import logging 
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
                    datefmt='%M/%d/%Y%H:%M:%S')
logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s', level = logging.DEBUG)
logging.debug('This is a debug message ')
logging.info('This is a info message ')
logging.warning('This is a worning message ')
logging.error('This is a error message ')
logging.critical('This is a critical message ')


# In[390]:


import json 
person = {"Name":"Eid","City":"NewYork","Age":30,"title":["enginer","programming"]}
PersonJSON = json.dumps(person , indent=4)
print(PersonJSON)


# In[391]:


with open ('person_s.json','w') as file:
    json.dump(person,file) # create a file 


# In[ ]:





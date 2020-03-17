#!/usr/bin/env python
# coding: utf-8

# ## COMMENTS IN PYTHON
# 
# Python only has a type of comments: single line comments which uses # as the beginnig of the comment. Some people argue that multine comments can be done by using triple quotation marks as follows:
# 
# *"""*
# 
# *multiline*
# 
# *commets*
# 
# *"""""*
# 
# However this is interpreted as long string by the interpreter and it is not skipped as single line comments. This type of coments are used to document things suchs as functions
# 
# The **only way** to insert comments in Python is shown as follows:

# In[14]:


# This is a single line comment


# ## USEFUL FUNCTIONS
# 
# ### TYPE OF A VARIABLE

# In[16]:


x = 14
type(x) # returns the type of a variable


# ### MINIMUN AND MAXIMUN

# In[306]:


numlist = [20, 34, 105, 14]
min(numlist)


# In[307]:


max(numlist)


# ### RANGE

# In[310]:


range (1, 10, 1) # (start, stop, step) this range can also be represented as: range(10)

#start: where the range begins, number included
#stop: ends at, but not inclusive
#step: if included it can say how many positions to jump

## This code does not print the range


# In[311]:


list(range(1,10,1))    #To print a range --> list(range(a,b,c))


# In[313]:


list(range(10))


# ### USER IMPUT
# 
# Everything accepted by this input is read a String
# 
# To convert it to another type you can do as follows:
# 
# *float(result)*
# 
# *int(result)*

# In[318]:


userinput = input('Insert your Name ')


# In[334]:


userage = input ('Insert your age ')


# In[335]:


type(userage)


# In[343]:


numericage=int(userage)
type(numericage)


# ### MATHS
# 
# 
# #### SQUARE ROOT & ROUND

# In[25]:


import math
r = 345
s = math.sqrt(r)  #returns the square root of a number
print ('The square root is {}'.format(s))
print ('The rounded square root is {}'.format(round(s))) #rounds a variable to its closest integer


# ### SHUFFLE
# 
# Shuflle is an **in-place** *(thus it does not return anything that can be asiggned to a variable, it affects directly the variable that is passed as a parameter)* function that is included within the random library
# Thus random shuffle should be imported or called in the following way:

# In[26]:


from random import shuffle
my_list=[1,2,3,4,5]
shuffle(my_list)
my_list


# ### RANDON INTEGER
# 
# This function returns something so it can be saved to a variable

# In[314]:


from random import randint
randint(0,100) # randint(a,b) a lower ranger upper range


# ## STRINGS
# 
# String objects are immutable, single letters cannot be changed

# In[42]:


mystring ='JULIAN'
fifthletter = mystring[4]
lastletter = mystring[-1]
print ('The fifth letter is {}'.format(fifthletter))
print ('The last letter is {}'.format(lastletter)) 


# In[35]:


len(mystring) #returns the number of characters of a variable


# In[36]:


type (x)


# In[40]:


xstring=str(x)
type (xstring) #converts a variable into a string


# In[43]:


my_string = "abcdefghij"
my_string[2:]


# In[44]:


my_string[:3]


# In[45]:


my_string[3:6]


# In[46]:


my_string[::2]


# In[47]:


my_string[::-1] # [start:stop(not included):steps]


# In[50]:


'Hello'+' '+'World'


# In[55]:


x = 'Hello World'
print ('Split in the space {}'.format(x.split()))
print ('Split in the l {}'.format(x.split('l')))


# In[62]:


x.lower()


# In[63]:


x.upper()


# In[67]:


letter = 'M'
letter * 5


# In[19]:


s1= "Julian"
s1.isupper()


# In[17]:


s2="JULIAN"
s2.isupper()


# In[18]:


s3="julian"
s3.islower()


# ### PRINTING WITH FORMAT

# In[79]:


print('Hello World {}'.format ('it is beautiful'))
print('Hello World {0} {1} {2}'.format ('it', 'is' ,'beautiful'))
print('Hello World {p1} {p2} {p3}'.format (p1='it', p2='is', p3='beautiful'))


# To print numbers with precicison
# 
# “Value:{width.precision f}”
# 
# Value: the variable to print
# Width: number of whitespaces
# Precision: number of digits after the dot
# f: always goes
# 
# print('The answer is {r:1.2f}'.format(r=result))

# In[110]:


result = 834/34
print('The answer is {r:1.2f}'.format(r=result))

# r is the value to print
# 1 number of white spaces to add
# 2 number of digits after the dot, the f always goes


# ## LISTS
# 
# Lists can contain mulitple data types eg:

# In[121]:


x = [1,'t',34.5, 45]
len(x) # lenght of the list


# In[119]:


x[1:3] #indexing work as in strings, in this example it is extracted postions one and two (three not include)


# In[123]:


x[-1] #last item in list


# In[18]:


x=[1,2,3]
y=[4,5,6]
x + y # Concatenation of two strings


# In[131]:


y.append('J') #adds an item to the list in the las position
y


# In[132]:


y.pop() #removes the last item from the list
y


# In[20]:


y.pop(1)
y


# In[137]:


messlist=[20.5,10,30]
sortedlist = messlist.sort() #this example shows function sort is an in-place function thus it does not return anything
print (sortedlist)


# In[150]:


messlist.sort() #sort only works with lists of same object types eg: interger or string but not mixes
messlist


# In[144]:


messletter = ['a','A','C','d']
messletter.sort() #sorted by ASCII code
messletter


# In[171]:


k=['a','b','d','e','c']
k.reverse() # this function reverses a list
k


# ## DICTIONARIES
# 
# Dictionaries have not an specific order, it is objects are found thorugh a key

# In[173]:


d={'k1':100, 'k2':200, 'k3':[1,2,3]}


# In[175]:


d.keys()


# In[176]:


d.values()


# ## TUPLES
# 
# Tuples are inmutable

# In[181]:


t=(1,2,3,1)


# In[182]:


t.count(1) # this function counts the number of ones within the tuple


# In[183]:


t.index(1) # this function returns the postions where the first value is found


# ## SETS
# 
# It is a collection of unique and unordered values 

# In[186]:


mylist=[1,1,1,2,2,2,3,3,3]
set(mylist)


# ## FILES

# In[214]:


get_ipython().run_cell_magic('writefile', 'my_file.txt', 'Insert text of the file\nSECOND LINE\nTHIRD LINE')


# In[213]:


myfile = open('my_file.txt') # this command opens the file so its contents can be seen


# In[215]:


myfile.read() # command to read a file


# In[198]:


myfile.seek(0) # this command returns cursor to the beginnung of the file, in the previos command .read() it went to the end


# In[199]:


myfile.readlines() #returns a list of the lines of the file


# In[200]:


myfile.close()


# In[217]:


with open('my_file.txt', mode='w') as f: #with this type of opening it is not neccesary to close the file
    f.write('This a new line')


# In[219]:


with open('my_file.txt', mode='r') as f: # r-read; w-write (writes or creates a new file); 
    print (f.read())


# ## DATE AND TIME

# In[233]:


from datetime import datetime
print(datetime.now())


# In[240]:


print('Son las: {0} horas, {1} minutos y {2} segundos '.format (now.hour, now.minute , now.second))
print('Del día {0} del mes {1} del año {2} '.format (now.day, now.month, now.year))


# ## IF ELIF ELSE

# In[246]:


x = 3

if x < 2:
    print ('x es menor a 2')
elif x == 2:
    print ('x es igual a 2')
else:
    print ('x es mayor a 2')


# In[248]:


hungry=False
if hungry:
    print("I NEED FOOD")
else:
    print("I'M OK")


# ## FOR

# In[249]:


my_list=[1,2,3,4,5,6,7,8,9,10]

for num in my_list:
    print(num)


# In[250]:


for i in my_list:
    if i%2 == 0:
        print(i)


# In[312]:


for i in range (12):
    print(i+1)


# ### NESTED FOR

# In[355]:


for x in [2,4,6,8]:
    for y in [10,100,100]:
        print(x*y)


# ### PASS

# In[254]:


for item in my_list:
    pass     #executes nothing but avoids error in Python 
print('I just passed the for')


# ### CONTINUE

# In[286]:


my_name = 'Julian'
for letter in my_name:
    if letter == 'a':
        continue # avoids execution the print statement and returns to the top of loop
    print(letter)


# ### BREAK

# In[287]:


my_name = 'Julian'
for letter in my_name:
    if letter == 'a':
        break # aborts the execution of the loop
    print(letter)


# ### TUPLE UNPACKING

# In[289]:


my_list= [(1,2),(3,4),(5,6)]
for (a) in my_list:
    print (a)


# In[290]:


my_list= [(1,2),(3,4),(5,6)]
for (a, b) in my_list:
    print (a)


# In[295]:


d={'k1':1,'k2':2,'k3':3}
for key,values in d.items():
    print(values)


# ### ENUMERATE

# In[300]:


word = 'abcde'
for index,letter in enumerate (word):
    print (letter)


# ## WHILE

# In[296]:


x=0
while x <=5:
    print (x)
    x+=1 # This is equivalent to x=x+1 
    if x == 2:
        break


# In[299]:


x=0
while x <=5:
    print (x)
    x+=1 # This is equivalent to x=x+1  
else:
    print('The End')


# ### ZIP

# In[301]:


list1=[1,2,3]
list2=['a','b','c','d']

for item in zip(list1,list2):
    print (item)      # If the list to combine have different sizes it only combines up to the size of the shortest list


# ### IN

# In[302]:


dic={'k1':1, 'k2':2, 'k3':3}
'k4' in dic.keys()


# ### LIST COMPRENHENSION

# In[349]:


mystring = "Hello"
mylist=[]

for letter in mystring:
    mylist.append(letter)    #puts every letter of the string as a single object in a list
mylist


# In[350]:


mystring = "Eliana"
mylist=[letter for letter in mystring] #performs the same action as the previus for but only in one line
mylist


# In[352]:


numlist=[x for x in range(10)] 
numlist


# In[353]:


numlist=[x**2 for x in range(10)] 
numlist


# In[354]:


numlist=[x for x in range(10) if x%2 ==0] 
numlist


# ## METHODS

# In[4]:


my_list=[1,2,3]
help(my_list.insert)


# ## FUNCTIONS

# In[8]:


def name_function():
    """
    Input
    Documentation
    """
    print('Hello')
name_function


# In[9]:


help(name_function)


# In[12]:


def say_hello(name):
    print('Hello '+ name)  # For this example the result cannot be assigned to a variable


# In[13]:


say_hello('Julian')


# In[15]:


def say_hello2(name):
    return 'Hello '+ name # This reult can be assigned to a variable


# In[16]:


result= say_hello('Julian')


# In[51]:


def piglatin (word):    
    letterlist=[x.lower() for x in word]
    
    if word[0]=='a'or word[0]=='e'or word [0]=='i' or word[0]=='o' or word[0]=='u':
        pass
    else:
        firstletter=letterlist.pop(0)
        letterlist.append(firstletter)
        
    letterlist.append('a')
    letterlist.append('y')
        
    return str(letterlist)
    


# In[52]:


piglatin('apple')


# In[71]:


def piglatin2 (word):    
    
    first_letter=word[0]
    
    if first_letter in 'aeiouAEIOU':
        pigword=word+'ay'
    else:
        pigword=word[1:]+first_letter+'ay'
    return pigword


# In[78]:


piglatin2('Word')


# In[1]:


def wordfunc (word):
    iteract=len(word)
    pos=0
    out=[]

    string_letter=[x for x in word]
   
    while iteract != pos:
        if pos%2 == 0:
            out.append(string_letter[pos].upper())
            pos+=1
        else:
            out.append(string_letter[pos].lower())
            pos+=1
      
    return ''.join(out)


# In[2]:


wordfunc('julian')


# In[90]:


def myfunc (*args):
    return sum(args)


# In[92]:


myfunc(2,10,50)


# In[101]:


def myfunceven (*args):
    evennum=[x for x in args if x%2==0]
    return evennum


# In[102]:


myfunceven(1,2,3,4,5,6,8,10)


# In[18]:


text='Levelheaded Llama Julian'
ab=text.split()
len(ab)


# In[7]:


ab[0]


# In[8]:


ab[0][0]


# In[9]:


text.split()[0][0]


# In[1]:


word='Julian'
pos=0
while in word:
    pos+=1
    


# In[11]:


range(4)


# In[15]:


def reverse_text(text):
    out=[]
    iter=len(text)-1
    for i in range(len(text)):
        out.append(text[iter])
        iter=iter-1
    return ''.join(out)


# In[16]:


reverse_text('Julian Meneses')


# In[4]:


def check_prime(num):
   
    if num==1 or num==0:
        return False
    elif num==2:
        return True
    else:
        for i in range(2,round((num**0.5))+1):
            if num%i == 0:
                return False
            else:
                continue
        return True


# In[152]:


check_prime(4)


# ## MAP and FILTER
# 
# FILTER needs always the function to return True or Flase

# In[1]:


def square (num):
    return num**2


# In[3]:


num_list=[1,2,3,4,5,6,7,8,9,10]
list(map(square,num_list))


# In[5]:


list(filter(check_prime,num_list))


# ## LAMBDA EXPRESSION
# 
# Used to create onetime usage expression rather than creating a whole function

# In[7]:


list(map(lambda num: num**2,num_list))    #rahter than creatin the function square


# In[2]:


int(9**0.5)


# ## OBJECT ORIENTED PROGRAMMING

# In[41]:


class Dog():
    def __init__(self,breed,name,color): #this shoulb be double underscore 
        self.breed = breed
        self.name = name
        self.color = color
    
    def bark(self,owner):
        print('WOOF my name is {} and my owner is {}'.format(self.name,owner)) # never forget the self.


# In[27]:


my_dog = Dog(breed='Huskie',name='Tommy',color='gray') # This can also be passed only with the parameters


# In[42]:


other_dog= Dog('Pitbull','Killer','Black')


# In[43]:


other_dog.bark('Julian') # This is a method so it should be aclle used parenthesis ()


# In[61]:


class Circle():
    def __init__(self,radius):
        self.radius = radius
        self.area = 3.1415*(self.radius**2)
    def circumference(self):
        return self.radius*3.1415*2


# In[63]:


my_circle = Circle(10)


# In[65]:


my_circle.area


# In[ ]:





FUNCTIONS
def square(x):
   return x * x

def sub(x, y):
   return x - y
   
   output : no values printed but excuted 
   
print(89 + 77)
print(sub(square(4),6))

output : 
166
10

print(sub(square(8),9))
output:
55

print(sub)
print(sub(6,7))
output :
<function sub>
-1

DATA TYPES

print(type("NJN"))
print(type(78))
output :
<class 'str'>
<class 'int'>

print(type("9.0"))
output:
<class 'str'>

print(type('This is a string.'))
print(type("And so is this."))
print(type("""and this."""))
print(type('''and even this...'''))
output:
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>

print('''" one day I'm sure ,I will be high on my field's ''') 
output:
" one day I'm sure ,I will be high on my field's 

print(""" he boy boy boy i 
      know , you get
      THE FEELS""")
output:
 he boy boy boy i 
      know , you get
      THE FEELS
      
print(837487)
print(8,37,487)
output:
837487
8 37 487

print(1,"hello",8.9)
output:
1 hello 8.9

TYPES OF CONVERSATION

print(8, float(8))
print(9.8,int(9.8))
print(int("56bags"))
output:
8 8.0
9.8 9
[print(int("56bags"))]Error
ValueError: invalid literal for int() with base 10: '56bags' on line 5
Description
A ValueError most often occurs when you pass a parameter to a function and the function is expecting one type and you pass another.

To Fix
The error message gives you a pretty good hint about the name of the function as well as the value that is incorrect. Look at the error message closely and then trace back to the variable containing the problematic value.

print(str(17))
print(str(123.45))
print(type(str(123.45)))
output:
17
123.45
<class 'str'>

val=50+4
print("the value is",str(val))
output:
the value is 54

VARIABLES

twice = " hlo once "
n = 9
pswrd = 9.99999

print(twice)
print(n)
print(pswrd)
output:
hlo once 
9
9.99999

day = "Thursday"
print(day)
day = "Friday"
print(day)
day = 21
print(day)
output:
Thursday
Friday
21

EXAMPLES OF ILLEGAL VARIABLE NAMES :
76trombones = "big parade"  #starts with no
more$ = 1000000  #contains symbol $ 
class = "Computer Science 101" #class is a keyword in python

KEYWORDS IN PYTHON

and

as

assert

break

class

continue

def

del

elif

else

except

exec

finally

for

from

global

if

import

in

is

lambda

nonlocal

not

or

pass

raise

return

try

while

with

yield

True

False

None

REASSINGMENT

blow = 3
print(blow)
blow = 4
print(blow)
output:
3
4

x = 6
y = 9
print(x,y)
y = 2
print(x,y)
output:
6 9
6 2

STATEMENT AND EXPRESSIONS

print(len("fchbbfh"))
output:
7

y = 3.14
x = len("hello")
print(x)
print(y)
a = 8
k = len("once")
print(a+k)
output:
5
3.14
12

print( len("twice") + len ("once"))
output:
9

x = 2
y = 1
print(square(y + 3))
print(square(y + square(x)))
print(sub(square(y), square(x)))
output:
16
25
-3

UPDATING VARIABLES

x = 6        # initialize x
print(x)
x = x + 1    # update x
print(x)
output:
6
7

x = 6        # initialize x
print(x)
x += 3       # increment x by 3; same as x = x + 3
print(x)
x -= 1       # decrement x by 1
print(x)
output:
6
9
8

INPUTS

n = input("Please enter your name: ")
print("Hello", n)
output:
Hello hari

CONVERTS SEC TO HOURS MIN SEC
[IP=5678]
str_seconds = input("Please enter the number of seconds you wish to convert")
total_secs = int(str_seconds)

hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes =  secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining  % 60
output:
Hrs= 1 mins= 34 secs= 38

print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)

STRINGS AND LISTS 

t = (5,)
print(type(t))

x = (5)
print(type(x))

output:
<class 'tuple'>
<class 'int'>

 Index Operator: Working with the Characters of a String??
 
 school = "Luther College"
m = school[2]
print(m)

lastchar = school[-1]
print(lastchar)
output:
t
e

numbers = [17, 123, 87, 34, 66, 8398, 44]
print(numbers[2])
print(numbers[9-8])
print(numbers[-2])
output:
87
123
8398

LENGTH 

fruit = "Banana"
print(len(fruit))
output:
6

fruit = "Banana"
sz = len(fruit)
lastch = fruit[sz-1]
print(lastch)
output:
a

alist =  ["hello", 2.0, 5]
print(len(alist))
print(len(alist[0]))
output:
3
5

LOOPS AND ITERATION

FOR LOOP

for name in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
    print("Hi", name, "Please come to my party on Saturday!")
for subs in["a","b","c","<"]:
    print("hi",subs,"something rubbish bye")
    
 OUTPUT :
Hi Joe Please come to my party on Saturday!
Hi Amy Please come to my party on Saturday!
Hi Brad Please come to my party on Saturday!
Hi Angelina Please come to my party on Saturday!
Hi Zuki Please come to my party on Saturday!
Hi Thandi Please come to my party on Saturday!
Hi Paris Please come to my party on Saturday!
hi a something rubbish bye
hi b something rubbish bye
hi c something rubbish bye
hi < something rubbish bye

for achar in "Go Spot Go":
    print(achar)
    
for love in[" I love python"]:
    print(love)
OUTPUT :
G
o
 
S
p
o
t
 
G
o
 I love python
 
 fruits = ["apple", "orange", "banana", "cherry"]

for afruits in fruits:     # by item
    print(afruits)
fruit = ["hi","bye","hello"]
for name in fruit:
    print(name)
OUTPUT :
apple
orange
banana
cherry
hi
bye
hello

for _ in range(3):
    print("This line will execute three times")
    print("This line will also execute three times")
OUTPUT :
This line will execute three times
This line will also execute three times
This line will execute three times
This line will also execute three times
This line will execute three times
This line will also execute three times

import turtle
a=turtle.Screen()
ohh=turtle.Turtle()

for i in [2,2,2,2,2]:
    ohh.forward(80)
    ohh.right(80)
    
a.exitonclick()

***************************

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
accum = 0
for w in nums:
    accum = accum + w
print(accum)

OUTPUT:
55

print("range(5): ")
for i in range(5):
    print(i)

print("range(0,5): ")
for i in range(0, 5):
    print(i)

# Notice the casting of `range` to the `list`
print(list(range(5)))
print(list(range(0,5)))

# Note: `range` function is already casted as `list` in the textbook
print(range(5))

OUTPUT :
range(5): 
0
1
2
3
4
range(0,5): 
0
1
2
3
4
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
range(0, 5)

accum = 0
for w in range(11):
    accum = accum + w
print(accum)

# or, if you use two inputs for the range function

sec_accum = 0
for w in range(1,11):
    sec_accum = sec_accum + w
print(sec_accum)

OUTPUT :
55
55

tom = ['song','facts','fun']
for n in range(3):
    print(n, tom[n])
OUTPUT :
0 song
1 facts
2 fun

fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(len(fruits)):
    print(n, fruits[n])

OUTPUT :
0 apple
1 pear
2 apricot
3 cherry
4 peach
######################
he RGB Color Model
import image

p = image.Pixel(45, 76, 200)
print(p.getRed())
p.setRed(66)
print(p.getRed())
p.setBlue(p.getGreen())
print(p.getGreen(), p.getBlue())

OUTPUT :
45
66
76 76

import image
img = image.Image("luther.jpg")

print(img.getWidth())
print(img.getHeight())

p = img.getPixel(45, 55)
print(p.getRed(), p.getGreen(), p.getBlue())

w = range(10)

tot = 0
for num in w:
    tot += num
print(tot)

OUTPUT
45

w = range(10)


tot = 0
for num in w:
    print(num)
    tot += num
    print(tot)
print(tot)
OUTPUT
0
0
1
1
2
3
3
6
4
10
5
15
6
21
7
28
8
36
9
45
45



























OUTPUT ;
400
244
165 161 158

#IMAGE PROCCESSING - NEGATIVE IMAGE 
import image

img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,15)   # setDelay(0) turns off animation

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        newred = 255 - p.getRed()
        newgreen = 255 - p.getGreen()
        newblue = 255 - p.getBlue()

        newpixel = image.Pixel(newred, newgreen, newblue)
      
      
 #*****************WEEK 3 **************************

total_weight = int(input('Enter total weight of luggage:'))
num_pieces = int(input('Number of pieces of luggage?'))

if num_pieces!=0 and total_weight / num_pieces > 50:
   print('Average weight is greater than 50 pounds -> $100 surcharge.')

print('Luggage check complete.')

#Precedence of Operators
Level

Category

Operators

7(high)

exponent

**

6

multiplication

*,/,//,%

5

addition

+,-

4

relational

==,!=,<=,>=,>,<

3

logical

not

2

logical

and

1(low)

logical

or


        img.setPixel(col, row, newpixel)

img.draw(win)
win.exitonclick()

******

x = 15

if x % 2 == 0:
    print(x, "is even")
else:
    print(x, "is odd")
OUTPUT 
15 is odd

#unary selection

x = 10
if x < 0:
    print("The negative number ",  x, " is not valid here.")
print("This is always printed")

OUTPUT
This is always printed
x = 10
y = 10

if x < y:
    print("x is less than y")
else:
    if x > y:
        print("x is greater than y")
    else:
        print("x and y must be equal")
OUTPUT 
x and y must be equal

# CHAINED COINDITIONAL

x = 10
y = 10

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x and y must be equal")
OUTPUT
x and y must be equal

percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
resps = []
for i in percent_rain:
    if i > 90:
        resps.append("Bring an umbrella.")
    elif i >80:
        resps.append("Good for the flowers?")                   
    elif i > 50:
        resps.append("Watch out for clouds!")
    else:
        resps.append("Nice day!")
         
#*************************************************************************************************************************


#The Accumulator Pattern with Conditionals

tom = " hlo maklae it i tom "
total = 0
for phra in tom:
    if phra != " ":
        total = total + 1
print(total)

OUTPUT 
15

msge = " hi tom, how are u tom, nice to meet you " ,"tom"
a=0
for msg in msge:
    if msg in["tom"]:
        a+=1
print(a)

OUTPUT
1

nums = [9, 3, 8, 11, 5, 29, 2]
best_num = [0]
for n in nums:
    if n > best_num:
        best_num = n
print(best_num)

OUTPUT 
29

#MUTABILITY

fruit = ["banana", "apple", "cherry"]
print(fruit)

fruit[0] = "pear"
fruit[-1] = "orange"
print(fruit)

OUTPUT
['banana', 'apple', 'cherry']
['pear', 'apple', 'orange']

alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = ['x', 'y']
print(alist)
OUTPUT
['a', 'x', 'y', 'd', 'e', 'f']

alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = []
print(alist)

OUTPUT
['a', 'd', 'e', 'f']

alist = ['a', 'd', 'f']
alist[1:1] = ['b', 'c']
print(alist)
alist[4:4] = ['e']
print(alist)

OUTPUT
['a', 'b', 'c', 'd', 'f']
['a', 'b', 'c', 'd', 'e', 'f']

greeting = "Hello, world!"
newGreeting = 'J' + greeting[1:]
print(newGreeting)
print(greeting)          # same as it was

OUTPUT
Jello, world!
Hello, world!

a = ['one', 'two', 'three']
del a[1]
print(a)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
del alist[1:5]
print(alist)

OUTPUT
['one', 'three']
['a', 'f']

a = "banana"
b = "banana"
print(a is b)
print(id(a))
print(id(b))

OUTPUT 
True
2
2

a = [81,82,83]
b = [81,82,83]

print(a is b)

print(a == b)

print(id(a))
print(id(b))
OUTPUT
False
True
3
4

ALIASING

a = [81, 82, 83]
b = a
print(a is b)

OUTPT

TRUE

a = [81,82,83]
b = [81,82,83]
print(a is b)

b = a
print(a == b)
print(a is b)

b[0] = 5
print(a)

OUTPUT 

False
True
True
[5, 82, 83]

CLONING LIST 

a = [81,82,83]

b = a[:]       # make a clone using slice
print(a == b)
print(a is b)

b[0] = 5

OUTPUT 
True
False
[81, 82, 83]
[5, 82, 83]

print(a)
print(b)

#*****************************************************
MUTATATING METHOD 

mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist.insert(1, 12)
print(mylist)
print(mylist.count(12))

print(mylist.index(3))
print(mylist.count(5))

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

mylist.remove(5)
print(mylist)

lastitem = mylist.pop()
print(lastitem)
print(mylist)

OUTPUT 

[5, 27, 3, 12]
[5, 12, 27, 3, 12]
2
3
1
[12, 3, 27, 12, 5]
[3, 5, 12, 12, 27]
[3, 12, 12, 27]
27
[3, 12, 12]

mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist = mylist.sort()   #probably an error
print(mylist)

OUTPUT 
[5, 27, 3, 12]
None


origlist = [45,32,88]

origlist.append("cat")
print(origlist)

OUTPUT 
[45, 32, 88, 'cat']

origlist = [45,32,88]
print("origlist:", origlist)
print("the identifier:", id(origlist))             #id of the list before changes
newlist = origlist + ['cat']
print("newlist:", newlist)
print("the identifier:", id(newlist))              #id of the list after concatentation
origlist.append('cat')
print("origlist:", origlist)
print("the identifier:", id(origlist))             #id of the list after append is used

OUTPUT 

origlist: [45, 32, 88]
the identifier: 2
newlist: [45, 32, 88, 'cat']
the identifier: 3
origlist: [45, 32, 88, 'cat']
the identifier: 2
   
st = "Warmth"
a = []
b = a + [st[0]]
c = b + [st[1]]
d = c + [st[2]]
e = d + [st[3]]
f = e + [st[4]]
g = f + [st[5]]
print(g)

OUTPUT 
['W', 'a', 'r', 'm', 't', 'h']

st = "Warmth"
a = []
a.append(st[0])
a.append(st[1])
a.append(st[2])
a.append(st[3])
a.append(st[4])
a.append(st[5])
print(a)

OUTPUT 
['W', 'a', 'r', 'm', 't', 'h']

#********************************************************

NON-MUTATING METHODS ON STRING 

ss = "Hello, World"
print(ss.upper())

tt = ss.lower()
print(tt)
print(ss)

OUTPUT 
HELLO, WORLD
hello, world
Hello, World

ss = "    Hello, World    "

els = ss.count("l")
print(els)

print("***"+ss.strip()+"***")

news = ss.replace("o", "***")
print(news)

OUTPUT 
3
***Hello, World***
    Hell***, W***rld    

   scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in scores:
    name = person[0]
    score = person[1]
    print("Hello " + name + ". Your score is " + str(score))
OUTPUT 
Hello Rodney Dangerfield. Your score is -1
Hello Marlon Brando. Your score is 1
Hello You. Your score is 100


scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in scores:
    name = person[0]
    score = person[1]
    print("Hello {}. Your score is {}.".format(name, score))

OUTPTUT 
Hello Rodney Dangerfield. Your score is -1.
Hello Marlon Brando. Your score is 1.
Hello You. Your score is 100.

person = input('Enter your name: ')
print('Hello {}!'.format(person))

OUTPUT 
Hello hp!

origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${} discounted by {}% is ${}.'.format(origPrice, discount, newPrice)
print(calculation)

OUTPUT 
$76.0 discounted by 70.0% is $22.8.


origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${:.2f} discounted by {}% is ${:.2f}.'.format(origPrice, discount, newPrice)
print(calculation)

OUTPUT 
$67.00 discounted by 89.0% is $7.37.

name = "Sally"
greeting = "Nice to meet you"
s = "Hello, {}. {}."

print(s.format(name,greeting)) # will print Hello, Sally. Nice to meet you.

print(s.format(greeting,name)) # will print Hello, Nice to meet you. Sally.

print(s.format(name)) # 2 {}s, only one interpolation item! Not ideal.

OUTPUT
Hello, Sally. Nice to meet you.
Hello, Nice to meet you. Sally


#**************************

The Accumulator Pattern with Lists

nums = [3, 5, 8]
accum = []
for w in nums:
    x = w**2
    accum.append(x)
print(accum)

OUTPUT
[9, 25, 64]



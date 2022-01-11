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

 Index Operator: Working with the Characters of a String¶
 
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




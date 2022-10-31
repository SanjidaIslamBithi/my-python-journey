#Lists in Python represent ordered sequences of values. Here is an example of how to create them:
primes = [2, 3, 5, 7]


#We can put other types of things in lists:

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

#We can even make a list of lists:

hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]
# (I could also have written this on one line, but it can get hard to read)
hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]

#A list can contain a mix of different types of variables:

my_favourite_things = [32, 'raindrops on roses', help]
# (Yes, Python's help function is *definitely* one of my favourite things)

planets[0]

#"Mercury"

planets[1]
#'Venus'

#Which planet is furthest from the sun?

#Elements at the end of the list can be accessed with negative numbers, starting from -1:

planets[-1]
#'Neptune'

planets[-2]
#'Uranus'



#Slicing-----*
#What are the first three planets? We can answer this question using slicing:

#planets[0:3] is our way of asking for the elements of planets starting from index 0 and continuing up to but not including index 3.

planets[0:3]
#['Mercury', 'Venus', 'Earth']

#The starting and ending indices are both optional. If I leave out the start index, it's assumed to be 0. So I could rewrite the expression above as:

planets[:3]
#['Mercury', 'Venus', 'Earth']

#If I leave out the end index, it's assumed to be the length of the list.

planets[3:]

#['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

#i.e. the expression above means "give me all the planets from index 3 onward".

#We can also use negative indices when slicing:

# All the planets except the first and last
planets[1:-1]
#['Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus']

# The last 3 planets
planets[-3:]
#['Saturn', 'Uranus', 'Neptune']

#Changing lists---***

planets[3] = 'Malacandra'
planets

# #['Mercury',
#  'Venus',
#  'Earth',
#  'Malacandra',----**** change occoured here
#  'Jupiter',
#  'Saturn',
#  'Uranus',
#  'Neptune']


#Hm, that's quite a mouthful. Let's compensate by shortening the names of the first 3 planets.


planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)

#['Mur', 'Vee', 'Ur', 'Malacandra', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']


# That was silly. Let's give them back their old names
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars',]

#['Mur', 'Vee', 'Ur', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']


###List functions---***
#len gives the length of a list:

# How many planets are there?
len(planets)

#8

#sorted returns a sorted version of a list:

# The planets sorted in alphabetical order
sorted(planets)
['Earth', 'Jupiter', 'Mars', 'Mercury', 'Neptune', 'Saturn', 'Uranus', 'Venus']
#sum does what you might expect:

primes = [2, 3, 5, 7]
#-------***
sum(primes)
#17

primes = [5, 7]
sum(primes)
#12

#We've previously used the min and max to get the minimum or maximum of several arguments. But we can also pass in a single list argument.
max(primes)

#7


#Interlude: objects---**

#numbers in Python carry around an associated variable called imag representing their imaginary part. (You'll probably never need to use this unless you're doing some very weird math.)

x = 12
# x is a real number, so its imaginary part is 0.
print(x.imag)
#0
# Here's how to make a complex number, in case you've ever been curious:
c = 12 + 3j
print(c.imag)

#3.0


#The things an object carries around can also include functions. A function attached to an object is called a method. (Non-function things attached to an object, such as imag, are called attributes).

#For example, numbers have a method called bit_length. Again, we access it using dot syntax:
x.bit_length
#<function int.bit_length()>

#To actually call it, we add parentheses:

x.bit_length()
#4

#Help on built-in function bit_length:

#bit_length() method of builtins.int instance
   # Number of bits necessary to represent self in binary.
bin(37)
    #'0b100101'
(37).bit_length()
    #6


    ######List methods¶
#list.append modifies a list by adding an item to the end:

# Pluto is a planet darn it!
planets.append('Pluto')
#Why does the cell above have no output? Let's check the documentation by calling help(planets.append).

#Aside: append is a method carried around by all objects of type list, not just planets, so we also could have called help(list.append). However, if we try to call help(append), Python will complain that no variable exists called "append". The "append" name only exists within lists - it doesn't exist as a standalone name like builtin functions such as max or len.

help(planets.append)
#Help on built-in function append:

#append(object, /) method of builtins.list instance
  #  Append object to the end of the list.

#The -> None part is telling us that list.append doesn't return anything. But if we check the value of planets, we can see that the method call modified the value of planets:

planets
['Mercury',
 'Venus',
 'Earth',
 'Mars',
 'Jupiter',
 'Saturn',
 'Uranus',
 'Neptune',
 'Pluto']

#list.pop removes and returns the last element of a list:

planets.pop()
'Pluto'
planets
['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']


###Searching lists


#Where does Earth fall in the order of planets? We can get its index using the list.index method.

planets.index('Earth')
#2

#It comes third (i.e. at index 2 - 0 indexing!).

#At what index does Pluto occur?

planets.index('Pluto')
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# /tmp/ipykernel_20/2263615293.py in <module>
# ----> 1 planets.index('Pluto')

# ValueError: 'Pluto' is not in list
# Oh, that's right...

#o avoid unpleasant surprises like this, we can use the in operator to determine whether a list contains a particular value:

# Is Earth a planet?
"Earth" in planets
True
# Is Calbefraques a planet?
"Calbefraques" in planets
False
# There are a few more interesting list methods we haven't covered. If you want to learn about all the methods and attributes attached to a particular object, we can call help() on the object itself. For example, help(planets) will tell us about all the list methods:

help(planets)
#Help on list object:

# class list(object)
#  |  list(iterable=(), /)
#  |  
#  |  Built-in mutable sequence.
#  |  
#  |  If no argument is given, the constructor creates a new empty list.
#  |  The argument must be an iterable if specified.
#  |  
#  |  Methods defined here:
#  |  
#  |  __add__(self, value, /)
#  |      Return self+value.
#  |  
#  |  __contains__(self, key, /)
#  |      Return key in self.
#  |  
#  |  __delitem__(self, key, /)
#  |      Delete self[key].
#  |  
#  |  __eq__(self, value, /)
#  |      Return self==value.
#  |  
#  |  __ge__(self, value, /)
#  |      Return self>=value.
#  |  
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |  
#  |  __getitem__(...)
#  |      x.__getitem__(y) <==> x[y]
#  |  
#  |  __gt__(self, value, /)
#  |      Return self>value.
#  |  
#  |  __iadd__(self, value, /)
#  |      Implement self+=value.
#  |  
#  |  __imul__(self, value, /)
#  |      Implement self*=value.
#  |  
#  |  __init__(self, /, *args, **kwargs)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |  
#  |  __iter__(self, /)
#  |      Implement iter(self).
#  |  
#  |  __le__(self, value, /)
#  |      Return self<=value.
#  |  
#  |  __len__(self, /)
#  |      Return len(self).
#  |  
#  |  __lt__(self, value, /)
#  |      Return self<value.
#  |  
#  |  __mul__(self, value, /)
#  |      Return self*value.
#  |  
#  |  __ne__(self, value, /)
#  |      Return self!=value.
#  |  
#  |  __repr__(self, /)
#  |      Return repr(self).
#  |  
#  |  __reversed__(self, /)
#  |      Return a reverse iterator over the list.
#  |  
#  |  __rmul__(self, value, /)
#  |      Return value*self.
#  |  
#  |  __setitem__(self, key, value, /)
#  |      Set self[key] to value.
#  |  
#  |  __sizeof__(self, /)
#  |      Return the size of the list in memory, in bytes.
#  |  
#  |  append(self, object, /)
#  |      Append object to the end of the list.
#  |  
#  |  clear(self, /)
#  |      Remove all items from list.
#  |  
#  |  copy(self, /)
#  |      Return a shallow copy of the list.
#  |  
#  |  count(self, value, /)
#  |      Return number of occurrences of value.
#  |  
#  |  extend(self, iterable, /)
#  |      Extend list by appending elements from the iterable.
#  |  
#  |  index(self, value, start=0, stop=9223372036854775807, /)
#  |      Return first index of value.
#  |      
#  |      Raises ValueError if the value is not present.
#  |  
#  |  insert(self, index, object, /)
#  |      Insert object before index.
#  |  
#  |  pop(self, index=-1, /)
#  |      Remove and return item at index (default last).
#  |      
#  |      Raises IndexError if list is empty or index is out of range.
#  |  
#  |  remove(self, value, /)
#  |      Remove first occurrence of value.
#  |      
#  |      Raises ValueError if the value is not present.
#  |  
#  |  reverse(self, /)
#  |      Reverse *IN PLACE*.
#  |  
#  |  sort(self, /, *, key=None, reverse=False)
#  |      Stable sort *IN PLACE*.
#  |  
#  |  ----------------------------------------------------------------------
#  |  Static methods defined here:
#  |  
#  |  __new__(*args, **kwargs) from builtins.type
#  |      Create and return a new object.  See help(type) for accurate signature.
#  |  
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes defined here:
#  |  
#  |  __hash__ = None

# Click the "output" button to see the full help page. Lists have lots of methods with weird-looking names like __eq__ and __iadd__. Don't worry too much about these for now. (You'll probably never call such methods directly. But they get called behind the scenes when we use syntax like indexing or comparison operators.) The most interesting methods are toward the bottom of the list (append, clear, copy, etc.).


#####Tuples

#Tuples are almost exactly the same as lists. They differ in just two ways.

#1: The syntax for creating them uses parentheses instead of square brackets

t = (1, 2, 3)
t = 1, 2, 3 # equivalent to above
t

#(1, 2, 3)


#2: They cannot be modified (they are immutable).

t[0] = 100
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_20/816329950.py in <module>
# ----> 1 t[0] = 100

# TypeError: 'tuple' object does not support item assignment
# Tuples are often used for functions that have multiple return values.

#For example, the as_integer_ratio() method of float objects returns a numerator and a denominator in the form of a tuple:

x = 0.125
x.as_integer_ratio()
#(1, 8)

#These multiple return values can be individually assigned as follows:

numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)
#0.125


# Finally we have some insight into the classic Stupid Python Trick™ for swapping two variables!

a = 1
b = 0
a, b = b, a
print(a, b)
#0 1


##-----------test
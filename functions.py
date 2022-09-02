help(round)
#Help on built-in function round in module builtins:

#round(number, ndigits=None)
   #Round a number to a given precision in decimal digits.

   # The return value is an integer if ndigits is omitted or None.  Otherwise
   # the return value has the same type as the number.  ndigits may be negative.
   
   
   #help() displays two things:

#the header of that function round(number, ndigits=None). In this case, this tells us that round() takes an argument we can describe as number. Additionally, we can optionally give a separate argument which could be described as ndigits.
#A brief English description of what the function does.

help(round(-2.01))

#Help on int object:

#class int(object)
#|  int([x]) -> integer
#|  int(x, base=10) -> integer
#|  
#|  Convert a number or string to an integer, or return 0 if no arguments
#|  are given.  If x is a number, return x.__int__().  For floating point
#|  numbers, this truncates towards zero.
#|  
#|  If x is not a number or if base is given, then x must be a string,
#|  bytes, or bytearray instance representing an integer literal in the
#|  given base.  The literal can be preceded by '+' or '-' and be surrounded
#|  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
#|  Base 0 means to interpret the base from the string as an integer literal.
#|  >>> int('0b100', base=0)
#|  4
#|  
#|  Built-in subclasses:
#|      bool
#|  
#|  Methods defined here:
#|  
#|  __abs__(self, /)
#|      abs(self)
#|  
#|  __add__(self, value, /)
#|      Return self+value.
#|  
#|  __and__(self, value, /)
#|      Return self&value.
#|  
#|  __bool__(self, /)
#|      True if self else False
#|  
#|  __ceil__(...)
#|      Ceiling of an Integral returns itself.
#|  
#|  __divmod__(self, value, /)
#|      Return divmod(self, value).
#|  
#|  __eq__(self, value, /)
#|      Return self==value.
#|  
#|  __float__(self, /)
#|      float(self)
#|  
#|  __floor__(...)
#|      Flooring an Integral returns itself.
#|  
#|  __floordiv__(self, value, /)
#|      Return self//value.
#|  
#|  __format__(self, format_spec, /)
#|      Default object formatter.
#|  
#|  __ge__(self, value, /)
#|      Return self>=value.
#|  
#|  __getattribute__(self, name, /)
#|      Return getattr(self, name).
#|  
#|  __getnewargs__(self, /)
#|  
#|  __gt__(self, value, /)
#|      Return self>value.
#|  
#|  __hash__(self, /)
#|      Return hash(self).
#|  
#|  __index__(self, /)
#|      Return self converted to an integer, if self is suitable for use as an index into a list.
#|  
#|  __int__(self, /)
#|      int(self)
#|  
#|  __invert__(self, /)
#|      ~self
#|  
#|  __le__(self, value, /)
#|      Return self<=value.
#|  
#|  __lshift__(self, value, /)
#|      Return self<<value.
#|  
#|  __lt__(self, value, /)
#|      Return self<value.
#|  
#|  __mod__(self, value, /)
#|      Return self%value.
#|  
#|  __mul__(self, value, /)
#|      Return self*value.
#|  
#|  __ne__(self, value, /)
#|      Return self!=value.
#|  
#|  __neg__(self, /)
#|      -self
#|  
#|  __or__(self, value, /)
#|      Return self|value.
#|  
#|  __pos__(self, /)
#|      +self
#|  
#|  __pow__(self, value, mod=None, /)
#|      Return pow(self, value, mod).
#|  
#|  __radd__(self, value, /)
#|      Return value+self.
#|  
#|  __rand__(self, value, /)
#|      Return value&self.
#|  
#|  __rdivmod__(self, value, /)
#|      Return divmod(value, self).
#|  
#|  __repr__(self, /)
#|      Return repr(self).
#|  
#|  __rfloordiv__(self, value, /)
#|      Return value//self.
#|  
#|  __rlshift__(self, value, /)
#|      Return value<<self.
#|  
#|  __rmod__(self, value, /)
#|      Return value%self.
#|  
#|  __rmul__(self, value, /)
#|      Return value*self.
#|  
#|  __ror__(self, value, /)
#|      Return value|self.
#|  
#|  __round__(...)
#|      Rounding an Integral returns itself.
#|      Rounding with an ndigits argument also returns an integer.
#|  
#|  __rpow__(self, value, mod=None, /)
#|      Return pow(value, self, mod).
#|  
#|  __rrshift__(self, value, /)
#|      Return value>>self.
#|  
#|  __rshift__(self, value, /)
#|      Return self>>value.
#|  
#|  __rsub__(self, value, /)
#|      Return value-self.
#|  
#|  __rtruediv__(self, value, /)
#|      Return value/self.
#|  
#|  __rxor__(self, value, /)
#|      Return value^self.
#|  
#|  __sizeof__(self, /)
#|      Returns size in memory, in bytes.
#|  
#|  __sub__(self, value, /)
#|      Return self-value.
#|  
#|  __truediv__(self, value, /)
#|      Return self/value.
#|  
#|  __trunc__(...)
#|      Truncating an Integral returns itself.
#|  
#|  __xor__(self, value, /)
#|      Return self^value.
#|  
#|  as_integer_ratio(self, /)
#|      Return integer ratio.
#|      
#|      Return a pair of integers, whose ratio is exactly equal to the original int
#|      and with a positive denominator.
#|      
#|      >>> (10).as_integer_ratio()
#|      (10, 1)
#|      >>> (-10).as_integer_ratio()
#|      (-10, 1)
#|      >>> (0).as_integer_ratio()
#|      (0, 1)
#|  
#|  bit_length(self, /)
#|      Number of bits necessary to represent self in binary.
#|      
#|      >>> bin(37)
#|      '0b100101'
#|      >>> (37).bit_length()
#|      6
#|  
#|  conjugate(...)
#|      Returns self, the complex conjugate of any int.
#|  
#|  to_bytes(self, /, length, byteorder, *, signed=False)
#|      Return an array of bytes representing an integer.
#|      
#|      length
#|        Length of bytes object to use.  An OverflowError is raised if the
#|        integer is not representable with the given number of bytes.
#|      byteorder
#|        The byte order used to represent the integer.  If byteorder is 'big',
#|        the most significant byte is at the beginning of the byte array.  If
#|        byteorder is 'little', the most significant byte is at the end of the
#|        byte array.  To request the native byte order of the host system, use
#|        `sys.byteorder' as the byte order value.
#|      signed
#|        Determines whether two's complement is used to represent the integer.
#|        If signed is False and a negative integer is given, an OverflowError
#|        is raised.
#|  
#|  ----------------------------------------------------------------------
#|  Class methods defined here:
#|  
#|  from_bytes(bytes, byteorder, *, signed=False) from builtins.type
#|      Return the integer represented by the given array of bytes.
#|      
#|      bytes
#|        Holds the array of bytes to convert.  The argument must either
#|        support the buffer protocol or be an iterable object producing bytes.
#|        Bytes and bytearray are examples of built-in objects that support the
#|        buffer protocol.
#|      byteorder
#|        The byte order used to represent the integer.  If byteorder is 'big',
#|        the most significant byte is at the beginning of the byte array.  If
#|        byteorder is 'little', the most significant byte is at the end of the
#|        byte array.  To request the native byte order of the host system, use
#|        `sys.byteorder' as the byte order value.
#|      signed
#|        Indicates whether two's complement is used to represent the integer.
#|  
#|  ----------------------------------------------------------------------
#|  Static methods defined here:
#|  
#|  __new__(*args, **kwargs) from builtins.type
#|      Create and return a new object.  See help(type) for accurate signature.
#|  
#|  ----------------------------------------------------------------------
#|  Data descriptors defined here:
#|  
#|  denominator
#|      the denominator of a rational number in lowest terms
#|  
#|  imag
#|      the imaginary part of a complex number
#|  
#|  numerator
#|      the numerator of a rational number in lowest terms
#|  
#|  real
#|      the real part of a complex number
#

help(print)
#Help on built-in function print in module builtins:

#print(...)
#   print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
#   
#   Prints the values to a stream, or to sys.stdout by default.
#   Optional keyword arguments:
#   file:  a file-like object (stream); defaults to the current sys.stdout.
#   sep:   string inserted between values, default a space.
#   end:   string appended after the last value, default a newline.
#   flush: whether to forcibly flush the stream.
#



def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

    #to understand
    print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7), 
    # Python allows trailing commas in argument lists. How nice is that?
)
#9 0 1

help(least_difference)
#Help on function least_difference in module __main__:

#least_difference(a, b, c)


#Docstrings

def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)
#The docstring is a triple-quoted string (which may span multiple lines) that comes immediately after the header of a function. When we call help() on a function, it shows the docstring.

help(least_difference)
#Help on function least_difference in module __main__:

#least_difference(a, b, c)
   # Return the smallest difference between any two numbers
   # among a, b and c.
    
   # >>> least_difference(1, 5, -5)
   # 4

#Functions that don't return¶
def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    min(diff1, diff2, diff3)
    
print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),
)

#None None None

mystery = print()
print(mystery)
#None


#Default arguments
print(1, 2, 3, sep=' < ')
#1 < 2 < 3

print(1, 2, 3)
#1 2 3

def greet(who="Colin"):
    print("Hello,", who)
    
greet()
greet(who="Kaggle")
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("world")
#Hello, Colin
#Hello, Kaggle
#Hello, world

#Functions Applied to Functions

def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1), 
    sep='\n', # '\n' is the newline character - it starts a new line
)
#5
#25

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)

#Which number is biggest?
#100
#Which number is the biggest modulo 5?
#14





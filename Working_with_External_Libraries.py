# Working with External Libraries
# --------Imports
# So far we've talked about types and functions which are built-in to the language.

# But one of the best things about Python (especially if you're a data scientist) is the vast number of high-quality custom libraries that have been written for it.

# Some of these libraries are in the "standard library", meaning you can find them anywhere you run Python. Other libraries can be easily added, even if they aren't always shipped with Python.

# Either way, we'll access this code with imports.

# We'll start our example by importing math from the standard library.

import math

print("It's math! It has type {}".format(type(math)))

# It's math! It has type <class 'module'>
# math is a module. A module is just a collection of variables (a namespace, if you like) defined by someone else. We can see all the names in math using the built-in function dir().


print(dir(math))
# ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']


# We can access these variables using dot syntax. Some of them refer to simple values, like math.pi:

print("pi to 4 significant digits = {:.4}".format(math.pi))
# pi to 4 significant digits = 3.142
# But most of what we'll find in the module are functions, like math.log:

math.log(32, 2)
# 5.0
# Of course, if we don't know what math.log does, we can call help() on it:

help(math.log)
# Help on built-in function log in module math:

# log(...)
#     log(x, [base=math.e])
#     Return the logarithm of x to the given base.
    
#     If the base not specified, returns the natural logarithm (base e) of x.

# We can also call help() on the module itself. This will give us the combined documentation for all the functions and values in the module (as well as a high-level description of the module). Click the "output" button to see the whole math help page.



help(math)
# Help on module math:

# NAME
#     math

# MODULE REFERENCE
#     https://docs.python.org/3.7/library/math
    
#     The following documentation is automatically generated from the Python
#     source files.  It may be incomplete, incorrect or include features that
#     are considered implementation detail and may vary between Python
#     implementations.  When in doubt, consult the module reference at the
#     location listed above.

# DESCRIPTION
#     This module provides access to the mathematical functions
#     defined by the C standard.

# FUNCTIONS
#     acos(x, /)
#         Return the arc cosine (measured in radians) of x.
    
#     acosh(x, /)
#         Return the inverse hyperbolic cosine of x.
    
#     asin(x, /)
#         Return the arc sine (measured in radians) of x.
    
#     asinh(x, /)
#         Return the inverse hyperbolic sine of x.
    
#     atan(x, /)
#         Return the arc tangent (measured in radians) of x.
    
#     atan2(y, x, /)
#         Return the arc tangent (measured in radians) of y/x.
        
#         Unlike atan(y/x), the signs of both x and y are considered.
    
#     atanh(x, /)
#         Return the inverse hyperbolic tangent of x.
    
#     ceil(x, /)
#         Return the ceiling of x as an Integral.
        
#         This is the smallest integer >= x.
    
#     copysign(x, y, /)
#         Return a float with the magnitude (absolute value) of x but the sign of y.
        
#         On platforms that support signed zeros, copysign(1.0, -0.0)
#         returns -1.0.
    
#     cos(x, /)
#         Return the cosine of x (measured in radians).
    
#     cosh(x, /)
#         Return the hyperbolic cosine of x.
    
#     degrees(x, /)
#         Convert angle x from radians to degrees.
    
#     erf(x, /)
#         Error function at x.
    
#     erfc(x, /)
#         Complementary error function at x.
    
#     exp(x, /)
#         Return e raised to the power of x.
    
#     expm1(x, /)
#         Return exp(x)-1.
        
#         This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    
#     fabs(x, /)
#         Return the absolute value of the float x.
    
#     factorial(x, /)
#         Find x!.
        
#         Raise a ValueError if x is negative or non-integral.
    
#     floor(x, /)
#         Return the floor of x as an Integral.
        
#         This is the largest integer <= x.
    
#     fmod(x, y, /)
#         Return fmod(x, y), according to platform C.
        
#         x % y may differ.
    
#     frexp(x, /)
#         Return the mantissa and exponent of x, as pair (m, e).
        
#         m is a float and e is an int, such that x = m * 2.**e.
#         If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    
#     fsum(seq, /)
#         Return an accurate floating point sum of values in the iterable seq.
        
#         Assumes IEEE-754 floating point arithmetic.
    
#     gamma(x, /)
#         Gamma function at x.
    
#     gcd(x, y, /)
#         greatest common divisor of x and y
    
#     hypot(x, y, /)
#         Return the Euclidean distance, sqrt(x*x + y*y).
    
#     isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
#         Determine whether two floating point numbers are close in value.
        
#           rel_tol
#             maximum difference for being considered "close", relative to the
#             magnitude of the input values
#           abs_tol
#             maximum difference for being considered "close", regardless of the
#             magnitude of the input values
        
#         Return True if a is close in value to b, and False otherwise.
        
#         For the values to be considered close, the difference between them
#         must be smaller than at least one of the tolerances.
        
#         -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
#         is, NaN is not close to anything, even itself.  inf and -inf are
#         only close to themselves.
    
#     isfinite(x, /)
#         Return True if x is neither an infinity nor a NaN, and False otherwise.
    
#     isinf(x, /)
#         Return True if x is a positive or negative infinity, and False otherwise.
    
#     isnan(x, /)
#         Return True if x is a NaN (not a number), and False otherwise.
    
#     ldexp(x, i, /)
#         Return x * (2**i).
        
#         This is essentially the inverse of frexp().
    
#     lgamma(x, /)
#         Natural logarithm of absolute value of Gamma function at x.
    
#     log(...)
#         log(x, [base=math.e])
#         Return the logarithm of x to the given base.
        
#         If the base not specified, returns the natural logarithm (base e) of x.
    
#     log10(x, /)
#         Return the base 10 logarithm of x.
    
#     log1p(x, /)
#         Return the natural logarithm of 1+x (base e).
        
#         The result is computed in a way which is accurate for x near zero.
    
#     log2(x, /)
#         Return the base 2 logarithm of x.
    
#     modf(x, /)
#         Return the fractional and integer parts of x.
        
#         Both results carry the sign of x and are floats.
    
#     pow(x, y, /)
#         Return x**y (x to the power of y).
    
#     radians(x, /)
#         Convert angle x from degrees to radians.
    
#     remainder(x, y, /)
#         Difference between x and the closest integer multiple of y.
        
#         Return x - n*y where n*y is the closest integer multiple of y.
#         In the case where x is exactly halfway between two multiples of
#         y, the nearest even value of n is used. The result is always exact.
    
#     sin(x, /)
#         Return the sine of x (measured in radians).
    
#     sinh(x, /)
#         Return the hyperbolic sine of x.
    
#     sqrt(x, /)
#         Return the square root of x.
    
#     tan(x, /)
#         Return the tangent of x (measured in radians).
    
#     tanh(x, /)
#         Return the hyperbolic tangent of x.
    
#     trunc(x, /)
#         Truncates the Real x to the nearest Integral toward 0.
        
#         Uses the __trunc__ magic method.

# DATA
#     e = 2.718281828459045
#     inf = inf
#     nan = nan
#     pi = 3.141592653589793
#     tau = 6.283185307179586

# FILE
#     /opt/conda/lib/python3.7/lib-dynload/math.cpython-37m-x86_64-linux-gnu.so







# ##-----Other import syntax
# If we know we'll be using functions in math frequently we can import it under a shorter alias to save some typing (though in this case "math" is already pretty short).

import math as mt
mt.pi
# 3.141592653589793


# You may have seen code that does this with certain popular libraries like Pandas, Numpy, Tensorflow, or Matplotlib. For example, it's a common convention to import numpy as np and import pandas as pd.

# The as simply renames the imported module. It's equivalent to doing something like:

import math
mt = math
# Wouldn't it be great if we could refer to all the variables in the math module by themselves? i.e. if we could just refer to pi instead of math.pi or mt.pi? Good news: we can do that.

from math import *
print(pi, log(32, 2))
# 3.141592653589793 5.0
# import * makes all the module's variables directly accessible to you (without any dotted prefix).

# Bad news: some purists might grumble at you for doing this.

# Worse: they kind of have a point.

from math import *
from numpy import *
print(pi, log(32, 2))
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_19/3018510453.py in <module>
#       1 from math import *
#       2 from numpy import *
# ----> 3 print(pi, log(32, 2))

# TypeError: return arrays must be of ArrayType
# What has happened? It worked before!

# These kinds of "star imports" can occasionally lead to weird, difficult-to-debug situations.

# The problem in this case is that the math and numpy modules both have functions called log, but they have different semantics. Because we import from numpy second, its log overwrites (or "shadows") the log variable we imported from math.

# A good compromise is to import only the specific things we'll need from each module:

from math import log, pi
from numpy import asarray
# Submodules
# We've seen that modules contain variables which can refer to functions or values. Something to be aware of is that they can also have variables referring to other modules.

import numpy
print("numpy.random is a", type(numpy.random))
print("it contains names such as...",
      dir(numpy.random)[-15:]
     )
# numpy.random is a <class 'module'>
# it contains names such as... ['seed', 'set_state', 'shuffle', 'standard_cauchy', 'standard_exponential', 'standard_gamma', 'standard_normal', 'standard_t', 'test', 'triangular', 'uniform', 'vonmises', 'wald', 'weibull', 'zipf']
# So if we import numpy as above, then calling a function in the random "submodule" will require two dots.

# Roll 10 dice
rolls = numpy.random.randint(low=1, high=6, size=10)
rolls
array([4, 2, 4, 5, 3, 1, 4, 2, 5, 1])
# Oh the places you'll go, oh the objects you'll see
# So after 6 lessons, you're a pro with ints, floats, bools, lists, strings, and dicts (right?).

# Even if that were true, it doesn't end there. As you work with various libraries for specialized tasks, you'll find that they define their own types which you'll have to learn to work with. For example, if you work with the graphing library matplotlib, you'll be coming into contact with objects it defines which represent Subplots, Figures, TickMarks, and Annotations. pandas functions will give you DataFrames and Series.

# In this section, I want to share with you a quick survival guide for working with strange types.

# Three tools for understanding strange objects
# In the cell above, we saw that calling a numpy function gave us an "array". We've never seen anything like this before (not in this course anyways). But don't panic: we have three familiar builtin functions to help us here.

# 1: type() (what is this thing?)

type(rolls)
numpy.ndarray
# 2: dir() (what can I do with it?)

print(dir(rolls))
# ['T', '__abs__', '__add__', '__and__', '__array__', '__array_finalize__', '__array_function__', '__array_interface__', '__array_prepare__', '__array_priority__', '__array_struct__', '__array_ufunc__', '__array_wrap__', '__bool__', '__class__', '__complex__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__iand__', '__ifloordiv__', '__ilshift__', '__imatmul__', '__imod__', '__imul__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__ior__', '__ipow__', '__irshift__', '__isub__', '__iter__', '__itruediv__', '__ixor__', '__le__', '__len__', '__lshift__', '__lt__', '__matmul__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmatmul__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__xor__', 'all', 'any', 'argmax', 'argmin', 'argpartition', 'argsort', 'astype', 'base', 'byteswap', 'choose', 'clip', 'compress', 'conj', 'conjugate', 'copy', 'ctypes', 'cumprod', 'cumsum', 'data', 'diagonal', 'dot', 'dtype', 'dump', 'dumps', 'fill', 'flags', 'flat', 'flatten', 'getfield', 'imag', 'item', 'itemset', 'itemsize', 'max', 'mean', 'min', 'nbytes', 'ndim', 'newbyteorder', 'nonzero', 'partition', 'prod', 'ptp', 'put', 'ravel', 'real', 'repeat', 'reshape', 'resize', 'round', 'searchsorted', 'setfield', 'setflags', 'shape', 'size', 'sort', 'squeeze', 'std', 'strides', 'sum', 'swapaxes', 'take', 'tobytes', 'tofile', 'tolist', 'tostring', 'trace', 'transpose', 'var', 'view']
# If I want the average roll, the "mean" method looks promising...
rolls.mean()
# 3.1
# Or maybe I just want to turn the array into a list, in which case I can use "tolist"
rolls.tolist()
# [4, 2, 4, 5, 3, 1, 4, 2, 5, 1]
# 3: help() (tell me more)

# That "ravel" attribute sounds interesting. I'm a big classical music fan.
help(rolls.ravel)
# Help on built-in function ravel:

# ravel(...) method of numpy.ndarray instance
#     a.ravel([order])
    
#     Return a flattened array.
    
#     Refer to `numpy.ravel` for full documentation.
    
#     See Also
#     --------
#     numpy.ravel : equivalent function
    
#     ndarray.flat : a flat iterator on the array.

# Okay, just tell me everything there is to know about numpy.ndarray
# (Click the "output" button to see the novel-length output)
help(rolls)
# (Of course, you might also prefer to check out the online docs.)

# Operator overloading
# What's the value of the below expression?

[3, 4, 1, 2, 2, 1] + 10
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_19/2144087748.py in <module>
# ----> 1 [3, 4, 1, 2, 2, 1] + 10

# TypeError: can only concatenate list (not "int") to list
# What a silly question. Of course it's an error.

# But what about...

rolls + 10
# array([14, 12, 14, 15, 13, 11, 14, 12, 15, 11])
# We might think that Python strictly polices how pieces of its core syntax behave such as +, <, in, ==, or square brackets for indexing and slicing. But in fact, it takes a very hands-off approach. When you define a new type, you can choose how addition works for it, or what it means for an object of that type to be equal to something else.

# The designers of lists decided that adding them to numbers wasn't allowed. The designers of numpy arrays went a different way (adding the number to each element of the array).

Here are a few more examples of how numpy arrays interact unexpectedly with Python operators (or at least differently from lists).

# At which indices are the dice less than or equal to 3?
rolls <= 3
array([False,  True, False, False,  True,  True, False,  True, False,
        True])
xlist = [[1,2,3],[2,4,6],]
# Create a 2-dimensional array
x = numpy.asarray(xlist)
print("xlist = {}\nx =\n{}".format(xlist, x))
xlist = [[1, 2, 3], [2, 4, 6]]
x =
[[1 2 3]
 [2 4 6]]
# Get the last element of the second row of our numpy array
x[1,-1]
6
# Get the last element of the second sublist of our nested list?
xlist[1,-1]
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_19/3020169379.py in <module>
#       1 # Get the last element of the second sublist of our nested list?
# ----> 2 xlist[1,-1]

# TypeError: list indices must be integers or slices, not tuple
# numpy's ndarray type is specialized for working with multi-dimensional data, so it defines its own logic for indexing, allowing us to index by a tuple to specify the index at each dimension.

# When does 1 + 1 not equal 2?
# Things can get weirder than this. You may have heard of (or even used) tensorflow, a Python library popularly used for deep learning. It makes extensive use of operator overloading.

import tensorflow as tf
# Create two constants, each with value 1
a = tf.constant(1)
b = tf.constant(1)
# Add them together to get...
a + b
# User settings:

#    KMP_AFFINITY=granularity=fine,verbose,compact,1,0
#    KMP_BLOCKTIME=0
#    KMP_SETTINGS=1
#    KMP_WARNINGS=0

# Effective settings:

#    KMP_ABORT_DELAY=0
#    KMP_ADAPTIVE_LOCK_PROPS='1,1024'
#    KMP_ALIGN_ALLOC=64
#    KMP_ALL_THREADPRIVATE=128
#    KMP_ATOMIC_MODE=2
#    KMP_BLOCKTIME=0
#    KMP_CPUINFO_FILE: value is not defined
#    KMP_DETERMINISTIC_REDUCTION=false
#    KMP_DEVICE_THREAD_LIMIT=2147483647
#    KMP_DISP_NUM_BUFFERS=7
#    KMP_DUPLICATE_LIB_OK=false
#    KMP_ENABLE_TASK_THROTTLING=true
#    KMP_FORCE_REDUCTION: value is not defined
#    KMP_FOREIGN_THREADS_THREADPRIVATE=true
#    KMP_FORKJOIN_BARRIER='2,2'
#    KMP_FORKJOIN_BARRIER_PATTERN='hyper,hyper'
#    KMP_GTID_MODE=3
#    KMP_HANDLE_SIGNALS=false
#    KMP_HOT_TEAMS_MAX_LEVEL=1
#    KMP_HOT_TEAMS_MODE=0
#    KMP_INIT_AT_FORK=true
#    KMP_LIBRARY=throughput
#    KMP_LOCK_KIND=queuing
#    KMP_MALLOC_POOL_INCR=1M
#    KMP_NUM_LOCKS_IN_BLOCK=1
#    KMP_PLAIN_BARRIER='2,2'
#    KMP_PLAIN_BARRIER_PATTERN='hyper,hyper'
#    KMP_REDUCTION_BARRIER='1,1'
#    KMP_REDUCTION_BARRIER_PATTERN='hyper,hyper'
#    KMP_SCHEDULE='static,balanced;guided,iterative'
#    KMP_SETTINGS=true
#    KMP_SPIN_BACKOFF_PARAMS='4096,100'
#    KMP_STACKOFFSET=64
#    KMP_STACKPAD=0
#    KMP_STACKSIZE=8M
#    KMP_STORAGE_MAP=false
#    KMP_TASKING=2
#    KMP_TASKLOOP_MIN_TASKS=0
#    KMP_TASK_STEALING_CONSTRAINT=1
#    KMP_TEAMS_THREAD_LIMIT=4
#    KMP_TOPOLOGY_METHOD=all
#    KMP_USE_YIELD=1
#    KMP_VERSION=false
#    KMP_WARNINGS=false
#    OMP_AFFINITY_FORMAT='OMP: pid %P tid %i thread %n bound to OS proc set {%A}'
#    OMP_ALLOCATOR=omp_default_mem_alloc
#    OMP_CANCELLATION=false
#    OMP_DEFAULT_DEVICE=0
#    OMP_DISPLAY_AFFINITY=false
#    OMP_DISPLAY_ENV=false
#    OMP_DYNAMIC=false
#    OMP_MAX_ACTIVE_LEVELS=1
#    OMP_MAX_TASK_PRIORITY=0
#    OMP_NESTED: deprecated; max-active-levels-var=1
#    OMP_NUM_THREADS: value is not defined
#    OMP_PLACES: value is not defined
#    OMP_PROC_BIND='intel'
#    OMP_SCHEDULE='static'
#    OMP_STACKSIZE=8M
#    OMP_TARGET_OFFLOAD=DEFAULT
#    OMP_THREAD_LIMIT=2147483647
#    OMP_WAIT_POLICY=PASSIVE
#    KMP_AFFINITY='verbose,warnings,respect,granularity=fine,compact,1,0'

# 2021-11-11 14:28:36.299104: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.
# <tf.Tensor: shape=(), dtype=int32, numpy=2>
# a + b isn't 2, it is (to quote tensorflow's documentation)...

# a symbolic handle to one of the outputs of an Operation. It does not hold the values of that operation's output, but instead provides a means of computing those values in a TensorFlow tf.Session.

# It's important just to be aware of the fact that this sort of thing is possible and that libraries will often use operator overloading in non-obvious or magical-seeming ways.

# Understanding how Python's operators work when applied to ints, strings, and lists is no guarantee that you'll be able to immediately understand what they do when applied to a tensorflow Tensor, or a numpy ndarray, or a pandas DataFrame.

# Once you've had a little taste of DataFrames, for example, an expression like the one below starts to look appealingly intuitive:

# # Get the rows with population over 1m in South America
# df[(df['population'] > 10**6) & (df['continent'] == 'South America')]
# But why does it work? The example above features something like 5 different overloaded operators. What's each of those operations doing? It can help to know the answer when things start going wrong.

# Curious how it all works?
# Have you ever called help() or dir() on an object and wondered what the heck all those names with the double-underscores were?

print(dir(list))
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# This turns out to be directly related to operator overloading.

# When Python programmers want to define how operators behave on their types, they do so by implementing methods with special names beginning and ending with 2 underscores such as __lt__, __setattr__, or __contains__. Generally, names that follow this double-underscore format have a special meaning to Python.

# So, for example, the expression x in [1, 2, 3] is actually calling the list method __contains__ behind-the-scenes. It's equivalent to (the much uglier) [1, 2, 3].__contains__(x).

# If you're curious to learn more, you can check out Python's official documentation, which describes many, many more of these special "underscores" methods.

# We won't be defining our own types in these lessons (if only there was time!), but I hope you'll get to experience the joys of defining your own wonderful, weird types later down the road.


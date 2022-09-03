#Booleans
x = True
print(x)
print(type(x))

#True
#<class 'bool'>

#Operation	Description		                  Operation	                   Description
#a == b	    a equal to b                        a != b	                  a not equal to b
#a < b	    a less than b		                a > b	                  a greater than b
#a <= b	    a less than or equal to b           a >= b	                    a greater than or equal to b


def can_run_for_president(age):
    """Can someone of the given age run for president in the US?"""
    # The US Constitution says you must be at least 35 years old
    return age >= 35

print("Can a 19-year-old run for president?", can_run_for_president(19))
print("Can a 45-year-old run for president?", can_run_for_president(45))


#Can a 19-year-old run for president? False
#Can a 45-year-old run for president? True



3.0 == 3
#True

#But sometimes they can be tricky

'3' == 3
#False


def is_odd(n):
    return (n % 2) == 1

print("Is 100 odd?", is_odd(100))
print("Is -1 odd?", is_odd(-1))

#Is 100 odd? False
#Is -1 odd? True

#Remember to use == instead of = when making comparisons. If you write n == 2 you are asking about the value of n. When you write n = 2 you are changing the value of n.

#Combining Boolean Values


def can_run_for_president(age, is_natural_born_citizen):
    """Can someone of the given age and citizenship status run for president in the US?"""
    # The US Constitution says you must be a natural born citizen *and* at least 35 years old
    return is_natural_born_citizen and (age >= 35)

print(can_run_for_president(19, True))
print(can_run_for_president(55, False))
print(can_run_for_president(55, True))
#False
#False
#True
True or True and False
#true

def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is unlike anything I've ever seen...")

inspect(0)
inspect(-15)

#0 is zero
#-15 is negative

def f(x):
    if x > 0:
        print("Only printed when x is positive; x =", x)
        print("Also only printed when x is positive; x =", x)
    print("Always printed, regardless of x's value; x =", x)

f(1)
f(0)

#Only printed when x is positive; x = 1
#Also only printed when x is positive; x = 1
#Always printed, regardless of x's value; x = 1
#Always printed, regardless of x's value; x = 0

#Boolean conversion

print(bool(1)) # all numbers are treated as true, except 0
print(bool(0))
print(bool("asf")) # all strings are treated as true, except the empty string ""
print(bool(""))
# Generally empty sequences (strings, lists, and other types we've yet to see like lists and tuples)
# are "falsey" and the rest are "truthy"


#True
#False
#True
#False

if 0:
    print(0)
elif "spam":
    print("spam")
#spam
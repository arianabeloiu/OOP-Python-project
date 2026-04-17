#  The wildcard * allow an arbitrary number of parameters
# *args - allow arbitrary number of non-key word arguments
def fun(*args):
    return sum(args)

print(fun(1, 2, 3, 4)) #values are not assigned to variables
print(fun(5, 10, 15))   

# kw stand for key words - allow arbitary number of keyword arguments
# **kwargs example 
def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, val)

fun(a=1, b=2, c=3) #note how the values are assigned to variable

#It collects all the additional keyword arguments
#passed to the function and stores them in a dictionary.

def fun(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

fun(1, 2, 3, a=4, b=5)

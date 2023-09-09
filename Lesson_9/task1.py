"""
Task 1
Write a function called oops that explicitly raises an IndexError exception when called.
Then write another function that calls oops inside a try/except statement to catch the error.
What happens if you change oops to raise KeyError instead of IndexError?
"""


def oops():
    """raises an IndexError exception"""
    raise IndexError


def oops_2():
    """raises an KeyError exception"""
    raise KeyError


def call_oops():
    """calls oops() inside a try/except statement to catch the Index error"""
    try:
        oops()
    except IndexError:
        print("You are in IndexError block. oops() was call")


call_oops()


def call_oops_2():
    """calls oops_2() inside a try/except statement to catch the error"""
    try:
        oops_2()
    except IndexError:
        # This code block will not be executed
        # because the error type does not correspond to IndexError
        print("You are in IndexError block. oops_2() was call")
    except KeyError:
        print("You are in KeyError block. oops_2() was call")


call_oops_2()

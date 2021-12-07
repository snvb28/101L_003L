########################################################################
##
## CS 101 Lab
## Program #13 (Grades program)
## Name: Steven Vu
## Email: snvb28@umsystem.edu
##
## PROBLEM: Creating programs to perform automated testing.
##
## ALGORITHM:
##      1. import math and statistics modules
##      2. define total function with the parameter values as a list, having it return the sum of all elements of the list
##      3. define average function with the parameter values as a list, having it return the average of the elements or nan if there are no elements
##      4. define median function with the parameter values as a list, having it return the median of the elements or raise ValueError if there are no elements
##
## ERROR HANDLING:
##          Raising ValueError in median function if there are no elements in the values list.
##
## OTHER COMMENTS:
##          No additional comments.
##
########################################################################

import math
import statistics

def total(values:list) -> float:
    return sum(values)

def average(values:list) -> float:
    if len(values) == 0:
        return math.nan
    else:
        return (sum(values)) / (len(values))

def median(values:list) -> float:
    if len(values) == 0:
        raise ValueError
    else:
        return statistics.median(values)

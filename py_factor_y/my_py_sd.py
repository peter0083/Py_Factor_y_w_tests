"""
Standard Deviation
------------------
This program will comput the standard deviation of a list of numbers.

"""
def standard_deviation(x):
    n = len(x)
    mean = sum(x) / n
    ssq = sum((x_i-mean)**2 for x_i in x)
    stdev = (ssq/n)**0.5
    return(stdev)

def standard_error(x):
    standard_error = lambda x: standard_deviation(x)/len(x)**0.5
    return(standard_error)


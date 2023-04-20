#Name: Zavier DePillo
#Email: depillzj@mail.uc.edu
#Assignment Title: Assignment 11
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: NumPy arrays and fun stuff
#Citations:
#Anything else that's relevant:

from functionsPackage.functions import *
def demo():
    
    '''
    NumPy arrays and fun stuff
    @author:
    nicomp
    '''
    import numpy as np
    
    # Problem #1: Here is a numPy array of Fahrenheit temperatures. Convert them to Centigrade temperatures and print the result
    f = [-100, 0, 32, 100, 212]
    Fahrenheit = np.array(f)
    print(Centigrade(np.array(f)))
    
    # Problem #2: Given two arrays, find the common values between them.
    a1 = np.array([1,2,3,4,5,6,7,8,9,10])
    a2 = np.array([2,4,6,8,10,12,14,16,18,20])
    print(find_common_values(np.array([1,2,3,4,5,6,7,8,9,10]), np.array([2,4,6,8,10,12,14,16,18,20])))
    
    # Problem #3: Given an array, a1, create a new array, a2, with all the values divisible by 3 in a1
    p3 = np.array([3,6,9,10,11,12,13,14,15,16,17,18])
    print(get_divisible_values(np.array([3,6,9,10,11,12,13,14,15,16,17,18])))
    
    # Problem #4: Create a 2-dimensional (2-axis) array with 5 rows and 6 columns. Initialize the elements to random integer values between 1 and 100
    print(new_array(np.random.randint(1, 101, size=(5,6))))
    
    # Problem #5: Given an array, a, compute the average of all the elements. Use a for loop and a flatten function.
    a = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])
    print(average(np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])))
    
    # Problem #6: Given an array of strings containing first/last names, convert them to title case.
    names = np.array(['calbert cheaney', 'lyndon jones', 'pat graham', 'chris reynolds', 'matt nover', 'greg graham', 'todd leary'], dtype=str)
    print(title(np.array(['calbert cheaney', 'lyndon jones', 'pat graham', 'chris reynolds', 'matt nover', 'greg graham', 'todd leary'])))
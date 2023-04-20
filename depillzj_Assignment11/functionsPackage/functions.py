#Name: Zavier DePillo
#Email: depillzj@mail.uc.edu
#Assignment Title: Assignment 11
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: NumPy arrays and fun stuff
#Citations:
#Anything else that's relevant:
import numpy as np 
import random as rand
#Problem 1
def Centigrade(Fahrenheit):
    Centigrade = ((Fahrenheit-32) * 5/9)
    return(Centigrade)
    

#Problem 2
def find_common_values(a1, a2):
    return np.intersect1d(a1, a2)

#Problem 3
def get_divisible_values(some_array):
    solution = [num for num in some_array if num % 3 == 0]
    return np.array(solution) #Return a numpy array

#Problem 4
def new_array(rand):
    new_array = np.random.randint(1, 101, size=(5,6))
    return(new_array)

#Problem 5
def average(a):
    sum_a = 0
    for num in a:
        sum_a += num
    average = sum_a / len(a)
    return(average)

#Problem 6
def title(names):
    title = np.char.title(names)
    return(title)
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:03:00 2020
The file inlcudes examples of Python List commands
@author: Bilgin Altundas
"""
import numpy as np
    
# Example of finding entries in a list    
def f(alist,val):
    st =0
    ed =0
    idx=0
    for i in range(len(alist)):
        if alist[i]==val:
            idx+=1
            if idx ==1:
                st = i+1
                ed = i+1
            else:
                ed = i+1
    if st ==0:
        return None
    return st-1,ed-1

def ff(alist,val):
    if val in alist:
        indx0 = alist.index(val)
    else:
        return None
    indx1=indx0
    alist.reverse()
    indx1 = len(alist) - alist.index(val)-1
    return indx0,indx1

alist = [1,2,3,5,5,5,7,2,8,8,11,12]
val = 2
print(f(alist,val))
print(ff(alist,val))

def findEntryIndex(x,value):
    x_numpy = np.array(x)
    if np.sum(x_numpy==value):
        indx = np.argwhere(x_numpy==value)
        return indx.flatten()
    else:
        return f'Value is not in the list'

alist = [1,2,3,5,5,5,7,2,8,8,11,12]
val = 2

print(findEntryIndex(alist,val))

###################### copy ##############################
# be careful about copying mutable object
import copy
x = [1,2,3,4,5]
y0=x
y1=copy.copy(x)
y2=x.copy()
print(x)

x.insert(2,15)
x.append(15)

print(x,'\n',y0,'\n',y1,'\n',y2)
y0.clear() # clearing a copied list objects clear the original

print(x,'\n',y0,'\n',y1,'\n',y2)

################ SORT #############################
vowels = ['e', 'a', 'u', 'o', 'i','A']

# sort the vowels
vowels.sort()

# print vowels
print('Sorted list:', vowels)

vowels.sort(reverse=True)
print('Sorted list:', vowels)

print(vowels[::-1])

# sorted can be used to save a copy of sorted list
vowels = ['e', 'a', 'u', 'o', 'i','A']
print(sorted(vowels, reverse=True))
print(vowels)

# ['u', 'o', 'i', 'e', 'a', 'A']
# ['e', 'a', 'u', 'o', 'i', 'A']

#### sorting with custome key ####
# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

# custom functions to get employee info
def get_name(employee):
    return employee.get('Name')


def get_age(employee):
    return employee.get('age')


def get_salary(employee):
    return employee.get('salary')

employees.sort(key=get_name)
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=get_age)
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=get_salary, reverse=True)
print(employees, end='\n\n')

vowels = ['eft', 'ar', 'ghju', 'o', 'yyyyyi','yA']
vowels.sort(key=len)
print(vowels)

# ['o', 'ar', 'yA', 'eft', 'ghju', 'yyyyyi']


##################### Index ###################
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# index of 'e' in vowels
index = vowels.index('e')
print('The index of e:', index)

################### Append ########################
vowels = ['a', 'e', 'i', 'o', 'i', 'u']
admore0 = ['ee','g']
vowels.append(admore0)
print(vowels)
admore = ('ee','g')
vowels.append(admore)
print(vowels)

# ['a', 'e', 'i', 'o', 'i', 'u', ['ee', 'g']]
# ['a', 'e', 'i', 'o', 'i', 'u', ['ee', 'g'], ('ee', 'g')]

######################## extend #############
# languages list
languages = ['French', 'English']

# another list of language
languages1 = ['Spanish', 'Portuguese']
print(languages)
languages.extend(languages1)
print(languages)

############## INSERT ###########################
# The insert() method takes two parameters:
languages = ['French', 'English']

languages.insert(2,'3')
print(languages)

################# remove ####################################
# The remove() method removes the first matching element (which is passed as an argument) from the list.

# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']

# 'rabbit' is removed
animals.remove('rabbit')

# Updated animals List
print('Updated animals list: ', animals)

################### count ##################
# count() Parameters
# The count() method takes a single argument:
# element - the element to be counted

# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# count element 'i'
count = vowels.count('i')
# print count
print('The count of i is:', count)

# The count of i is: 2

###############
# random list
random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]

# count element ('a', 'b')
count = random.count(('a', 'b'))

# print count
print("The count of ('a', 'b') is:", count)


############################# POP #########################
# programming languages list
languages = ['Python', 'Java', 'C++', 'French', 'C']

# remove and return the 4th item
return_value = languages.pop(3)

print('Return Value:', return_value)

# Updated List
print('Updated List:', languages)


####################### reverse ############################
# The reverse() method reverses the elements of the list.

languages = ['Python', 'Java', 'C++', 'French', 'C']
languages.reverse()
print(languages)
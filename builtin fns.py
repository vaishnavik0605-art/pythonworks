# Write a program to create a list of 5 random 3 digit numbers
# import random
from abc import update_abstractmethods
from builtins import min
from multiprocessing.reduction import duplicate

#
# new=[]
# for i in range(5):
#         new.append(random.randint(100,1000))
# print(new)


#write a program to create a 5digit random otp number
# print(random.randrange(10000, 100000))

#write a program to find the position of a character in a string
# s="worlld"
# # for i in s:
# print(s.index('w'))


#define a function that takes a string as argument and returns a new dictionary where keys
# are character and values are count of each character

# def  dict(s):
#     new={}
#     for i in s:
#         new[i]=s.count(i)
#     return new
# f=dict("welcome")
# print(f)

#
#
# #Define a function that takes string as argument and print the count of
# # digits,spaces,letters in that string

# def arg(s):
#     d=0
#     b=0
#     l=0
#     for i in s:
#         if i.isdigit():
#             d=d+1
#         elif i.isspace():
#              b=b+1
#         elif i.isalpha():
#             l=l+1
#     print("digits",d)
#     print("space",b)
#     print("letters",l)
#
# arg(" hei manu 234")


#######list#################3

# l=[1,2,3,4]
# a=l.append(5)
# print(a)
#
#
# print(l.extend((6,7,8,9)))
# #
# l=[23,54,67,12,45,68,98]
# print(l.sort())
# print(l.pop())
# print(l.pop(3))
#
# print(l.reverse())
# l=[68, 67, 45, 23, 12]
#
# print(l.remove(23))
# l=[68, 67, 45, 12]
# l.insert(2,55)



# #given a list
# l=[1,2,2,3,4,4,5,6]
# #create a new dict where keys are numbers and values are number occurence of each number
# new={i:l.count(i)for i in l}
# print(new)
# new={}
# for i in l:
#     new[i]=l.count(i)
# print(new)
#
# #given a list
# l=[11,34,78,23,90,65]
# #find the largest number
# print("largest number-",max(l))
# #find the second larger
# l.sort()
# print("second largest number-",l[-2])
#
# #find the smallest number
# print("smallest number-",min(l))
# #find the second smallest
# print("second smallest-",l[1])

# #given list
l=[['arun',23,30000],
   ['amal',25,50000],
   ['anu',27,40000]]
#max salary
# m=0
# for i in l:
#     if i[2]>m:
#         m=i[2]
# print(m)
#
#
# new=max([i[2] for i in l])
# print(new)
#
#
# #min age
#
# new=min([i[1] for i in l])
# print(new)

# #given a list
# l=[23,45,67,12,90,78]
# # find the largest number without using builtin methods
#
# max=l[0]
# for i in l:
#     if i>max:
#         max=i
# print("maximum",max)
#
#
# #minimum number
# min=l[0]
# for i in l:
#     if i<min:
#         min=i
# print("maximum",min)



##############    set    ##############
# s={1,2,3,4,5}
# s.update((6,8,7,9))
# print(s)
# s.remove(4)
# print(s)
# t={4,5,6,7}
# a=s.union(t)
# print(a)
# print(s.intersection(t))
# print(t.symmetric_difference(s))
# print(s.difference(t))



# #given a list
# l=[1,1,2,3,3,4]
# # remove the duplicates?
# print(set(l))
#
# # remove duplicates without using set() (order should be preserved)
# n=[]
# for i  in l:
#     if i not in n:
#         n.append(i)
# print(n)

# # $given 2 list
# l1=[13,27,30,42,57]
# l2=[13,57,89,33,80]
# #find the common elements
# s1=set(l1)
# s2=set(l2)
# print(s1.intersection(s2))



##############dictionary##################
# d={'name':'arun','age':24,'course':'python'}
# # print(d)
# a=d.keys()
# # print(d)
# # a=d.values()
# print(a)
# a=d.get('age')


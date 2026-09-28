#  # Q1.Define a function that takes 2 numbers and returns their product
#
# def fact(n1,n2):
#     p=n1*n2
#     return p
# a=fact(10,3)
# print(a)
#
# #
# # # Q2.Define a function that takes a string and returns number of vowels
#
# def vowels(s):
#     v='aeiou'
#     c=0
#     for i in s:
#       if i in v:
#          c=c+1
#     return c
# s=input("enter a string:")
# a=vowels(s)
# print(a)
#
# #
# # # Q3.Define a function that takes length and breadth and returns area of
# # #rectangle
#
# def area(l,b):
#     a=l*b
#     return a
# a=area(6,5)
# print(a)
#
# # # Q4.Define a function that takes a list of numbers and creates a new list
# # # with even numbers and returns the new list
# #
# l=[45,78,90,12,35]
# def even(l):
#     new=[]
#     for i in l:
#         if i%2==0:
#             new.append(i)
#     return(new)
# l=[45,78,90,12,35]
# e=even(l)
# print(e)
#
#
#
# # #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # # each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]
# #
# def sum(l):
#     new=[]
#     s=0
#     for i in l:
#         for j in str(i):
#             s=s+int(j)
#         new.append(s)
#     return new
# l = [123, 345, 111, 678, 134, 809]
# m=sum(l)
# print(m)
# #
# #
#
# #Q6.Define a function that takes a list and returns a new list containing unique elements from the given
# # list
# # l=[12,34,78,12,67,34,90,23]
#
# def uni(l):
#     new=[]
#     for i in l:
#         if i  in new:
#             continue
#         new.append(i)
#     return new
# l=[12,34,78,12,67,34,90,23]
# uni=uni(l)
# print(uni)
#
# #Q7.Define a function that takes 2 list as arguments and returns a new list containing common elements
# list1=[12,34,56,78,90]
# list2=[90,34,11,57,45]
#
# def com():
#     new=[]
#     list1 = [12, 34, 56, 78, 90]
#     list2 = [90, 34, 11, 57, 45]
#     for i in list1:
#         if i in list2:
#             new.append(i)
#     return new
#
# # list=com(list1,list2)
# print(com())
#






#define a fn that takes a string as arguments and return a new dictionary where keys are words
 # and values are length of each word
#call the fn and print the dict


# def dict(s):
#     new={}
#     for i in s.split():
#         new[i]=len(i)
#     return new
# a=dict("hai welcome to python")
# print(a)


#define a function that takes a number as argument and check whether that  number is spy no or not
#(sum of digit = product of digits)
#eg22-->2+2=2*2=4  1124 1+1+2+4=8 1*1*2*4=8 

# def spy(n):
#     sum=0
#     p=1
#     for i in str(n):
#         sum=sum+int(i)
#         p=p*int(i)
#     if sum==p:
#         return "spy number"
#     else:
#         return "not spy"
#
# n=int(input("enter a number:"))
# s=spy(n)
# print(s)
#

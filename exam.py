# Define a function that takes a number as an argument and returns True if the number is divisible
# by the sum of its digits.
# Example: 18 → 1 + 8 = 9, and 18 % 9 = 0.

# def arg(n):
#     s=0
#     for i in str(n):
#      s=s+int(i)
#     if n%s==0:
#         return True
#     else:
#          return False
# a=arg()
# print(a)

# define a function that takes a list containing numbers from 1 to n with 1 no. is missing and returns the missing no.
# eg: [1,2,3,5,6] --> 4

# def mis():
#     l=[1,2,4,5,6,7,9]
#     for i in range(1,10):
#         if i in l:
#             continue
#         else:
#             print(i)
# mis()

# 4qs Define a function that accepts two lists and returns the elements that are common to both
# lists without using set().

# def list():
#     new=[]
#     list1 = [12, 34, 56, 78,76]
#     list2 = [12, 34, 65, 87,76]
#     for i in list1:
#         if i in list2:
#             new.append(i)
#     return new
# print(list())

# Define a function that takes a number as an argument and prints its multiplication table
# from 1 to 10. Call the function

# def mul(n):
#     p=1
#     for i in range(1,11):
#      # p=i*n
#      print(i,'*',n,'=',i*n)
# mul(4)
# #

#prime number upto a given number
# def fun(n):
#     new=[]
#     for i in range(2,n):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             new.append(i)
#     return new
# h=fun(10)
# print(h)
#


######################    MAIN EXAM 1/09/2026 #################################

# Print Series
# a.1 8 27 64 125

# for i in range(1,6):
#     i=i**3
#     print(i,end=" ")
# print()
# b.100 90 80 70 60 50

# i=100
# while(i>=50):
#     print(i,end=" ")
#     i=i-10
# print()

# c.1 3 6 10 15 21
# s=0
# for i in range(1,7):
#     s=s+i
#     print(s,end=" ")
# print()

# d.1 10 100 1000 10000
# i=1
# while(i<=10000):
#     print(i,end=" ")
#     i=i*10
# print()
#
# # e.3 6 9 12 15 18
#
# # for i in range(1,7):
# #     i=i*3
# #     print(i,end=" ")
# # print()
#
# # 2.Given a list
# l=[0,1,0,3,12]
# new=[]
# for i in l:
#     if i!=0:
#      new.append(i)
# for i in l:
#         if i==0:
#             new.append(i)
# print(new)

# Write a program to Move all  zeroes to the end

# output:[1,3,12,0,0]




# 3.Write a program to find the Count of vowels and consonants in a string

# s="python language"
# v="AEIOUaeiou"
# c=0
# c1=0
# for i in s:
#     if i in v:
#         c=c+1
#     elif i.isalpha():     ###isalpha removes the spaces while taking other letters than vowels
#         c1=c1+1
# print("count of vowels:",c)
# print("count of consonants:",c1)

# 4.Define a function that takes a list as argument and returns the Most frequent number in a list.
# Eg:

# Output:2

# def fr(l):
#     c=l[0]
#     m=0
#     for i in l:
#         if l.count(i)>c:    #### this is the count fn which works
#             c=l.count(i)
#             m=i
#     return m
# l=[1,2,3,3,4,5,6,7]
# print(fr(l))







# 5.Print Pattern
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

# for i in range(1,6):
#     for j in range(6-i):
#         print(i,end=" ")
#     print()
#





#
# def fr(l):
#     m=l[0]
#     c1=0
#     for i in l:
#         if l.count(i)>c1:
#             c1=l.count(i)
#             m=i
#     return m
# l=[1,2,2,3,4,2,5,3,4,6]
# a=fr(l)
# print(a)
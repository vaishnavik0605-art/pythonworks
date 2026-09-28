# ## 1. Basics (Input & Output)
#
# 1. Print `"Hello, World!"`
from operator import contains
from pydoc import apropos


# print("hello")

# 2. Read a person's name and print a greeting.

# s=input("enter your name:")
# print("good morning "+s)

# 3. Read two numbers and print their sum.

# n1=int(input("enter num1:"))
# n2=int(input("enter num2:"))
# sum=0
# sum=n1+n2
# print("sum",sum)


# 4. Find the area of a rectangle.

# l=int(input("enter length:"))
# h=int(input("enter breadth:"))
# a=l*h
# print("area of rectangle:",a)
#



# 5. Convert Celsius to Fahrenheit
#(c*9/5)+32

# c=float(input("enter celsius:"))
# f=(c*9/5)+32
# print("farenhrit=",f)


# ## 2. If-Else
#
# 6. Check whether a number is positive, negative, or zero.

# n=int(input("enter a number:"))
# if n>=1:
#     print(n,"is a positive number")
# elif n<0:
#     print(n, "is a negative number")
# else:
#     print(n,"is zero")

# 7. Check whether a number is even or odd.

# n=int(input("enter a number:"))
# if n%2==0:
#     print(n,"is a even number")
# else:
#     print(n,"is odd number")


# 8. Find the largest of two numbers.

# n1=int(input("enter num1:"))
# n2=int(input("enter num2:"))
# if n1>n2:
#     print(n1,"is larger")
# else:
#     print(n2,"is larger")


# 9. Find the largest of three numbers.


# n1=int(input("enter num1:"))
# n2=int(input("enter num2:"))
# n3=int(input("enter num3:"))
# if n1>n2 and n1>n3:
#     print(n1,"is larger")
# elif n2>n3 and n2>n1:
#       print(n2, "is larger")
# else:
#     print(n3, "is larger")


# 10. Check whether a year is a leap year.

# year=int(input("enter a year:"))
# if (year%4==0 and year%100!=0) or year%400==0:
#     print("leap year")
# else:
#     print("not leap year")


# 11. Check whether a person is eligible to vote (age ≥ 18).
#
# age=int(input('enter your enter:'))
# if age>=18:
#     print("you are eligible to vote!")
# else:
#     print("you are not eligible to vote!")




# 12. Calculate a student's grade based on marks.

# grade=int(input("enter your grade:"))
# if grade>=90:
#     print("A+")
# elif grade>=80:
#     print("B+")
# elif grade>=70:
#     print("C+")
# elif grade>=60:
#     print("D+")
# else:
#     print("failed")

#
# ## 3. Loops
#
# 13. Print numbers from 1 to 10.

# for i in range(1,11):
#     print(i)

# 14. Print numbers from 10 to 1.

# for i in range(10,0,-1):
#     print(i)

# 15. Find the sum of the first `n` natural numbers.

# n=int(input("enter the value for n:"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum,end=" ")

# 16. Print the multiplication table of a given number.

# n=int(input("enter a number:"))
# for i in range(1,11):
#     print(i,"*",n,"=",i*n)


# 17. Find the factorial of a number.
# def fact():
#     i=1
#     fact=1
#     n=int(input("enter a number:"))
#     while(i<=n):
#         fact=fact*i
#         i=i+1
#     print("factorial",fact)
# fact()



# 18. Count the number of digits in a number.
# n='35367'
# count=0
# for i in str(n):
#     count=count+1
# print(count)

# 19. Reverse a number.
# rev=""
# for i in n:
#     rev=i+rev
# print("reverse",rev)
#
# # 20. Check whether a number is a palindrome.
# n=input("enter a number:")
# r=n[::-1]
# if n==r:
#     print("palindrome")
# else:
#     print("not")


# 21. Find the sum of the digits of a number.

# n=int(input("enter a number:"))
# for i in str(n):
#     sum=sum+i
#     print("sum",sum)


# 22. Find all Armstrong numbers between 100 and 1000.
# s=0

# for i in range(100,1001):
#     s=s+i**3
# if s==i:
#     print(i)



# 23. Print all even numbers between 1 and 100.

# for i in range(1,101):
#     if i%2==0:
#         print(i,end=" ")

# 24. Print all odd numbers between 1 and 100.
# for i in range(1,101):
#     if i%2!=0:
#         print(i,end=" ")


# ## 4. Patterns
#
# 25. Print a square of `*`.
#
# ```
# ****
# ****
# ****
# ****
# ```
# for i in range(1,5):
#     for j in range(1,5):
#         print('*',end=" ")
#     print('\n')


# 26. Print a right triangle.
#
# ```
# *
# **
# ***
# ****
# *****

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()



#
# 27. Print an inverted triangle.
#
# ```
# *****
# ****
# ***
# **
# *

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()



# 28. Print Floyd's Triangle.
#
# ```
# 1
# 2 3
# 4 5 6
# 7 8 9 10

# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k=k+1
#     print()


# ## 5. Strings
#
# 29. Count the number of vowels in a string.

# c=0
# # v="aeiou"
# str=input("enter a string")
# for i in str:
#     if i in 'aeiou':
#         c=c+1
# print(c)

# 30. Check whether a string is a palindrome.
# str=input("enter a string:")
# r=str[::-1]
# if str==r:
#     print("palindrome")
# else:
#     print("not")



# 31. Count the number of words in a sentence.
# str=input("enter a sentence:")
# l=len(str)
# c=0
# for i in str:
#     # len(str)
#     c=c+1
# print(c)



# 32. Reverse a string.
# str=input("enter a string:")
# r=str[::-1]
# print("reverse",r)

# 33. Count the occurrences of a character in a string.

# str=input("enter a string:")
# occ=input("enter ur character:")
# c=0
# for i in str:
#     if occ in i:
#         c=c+1
# print(c)

# ## 6. Lists
#
# 34. Find the largest element in a list.
# l=[12,45,67,3,4,56,8,88,45]
# print(max(l))

# 35. Find the smallest element in a list.
# print(min(l))

# 36. Find the sum of all elements in a list.
# l=[12,34,4,6]
# s=0
# for i in l:
#     s=s+i
# print(s)

# 37. Find the average of a list.
# l=[12,34,4,6]
# avg=0
# s=0
# for i in l:
#     s=s+i
#     avg=s//4
# print(avg)

# 38. Count even and odd numbers in a list.

# l=[2,3,4,5,6,7,8,9,12,14]
# c=0
# c1=0
# for i in l:
#     if i%2==0:
#         c=c+1
#     else:
#         c1=c1+1
# print("even count",c)
# print("odd count",c1)



# 39. Remove duplicate elements from a list.

# l=[12,34,34,12,56,78,35]
# print(l)
# s=set(l)
# print(s)

# 40. Sort a list without using `sort()`.




# ## 7. Functions
#
# 41. Write a function to add two numbers.

# def add():
#     n1=int(input("enter no1:"))
#     n2=int(input("enter no2:"))
#     a=n1+n2
#     print(a)
# add()


# 42. Write a function to find the factorial of a number.

# fact=1
# n=int(input("enter no:"))
# for i in range(1,n+1):
#     fact=fact*i
# print("factorial",fact)

# 43. Write a function to check whether a number is prime.
# n1 = int(input("enter no1:"))
# if n1>1:
#     for i in range(2,n1-1):
#         if n1%i==0:
#             print(n1,"not a prime")
#             break
#     else:
#         print(n1,"is prime number")
# else:
#     print(n1,"neither a prime or composite")


# 44. Write a function to check whether a number is an Armstrong number.
# def arm():
#     n1 = int(input("enter no1:"))
#     s=str(n1)
#     l=len(s)
#     sum=0
#     for i in s:
#         sum=sum+int(i)**l
#     if sum==n1:

#         print("armstrong")
#     else:
#         print("not")
# arm()

# 45. Write a function to find the maximum of three numbers.

# n1 = int(input("enter no1:"))
# n2 = int(input("enter no2:"))
# n3 = int(input("enter no3:"))
# if n1>n2 and n1>n3:
#     print(n1,"is largest")
# elif n2>n1 and n2>n3:
#     print(n2,"is largest")
# else:
#     print(n3,"is largest")


# ## 8. Mixed Practice

# 46. Guess the number game.


# 47. Simple calculator using `if-elif`.
# 48. ATM menu (Deposit, Withdraw, Balance).
# 49. Student marks calculator.
# 50. Number guessing game with 3 chances.
#
# ### Challenge Questions
#
# * Print all prime numbers between 1 and 100.
# * Find the Fibonacci series up to `n` terms.
# * Find the GCD and LCM of two numbers.
# * Count uppercase, lowercase, digits, and special characters in a string.
# * Create a simple password checker.
#


#odd/even
# n=int(input("enter a number"))
# if n%2==0:
#     print("even number")
# else:
#     print("odd number")

##+,-,0
# n=int(input("enter a number"))
# if n>0:
#     print("positive")
# elif n==0:
#     print("zero")
# else:
#     print("negative")


###print 1 to n

# n=int(input("enter a number"))
# for i in range(1,n+1):
#     print(i,end=" ")


##sum of n numbers
# s=0
# n=int(input("enter a number"))
# for i in range(1,n+1):
#     s=s+i
# print("sum",s)

###multiplication

# n=int(input("enter a number:"))
# for i in range(1,11):
#     print(i,"*",n,"=",i*n)

###factorial
# fact=1
# n=int(input("enter a number"))
# for i in range(1,n+1):
#     fact=fact*i
#     i=i+1
# print("factorial",fact)


###prime
# n=int(input("enter a number"))
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime")
# else:
#     print("neither prime nor composite")

###prime upto n

# n=int(input("enter a number"))
# if n>1:
#     for i in range(2,n):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i,end=" ")

###rev a numbr
# n=int(input("enter a number"))
# rev=""
# for i in str(n):
#     rev=i+rev
# print("reverse",rev)

####palindrome number
# n=int(input("enter a number"))
# if str(n)==str(n)[::-1]:
#     print("palindrome")
# else:
#     print("not")


###multiplication

# n=int(input("enter a number:"))
# # p=1
# for i in range(1,11):
#     print(i,'*',n,'=',i*n)



# fact=1
# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     fact=fact*i
#     i=i+1
# print("factorial",fact)


# l=[1,3,4,5,8,9]
# for i in range(1,10):
#     if i in l:
#         continue
#     else:
#         print(i)

# def s():
#     n=int(input("enter a number:"))
#     s=0
#     for i in str(n):
#         s=s+int(i)
#     if n%s==0:
#         return True
#     else:
#         return False
# a=s()
# print(a)

# n=int(input("enter a number:"))
# s=0
# for i in str(n):
#     s=s+int(i)
# if n%s==0:
#     print("True")
# else:
#     print("False")


# def list():
#     l1=[1,2,3,4,5]
#     l2=[2,3,4,5,6,7]
#     new=[]
#     for i in l1:
#         if i in l2:
#             new.append(i)
#     return new
# a=list()
# print(a)

# n=int(input("enter a number:"))
# if n%3==0 and n%10==3:
#     print(n,"is a divisible by 3 and ends with 3")
# else:
#     print("no")

# n='1234'
# rev=""
# for i in str(n):
#     rev=i+rev
# print("reverse",rev)


# l=[1,2,3,4]
# new={i:i**2 for i in l}
# print(new)


# s='hai welcome'
# v='aeiou'
# new=""
# for i in s:
#     if i in v:
#      new=new+i
# print(new)


# n=4567
# s=0
# for i in range(4,8):
#     s=s+i
# print("sum of digits",s)

# def c():
#     c=0
#     chr="hello world"
#     sp="l"
#     for i in chr:
#         if i in sp:
#             c=c+1
#     return c
# print(c())


# def si(p,n,r):
#     si=p*n*r/100
#     return si
# print(si(2000,2,4))


# def add(n1,n2):
#     s=n1+n2
#     return s
# print(add(6,4))

# n=152
# st=str(n)
# l=len(st)
# s=0
# for i in st:
#     s=s*int(i)**l
# if s==n:
#     print("armstrong number")
#     # break
# else:
#     print("not armstrong")


# year=int(input("enter year:"))
# if (year%4==0 and year%100!=0) or year%400==0:
#     print(year,"leap year")
# else:
#     print("not a leap year")



# largest
# l=[1,2,3,4,5,6,7,8,9]
# lr=l[0]
# for i in l:
#     if i>lr:
#         lr=i
# print(lr)


# s="good morning sara"
# for i in s.split():
#     print(i,len(i))


# n=int(input("enter a number:"))
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             print("not prime")
#             break
#     else:
#      print("prime")
# else:
#     print("not prime nor composite")



# n=int(input("enter a number:"))
# for i in range(2,n):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()



# 1 2 3 4
# 1 2 3
# 1 2
# 1

# for i in range(1,6):
#     for j in range(1,6-i):
#         print(j,end=" ")
#     print()


# n=int(input("enter a no:"))
# for i in range(n):
#     s=0
#     r=str(i)
#     l=len(r)
#     for j in r:
#         s=s+int(j)**l
# if n==s:
#     print("yes")
#     # break
# else:
#     print("no")


# l= [0, 1, 0, 3, 12]
# new=[]
# for i in l:
#     if i!=0:
#         new.append(i)
# for i in l:
#     if i==0:
#         new.append(i)
# print(new)


# l=[10, 25, 5, 40, 15]
# l1=l[0]
# for i in l:
#     if i>l1:
#         l1=i
# print(l1)


#
# l=[1,2,2,3,4,2,5,3,4,6]
# def fr(l):
#     l1=l[0]
#     c=0
#     for i in l:
#         if l.count(i)>c:
#             c=l.count(i)
#             l1=i
#     return l1
# print(fr(l))


for i in range(6,0,-1):
    for j in range(i):
        print(1,end=" ")
    print()
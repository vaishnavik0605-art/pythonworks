# def add():
#     #addition of 2 numbers
#
#     n1=int(input("enter a n1:"))
#     n2=int(input("enter a n2:"))
#     sum=n1+n2
#     print("sum",sum)
#
#     return #   it is not compulsory when there is no return element but we want to exit from it we can gave
# add()

#define a function to display "hello your name"
# def dis():
#     s=input("enter your name:")
#     print("hello "+s)
#
#     return
# dis()

# define a function to find factorial of a number

# def fact():
#     n=int(input("enter a number : "))
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     print(f)
# fact()

#define a function to find count of a specific character in a string
# def count():
#     s=input("enter a string: ")
#     f=input("specific character : ")
#     c = 0
#     for i in s:
#         if i==f:
#            c=c+1
#     print("count:", c)
#
# count()

#define a fn to check a number is prime or not

# def prime():
#     n=int(input("enter a number: "))
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 print("not prime")
#                 break
#         else:
#             print("prime")
#     else:
#         print("enter a number greater than 1")
#
# prime()


#define a function to find the factors of a number


# def fact():
#     n=int(input("enter a number:" ))
#     for i in range(1,n+1):
#         if n%i==0:
#              print(i)
#         # else:
#         #     continue
#     return
# fact()


##with arguments and parameters
# def add(n1,n2):
#     s=n1+n2
#     print("sum",s)
#     return
#
# add(12,34)

#define a fn that takes 3 arguments amount,years and rate, find the simple interest(dynamic input)
#si=p*n*r/100
# def si(p,n,r):
#     si=p*n*r/100
#     print(si)
#     return
#
# p=int(input("enter amount:"))
# n=int(input("enter year:"))
# r=int(input("enter rate:"))
# si(p,n,r)

 #here we can avoid giving arguments and parameters and give this is as dynamic and passing is also possible


#define a fn that takes 2 numbers as arguments and return sum as result call the fn and print result
# def add(n1,n2):
#     sum=n1+n2
#     return sum
# a=add(45,67)
# print(a)

# def add(n1,n2):
#     sum=n1+n2
#     print(sum)
# add(45,67)
################################################333333
####################################################3
######################################################3
#######################################################

# def fact(n):
#     # n=int(input("enter a number:"))
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     print(f)
# fact(6)


#define a function to find count of a specific character in a string
# def count():
#     count=0
#     s=input("enter a string")
#     c=input("enter a character")
#     for i in s:
#         if i in c:
#             count=count+1
#     print(count)
# count()

# def factors():
#     n=int(input("enter a number:"))
#     for i in range(1,n+1):
#         if n%i==0:
#             print(i)
# factors()

#define a fn that takes 3 arguments amount,years and rate, find the simple interest(dynamic input)
#si=p*n*r/100


# def simple():
#     p = int(input("enter amount:"))
#     n = int(input("enter year:"))
#     r = int(input("enter rate:"))
#     si=p*n*r/100
#     return si
#
# i=simple()
# print(i)


#define a fn that takes 2 numbers as arguments and return sum as result call the fn and print result
# def add(n1,n2):
#     sum=n1+n2
#     return sum
# n1=int(input("enter a no1"))
# n2=int(input("enter a no2"))
# a=add(n1,n2)
# print(a)
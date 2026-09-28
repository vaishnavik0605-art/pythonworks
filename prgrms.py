#write a program to check whether a number is armstrong number


# n=int(input("enter a number:"))
# sum=0
# s=str(n)
# l=len(s)
# for i in s:
#      sum=sum+int(i)**l
# if sum==n:
#     print(n,"is an armstrong number")
# else:
#     print(n,"is not an armstrong number")



#factors of number

# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i,end=" ")


#prime or not

# n=int(input("enter a number:"))
# if n>1:
#  for i in range(2,n):
#     if n%i==0:
#         print(n,'is not a prime number')
#         break # without break  it also print else condition
#  else:#(for)
#     print(n, 'is  a prime number')
# else: # numbr 1 or 0 or negative(if)
#     print(n, 'is neither prime nor composite')









# def armstrong(n):
#     s=str(n)
#     l=len(s)
#     sum=0
#     for i in s:
#         sum=sum+int(i)**l
#     if sum==n:
#         return "armstrong"
#
#     else:
#         return "not armstrong"
# n=int(input("enter a number:"))
# a=armstrong(n)
# print(a)
#
#
#

# n=1234
# rev=""
# for i in str(n):
#     rev=i+rev
# print("rev",rev)
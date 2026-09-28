# # Python Retest — Coding Practice
# # High-priority coding questions based on your exam syllabus. Questions only — use this as a practice
# # sheet.
# import functools
# from asyncio import events
#
# import classwork1
#
# # Level 1 — Easy
#
#
# # 1. Print Series
#
# # Print: 1 4 9 16 25
# # for i in range(1,6):
# #     i=i**2
# #     print(i,end=" ")
# # print()
#
# # Print: 10 20 30 40 50
#
# # i=10
# # while(i<=50):
# #     print(i,end=" ")
# #     i=i+10
# # print()
#
#
# # Print: 5 10 15 20 25 30
#
# # i=5
# # while(i<=30):
# #     print(i,end=" ")
# #     i=i+5
# # print()
#
# # Print: 100 90 80 70 60
#
# # i=100
# # while(i>=60):
# #     print(i,end=" ")
# #     i=i-10
# # print()
#
#
# # Print: 1 10 100 1000 10000
#
# # i=1
# # while(i<=10000):
# #     print(i,end=" ")
# #     i=i*10
# # print()
#
#
#
#
#
# # 2. Even Numbers
# # Write a program to print all even numbers from 1 to 50.
# # for i in range(2,51,2):
# #     print(i,end=" ")
# # print()
#
#
# # 3. Odd Numbers
# # Write a program to print all odd numbers from 1 to 50.
#
# # for i in range(1,50,2):
# #     print(i,end=" ")
# # print()
#
#
# # 4. Sum of Numbers
# # Write a program to find the sum of numbers from 1 to N. Example: Input 5 fi Output 15.
#
# # s=0
# # n=int(input("enter a number:"))
# # for i in range(1,n+1):
# #     s=s+i
# # print("sum of numbers from 1 to N:",s)
# # print()
#
#
# # 5. Multiplication Table
# # Write a program to print the multiplication table of a given number.
#
# # n=int(input("enter a number:"))
# # for i in range(1,11):
# #     print(i,"*",n,"=",i*n)
# # print()
#
#
#
# # Level 2 — Important
# # 6. Factorial
# # Write a program to find the factorial of a number. Example: 5 fi 120.
#
# # fact=1
# # n=int(input("enter a number:"))
# # for i in range(1,n+1):
# #     fact=fact*i
# # print("Factorial",fact)
# # print()
#
#
#
# # 7. Reverse a Number
# # Write a program to reverse a number. Example: 1234 fi 4321.
# # n=58769
# # rev=""
# # for i in str(n):
# #     rev=i+rev
# # print("Reverse of a number:",rev)
#
# # 8. Palindrome Number
# # Write a program to check whether a number is a palindrome. Example: 121 fi Palindrome.
# # n=input("enter a number:")
# # if n==n[::-1]:
# #     print("PALINDROME")
# # else:
# #     print("NOT")
#
#
# # 9. Prime Number
# # Write a program to check whether a number is prime.
# # n=int(input("enter a number:"))
# # if n>1:
# #     for i in range(2,n):
# #         if n%i==0:
# #             print("not prime")
# #             break
# #     else:
# #         print("prime")
# # else:
# #     print("not a prime nor composite")
#
# # 10. Prime Numbers
# # Write a program to print all prime numbers between 1 and 100.
#
# # for i in range(2,101):
# #     for j in range(2,i):
# #         if i%j==0:
# #             break
# #     else:
# #         print(i,end=" ")
# #
# # n=int(input("enter a number:"))
# # for i in range(2,n):
# #     for j in range(2,i):
# #         if i%j==0:
# #             break
# #     else:
# #         print(i)
#
#
# # 11. Armstrong Number
# # Write a program to check whether a number is an Armstrong number. Example: 153 fi Armstrong.
#
# # n=407
# # st=str(n)
# # l=len(st)
# # s=0
# # for i in st:
# #     s=s+int(i)**l
# # if n==s:
# #     print("ARMSTRONG")
# # else:
# #     print('no')
#
#
#
# # 12. Armstrong Numbers
# # Write a program to print all Armstrong numbers between 100 and 1000.
# # for i in range(100,1001):
# #     s=0
# #     a=str(i)
# #     for j in a:
# #         s=s+int(j)**3
# #     if i==s:
# #         print(i)
#
# # 13. Fibonacci Series
# # Write a program to print the first N Fibonacci terms. Example: 6 fi 0 1 1 2 3 5.
#
# # a=0
# # b=1
# # n=6
# # for i in range(6):
# #     print(a)
# #     c=a+b
# #     a=b
# #     b=c
#
# # 14. Sum of Digits
# # Write a program to find the sum of digits. Example: 1234 fi 10.
#
# # d="345"
# # s=0
# # for i in d:
# #     s=s+int(i)
# # print(s)
# #
#
#
# # 15. Count Digits
# # Write a program to count the number of digits in a number. Example: 12345 fi 5.
#
#
# # d="2345"
# # c=0
# # for i in d:
# #     c=c+1
# # print(c)
#
#
#
# # Level 3 — Lists & Strings
#
#
#
#
# # 16. Move Zeroes
# # Given L = [0, 1, 0, 3, 12], move all zeroes to the end. Expected: [1, 3, 12, 0, 0].
#
# l = [0, 1, 0, 3, 12]
#
# # l=[1,3,12]
# # l1=[0,0]
# # new=[]
# # c=l+l1
# # new.append(c)
# # print(new)
#
# # new=[]
# # for i in l:
# #     if i!=0:
# #         new.append(i)
# # for i in l:
# #     if i==0:
# #         new.append(i)
# # print(new)
#
# # 17. Find Largest
# # Find the largest number in a list without using max(). Example: [10, 25, 5, 40, 15] fi 40.
#
# # l=[10, 25, 5, 40, 15]
# # l1=l[0]
# # for i in l:
# #     if i>l1:
# #         l1=i
# # print(l1)
#
#
#
#
# # 18. Find Smallest
# # Find the smallest number in a list without using min().
# # l=[10, 25, 5, 40, 15]
# # l1=l[0]
# # for i in l:
# #    if i<l1:
# #        l1=i
# # print(l1)
#
#
# # 19. Count Even and Odd
# # Given a list, count how many even and odd numbers are present.
#
# # l=[1,2,3,4,5,6,7,8]
# # c=0
# # c1=0
# # for i in l:
# #     if i%2==0:
# #         c=c+1
# #     else:
# #         c1=c1+1
# # print("even numbers:",c)
# # print("odd numbers",c1)
#
#
# # 20. Most Frequent Number
# # Define a function that takes a list and returns the most frequent number. Example: [1,2,2,3,4,2,5,3,4,6] fi
# # l=[1,2,2,3,4,2,5,3,4,6]
# # def f(l):
# #     l1=l[0]
# #     c=0
# #     for i in l:
# #         if l.count(i)>c:
# #             c=l.count(i)
# #             l1=i
# #     return l1
# # print(f(l))
#
# # 21. Count Vowels and Consonants
# # Write a program to count vowels and consonants in a string. Example: Hello World fi Vowels: 3,
# # Consonants: 7.
#
# # s="hello world"
# # c=0
# # c1=0
# # v="AEIOUaeiou"
# # for i in s:
# #     if i in v:
# #         c=c+1
# #     elif i.isalpha():
# #         c1=c1+1
# # print("vowels",c)
# # print("consosnants",c1)
#
#
#
# # 22. Reverse a String
# # Write a program to reverse a string. Example: Python fi nohtyP.
#
# # s="python"
# # r=s[::-1]
# # print("reverse",r)
#
#
# # 23. Palindrome String
# # Write a program to check whether a string is a palindrome. Example: madam fi Palindrome.
#
#
# # s="mady"
# # r=s[::-1]
# # if s==r:
# #     print("palindrome")
# # else:
# #     print("not palindrome")
#
#
# # 24. Count Vowels
# # Write a program to count only the vowels in a string.
#
#
# # s="madam"
# # c=0
# # for i in s:
# #     if i in "aeiou":
# #         c=c+1
# # print("vowels",c)
#
#
#
# # Level 4 — Functions
# # 25. Add Numbers
# # Define a function that takes two numbers and returns their sum.
#
# # def s(a,b):
# #     sum=a+b
# #     return sum
# # print(s(3,4))
#
#
#
# # 26. Even or Odd Function
# # Define a function that takes a number and returns whether it is even or odd.
#
# # def w(a):
# #     if a%2==0:
# #         return "even"
# #     else:
# #         return "odd"
# # print(w(9))
#
#
#
#
# # 27. Prime Function
# # Define a function that takes a number and checks whether it is prime
# #
# # def p(n):
# #     if n%2==0:
# #         return "not prime"
# #     else:
# #         return "prime"
# # print(p(6))
#
#
#
#
#
#
# # 28. Factorial Function
# # Define a function to calculate the factorial of a number.
#
# # def f(n):
# #     fa=1
# #     for i in range(1,n+1):
# #         fa=fa*i
# #     print("factorial",fa)
# # f(6)
#
#
#
# # 29. Maximum Function
# # Define a function that takes a list and returns the largest number without using max().
#
# # l=[5,6,7,2,4,6,8,9]
# # def lr(l):
# #     l1=l[0]
# #     for i in l:
# #         if i>l1:
# #             l1=i
# #     return l1
# # print(lr(l))
#
#
#
# # 30. Vowel Function
# # Define a function that takes a string and returns the number of vowels.
# # s="hello"
# # def vo(s):
# #     v="aeiou"
# #     c=0
# #     for i in s:
# #         if i in v:
# #             c=c+1
# #     return c
# # print(vo(s))
#
#
#
# # Level 5 — Lambda, map(), filter(), reduce()
# # 31. Lambda Square
# # Use a lambda function to find the square of a number.
#
# # l=lambda x:x**2
# # print(l(10))
#
#
# # 32. Lambda Even/Odd
# # Use a lambda function to check whether a number is even.
#
# # a=lambda x:x%2==0
# # print(a(4))
#
#
# # 33. Map — Double
# # Using map(), double every number in L = [1,2,3,4,5]. Expected: [2,4,6,8,10].
# # L = [1,2,3,4,5]
# # print(list(map(lambda x:x*2,L)))
#
# # 34. Map — Square
# # Using map() and lambda, find the square of every number in L = [1,2,3,4,5].
# # L = [1,2,3,4,5]
# # print(list(map(lambda x:x**2,L)))
#
#
# # 35. Filter — Even Numbers
# # Using filter(), find all even numbers in L = [1,2,3,4,5,6,7,8].
#
# # L = [1,2,3,4,5,6,7,8]
# # print(list(filter(lambda x:x%2==0,L)))
# # print(list(filter(lambda x:x%2!=0,L)))
#
#
# # 36. Filter — Greater Than 10
# # Using filter(), find numbers greater than 10 in L = [5,12,8,20,3,15].
#
# # L = [5,12,8,20,3,15]
# # print(list(filter(lambda x:x>10,L)))
# # print(list(filter(lambda x:x<10,L)))
#
# # 37. Reduce — Sum
# # Using reduce(), find the sum of L = [1,2,3,4,5].
# # L = [1, 2, 3, 4, 5]
# # print(functools.reduce(lambda x,y:x+y,L))
#
#
# # 38. Reduce — Product
# # Using reduce(), find the product of L = [1,2,3,4,5]. Expected: 120.
#
# # L = [1,2,3,4,5]
# # print(functools.reduce(lambda x,y:x*y,L))
#
# # Level 6 — Patterns
# # 39. Pattern
# # Print:
# # 1
# # 1 1
# # 1 1 1
# # 1 1 1 1
# # 1 1 1 1 1
#
# # for i in range(1,6):
# #     for j in range(i):
# #         print(1,end=" ")
# #     print()
#
#
#
# # 40. Pattern
# # Print:
# # 1 1 1 1 1
# # 2 2 2 2
# # 3 3 3
# # 4 4
# # 5
#
# # for i in range(1,6):
# #     for j in range(6-i):
# #         print(i,end=" ")
# #     print()
#
#
# # 41. Pattern
# # Print:
# # *
# # * *
# # * * *
# # * * * *
# # * * * * *
# # for i in range(1,6):
# #     for j in range(1,i+1):
# #         print("*",end=" ")
# #     print()
# # 42. Pattern
# # Print:
# # 1
# # 2 3
# # 4 5 6
# # 7 8 9 10
#
# # k=1
# # for i in range(1,5):
# #     for j in range(1,i+1):
# #         print(k,end=" ")
# #         k=k+1
# #     print()
#
#
# # 43. Pattern
# # Print:
# # 5 5 5 5 5
# # 4 4 4 4
# # 3 3 3
# # 2 2
# # 1
#
# # for i in range(5,0,-1):
# #     for j in range(i):
# #         print(i,end=" ")
# #     print()
#
#
# # n Top 15 to Practice First
# # 1 1. Series using for and range()
# # 2 2. Fibonacci
# # 3 3. Armstrong
# # 4 4. Prime
# # 5 5. Palindrome
# # 6 6. Factorial
# # 7 7. Reverse number
# # 8 8. Sum of digits
# # 9 9. Move zeroes
# # 10 10. Most frequent number
# # 11 11. Vowels & consonants
# # 12 12. Function to find maximum
# # 13 13. Pattern using nested loops
# # 14 14. map() + lambda
# # 15 15. filter() + lambda
# # Exam tip: Practice writing the programs yourself. Focus especially on range(), for/while loops, if/else,
# # nested loops, append(), count(), functions, lambda, map(), filter(), and reduce().
#
#
# # 1
# # 2 2
# # 3 3 3
# # 4 4 4 4
# # 5 5 5 5 5
#
# # for i in range(1,6):
# #     for j in range(1,i+1):
# #         print(i,end=" ")
# #     print()
#
# # 1
# # 1 1
# # 1 1 1
# # 1 1 1 1
# # 1 1 1 1 1
# #
# # for i in range(1,6):
# #     for j in range(1,i+1):
# #         print(1,end=" ")
# #     print()
#
#
# # 1 1 1 1 1
# # 1 1 1 1
# # 1 1 1
# # 1 1
# # 1
# #
# # for i in range(6,0,-1):
# #     for j in range(i-1):
# #         print(1,end=" ")
# #     print()
# # 5 5 5 5 5
# # 4 4 4 4
# # 3 3 3
# # 2 2
# # 1
#
# # for i in range(5,0,-1):
# #     for j in range(i):
# #         print(i,end=" ")
# #     print()
#
#
#
#
#
#
# # 1 4 9 16 25
#
#
# # for i in range(1,6):
# #     i=i**2
# #     print(i,end=" ")
#
#
# #even numbers from 1,50
# # for i in range(1,51):
# #     if i%2==0:
# #         print(i,end=" ")
#
# #factorial of a number
# # fact=1
# # n=6
# # for i in range(1,n+1):
# #     fact=fact*i
# # print("Factorial",fact)
#
#
# #prime or not
#
# # n=int(input("enter a number:"))
# # if n>1:
# #     for i in range(2,n):
# #         if n%i==0:
# #             print("not prime")
# #             break
# #     else:
# #         print("prime")
#
# #1st 7 fibonacci
# # a=0
# # b=1
# # for i in range(1,8):
# #     print(a)
# #     c=a+b
# #     a=b
# #     b=c
#
# #nmbr palindrome
#
# # n="12321"
# # n1=n[::-1]
# # for i in n:
# #     if n==n1:
# #         print("palindrome")
# #         break
# # else:
# #     print("not")
#
# ##armstrong blw 100,1000
# # for i in range(100,1001):
# #     s=0
# #     for j in str(i):
# #         s=s+int(j)**3
# #     if i==s:
# #         print(i)
#
#
# # l=[0,2,0,5,7]
# # new=[]
# # for i in l:
# #     if i!=0:
# #         new.append(i)
# # for i in l:
# #     if i==0:
# #         new.append(i)
# # print(new)
#
#
# # 1
# # 2 2
# # 3 3 3
# # 4 4 4 4
# # 5 5 5 5 5
# # for i in range(1,6):
# #     for j in range(1,i+1):
# #         print(i,end=" ")
# #     print()
#
# l=[1,2,3,3,4,5,6,6,7,2,3,4,2.3,3]
# l1=l[0]
# for i in l:
#     if i>l1:
#         l1=i
# print(i)
# #
#
#
# # for i in range(1,6):
# #     i=i**2
# #     print(i,end=" ")
#
# # i=100
# # while(i>=50):
# #     print(i,end=" ")
# #     i=i-10
#
#
# # s=0
# # for i in range(1,7):
# #     s=s+i
# #     print(s,end=" ")
#
# # for i in range(2,11,2):
# #     print(i)
#
# # for i in range(1,10,2):
# #     print(i)
#
# # n=int(input("enter a number:"))
# # f=1
# # for i in range(1,n+1):
# #     f=f*i
# # print(f)
#
#
# # rev=""
# # for i in str(n):
# #     rev=i+rev
# # print(rev)
#
# # s=str(n)
# # r=s[::-1]
# # if s==r:
# #     print("palindrome")
# # else:
# #     print("np")
#
# # if n>1:
# #     for i in range(2,n):
# #         if n%i==0:
# #             print("not prime")
# #             break
# #     else:
# #         print("prime")
#
# # for i in range(2,101):
# #     for j in range(2,i):
# #         if i%j==0:
# #             break
# #     else:
# #         print(i,end=" ")
#
#
# # for i in range(100,1001):
# #     a=str(i)
# #     s=0
# #     for j in a:
# #         s=s+int(j)**3
# #     if i==s:
# #         print(i)
#
#
# # a=0
# # b=1
# # for i in range(1,8):
# #     print(a,end=" ")
# #     c=a+b
# #     a=b
# #     b=c
#
# # n="1234"
# # s=0
# # for i in n:
# #     s=s+int(i)
# # print(s)
#
#
# # l=[0,1,0,3,12]
# # new=[]
# # for i in l:
# #     if i!=0:
# #         new.append(i)
# # for i in l:
# #     if i==0:
# #         new.append(i)
# # print(new)
#
#
# # l=[0,1,0,3,12]
# # j=l[0]
# # for i in l:
# #     if i>j:
# #         j=i
# # print(j)
#
#
#
# # l=[2,6,8,3,45]
# # m=l[0]
# # for i in l:
# #     if i<m:
# #         i=m
# # print(m)
#
#
# # l=[10,11,12,13,14,15,16,17,18,19,20]
# # e=0
# # o=0
# # for i in l:
# #     if i%2==0:
# #         e=e+1
# #     else:
# #         o=o+1
# # print("even count:",e)
# # print("odd count:",o)
#
#
# # s="python programming"
# # v=0
# # c=0
# # for i in s:
# #     if i in "aeiou":
# #         v=v+1
# #     elif i.isalpha():
# #         c=c+1
# # print("vowels count:",v)
# # print("consonants count:",c)
#
#
# # s="hello world"
# # rev=""
# # for i in s:
# #     rev=i+rev
# # print("reverse of the string:",rev)
#
#
# # s="mad"
# # r=s[::-1]
# # if s==r:
# #     print("palindrome")
# # else:
# #     print("nop")
#
# # l=[1,2,3,4,4,4,5,6]
# # def fr(l):
# #     l1=l[0]
# #     c=0
# #     for i in l:
# #         if l.count(i)>c:
# #             c=l.count(i)
# #             l1=i
# #     return l1
# # print(fr(l))
#
# # for i in range(1,6):
# #     for j in range(i):
# #         print(i,end=" ")
# #     print()
#
# # for i in range(5,0,-1):
# #     for j in range(i):
# #         print(i,end=" ")
# #     print()
#
# # for i in range(1,6):
# #     for j in range(i):
# #         print("*",end=" ")
# #     print()
#
# # for i in range(5,0,-1):
# #     for j in range(i):
# #         print("*",end=" ")
# #     print()
#
#
#
#
#
#
#
# # i=2
# # for j in range(5):
# #     print(i,end=" ")
# #     i=i*2
#
# # i=50
# # while(i>=25):
# #     print(i,end=" ")
# #     i=i-5
#
#
# # a=0
# # b=1
# # for i in range(1,9):
# #     print(a,end=" ")
# #     c=a+b
# #     a=b
# #     b=c
#
#
# # for i in range(2,51):
# #     for j in range(2,i):
# #         if i%j==0:
# #             break
# #     else:
# #         print(i,end=" ")
#
#
#
# # for i in range(100,1000):
# #     st=str(i)
# #     s=0
# #     for j in st:
# #         s=s+int(j)**3
# #     if i==s:
# #         print(i,end=" ")
#
#
# # n="12345"
# # rev=""
# # for i in n:
# #     rev=i+rev
# # print(rev)
#
#
# # n="123"
# # r=n[::-1]
# # if n==r:
# #     print("palindrome")
# # else:
# #     print("not palindrome")
#
#
# # n=123
# # s=0
# # for i in str(n):
# #     s=s+int(i)
# # print(s)
#
# # n="456"
# # s=0
# # for i in n:
# #     s=s+int(i)
# # print(s)
#
#
# # l=[4,7,2,9,1,6]
# # l1=l[0]
# # for i in l:
# #     if i>l1:
# #         l1=i
# # print(l1)
#
#
#
# # l=[4,7,2,9,1,6]
# # l1=l[0]
# # for i in l:
# #     if i<l1:
# #         l1=i
# # print(l1)
#
#
# # for i in range(1,6):
# #     for j in range(i) :
# #         print(i,end=" ")
# #     print()
#
#
# # for i in range(1,8):
# #     print(i*3,end=" ")
#
#
# # i=80
# # while(i>=30):
# #     print(i,end=" ")
# #     i=i-10
#
# # a=0
# # b=1
# # for i in range(1,8):
# #     print(a,end=" ")
# #     c=a+b
# #     a=b
# #     b=c
#
#
# # for i in range(2,31):
# #     for j in range(2,i):
# #         if i%j==0:
# #             break
# #     else:
# #         print(i,end=" ")
#
#
#
# # for i in range(100,501):
# #     st=str(i)
# #     s=0
# #     for j in st:
# #         s=s+int(j)**3
# #     if i==s:
# #         print(i)
#
#
#
# # n="67890"
# # r=n[::-1]
# # print(r)
#
#
# # for i in range(1,6):
# #     for j in range(i):
# #         print(i,end=" ")
# #     print()
#
# # for i in range(5,0,-1):
# #     for j in range(i):
# #         print(i,end=" ")
# #     print()
#
#
# # for i in range(1,11):
# #     m= i * 7
# #     print(i,"*","7","=",m)
#
# # for i in range(20,51,2):
# #     print(i)
#
# # n="583921"
# # c=0
# # for i in n:
# #     c=c+1
# # print(c)
#
#
# # l=[2,4,2,7,4,9,7]
# # a=set(l)
# # b=[a]
# # print(b)
#
# # l=[3,8,11,14,17,20]
# # new=[]
# # new1=[]
# # for i in l:
# #     if i%2==0:
# #         new.append(i)
# #     else:
# #         new1.append(i)
# #
# # print(new)
# # print(new1)
#
#
# # s="hello"
# # rev=""
# # for i in s:
# #     rev=i+rev
# # if s==rev:
# #     print("palindrome")
# # else:
# #     print('not palindrome')
#
#
# # s="MaLAyaLaM"
# # u=0
# # l=0
# # for i in s:
# #     if i.isupper():
# #         u=u+1
# #     elif i.islower():
# #         l=l+1
# # print("uppercount:",u)
# # print("lowercount",l)
#
# # c=lambda n:n**3
# # print(c(3))
#
# # s=lambda m:m**2
# # print(s(6))
#
#
# # l=[4,15,7,22,9,18]
# # print(list(filter(lambda x:x>10,l)))
#
#
# # l=[3,6,9,12]
# # print(list(map(lambda x:x**2,l)))
#
#
# # l=[2,3,4,5]
# # print(functools.reduce(lambda x,y:x*y,l))
#
#
# # for i in range(5,1,-1):
# #     for j in range(1,i):
# #         print(j,end=" ")
# #     print()
#
#
# # for i in range(1,7):
# #     for j in range(1,i):
# #         print(j,end=" ")
# #     print()
#
#
#
# # 5
# # 5 4
# # 5 4 3
# # 5 4 3 2
# # 5 4 3 2 1
# #
# # for i in range(1,6):
# #     for j in range(5,5-i,-1):
# #         print(j,end=" ")
# #     print()
#
#
#
# # n=28
# # s=0
# # for i in range(1,n):
# #     if n%i==0:
# #         s=s+i
# # if s==n:
# #     print("perfect number")
# # else:
# #     print("not perfect")
#
# # duplicate removal
# # l=[1,2,2,4,5,6,6,7]
# # r=[]
# # for i in l:
# #     if i not in r:
# #         r.append(i)
# # print(r)
#
# # n=8
# # for i in range(1,11):
# #     print(i,"*",n,"=",i*n)
#
# # s=0
# # for i in range(2,51,2):
# #     print(i,end=" ")
# #     s=s+i
# # print(s)
#
# # n="728451"
# # c=0
# # for i in n:
# #     c=c+1
# # print(c)
#
# # sum of factors==numbers
#
# # n=28
# # s=0
# # for i in range(1,n):
# #     if n%i==0:
# #         s=s+i
# # if s==n:
# #     print("perfect")
# # else:
# #     print("not perfect")
#
#
#
# # l=[4,7,4,2,7,9,2,1]
# # l1=[]
# # for i in l:
# #     if i not in l1:
# #         l1.append(i)
# # print(l1)
#
#
#
# # l=[12,45,23,67,34,89,56]
# # l1=l[0]
# # l2=l[0]
# # for i in l:
# #     if i>l1:
# #         l2=l1
# #         l1=i
# #     elif i>l1 and i!=l1:
# #         l2=i
# # print(l2)
#
#



# # 1
# # 2 1
# # 3 2 1
# # 4 3 2 1
# # 5 4 3 2 1
# #
# # for i in range(1,6):
# #     for j in range(i,0,-1):
# #         print(j,end=" ")
# #     print()
#
#
# s="apple"
# d=""
# for i in s:
#     if i not in d:
#         c=0
#         for j in s:
#             if i==j:
#                 c=c+1
#         print(i,c)
#         d=d+i
#
#
# # l=[1,2,3,3,3,4,5]
# # l1=l[0]
# # c=0
# # for i in l:
# #     if l.count(i)>c:
# #         c=l.count(i)
# #         l1=i
# # print(l1)
#
#
# # l=[1,3,0,5,0]
# # new=[]
# # for i in l:
# #     if i!=0:
# #         new.append(i)
# # for i in l:
# #     if i==0:
# #         new.append(i)
# # print(new   )
#
#
# # 5 10 20 40 80
# # i=5
# # while(i<=80):
# #     print(i,end=" ")
# #     i=i+i
#
# # 2 5 8 11 14 17
# # for i in range(2,18,3):
# #     print(i,end=" ")
#
#
# # l=[3,4,5]
# # print(functools.reduce(lambda x,y:x*y,l,1))
#
# # count without using count()
#
# # l=[2,4,5,2,7,8,2]
# # c=0
# # for i in l:
# #     if i==2:
# #         c=c+1
# # print(c)
import functools
from ctypes import c_int16
from pickletools import long1

# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1

# for i in range(1,6):
#     for j in range(5,5-i,-1):
#         print(j,end=" ")
#     print()



# a --> 1
# e --> 1
# i --> 1
# o --> 1
# u --> 1    count of each vowel

# s="education"
# for i in "aeiou":
#     c = 0
#     for ch in s:
#
#         if ch==i:
#             c=c+1
#     print(i,"-->",c)

# find even numbers and their sum

# l=[3,8,11,14,17,20,25]
# even=(list(filter(lambda x:x%2==0,l)))
# print(functools.reduce(lambda x,y:x+y,even))

# find odd numbers and their sum

# l=[3,8,11,14,17,20,25]
#
# od=(list(filter(lambda x:x%2!=0,l)))
# print(functools.reduce(lambda x,y:x+y,od))



# 3 9 27 81 243
# i=3
# while(i<=243):
#     print(i,end=" ")
#     i=i*3





# s="apple"
# d=""
# for i in s:
#     if i not in d:
#         c=0
#         for j in s:
#             if i==j:
#                 c=c+1
#         print(i,c)
#         d=d+i
#
# #while
#
#
# # # #1,2,3,4,5,.....100
#
# i=1
# while(i<=100):
#     print(i,end=" ")
#     i=i+1
# print("\n")
#
#
# # # #1,3,5,7,9,11,13,15
#
# i=1
# while(i<=15):
#     print(i,end=" ")
#     i=i+2
# print("\n")
#
#
# # #2,4,6,8,10,12
#
# i=2
# while(i<=12):
#     print(i,end=" ")
#     i=i+2
# print("\n")
#
#
# # #1,4,7,10,13,16
#
# i=1
# while(i<=16):
#     print(i,end=" ")
#     i=i+3
# print("\n")
#
#
# #10,20,30,40,50,60,70,80
#
# i=10
# while(i<=80):
#     print(i,end=" ")
#     i=i+10
# print("\n")
#
#
# #3,6,9,12,15,18,21
#
# i=3
# while(i<=21):
#     print(i,end=" ")
#     i=i+3
# print("\n")
#
#
# #5,4,3,2,1
#
# i=5
# while(i>=1):
#     print(i,end=" ")
#     i=i-1
#
# #8,6,4,2,0
#
# i=8
# while(i>=0):
#     print(i,end=" ")
#     i=i-2
# print("\n")
#
#
# #100,101,102,.....200
#
# i=100
# while(i<=200):
#     print(i,end=" ")
#     i=i+1
# print()
#
#
#
# #print all 4 digit numbers(1000-9999)
#
# i=1000
# while(i<=9999):
#     print(i,end=" ")
#     i=i+1

#print(), print("\n") ----both are used for spacing
# print(i,end=" ") ------ print item horizontally


#print those numbers that are divisible by 3 in range 1,50

#
# i=1
# while(i<=50):
#     if i%3==0:
#          print(i,end=" ")
#     i=i+1
# print("\n")


#print those 3 digits numbers that are divisible by 5 and 7


# i=100
# while(i<=999):
#     if i%5==0 and i%7==0:
#         print(i,end=" ")
#     i=i+1
# print()

#print those numbers in the range(100,200) which contains the digit 3

# i=100
# while(i<=200):
#     s=str(i)
#     if '3' in s:
#          print(i,end=" ")
#     i=i+1
# print()


#count
#------------------------------

# i=1
# count=1
# while(i<=50):
#     if i%3==0:
#          # print(i,end=" ")
#          count=count+1
#     i=i+1
# print(count)
# print("\n")

#
# i=100
# count=0
# while(i<=200):
#     s=str(i)
#     if '3' in s:
#          # print(i,end=" ")
#        count=count+1
#     i=i+1
# print(count)
# print()


#sum of series 1,2,3,4,5
# i=1
# sum=0
# while(i<=5):
#     sum=sum+i
#     i=i+1
# print("sum",sum)


# product of series
# i=1
# prdt=1
# while(i<=5):
#     prdt=prdt*i
#     i=i+1
# print("product",prdt)

#sum of 1st 10 even numbers
# i=2
# sum=0
# while(i<=20):
#      if i%2==0:
#       sum=sum+i
#      i=i+2
# print("sum",sum)

#product---------
# i=2
# sum=0
# product=1
# while(i<=20):
#     sum=sum*i
#     product=product*i
#     i=i+2
# print("product",product)


#4,9,14,19,24,29,34,39
# i=4
# while(i<=39):
#     print(i,end=" ")
#     i=i+5
# print("\n")

# sum of series 1,3,5,7,9,11

# i=1
# sum=0
# while(i<=11):
#     sum=sum+i
#     i=i+2
# print("sum",sum)


# product of numbers that sre divisible by 3 ans 5 in the range(1,50)
# i=1
# product=1
# while(i<=50):
#     if i%3==0 and i%5==0:
#      product=product*i
#     i=i+1
#         # print(i,end=" ")
# print("product", product)


# count of 3 digits numbers that are divisible by 7
# i=100
# count=0
# while(i<=999):
#     if i%7==0:
#          # print(i,end=" ")
#          count=count+1
#     i=i+1

# print(count)
# print("\n")




#factorial of a number

# i=1
# fact=1
# n=int(input("enter a number:"))
# while(i<=n):
#     fact=fact*i
#     i=i+1
# print("factorial",fact)


#multiplication table of a number upto(10)

n=int(input("enter a number:"))
i=1
while(i<=10):
    print(i,'*',n,'=',i*n)
    i=i+1




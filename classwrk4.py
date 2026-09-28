#write a program to find BMI(Body Mass Index)
#
# BMI= weight in (kg)/ height**2 in (m)
#
#
# BMI	                 Status
# ≤ 18.4	             Underweight
# 18.5 - 24.9	         Normal
# 25.0 - 39.9	         Overweight
# ≥ 40.0	             Obese

#answer
# wt=int(input("enter weight in kg:"))
# ht=int(input("enter height in m:"))
# BMI= wt/ht**2
# if BMI<=18.4:
#     print("underweight")
# elif BMI>=18.5 and BMI<=24.5:
#         print("normal")
# elif BMI>=25.0 and BMI<=39.9:
#         print("overweight")
# else:
#      if BMI>=40.0:
#        print("obese")




#2.# A toy vendor supplies three types of toys:

# Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.

# The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.

# On orders of more than Rs. 100 for key-based toys,a discount of 5% is given,

# and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.

# Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.

# Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.

# code1-battery toy
# code2-key based
# code3-electrical)


#answer
#cod=int(input("enter the code, (code1-battery toy code2-key based code3-electrical)  :"))
# price=int(input("enter the price:"))
# if cod == 1:
#     if price>=1000:
#         d=price-(price*0.10)
#         print(d)
#     else:
#         print("no disc")
#
# elif cod==2:
#     if price>=500:
#         d=price-(price*0.05)
#         print(d)
#     else:
#         print("no disc")
#
# elif cod==3:
#     if price>=500:
#         d=price-(price*0.10)
#         print(d)
#     else:
#         print("no disc")




#3 FIZZBUZZ PRoblem

# if divisible by 3 only -print fizz
# if divisible by 5 only -print buzz
# if a number is divisible by 3 and 5
#     print fizzbuzz
#     otherwise -print the number


#answer
# n=int(input("enter a number: "))
# if n%3==0 and n%5==0:
#     print("FizzBuzz")
# elif n%3==0:
#     print("Fizz")
# elif n%5==0:
#     print("Buzz")
# else:
#     print(n)
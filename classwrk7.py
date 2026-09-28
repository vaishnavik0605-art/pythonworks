# # Q.Write Python Programs Using map(), filter(), or reduce()
# #
# # 1.Capitalize all names in a list
# import functools
#
# names = ['alin', 'arun', 'anu']
# print(list(map(lambda n:n.capitalize(),names)))
# # print(list(map(lambda n:n.capitalize(),names)))
#
# # 2.Append "@gmail.com" to a list of usernames
# users = ['user1', 'user2']
# print(list(map(lambda u:u+"@gmail.com",users)))
# # print(list(map(lambda x:x+"@gmail.com",users)))
#
# # 3.Filter out all empty strings from a list
# words = ['hello', ' ', 'world', ' ', 'python']
# print(list(filter(lambda w:w!=" ",words)))
# print(list(filter(lambda w:w!=" ",words)))
#
# # 4.Filter names that start with the letter 'A'
# names = ['Anu', 'Neenu', 'Arun', 'Ravi']
# print(list(filter(lambda n:n[0]=='A',names)))
# # print(list(filter(lambda n:n[0]=='A',names)))
#
# # 5.Concatenate all strings in a list
# w= ['Python', 'is', 'fun']
import functools
# print(functools.reduce(lambda x,y:x + y,w))
#
# # # 6.Multiply all numbers in a list
# nums = [2, 3, 4]
# # print(functools.reduce(lambda x,y:x*y,nums,1))
# print(functools.reduce(lambda x,y:x*y,nums,1))
# print(list(map(lambda x:x**2,nums)))
#
# # 7.Extract First Character of Each Word
# # words = ["apple", "banana", "cherry"]
# # print(list(map(lambda i:i[0],words)))
#
# # 8.Add 10 to Each Number
# # nums = [5, 10, 15]
# # print(list(map(lambda n:n+10,nums)))
#
# # 9.Given a list
l=[12,-4,78,-34,90,45,16,26,-2,-11,3]
#     # #Sum of positive even numbers
# even=(list(filter(lambda x:x>0 and x%2==0,l)))
# print(functools.reduce(lambda x,y:x+y,even,0))

#     # #Sum of Positive Odd numbers
# # odd=(list(filter(lambda x:x%2!=0 and x>0,l)))
# # print(functools.reduce(lambda x,y:x+y,odd,0))
#
#     # #Sum of Negative  odd numbers
# # even=(list(filter(lambda x:x<0 and x%2==0,l)))
# # print(functools.reduce(lambda x,y:x+y,even,0))
#
#     # #Sum of Negative Even numbers
# # odd=(list(filter(lambda x:x%2!=0 and x<0,l)))
# # print(functools.reduce(lambda x,y:x+y,odd,0))
#
#     # #Count of Positive numbers
# # pos=(list(filter(lambda x:x>0,l)))
# # print(len(pos))
#
#     # #Count of negative numbers
# # neg=(list(filter(lambda x:x<0,l)))
# # print(len(neg))
# # 10.Given a list
# nums = ["1", "2", "3", "4"]
# # Convert all Strings to Integers [1,2,3,4]
# # print(list(map(lambda n:int(n),nums)))
#
# # 11.
# p= [{'name':'laptop','price':50000},
#     {'name':'phone','price':20000},
#     {'name':'watch','price':3000},
#     {'name':'Tablet','price':25000}]
# #
# #print list of product names in Uppercase
# # print(list(map(lambda n:n['name'].upper(),p)))
#
# #print products with price greater than 10000
# # print(list(filter(lambda x:x['price']>10000,p)))
#
# #Find the total price of all products
#
#
# total=(list(map(lambda x:x['price'],p)))
# print(functools.reduce(lambda x,y:x+y,total,0))
#
#
# print(functools.reduce(lambda x,y:x+y['price'],p,0))
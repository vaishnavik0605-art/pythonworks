#define a fn that a number as arguments returns its square


# def sqr(n):
#     a=n**2
#     return a
# x=sqr(5)
# print(x)

##########lambda##########
#square of a number
# sq=lambda n:n**2
# print(sq(5))
#
# #sum of 2 numbers
# a=lambda a,b:a+b
# print(a(2,3))
#
#
# #product of 3 numbers
# p=lambda p,q,r:p*q*r
# print(p(2,3,4))
#
# #cube of a number
# c=lambda n:n**3
# print(c(3))
#
# #first letter of a string
# s=lambda s:s[0]
# print(s('hello'))
#
# #length of a string
# l=lambda t:len(t)
# print(l('world'))

#reverse of a string
# r=lambda a:a[::-1]
# print(r('welcome'))
#
# #name value from a dictionary
# n=lambda d:d['name']
# print(n({'name':'amal','age':22}))
#
# #second element from a list
# s=lambda e:e[1]
# print(s([10,30,50]))

#add 10 to a number
# t=lambda d:d+10
# print(t(40))



##########   map  (higher order fns #############

# l=[1,2,3,4]
# # print(set(map(lambda n:n**2,l)))
# # print(tuple(map(lambda n:n**2,l)))
# #
# #
# #
# # l=[25,36,81]
#
# #create a new list of cubes
# # l=[1,2,3,4]
# print(list(map(lambda c:c**3,l)))
#
# #create a new list of square roots
# l=[25,36,81,100]
# print(list(map(lambda s:s**0.5,l)))
#
#
# #create a new list of lengths
# colors=['red','green','blue','yellow','black']
# print(list(map(lambda c:len(c),colors)))
#
# #create a new list of first characters
# print(list(map(lambda c:c[0],colors)))
#
# #create a new list of last characters
# print(list(map(lambda c:c[-1],colors)))
#
# #create a new list of reverse of each element
# print(list(map(lambda c:c[::-1],colors)))
#
# #Given a list
# l=[23,78,12,56]
# #Add 10 to each element in the given sequence
# print(list(map(lambda a:a+10,l)))
#
# ##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
# #
# # # create a new list of emails
# print(list(map(lambda e:e['email'],l)))
#
#
#
# #####  filter ######
# l=[1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda e:e%2==0,l)))

#FILTERS EVEN VALUE GREATER THAN 50
l=[23,45,67,12,89,70]
print(list(filter(lambda x:x%2==0 and x>50,l)))
# GIVEN A LIST
colors=['red','green','blue','yellow','black']
# FILTER THE COLORS WHOSE LENGHT IS GREATER THAN 5
print(list(filter(lambda x:len(x)>5,colors)))
#FILTER THE COLOR CONTAINING LETTER N
print(list(filter(lambda x:'n' in x,colors )))




#########reduce###########



import functools
l=[1,2,3,4]
print(functools.reduce(lambda x,y:x+y,l,0))
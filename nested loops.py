# l=[10,20,30]
# for i in l:
#     for j in range(1,4):  # here this loop works 2 (in this case) times for every outer loop works
#         print(i,end=" ")
#     print()
from logging import addLevelName

#to print
# 1111
# 2222
# 3333

# l=[1,2,3]
# for i in l:
#     for j in range(1,5):
#         print(i, end=" ")
#     print()

# l=[1,2,3,4]
# for i in range(1,4):
#     for j in range(1,5):
#         print(j, end=" ")
#     print()
#
#


#* * * *
# * * * *
# * * * *
# * * * *

# for i in range(1,5): # this loop is to increase rows
#     for j in range(1,5):
#         print('*', end=" ")
#     print()

l=[['lion','tiger'],['elephant','cat']]
# for i in l:
#     # print(i)
#     for j in i:
#        print(j)


#given a list
names=['kelly','alan','jeny']
# print
# kelly kelly kelly
# alan alan alan
# jeny jeny jeny
#
# for i in names:
#     for j in range(1,4):
#         print(i,end=" ")
#     print()


n=[1,2,3]
q=['what','when','why']
# print
# 1
# what when why
# 2
# what when why
# 3
# what when why
# for i in n:
#     print(i)
#     for j in q:
#         print(j,end=" ")
#     print()


# d=[{'id':101,'name':'arun','age':23},{'id':102,'name':'amal','age':24},{'id':103,'name':'anu','age':25}]
# print each student details
# id name age


# print('id','name','age')
# for i in d:
#     for j in i.values():
#      print(j,end=" ")
#     print()


#prime only
# l=[23,45,78,90,12,13,91]
# for i in l:
#       for j in range(2,i):
#         if i%j==0:
#          break
#       else:
#            print(i,end=" ")




#find all prime numbers in range(1,100)

for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")

# find all armstrong numbers in range(100,1000)

for i in range(100,1001):
    sum = 0
    for j in str(i):
        sum=sum+int(j)**3
    if sum==i:
        print(i)


l=[23,45,78,90,12,13,91]

for i in l:
    for j in range(2,i):
        if i%j==0:
            break
    else:
      print(i)



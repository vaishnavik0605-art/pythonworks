# *
# **
# ***
# ****

# for i in range(1,5):    ###row
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()

# *
# ***
# *****
# *******

# for i in range(1,8,2):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()


# 1
# 22
# 333
# 4444

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()


# 1
# 12
# 123
# 1234

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# ****
# ***
# **
# *
#
# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()

# for i in range(4,0,-1):
#     for j in range(i):
#         print('*',end=" ")
#     print()


# for i in range(4,0,-1):
#     print("* " * i)
#
# for i in range(1,5):
#     print('* ' *i)


# for i in range(1,15,3):
#    for j in range(1,i+1):
#        print('*',end=" ")
#    print()



# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# for i in range(1,5):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()


# * * * *
# * * *
# * *
# *
# for i in range(4,0,-1):
#     for i in range(1,i+1):
#         print("*",end=" ")
#     print()

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


# A
# B C
# D E F
# G H I J

# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()


# A
# A B
# A B C
# A B C D

# for i in range(1,5):
#     k = ord('A')
#     for j in range(i):
#         print(chr(k),end=" ")
#         k=k+1
#     print()

# A
# B B
# C C C
# D D D D

# k = ord('A')
# for i in range(1,5):
#     for j in range(i):
#         print(chr(k),end=" ")
#     k=k+1
#     print()


# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4

# for i in range(1,5):
#     for j in range(1,5):
# #         print(i,end=" ")
# #     print()
#


# 1 0 0 0
# 0 2 0 0
# 0 0 3 0
# 0 0 0 4
#
#
# for i in range(1,5):
#     for j in range(1,5):
#         if i==j:
#          print(i,end=" ")
#         else:
#          print('0',end=" ")
#     print()
# print('\n')
#

# 0
# 0 1
# 0 1 0
# 0 1 0 1
#
# for i in range(1,5):
#     for j in range(1,i+1):
#         if j%2==0:
#          print(1,end=" ")
#         else:
#          print('0',end=" ")
#     print()

# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4
#
# for i in range(1,5):
#     for j in range(i+1):
#          print(j,end=" ")
#        # else:
#        #   print('0',end=" ")
#     print()

# h
# h e
# h e l
# h e l l
# h e l l o


# s='hello'
# for i in range(1,6):
#     for j in range(i):
#         print(s[j], end=" ")
#     print()


# h
# h a
# h a i
# h a i
# h a i   m
# h a i   m a
#
# s='hai mam'
# for i in range(1,7):
#     for j in range(0,i):
#         print(s[j], end=" ")
#     print()
#
#       *
#     * *
#   * * *
# * * * *


# k=6
# for i in range(1,5):
#     for p in range(k):
#         print(end=" ")
#     for j in range(i):
#         print('*',end=" ")
#     k=k-2
#     print()

#        1
#      2 2
#     3 3 3
#    4 4 4 4


# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print(i,end=" ")
#     k=k-1
#     print()

# * * *
# * *
# *
#
# k=2
# for i in range(3,0,-1):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(i):
#         print('*',end=" ")
#     k=k+2
    # print()
#



#       *
#     * *
#   * * *
# * * * *
#   * * *
#     * *
#       *
#
# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print('*',end=" ")
#     k=k-2
#     print()
#
# k = 2
# for i in range(3, 0, -1):
#     for p in range(1, k + 1):
#         print(end=" ")
#     for j in range(1, i + 1):
#         print('*', end=" ")
#     k = k + 2
#     print()

#      *
#     *  *
#   *  *  *
# *  *  *  *
#
# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print('*',end="  ")
#     k=k-2
#     print()

#      1
#     1   2
#   1   2   3
# 1   2   3   4
#   1   2   3
#     1   2
#       1

# k=6
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print(j,end="   ")
#     k=k-2
#     print()
# k=2
# for i in range(3,0,-1):
#     for p in range(1, k+ 1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print(j,end="   ")
#     k=k+2
#     print()



####11111
# 2222
# 333
# 44
# 5


# for i in range(1,6):
#     for j in range(6-i):
#         print(i,end=" ")
#     print()


# for i in range(1,6):
#     for j in range(6-i):
#         print(i,end=" ")
#     print()

# 11111
# 2222
# 333
# 44
# 5

# for i in range(1,6):
#     for j in range(6-i):
#         print(i,end=" ")
#     print()





# 1 2 3 4
# 1 2 3
# 1 2
# 1

for i in range(1,6):
    for j in range(1,6-i):
        print(j,end=" ")
    print()

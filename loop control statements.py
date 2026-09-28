# s="hello"
# for i in s:
#     print(i)


# 3using break
# s="morning"
# for i in s:
#     if(i=="r"):
#         break
#     print(i)


#using continue
# s="language"
# for i in s:
#     if(i=="g"):
#         continue
#     print(i)

#given a list of numbers
l=[25,67,34,78,17,44,82]
#print all numbers
# for i in l:
#     print(i)
#
#stop the loop when i>50
# for i in l:
#     if i>50:
#         break
#     print(i)

#skip all the even numbers
# for i in l:
#     if i%2==0:
#         continue
#     print(i)

#2. Given a list
colors=['red','green','yellow','blue','orange','black']
#print all colors
# for i in colors:
#     print(i)


#print those colors starting with 'b' #blue black
# for i in colors:
#     if i[0]=="b":
#      print(i)


#print the first color starting with 'b' #blue
# for i in colors:
#     if i[0]=="b":
#         break
# print(i)

#skips all colors starting with 'b'
# for i in colors:
#     if i[0]=="b":
#         continue
#     print(i)


# Given
s="python coding is easy and fun"

# print all characters upto a specific character(including that character)
for i in s:
    print(i, end=" ")
    if i=="f":
      break



# #using pass
# for i in range(1,11):
#     pass
# print(i)

#for else
# for i in range(1,6):
#     print(i)
# else:
#     print('hello')


# break
# for i in range(1,6):
#     if i==4:
#         break
#     print(i)
# else:# it works only after the the normal execution thats after completing the loop
#     print('hello')

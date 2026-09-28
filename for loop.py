#for

# s="morning"
# for i in s:
#     print(i)
#
# l=[2,3,4,5]
# for i in l:
#     print(i)

# t=('hello','bunny')
# for i in t:
#     print(i)

# t=(5,8,4,2,2)
# for i in t:
#     print(i)

# s={'a','b'}
# for i in s:
#     print(i)

#


#given a list

# l=[12,34,56,45,89,16,69,33]
# # print each numbers in a list
# for i in l:
#     print(i)

# print even numbers
# for i in l:
#     if i%2==0:
#        print(i)



# print those numbers divisibly by 5
# for i in l:
#     if i%5==0:
#        print(i)

# print those numbers that contains digit 3
# for i in l:
      # s=str(i)
  # if '3' in str(i):
        # print(i)



#given a string
s="hello world"
# peint each characters
# for i in s:
#     print(i)


# print those characters that are not vowel
# v='a','e','i','o','u'      v='aeiou'
# for i in s:
#     if i not in v:
#         print(i)


# #given a dictionary
# d={'n1':23,'n2':46,'n3':89,'n4':24}
# print each value
# for i in d.values():
#     print(i)
# print odd values
# for i in d.values():
#     if i%2!=0:
#       print(i)

# #given a list
# l=['red','green','orange','blue','black','yellow']
# print each colour
# for i in l:
#     print(i)


# print colour starting with 'b'
# for i in l:
#     if i[0]=='b':
#      print(i)

# print colours whose length is greater than 5
# print("colours greater than 5")
# for i in l:
#     if len(i)>5:
#      print(i)



# Given a list
# l=[10,'arun','amal',35,3.6,6.9,89]
# print  string values
# for i in l:
#     if type(i)==str:
#         print(i)

# print float values
# for i in l:
#     if type(i)==float:
#         print(i)




# l=[45,78,90,12,67]
#sum of list
# sum=0
# for i in l:
#     sum=sum+i
# print("sum",sum)


#product of even values

# product=1
# for i in l:
#     if i%2==0:
#      product=product*i
# print(product)

# #count odd values
# count=0
# for i in l:
#     if i%2!=0:
#         count=count+1
# print(count)



#range
#1,3,5,7,9
# for i in range(1,10,2):
#     print(i,end=" ")
#     print()
# #2,4,6,8,10
# for i in range(2,11,2):
#     print(i,end=" ")
# #1,4,9,16,25
#
# for i in range(1,6):
#     print(i*i,end=" ")

#4,9,14,19,24,29,34,39
# for i in range(4,40,5):
#     print(i,end=" ")
#5,4,3,2,1
# for i in range(5,0,-1):
#     print(i,end=" ")
#8,6,4,2,0
# for i in range(8,-1,-2):
#     print(i,end=" ")
# #7.4,21,28,35,42
# for i in range(7,43,7):
#     print(i,end=" ")



#for loop
#100,200,300,....1000
# for i in range(100,1001,100):
#     print(i)
#
# #1,8,27,64,125
# for i in range(1,6):
#     print(i*i*i,end=" ")  #(i**3)
#     print("\n")
#
# #find all 3 digit numbers that are divisible by 3
# for i in range(100,1000):
#     if i%3==0:
#         print(i,end=" ")
#         print()
#
# colors=['red','green','blue','yellow','black']
# # reverse of each color
# for i in colors:
#     print(i[::-1])



#print each digit in a number
# n=1234
# for i in str(n):
#     print(i)


#sum pf digits in a number
# n=1234
# sum=0
# # for i in range(1,5):
# #
# #     sum=sum+i   sum=sum+int(i)
# #     print(sum)
#
# for i in str(n):
#     sum=sum+int(i)
# print(sum)


#given a list
l=[1,2,3,4]
# # print squares of ecah number
# for i in l:
#     print(i**2)

# 3create a new list with square of each numbers[1,4,9,16]
# new=[]
# for i in l:
#     new.append(i**2)
#     print(i,"iteration",new)
# print(new)

#set
# new=set()
# for i in l:
#     new.add(i**2)
#     print(i,"iteration",new)
# print(new)

# given a string
# s="hello world"
# # create a new string with only vowels
# new=""
# v='aeiou'
# for i in s:
#     if i in v:
#         new=new+i
# print(new)


#given a list
# l=[1,2,3,4]
# # create a new dictionary where keys are numbers and values of square of each number
# #new->{1:1,2:4,3:9,4:16}  dictionary[keyname]=value
# new={}
# for i in l:
#     new[i]=i**2
# print(new)
# new={i:i**2 for i in l}
# print(new)

#reverse of a string
# s="hello"
# rev=""
# for i in s:
#     rev=i+rev
# print("reverse:",rev)

#rev of a number
# n=1234
# rev=""
# for i in str(n):
#     rev=i+rev
# print("reverse:", rev)


#
# #another method
# n=1234
# s=str(n)
# rev=""
# for i in s:
#     rev=i+rev
# print("reverse:", rev)

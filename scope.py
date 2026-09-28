##############global############

# x=20     #global can be used anywhere in the prgrm
# print("outside fn",x)
# def f():
#     print("inside fn", x)
# f()


###########local###############

# def f():
#     x=20
#     print("inside fn", x)
# f()
#
# print("outside fn",x)   # NameError: name 'x' is not defined bcz local only use inside the fn
                           # when it declared inside

###part2#######

# def f():
#     global x #used to change the local scope into global
#     x=20
#     print("inside f fn", x)
#
#
# def g():
#     y=30
#     print(x)   # here in th above f fn x is globally declared so that we can use it here too
#     print("inside g fn",y)
# f()
# g()


##############nonlocal/enclosed###########
###nested fun
# def outer():
#     x=10  ####### nonlocal/enclosed it can be use both inner and outer fn
#     print("outer",x)
#     def inner():
#        y=23  ##local
#        print("inner",x)
#     return
# inner()
# outer()


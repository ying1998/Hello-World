def inner_peace(game , food):
    print " Life is %s and %s " %(game,food)

inner_peace("zork","bread")

a= "zork"
b="bread"
inner_peace(a,b)

c= "zo"
d="rk"
e="bread"
inner_peace(c+d,e)

list1 = ["zork","bread"]
inner_peace(*list1)
inner_peace(list1[0],list1[1])

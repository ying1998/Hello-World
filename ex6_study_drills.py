# make a new variable x equal "There are %d types of people."  %d = 10
x = "There are %d types of people." %10

# make a new variable binary equal "binary"
binary = "binary"

# make a new variable do_not equal "don't"
do_not = "don't"

# make a new variable y equal "Those who know %s and those who %s."%(binary, do_not)  1st  %s=binary  2nd%s=do_not
y = "Those who know %s and those who %s."%(binary, do_not)

print x
print y 
# print "I said: 'There are 10 types of people.'."
print "I said: %r."%x
# print "I also said :'Those who know binary and those who don't.'."
print "I also said :'%s'." %y

hilarious = False
# create a new variable and it isn't single
joke_evaluation = "Isn't that joke so funny?! %r"
# print "Isn't that joke so funny?! False"
print joke_evaluation % hilarious

# print "This is the left side of ...a string with a right side."
w = "This is the left side of ..."
e = "a string with a right side."

print w+e


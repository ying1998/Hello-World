
from sys import argv
#TWO Variable >>argv
script,filename = argv
#open  the file and connect txt with the file
txt = open(filename)

print "Here's your file %r:" %filename
#read txt and print for us
print txt.read() 

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

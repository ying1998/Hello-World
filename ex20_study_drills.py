from sys import argv
# 两个变量
script,input_file = argv 
# 一个函数显示f的内容
def print_all(f):
      print f.read()
# seek() 方法用于移动文件读取指针到指定位置。
def rewind(f):
       f.seek(0)
# 使用readline方法逐行读取
def print_a_line(line_count,f):
       print line_count , f.readline()

current_file = open(input_file)

print "First let's print the whole file : \n"

print_all(current_file)

print "Now let's rewind,kind of like a tape."

rewind(current_file)

print "let's print three lines: "

current_line = 1
print_a_line(current_line,current_file)
print current_line

current_line = current_line+1
print_a_line(current_line,current_file)
print current_line

current_line = current_line +1
print_a_line(current_line,current_file)
print current_line

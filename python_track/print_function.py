'''
print function in python 3 returns None and prints into file(standard output)
The parameters of print function

objects - since everything in python is object
sep - used to seperate values passed to the print function. by default it is a white space
end - used to add ending string
file - used when writing on or over a file
flush - used to set either a flushed or a buffered output

'''
print(3,4,5,[4,5],(3,4),"buna") # takes multiple parameters and print them in one line with white space difault separator
# output
# 3 4 5 [4,5] (3,4) buna
print(3,4,5,[4,5],(3,4),"buna",sep='#') # uses to separate the values by #
# output
#3#4#5#[4,5]#(3,4)#buna
print(3,4,5,[4,5],(3,4),"buna",sep='#',end='Abrish') # add string at the end of the printed string
# output
#3#4#5#[4,5]#(3,4)#bunaabrish
# my_file = open('python_track/simple.txt','r')
# print(my_file.read(),3, 4, 5, [4,5], (3,4),"buna", sep='#', end='Abrish')
import sys
print('kebede','lemma','muktar',file=sys.stderr)  # printing to sys.stderr == system standard error
#output as error with red color
# kebede lemma muktar
"""print function implemetation"""
def custom_print(*args):
    pass



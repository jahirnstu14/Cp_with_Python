# https://leetcode.com/problems/goal-parser-interpretation/

# one solution

# def interpret(command):
#
#     command_new1 = command.replace("()","o")
#     command_new2 = command_new1.replace("(al)","al")
#     return command_new2
    
        
# command = input()
# newthing = interpret(command)

# print(newthing)


# second solution using dictionary

def interpret(command):

    d = {'G':'G','()':'o','(al)':'al'}

    temp = ''
    res = ''

    for x in command:
        temp+=x
        if temp in d:
            res+=d[temp]
            temp=''
    return res

command = input()
newthing = interpret(command)

print(newthing)
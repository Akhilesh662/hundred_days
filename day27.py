'''
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.

'''

string = "([])[]({})"



def check(string):
    print(string)
    stack = []
    maps = {"}":"{","]":"[",")":"("}
    for i in range(len(string)):
        if string[i] in ("]",")","}"):
            if stack:
                popped = stack.pop()
                if maps[string[i]]!= popped:
                    return False
            else:
                return False
        else:
            stack.append(string[i])
    return len(stack)==0


print(check(string))
print(check("(([])[]({}))"))
print(check("([]){}"))
print(check("([]})"))
print(check("([)]"))

"""
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
"""
from collections import Counter


def checkValidString( s):
    parentheses_count = Counter(s)
    while parentheses_count["("] != parentheses_count[")"] and parentheses_count["*"] > 0:
        if parentheses_count["("] < parentheses_count[")"]:
            parentheses_count["("] += 1
            parentheses_count["*"] -= 1
        else:
            parentheses_count[")"] += 1
            parentheses_count["*"] -= 1
    else:
        if parentheses_count["("] == parentheses_count[")"]:
            return True
        return False

print(checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
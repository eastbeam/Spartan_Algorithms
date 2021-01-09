from collections import deque

balanced_parentheses_string = "()))((()"

def is_correct_parentheses(string):
    stack = []
    for s in string:
        if s == "(":
            stack.append(s)
        else:
            stack.pop()

    return len(stack) == 0

# 1. 입력이 빈 문자열인 경우 
def change_to_correct_parenthesis(string):


def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parentheses(balanced_parentheses_string):
        return balanced_parentheses_string
    else:

    return


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!
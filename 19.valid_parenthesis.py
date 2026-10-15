# Challenge - determine if a string contains valid parenthesis
# The valid parentheses are: ( , ) , { , } , [ , ] 
# A input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.

# eg. '()[]{}' - result = True 

import re

def is_valid(s):
    # remove everthing but brackets including spaces: 
    onlyBrackets = re.sub(r'[^()\[\]{}]', '', s)

    # To keep track of brackets that are opened and the order of opening
    openBracks = ''

    for b in onlyBrackets:
        # If open brackets add to openBracks
        if b in '({[':
            openBracks += b

        # If closing bracket see if it matches open bracket order:
        else: 
            # if there is a close bracket and no open brackets not valid
            if len(openBracks) == 0:
                return False
            
            if (b == '}' and openBracks[0] == '{'):
                # Remove bracket if match as it has a pair in correct order
                openBracks = openBracks[1:]

            elif (b == ')' and openBracks[0] == '('):
                # Remove bracket if match as it has a pair in correct order
                openBracks = openBracks[1:]

            elif (b == ']' and openBracks[0] == '['):
                # Remove bracket if match as it has a pair in correct order
                openBracks = openBracks[1:]
            
            # else the openning bracket does not match close order
            else: 
                return False
    
    # if there is nothing in open bracket
    if len(openBracks) == 0 :
        return True

    # else there was no closing brackets:
    else:
        return False



if __name__ == "__main__":
    print(is_valid('()[]{}'))  # True - right brackets and order
    print(is_valid('()[)]{}'))  # False - mismatch brackets
    print(is_valid('}])'))  # False - only closing pairs
    print(is_valid('({['))  # False - only opening pairs
    print(is_valid('([)]{}'))  # True - closed in order
    print(is_valid('([]{})'))  # False - closed out of order
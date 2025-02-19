import stackLinkedList

def get_open_parenthese(c):
    if c == '}':
        return '{'
    elif c == ']':
        return '['
    elif c == ')':
        return '('
    
    return ' '

def is_valid_paratheses(s):
    stack = stackLinkedList.Stack()    

    for c in s:
        if c in '[{(':
            stack.push(c)
        else:
            if stack.get_size() == 0 or get_open_parenthese(c) != stack.pop():
                return False

    return stack.get_size() == 0

if __name__ == '__main__':    

    s = "[()]{}{[()()]()}"
    #s = "[(])"

    print(is_valid_paratheses(s))

    

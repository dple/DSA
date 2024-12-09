"""
Implement two stacks using ONLY one array
"""

MAX_SIZE = 100

class TwoStacks:
    def __init__(self, size = 2*MAX_SIZE):
        self.stacks = [0]* size
        self.size1 = 0
        self.size2 = 0
    
    
    def is_stack1_empty(self):
        return self.size1 == 0
    
    def is_stack2_empty(self):
        return self.size2 == 0
    
    def get_stack1_size(self):
        return self.size1
    
    def get_stack2_size(self):
        return self.size2
    
    # Elements of stack 1 will be stored in the even positions of the list
    def push1(self, value):        
        self.stacks[2*self.size1] = value   #.insert(2*self.size1, value)
        self.size1 += 1

    # Elements of stack 2 will be stored in the odd positions of the list
    def push2(self, value):        
        self.stacks[2*self.size2 + 1] = value
        self.size2 += 1

    def pop1(self):        
        res = self.stacks[2*self.size1]
        self.stacks[2*self.size1] = 0
        self.size1 -= 1
        return res

    def pop2(self):        
        res = self.stacks[2*self.size2 + 1]
        self.stacks[2*self.size2 + 1] = 0
        self.size2 -= 1
        return res

    def print_stack1(self):
        print("Stack1 :", end="")
        res = ""
        for i in range(self.size1):
            res += str(self.stacks[2*i]) + "->"
        
        print(res[:-2])

    def print_stack2(self):
        print("Stack2 :", end="")
        res = ""
        for i in range(self.size2):
            res += str(self.stacks[2*i + 1]) + "->"
        
        print(res[:-2])

    def print_stacks(self):
        self.print_stack1()
        self.print_stack2()

if __name__ == '__main__':
    twostacks = TwoStacks(10)
    twostacks.push1('a')
    twostacks.push1('b')
    twostacks.push1('c')

    twostacks.push2(1)
    twostacks.push2(2)
    twostacks.push2(3)
    twostacks.push2(4)

    twostacks.print_stack1()
    twostacks.print_stack2()
    twostacks.pop1()
    twostacks.pop2()
    twostacks.print_stacks()
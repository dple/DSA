MAX_SIZE = 1000

class KStacks:

    def __init__(self, k = 1, n = MAX_SIZE):
        self.k = k
        self.n = n
        self.stacks = [0] * (k * n)
        self.sizes = [0] * k

        self.free = 0

    def is_full(self):
        return self.free == -1

    def is_empty(self, stack_number):
        
        return self.sizes[stack_number] == 0
    
    def push(self, value, stack_number):
        if self.is_full():
            raise Exception("The stack is full!")
        
        self.stacks[self.sizes[stack_number]*self.k + stack_number] = value 
        self.sizes[stack_number] += 1

    def pop(self, stack_number):
        
        res = self.stacks[self.k * (self.sizes[stack_number] - 1)  + stack_number]
        self.stacks[self.k * (self.sizes[stack_number] - 1)  + stack_number] = 0
        self.sizes[stack_number] -= 1
    
        return res 
    
    def printstack(self, stack_number):        
        res = ""
        for i in range(self.sizes[stack_number]):
            res += str(self.stacks[self.k * i + stack_number]) + "->"
        
        print(res[:-2])

if __name__ == '__main__':
    # Create 3 stacks using an 
    # array of size 10.
    kstacks = KStacks(3, 10)

    # Push some items onto stack number 2.
    kstacks.push(15, 2)
    kstacks.push(45, 2)

    # Push some items onto stack number 1.
    kstacks.push(17, 1)
    kstacks.push(49, 1)
    kstacks.push(39, 1)

    # Push some items onto stack number 0.
    kstacks.push(11, 0)
    kstacks.push(9, 0)
    kstacks.push(7, 0)

    print("Popped element from stack 2 is " + str(kstacks.pop(2)))
    print("Popped element from stack 1 is " + str(kstacks.pop(1)))
    print("Popped element from stack 0 is " + str(kstacks.pop(0)))

    kstacks.printstack(0)
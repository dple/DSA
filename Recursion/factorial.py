class Factorial:
    def recur(self, num):        
        if num == 1:
            return 1
        else:            
            return num * self.recur(num-1)        

if __name__ == '__main__':
    fac = Factorial()
    n = 10
    print("Factorial of ", n, "is: ", fac.recur(n))
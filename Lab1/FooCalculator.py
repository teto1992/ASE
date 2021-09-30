import lab1 as c

class FooCalculator:

    def __init__(self):
        pass

    def sum(self, m, n):
        return c.sum(m,n)
    
cal = FooCalculator()
print(cal.sum(3,2))

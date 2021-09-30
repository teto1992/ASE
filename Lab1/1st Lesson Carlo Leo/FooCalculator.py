import calculator as c

class FooCalculator:
    def __init__(self):
        pass

    def sum(self,m,n):
        return c.sum(m,n)
   
    def divide(self,m,n):
        return c.divide(m,n)

if __name__ == "__main__":
    obj = FooCalculator()
    print("7 - 77 " + str(obj.sum(7,-77)))
    print("17 / 3 " + str(obj.divide(8,3)))
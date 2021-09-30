#calculator.py

def sum(m,n):
    s = m
    step = 1 if(n > 0) else -1
    for i in range(abs(n)):
        s += step
    return s

def divide(m,n):
    if n == 0:
        raise Exception("cannot divide for 0")
    t = n * -1 if n < 0  else n
    p = m * -1 if m < 0 else m
    r = p - t
    i = 0
    while r >= 0:
        r -= t
        i += 1
   
    return i if n * m > 0  else i * -1

if __name__ == "__main__":
    print("5 + 5  = " + str(sum(5,5)))
    print("8 / -4 = " + str(divide(8,-4)))
# calculator.py

def sum(m,n):
    result = m
    if n < 0:
        for i in range(abs(n)):
            result -= 1
    else:
        for i in range(n):
            result += 1

    return result


def divide(m,n):
    res = 0;
    negativeRes = m > 0 and n < 0 or m < 0 and n > 0;

    n = abs(n);
    m = abs(m);

    if(n == 0):
        raise ZeroDivisionError;

    while (m - n >= 0):
        m -= n;
        res += 1;

    res = -res if negativeRes else res;

    return res;

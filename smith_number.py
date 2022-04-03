def digitSum(n):
    sum = 0
    while n>0:
        sum+=n%10
        n//=10
    return sum

def primeFactors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d = d + 1
        if d*d > n:
            if n > 1:
                factors.append(n)
            break
    return factors

def primeFactorSum(ls):
    return sum(digitSum(i) for i in ls)

def isSmithNumber(n):
    return digitSum(n) if digitSum(n)==primeFactorSum(primeFactors(n)) else -1
n = int(input())
print(isSmithNumber(n))
import itertools

def permutations(n):
    remainder = n
    total = 1
    if n == 0:
        return 0
    else:
        while remainder > 1:
            total = total * remainder
            remainder -= 1
    return total

def choose(n, k):
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0
    
if __name__ == '__main__':
    n = int(raw_input())
    l = list(map(int, raw_input().split()))
    ll = itertools.permutations(l)
           
    total = 0
    remainder = len(l)
    while remainder > 1:
        a = l[0]
        b = l[1]
        l.remove(b)
        l[0] = a + b + a*b
        remainder -= 1
    total += l[0]

    print total % 1000000007

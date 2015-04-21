def modified_fib_sequence(a, b, n):
    count = 2
    while count <= n:
        a, b = b, b*b + a
        count += 1
    return a

modified_fib_sequence(0, 1, 5)

if __name__ == '__main__':
    
    a, b, n = list(map(int, raw_input().split()))
    print modified_fib_sequence(a, b, n)

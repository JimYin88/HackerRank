def find_digits(n):
    count = 0
    s = str(n)
    for i in s:
        if int(i) == 0:
            count = count
        elif n % int(i) == 0:
            count += 1
        else:
            count = count
    print count
        

if __name__ == '__main__':
    T = int(raw_input())

    for _ in range(T):
        N = int(raw_input())
        find_digits(N)

def slices_of_cakes(n):
    if n <= 1:
        return 0
    elif n % 2 == 0:
        return n*n/4
    else:
        return (n + 1)*(n - 1)/4

if __name__ == '__main__':
    
    T = int(raw_input())
    
    for x in range(T):
        cuts = int(raw_input())
        print slices_of_cakes(cuts)

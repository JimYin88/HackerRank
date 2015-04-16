def utopian_tree(n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return  utopian_tree(n-1) + 1
    else:
        return utopian_tree(n-1) * 2
    
if __name__ == '__main__':
    
    T = int(raw_input())
    
    for x in range(T):
        N = int(raw_input())
        print utopian_tree(N)

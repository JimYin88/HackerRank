if __name__ == '__main__':
    
    N = int(raw_input())
    
    orders = []
    for i in range(1, N+1):        
        t, d = list(map(int, raw_input().split()))
        orders.append((i, t+d))
    
    orders = sorted(orders, key = lambda x: (x[1], x[0]))
    
    for order in orders:
        print order[0],

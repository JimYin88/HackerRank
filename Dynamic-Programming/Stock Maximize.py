if __name__ == '__main__':
    T = int(raw_input())
    
    for _ in range(T):        
        N = int(raw_input())
        prices = list(map(int, raw_input().split()))
        
        profit = 0
        max_prices = prices[-1]
        
        for i in range(N-1, 0, -1):
            if prices[i-1] > max_prices:
                max_prices = prices[i-1]
            profit += max_prices - prices[i-1]
                
        print profit

if __name__ == '__main__':
    
    n, k = list(map(int, raw_input().split()))
    costs = sorted(list(map(int, raw_input().split())), reverse=True)
    
    total = 0
    for i, items in enumerate(costs):        
        total += (i // k + 1) * items
        
    print total

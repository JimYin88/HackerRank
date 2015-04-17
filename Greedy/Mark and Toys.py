if __name__ == '__main__':
    
    n, k = list(map(int, raw_input().split()))
    prices = sorted(list(map(int, raw_input().split())))
    
    count = 0
    amount = k
    for item in prices:
        if item > amount:
            break
        else:
            count += 1
            amount -= item
            
    print count

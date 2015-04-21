def coin_change(n, coins_available, coins_so_far):
    if sum(coins_so_far) == n:
        yield coins_so_far
    elif sum(coins_so_far) > n:
        pass
    elif coins_available == []:
        pass
    else:
        for c in coin_change(n, coins_available[:], coins_so_far+[coins_available[0]]):
            yield c
        for c in coin_change(n, coins_available[1:], coins_so_far):
            yield c
            
            
            
if __name__ == '__main__':
    
    n, m = list(map(int, raw_input().split()))
    coins = list(map(int, raw_input().split()))
    
    solutions = coin_change(n, coins, [])
    count = sum([1 for x in solutions])
    print count

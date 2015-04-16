N = input()
K = input()
lists = [input() for _ in range(0,N)]
lists.sort()

def min_difference(a, n):
    results = 1000000000000
    for i in range(len(a) - n):
        difference = a[i+n-1]-a[i]
        if difference < results:
            results = difference
    return results        

print min_difference(lists, K)

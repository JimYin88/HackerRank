import collections

if __name__ == '__main__':
    
    n = int(raw_input())
    A = collections.Counter(list(map(int, raw_input().split())))
    m = int(raw_input())
    B = collections.Counter(list(map(int, raw_input().split())))
    
    result = []
    
    for i in A:
        if i not in B:
            result.append(i)
        elif A[i] < B[i]:
            result.append(i)
    
    for j in result:
        print j,

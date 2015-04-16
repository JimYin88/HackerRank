import operator

if __name__ == '__main__':
    L = int(raw_input())
    R = int(raw_input())
    
    max_result = 0
    for i in range(L, R + 1):
        for j in range(L, R + 1):
            result = operator.xor(i, j)
            if result > max_result:
                max_result = result
    print max_result

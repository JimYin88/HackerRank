if __name__ == '__main__':
    
    N = int(raw_input())
    
    x_list = []
    y_list = []
    
    for _ in range(N):
        x, y = list(map(int, raw_input().split()))
        x_list.append(x)
        y_list.append(y)
        
    print min(x_list) * min(y_list)

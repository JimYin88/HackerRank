if __name__ == '__main__':
    
    N = int(raw_input())
    W = sorted(list(map(int, raw_input().split())))
    
    weight_limit = ""
    count = 0
    
    for i in W:
        if weight_limit == "":
            count += 1
            weight_limit = i + 4
        elif i > weight_limit:
            count += 1
            weight_limit = i + 4
        else:
            continue
            
    print count  

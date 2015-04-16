if __name__ == '__main__':
    
    N = int(raw_input())
    A = map(int, raw_input().split())
    
    list1 = A
    while len(list1) > 0:
        print len(list1)
        list1 = [x - min(list1) for x in list1 if x - min(list1) > 0]

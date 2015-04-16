if __name__ == '__main__':

    T = int(raw_input())

    for _ in range(T):
        n = int(raw_input())
        a = int(raw_input())
        b = int(raw_input())
        
        list1 = sorted(set([x * a + (n - 1 - x) * b for x in range(n)]))
        
        if n == 0:
            print 0
        for i in range(len(list1)):
            if i == len(list1)-1:
                print list1[i]
            else:
                print list1[i],

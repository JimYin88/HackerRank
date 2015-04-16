def kaprekar_number(n):
    if n == 1:
        return True
    elif n < 5:
        return False
    else:
        d = len(str(n))
        square = n*n
        if int(str(square)[:-d]) + int(str(square)[-d:]) == n:
            return True
        else:
            return False

if __name__ == '__main__':

    p = int(raw_input())
    q = int(raw_input())

    list1 = [x for x in range(p, q + 1) if kaprekar_number(x)]

    if list1 == []:
        print 'INVALID RANGE'
    else:
        for i in list1:
            print i,

def triangle_number(nrow):
    if nrow == 1:
        return [1]
    elif nrow == 2:
        return [1, 1, 1]
    oldrow = [1, 1, 1]
    x = 3
    while x <= nrow:
        newrow = [0] * (2 * x - 3)
        for i in range(2 * x - 3):
            if i == 0:
                newrow[i] = oldrow[i] + oldrow[i+1]
            elif i == 2 * x - 4:
                newrow[i] = oldrow[i] + oldrow[i-1]
            else:
                newrow[i] = oldrow[i-1] + oldrow[i] + oldrow[i+1]
        newrow = [1] + newrow + [1]
        oldrow = newrow
        x += 1
    return newrow

if __name__ == '__main__':
    T = int(raw_input())
    
    for _ in range(T):
        n = int(raw_input())
#        triangle = triangle_number(n)
        if n < 3:
            print -1
        elif n % 2 == 0:
            print(3 if (n // 2) % 2 == 0 else 4)
        else:
            print 2
                

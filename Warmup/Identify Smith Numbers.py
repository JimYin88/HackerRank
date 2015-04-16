def prime_factors(n):
    result = []
    remainder = n
    factor = 2
    while remainder > 1:
        if remainder % factor == 0:
            result.append(factor)
            remainder /= factor
        else:
            factor += 1            
    return result

def sum_of_digits(n):
    s = str(n)
    total = 0
    for i in s:
        total = total + int(i)
    return total
        
if __name__ == '__main__':
    
    T = int(raw_input())
    
    print '1' if sum_of_digits(T) == sum([sum_of_digits(x) for x in prime_factors(T)]) else '0'

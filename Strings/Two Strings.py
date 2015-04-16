import collections

if __name__ == '__main__':
    number_of_tests = int(raw_input().strip())
    
    for x in range(number_of_tests):
        A = raw_input().strip().lower()
        B = raw_input().strip().lower()
     
        a = collections.Counter(A) 
        b = collections.Counter(B)
     
        length = sum(min(a[c], b[c]) for c in (set(A) & set(B))) 
        print 'YES' if length > 0 else 'NO'

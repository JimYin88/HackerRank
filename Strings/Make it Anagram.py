import collections

if __name__ == '__main__':

    A = raw_input().strip()
    B = raw_input().strip()
     
    a = collections.Counter(A) 
    b = collections.Counter(B)
     
    length = sum(min(a[c], b[c]) for c in (set(A) & set(B))) 
    print (len(A) - length) + (len(B) - length)

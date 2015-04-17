import collections

A = raw_input()
a = collections.Counter(A) 
     
odd_count = 0
for key, value in a.iteritems():
    if value % 2 != 0:
        odd_count += 1
          
if odd_count > 1:
    print 'NO'
else:
    print 'YES'

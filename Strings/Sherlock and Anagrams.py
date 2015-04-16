import collections
 
if __name__ == '__main__': 
    T = int(raw_input()) 
     
    for _ in range(T): 
        S = raw_input().strip() 
 
        # Count the each sorted substring 
        substrings = (''.join(sorted(S[j : j + i])) for i in range(1, len(S)) for j in range(len(S) - i + 1))
        substrings = collections.Counter(substrings)

        # Count pairs for each set of anagrams 
        print sum(v * (v - 1) // 2 for v in substrings.values()) 

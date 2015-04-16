def palindrome_moves(s):
    if len(s) == 1:
        return 0
    elif len(s) % 2 == 0:
        result = 0
        for i in range(len(s)/2):
            result += abs(ord(s[i])-ord(s[-1-i]))
        return result
    else:
        result = 0
        for i in range((len(s)-1)/2):
            result += abs(ord(s[i])-ord(s[-1-i]))
        return result
    
if __name__ == '__main__':
    
    T = int(raw_input())
    
    for x in range(T):
        s1 = raw_input()
        print palindrome_moves(s1)

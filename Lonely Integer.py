def lonelyinteger(a):
    answer = []
    for i in a:
        if i not in answer:
            answer.append(i)
        else:
            answer.remove(i)
    return sum(answer)
    
if __name__ == '__main__':

    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)

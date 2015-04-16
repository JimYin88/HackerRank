T = int(raw_input())
for i in range (0,T):
    A,B,C1 = [int(x) for x in raw_input().split(' ')]
    
    answer = 0
    answer += int(A/B)
    wrapper = answer
    while wrapper >= C1:
        answer += int(wrapper/C1)
        wrapper = int(wrapper/C1) + (wrapper % C1)
    # write code to compute answer
    print answer

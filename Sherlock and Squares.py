import math

def number_of_squares(lower, upper):
    if math.sqrt(lower) == int(math.sqrt(lower)):
        return int(math.sqrt(upper)) - int(math.sqrt(lower)) + 1
    else:
        return int(math.sqrt(upper)) - int(math.sqrt(lower))

if __name__ == '__main__':

    N = int(raw_input())

    for _ in range(N):
        a, b = raw_input().split()
        a, b = int(a), int(b)
        print number_of_squares(a, b)

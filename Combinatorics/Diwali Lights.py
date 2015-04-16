if __name__ == '__main__':
    T = int(raw_input())
    
    for _ in range(T):
        n = int(raw_input())
        print(pow(2, n, 10**5) - 1)

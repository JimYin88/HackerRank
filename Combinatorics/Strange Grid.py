if __name__ == '__main__':

    r, c = map(int, raw_input().split())
    
    if r % 2 == 0:
        print ((r-1) // 2) * 10 + (c-1) * 2 + 1
    else:
        print ((r-1) // 2) * 10 + (c-1) * 2

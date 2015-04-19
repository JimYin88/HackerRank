if __name__ == '__main__':
    
    T = int(raw_input())
    
    for _ in range(T):
        Px, Py, Qx, Qy = (list(map(int, raw_input().split())))
        print Qx + Qx - Px, Qy + Qy - Py

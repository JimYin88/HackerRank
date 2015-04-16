from __future__ import print_function

if __name__ == '__main__':

    N = int(raw_input())
    A = [list(map(int, raw_input().strip())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == 0 or i == N - 1 or j == 0 or j == N - 1:
                print(A[i][j], end = '')
            elif A[i][j] > A[i - 1][j] and A[i][j] > A[i + 1][j] and A[i][j] > A[i][j - 1] and A[i][j] > A[i][j + 1]:
                print('X', end = '')
            else:
                print(A[i][j], end = '')
        print()


def diagonalDifference(arr):
    left_to_right_diagonal = 0
    right_to_left_diagonal = 0
    
    for i in range(n):
        left_to_right_diagonal += arr[i][i]
        right_to_left_diagonal += arr[i][n-1-i]
    print(abs(left_to_right_diagonal-right_to_left_diagonal))
    
        


if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)


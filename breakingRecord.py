def breakingRecords(scores):
    hihgest = 0
    lowest = 0
    highScore_arr = [scores[0]]
    lowScore_arr = [scores[0]]
    for i in range(1, len(scores)):
        if highScore_arr[len(highScore_arr)-1] < scores[i]:
            highScore_arr.append(scores[i])
            hihgest += 1
        if lowScore_arr[len(lowScore_arr)-1] > scores[i]:
            lowScore_arr.append(scores[i])
            lowest += 1

    print(hihgest, lowest)
        


if __name__ == '__main__':

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
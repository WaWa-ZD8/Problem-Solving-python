def plusMinus(arr):
    positive = []
    negative = []
    zero = []
    for i in arr:
        if i > 0:
            positive.append(i)
        elif i < 0:
            negative.append(i)
        elif i == 0:
            zero.append(i)

    print("{:.6f}".format(len(positive)/len(arr)))
    print("{:.6f}".format(len(negative)/len(arr)))
    print("{:.6f}".format(len(zero)/len(arr)))
 
            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
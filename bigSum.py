def aVeryBigSum(ar):
    add = 0
    for i in ar:
        add += i
    return add

if __name__ == '__main__':

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)
def simpleArraySum(ar):
    array_sum = 0
    for i in ar:
        array_sum += i
    return array_sum
if __name__ == '__main__':


    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)
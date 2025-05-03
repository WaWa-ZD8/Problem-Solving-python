def getMoneySpent(keyboards, drives, b):
    max_total = -1
    for keyboard in keyboards:
        for drive in drives:
            total = keyboard + drive
            if total <= b and total > max_total:
                max_total = total

    print(max_total)
if __name__ == '__main__':

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)
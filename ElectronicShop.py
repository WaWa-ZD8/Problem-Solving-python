def getMoneySpent(keyboards, drives, b):
    prices = []
    for keyboard in keyboards:
        for drive in drives:
            total = keyboard + drive
            if total <= b:
                prices.append(total)
            else:
                prices.append(-1)
    print(max(prices))
if __name__ == '__main__':

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)
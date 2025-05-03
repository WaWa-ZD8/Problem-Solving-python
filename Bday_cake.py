def birthdayCakeCandles(candles):
    x = candles.count(max(candles))
    return x
if __name__ == '__main__':

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

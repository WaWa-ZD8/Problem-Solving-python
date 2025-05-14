def beautifulDays(i, j, k):
    beautiful_days = 0
    for days in range(i, j+1):
        reversed_day = int(str(days)[::-1])
        difference = abs(days - reversed_day)
        
        if difference % k == 0:
            beautiful_days += 1
    print(beautiful_days)

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)
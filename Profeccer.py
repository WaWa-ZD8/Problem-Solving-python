def angryProfessor(k, a):
    threshold = 0
    for time in a:
        if time <= 0 :
            threshold += 1
            print(time)
    if threshold >= k:
        print ("NO")
    else:
        print ("YES")


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

# 2
# 4 3
# -1 -3 4 2
# 4 2
# 0 -1 2 1

# YES
# NO
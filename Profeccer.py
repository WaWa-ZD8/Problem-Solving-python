def angryProfessor(k, a):
    threshold = sum(1 for time in a if time <= 0)        
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

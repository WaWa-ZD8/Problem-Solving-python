def saveThePrisoner(n, m, s):
    chair_num = s-1
    end_no =(m % n + chair_num)%n
    if end_no == 0:
        print (n)
    
    print(end_no)

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    s = int(first_multiple_input[2])

    result = saveThePrisoner(n, m, s)

        
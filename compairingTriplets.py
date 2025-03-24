def compareTriplets(a, b):
    alice = 0
    bob = 0
    index_num = 0
    
    for i in range (3):
        if a[index_num] > b[index_num]:
            alice += 1
        elif a[index_num] < b[index_num]:
            bob += 1
        index_num += 1
    print(" ".join(map(str, [alice, bob])))
    

    
    

if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

from itertools import permutations

def divisibleSumPairs(n, k, ar):
    count = 0
    new_arr =list(permutations(ar, 2))
    for array in new_arr:
        if sum(array) % k == 0:
            count += 1
    print(count // 2)
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))


from collections import Counter

def migratoryBirds(arr):
    types = Counter(arr)
    maximum_amount = max(types.values())
    most_seen_types = [i for i in types if maximum_amount == types[i]]

    print(min(most_seen_types))
    

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
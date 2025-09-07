def appendAndDelete(s, t, k):
    count = 0
    total_len = len(s) + len(t)
    for i,j in zip(s, t):
        if i == j:
            count += 1
        else:
            break
    if total_len <= 2*count + k and total_len%2 == k%2 or total_len < k:
        print("Yes")
    else:
        print("No")
        

if __name__ == '__main__':

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)
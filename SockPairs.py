
def sockMerchant(n, ar):
    paires = 0
    for i in set(ar):
        socks = ar.count(i)
        if socks % 2 > 0 and socks > 1:
            paires += (socks - 1) // 2
        else:
            paires += (socks // 2)
    print(paires)
    
if __name__ == '__main__':

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))


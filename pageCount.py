def pageCount(n, p):
    if p == 0 or p == n:
        return 0
    return (min(p//2, (n-p)//2))

if __name__ == '__main__':

    n = int(input().strip())

    p = int(input().strip())
    if n%2 !=0:
        n-=1
    if p%2 !=0:
        p-=1
    result = pageCount(n, p)
    print (result)
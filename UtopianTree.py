def utopianTree(n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return 2**(n//2 + 1) - 1
    else:
        return 2**(n//2 + 2) - 2
if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

    

def viralAdvertising(n):
    day_likes = 2
    Cumulative = 0
    if n == 1:
        print(5//2)
    else:
        for _ in range (1,n):
            likes = (day_likes*3)//2
            day_likes = likes
            Cumulative += likes
    print(Cumulative + 2)
if __name__ == '__main__':
    n = int(input().strip())

    result = viralAdvertising(n)
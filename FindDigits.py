def findDigits(n):
    divisors = [nums for nums in str(n) if nums != str(0) and n % int(nums) == 0]
    print(len(divisors))
if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)
def bonAppetit(bill, k, b):
    payment = 0
    if bill[k] in bill:
        bill.remove(bill[k])
    for prices in bill:
        payment += prices
    
    if payment // 2 == b:
        print ("Bon Appetit")
    else:
        print(b - payment //2)
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
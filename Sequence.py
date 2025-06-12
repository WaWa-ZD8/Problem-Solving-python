def permutationEquation(p):
    p = list(p)
    new_list = []
    for i in range(1,n+1):
        place = p.index(i)+1
        new_list.append(p.index(place)+1) 
    

if __name__ == '__main__':

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)
    
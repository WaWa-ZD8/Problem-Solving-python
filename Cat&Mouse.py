
def catAndMouse(x, y, z):
    if abs((z-x)) < abs(z-y) :
        return("Cat A")
    elif abs(z-x) > abs(z-y) :
        return("Cat B")
    elif abs(z-x) == abs(z-y):
        return("Mouse C")

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])


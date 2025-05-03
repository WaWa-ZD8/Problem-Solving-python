def countingValleys(steps, path):
    valleys = 0
    sea_level = 0
    different_steps = {"U":1, "D":-1}  

    for step in path:
        sea_level += different_steps[step]
        if sea_level == 0 and step == "U":
            valleys += 1 
    
    print(valleys)
    
if __name__ == '__main__':

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)
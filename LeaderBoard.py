def climbingLeaderboard(ranked, player):
    ranked = sorted(set(ranked), reverse=True)  
    result = []
    i = len(ranked) - 1  

    for score in player:
        
        while i >= 0 and score >= ranked[i]:
            i -= 1
        result.append(i + 2)  

    print (result)
    
       
if __name__ == '__main__':
    

    ranked_count =  int(input().strip())
    
    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

# 7                                                    
# 100 100 50 40 40 20 10
# 4
# 5 25 50 120

# 6
# 4
# 2
# 1

# 6
# 100 90 90 80 75 60
# 5
# 50 65 77 90 102


# 6
# 5
# 4
# 2
# 1

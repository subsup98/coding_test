from itertools import permutations
def solution(k, dungeons):
    
    all_per =permutations(dungeons)
    max_du=0
    z= list(all_per)
    for per in z:
        hp=k
        count=0
        for min_hp,loss in per:
            if hp< min_hp:
                break
            else:
                count+=1
                hp -=loss
            max_du=max(max_du,count)
    return max_du1
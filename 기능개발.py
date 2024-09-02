def solution(progeresses, speeds):
    answer=[]
    while progeresses[0]<=100:
        progeresses=[progresse + speed for progresse, speed in zip(progresses,speeds)]
        if progresses[0]>= 100:
            over_100 =sum(x >= 100 for x in progresses)
            progresses
    return answer 
progresses=[93,30,55]
speeds=[1,30,5]

a=[progresse + speed for progresse, speed in zip(progresses,speeds)]
print(a)
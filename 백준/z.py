import sys
n,r,c = map(int,sys.stdin.readline().split())
answer = 0

while n !=0:
    n  -=1  #4등분하기 -> n-1이 딱 중간으로 나눔 n제곱으로 들어가니까
    # 1사
    if r < 2**n and c >=2 **n:
        answer += (2**n) * (2**n)*1
        c -= (2**n)
    # 2사
    elif r < 2**n and c<2**n:
        answer += (2**n) *(2**n) *0
    # 3사
    elif r>= 2**n and c< 2**n :
        answer += (2**n) *(2**n) * 2
        r -=(2**n)
    # 4사
    else:
        answer += (2**n)*(2**n)*3
        r -=(2**n)
        c -= (2**n)

print(answer)    

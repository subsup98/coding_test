from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer=[]
    for i in range(len(orders)):
        orders[i]=sorted(orders[i])
   
    orders=[''.join(order) for order in orders]
   
    for num in course:
        set_menu=[]
        for order in orders:
            comb=combinations(order,num)
            set_menu += comb
        comb_count=Counter(set_menu)
        if comb_count:
            max_order=max(comb_count.values())
            if max_order >1:
                for order, count in comb_count.items():
                    if count == max_order:
                        answer.append(''.join(order))
    return sorted(answer)
import sys
n,m = map(int,sys.stdin.readline().split())

pokemons=[0]
querys=[]
for i in range(1,n+1):
    pokemon = sys.stdin.readline().rstrip()
    pokemons.append(pokemon)
for j in range(m):
    query=sys.stdin.readline().rstrip()
    querys.append(query)

for query in querys:
    if query.isdigit():
        print(pokemons[int(query)])

    else:
        print(pokemons.index(query))
    


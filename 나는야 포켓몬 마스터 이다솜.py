import sys
n, m = map(int, sys.stdin.readline().split())
querys = []
pokemons_index = [0]  
pokemons_name = {} 


for i in range(1, n + 1):
    pokemon = sys.stdin.readline().rstrip()
    pokemons_index.append(pokemon)
    pokemons_name[pokemon] = i  

for j in range(m):
    query = sys.stdin.readline().rstrip()
    querys.append(query)

for query in querys:
    
    if query.isdigit():
        print(pokemons_index[int(query)])
    
    else:
        print(pokemons_name[query])

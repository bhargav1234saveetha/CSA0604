from itertools import permutations

def tsp_dp(cost):
    n=len(cost)
    if n < 2 or any(len(row)!=n for row in cost):
        raise ValueError("Cost matrix must be square and have at least two nodes")
    full=(1<<n)-1
    dp={(1,0):0}; parent={}
    for mask in range(1<<n):
        if not mask & 1: continue
        for last in range(n):
            if (mask,last) not in dp: continue
            for nxt in range(1,n):
                if mask & (1<<nxt): continue
                new=mask | (1<<nxt)
                candidate=dp[(mask,last)] + cost[last][nxt]
                if candidate < dp.get((new,nxt),float("inf")):
                    dp[(new,nxt)]=candidate; parent[(new,nxt)]=last
    best,last=float("inf"),None
    for j in range(1,n):
        value=dp[(full,j)] + cost[j][0]
        if value < best: best,last=value,j
    route=[last]; mask=full
    while last != 0:
        previous=parent[(mask,last)]
        mask ^= (1<<last); last=previous
        if last != 0: route.append(last)
    route.reverse()
    return best,[0]+route+[0],len(dp)

def tsp_exhaustive(cost):
    n=len(cost); best=float("inf"); best_route=None
    for order in permutations(range(1,n)):
        route=(0,)+order+(0,)
        value=sum(cost[route[i]][route[i+1]] for i in range(len(route)-1))
        if value < best: best,best_route=value,route
    return best,best_route

def run():
    cost=[[0,10,15,20,10,25,18],
          [10,0,35,25,17,28,20],
          [15,35,0,30,20,18,22],
          [20,25,30,0,16,14,24],
          [10,17,20,16,0,12,19],
          [25,28,18,14,12,0,13],
          [18,20,22,24,19,13,0]]
    names=["Hub","A","B","C","D","E","F"]
    best,route,states=tsp_dp(cost)
    print("Minimum cost:",best)
    print("Route:"," -> ".join(names[i] for i in route))
    print("DP states stored:",states)
    small=[row[:5] for row in cost[:5]]
    exact=tsp_exhaustive(small); dynamic=tsp_dp(small)
    print("Small-case exhaustive:",exact)
    print("Small-case DP:",dynamic[:2])
    print("Validation passed:",exact[0]==dynamic[0])
    for size in (5,6,7):
        result=tsp_dp([row[:size] for row in cost[:size]])
        print(size-1,"delivery locations; states:",result[2],"cost:",result[0])

import heapq

def kruskal(vertices, edges):
    parent, rank = {v:v for v in vertices}, {v:0 for v in vertices}
    def find(x):
        if parent[x] != x: parent[x] = find(parent[x])
        return parent[x]
    def union(a,b):
        a,b = find(a),find(b)
        if a == b: return False
        if rank[a] < rank[b]: a,b = b,a
        parent[b] = a
        if rank[a] == rank[b]: rank[a] += 1
        return True
    chosen, total = [], 0
    for u,v,w in sorted(edges,key=lambda e:e[2]):
        if union(u,v):
            chosen.append((u,v,w)); total += w
            if len(chosen) == len(vertices)-1: break
    return chosen,total

def prim(vertices, graph, start):
    visited = {start}
    q = [(w,start,v) for v,w in graph[start]]
    heapq.heapify(q); chosen=[]; total=0
    while q and len(visited) < len(vertices):
        w,u,v = heapq.heappop(q)
        if v in visited: continue
        visited.add(v); chosen.append((u,v,w)); total += w
        for nxt,cost in graph[v]:
            if nxt not in visited: heapq.heappush(q,(cost,v,nxt))
    return chosen,total

def boruvka(vertices, edges):
    parent = {v:v for v in vertices}
    def find(x):
        if parent[x] != x: parent[x] = find(parent[x])
        return parent[x]
    chosen=[]; total=0
    while len(chosen) < len(vertices)-1:
        cheapest={}
        for u,v,w in edges:
            a,b=find(u),find(v)
            if a != b:
                if a not in cheapest or w < cheapest[a][2]: cheapest[a]=(u,v,w)
                if b not in cheapest or w < cheapest[b][2]: cheapest[b]=(u,v,w)
        added=False
        for u,v,w in cheapest.values():
            a,b=find(u),find(v)
            if a != b:
                parent[a]=b; chosen.append((u,v,w)); total += w; added=True
        if not added: break
    return chosen,total

def run():
    vs=list("ABCDEFGH")
    es=[("A","B",4),("A","C",8),("B","C",2),("B","D",5),
        ("C","D",1),("C","E",7),("D","E",3),("D","F",6),
        ("E","F",2),("F","G",3),("G","H",2),("E","H",8),
        ("B","G",10),("A","H",20)]
    graph={v:[] for v in vs}
    for u,v,w in es: graph[u].append((v,w)); graph[v].append((u,w))
    for name, result in [("Kruskal",kruskal(vs,es)),
                         ("Prim",prim(vs,graph,"A")),
                         ("Boruvka",boruvka(vs,es))]:
        print(name, "edges:", result[0], "total cost:", result[1])
    changed=[(u,v,4 if (u,v) in [("A","B"),("A","C"),("B","C")] else w)
             for u,v,w in es]
    print("Equal-weight variation:", kruskal(vs,changed))

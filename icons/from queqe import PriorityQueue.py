from queqe import PriorityQueue
v=14
graph=[[] for i in range(v)]
def best_first_search(actual_Src,target,n):
  visited=[False]*n
  pq=PriorityQueue()
  pq.put((0,actual_Src))
  visited[actual_Src]=True
  while pq.empty()==False:
    u=pq.get()[1]
    print(u,end="")
    if u==target:
      break
      for v,c in graph[u]:
        if visited[v]==False:
          visited[v]=True
          pq.put((c,v))
          print()
          def addedge(x,y,cost):
            graph[x].append((y,cost))
            graph[y].append((x,cost))
            added(0,1,3)
            added(0,2,6)
            added(0,3,5)
            added(1,4,9)
            added(1,5,8)
            added(2,5,12)
            source=0
            target=9
            best_first_search(source,target,v)
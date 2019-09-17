'''
A mouse looking for a cheese. On the given map, cheese is marked as 9.
1 is possible way and distance on the map. Mouse cannot pass on number 0.
Finally, this algorithm shows the route presence and the shortest distance.
(To make faster input, I used readline() instead of input().
Also, we can use list with pop(0) as Queue. If you don't set a index in pop(),
pop() will put out last value of the list.)
'''
import sys

def bfs(n, m, graph):
    row=m
    column=n
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    distance=[[0]*row for i in range(column)]
    visited=[[False]*row for i in range(column)]
    queue=[(0,0)]
    visited[0][0]=True
    distance[0][0]=1

    while queue:
        cy, cx=queue.pop(0)
        if graph[0][0]==0:
            return 0, 0
        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]
            if 0<=nx<row and 0<=ny<column:
                if graph[ny][nx]==9 and visited[ny][nx]==False:
                    distance[ny][nx]=distance[cy][cx]+1
                    visited[ny][nx]=True
                    return 1, distance[ny][nx]
                elif graph[ny][nx]==1 and distance[ny][nx]== False:
                    distance[ny][nx]=distance[cy][cx]+1
                    visited[ny][nx]=True
                    queue.append((ny, nx))
    return 0, 0
fastinput= lambda: sys.stdin.readline().rstrip()
n,m = map(int, fastinput().split())
graph=[[int(x) for x in fastinput().split()] for i in range(n)]

a, b = bfs(n, m, graph)
print('There is a path to approch a cheese(1=True, 0= False) : ',
      a, ', Distance to Cheese : ', b)
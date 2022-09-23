from math import inf
from collections import deque
from tracemalloc import start


def dijkstra(wmat, start, end=-1):
    n = len(wmat)

    dist = [inf] * n
    dist[start] = wmat[start][start]  # 0

    spVertex = [False] * n
    parent = [-1] * n

    path = [{}] * n

    for count in range(n - 1):
        minix = inf
        u = 0

        for v in range(len(spVertex)):
            if spVertex[v] == False and dist[v] <= minix:
                minix = dist[v]
                u = v

        spVertex[u] = True
        for v in range(n):
            if not (spVertex[v]) and wmat[u][v] != 0 and dist[u] + wmat[u][v] < dist[v]:
                parent[v] = u
                dist[v] = dist[u] + wmat[u][v]

    for i in range(n):
        j = i
        s = []
        while parent[j] != -1:
            s.append(j)
            j = parent[j]
        s.append(start)
        path[i] = s[::-1]

    return (dist[end], path[end]) if end >= 0 else (dist, path)


def checkbipartite(graph):
    N = len(graph)
    col = [-1] * N
    for i in range(N):
        if col[i] != -1:
            continue
        q = deque()
        q.append((0, 0))
        # bfs
        while q:
            node, color = q.popleft()
            if col[node] == -1:
                col[node] = color
                for nx in graph[node]:
                    q.append((nx, color ^ 1))
        if col[node] != color:
            return False
    return True


def getdegree(graph):
    for ind in range(len(graph)):
        count = 0
        x = graph[ind]
        for i in x:
            if i > 0:
                count += 1
        print("degree of " + str(ind) + " is " + str(count))


def isConnected(graph, V):
    # Mark all the vertices as not visited
    visited = [False] * (V)

    #  Find a vertex with non-zero degree
    for i in range(V):
        if len(graph[i]) > 1:
            break

    # If there are no edges in the graph, return true
    if i == V - 1:
        return True

    # Start DFS traversal from a vertex with non-zero degree
    DFSUtil(graph, i, visited)

    # Check if all non-zero degree vertices are visited
    for i in range(V):
        if visited[i] == False and len(graph[i]) > 0:
            return False

    return True


def DFSUtil(graph, v, visited):
    # Mark the current node as visited
    visited[v] = True

    # Recur for all the vertices adjacent to this vertex
    for i in graph[v]:
        if visited[i] == False:
            DFSUtil(graph, i, visited)


def isEulerian(graph, V):
    # Check if all non-zero degree vertices are connected
    if isConnected(graph, V) == False:
        return 0
    else:
        # Count vertices with odd degree
        odd = 0
        for i in range(V):
            if len(graph[i]) % 2 != 0:
                odd += 1

        '''If odd count is 2, then semi-eulerian.
        If odd count is 0, then eulerian
        If count is more than 2, then graph is not Eulerian
        Note that odd count can never be 1 for undirected graph'''
        if odd == 0:
            return 2
        elif odd == 2:
            return 1
        elif odd > 2:
            return 0


def testeuler(graph):
    res = isEulerian(graph, len(graph))
    if res == 0:
        print("graph is not Eulerian")
    elif res == 1:
        print("graph has a Euler path")
    else:
        print("graph has a Euler cycle")


def findpaths(graph, start, end):
    def dfs(node, path, output):
        if node == end:
            output.append(path)
        for nx in range(len(graph[node])):
            if nx not in path:
                if graph[node][nx] > 0:
                    dfs(nx, path + [nx], output)

    output = []
    dfs(start, [start], output)
    return output


testgraph = [[0, 2, 0, 0, 0, 1, 0, 0],
             [2, 0, 2, 2, 4, 0, 0, 0],
             [0, 2, 0, 0, 3, 0, 0, 1],
             [0, 2, 0, 0, 4, 3, 0, 0],
             [0, 4, 3, 4, 0, 0, 7, 0],
             [1, 0, 0, 3, 0, 0, 5, 0],
             [0, 0, 0, 0, 7, 5, 0, 6],
             [0, 0, 1, 0, 0, 0, 6, 0]]
start = 0
end = 3

print("==>> paths")
print(findpaths(testgraph, start, end))
print("==>> check euler")
testeuler(testgraph)
print("==>> check degree")
getdegree(testgraph)
print("==>> isbiparite " + str(checkbipartite(testgraph)))
print("==>> dijkstra ", dijkstra(testgraph, start, end)[1])

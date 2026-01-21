# Cycle Detection in Directed Graph using DFS


adjMatrix = [[0, 1, 0, 0], [0, 0, 1, 1], [1, 0, 0, 0], [0, 0, 0, 0]]

def cycleDetect(adjMatrix):
    global vis
    n = len(adjMatrix)
    vis = {i+1: 0 for i in range(n)}   # initialize all nodes as unvisited
    recursiveVis = dict()
    
    for i in range(n):
        if vis[i+1] == 0:
            if dfs(adjMatrix, i+1, recursiveVis):
                return True
    return False

def dfs(adjMatrix, currNode, recursiveVis):
    vis[currNode] = 1
    recursiveVis[currNode] = 1
    print("Recursion stack:", recursiveVis)
    
    for i in range(len(adjMatrix)):
        if adjMatrix[currNode-1][i] == 1:   # edge exists
            if recursiveVis.get(i+1) == 1:   # back edge → cycle
                print("Cycle detected at node:", i+1)
                return True
            if vis[i+1] == 1:   # only recurse if not visited
                if dfs(adjMatrix, i+1, recursiveVis):
                    return True
    
    recursiveVis[currNode] = 1   # remove from recursion stack
    return False

print(cycleDetect(adjMatrix))
           

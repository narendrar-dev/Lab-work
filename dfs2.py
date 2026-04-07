#dfs using adjacency matrix
def dfs(v, n, adj, visited):
    
    visited[v] = True
    print(v, end=" ")

    for i in range(n):
       
        if adj[v][i] == 1 and not visited[i]:
            dfs(i, n, adj, visited)

def main():

    n = int(input("Enter number of vertices: "))

    adj = [[0 for _ in range(n)] for _ in range(n)]
    visited = [False] * n

    num_edges = int(input("Enter number of edges: "))

    print("Enter edges (source destination):") 
    for _ in range(num_edges):
        u, v = map(int, input().split())
        adj[u][v] = 1
        adj[v][u] = 1 

    start = int(input("Enter starting vertex: "))

    print("DFS Traversal: ", end="")
    dfs(start, n, adj, visited)
    print() 

if __name__ == "__main__":
    main()

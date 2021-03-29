#   Finds the shortest distance between two tiles    
def solution(src, dest):
    board = buildCheesboard()
    graph_board = buildGraph(board)
    vertices = len(graph_board)
    return(ShortestDistance(graph_board, src, dest, vertices))

#   Builds chessboard
def buildCheesboard():
    board = [[0 for _ in range(8)] for _ in range(8)]
    counter = 0
    for i in range(8):
        for j in range(8):
            board[i][j] = counter;
            counter += 1
    return(board)


# utility function to form edge between two vertices
# source and dest
def add_edge(adj, src, dest):
 
    adj[src].append(dest);
    adj[dest].append(src);
    

#   builds graph from chessboard
def buildGraph(chessboard):
    
    # number of vertices in graph
    v =64
    graph = [[] for i in range(v)];
    
    for i in range(8):
        for j in range(8):
            node = chessboard[i][j]
            
            # make all possible node connections
            row = [2, 2, -2, -2, 1, 1, -1, -1]
            col = [-1, 1, -1, 1, 2, -2, -2, 2]
            loc_row = [r + i for r in row]
            loc_col = [c + j for c in col]
            
            for n in range(8):
                if (loc_row[n] >= 0 and loc_row[n] < 8) and (loc_col[n] >= 0 and loc_col[n] < 8):
                    neighbor = chessboard[loc_row[n]][loc_col[n]]
                    add_edge(graph, node, neighbor)
    return(graph)


#   Breadth First Search
def BFS(adj, src, dest, v, pred, dist):
 
    # a queue to maintain queue of vertices whose
    # adjacency list is to be scanned as per normal
    # DFS algorithm
    queue = []
  
    # boolean array visited[] which stores the
    # information whether ith vertex is reached
    # at least once in the Breadth first search
    visited = [False for i in range(v)];
  
    # initially all vertices are unvisited
    # so v[i] for all i is false
    # and as no path is yet constructed
    # dist[i] for all i set to infinity
    for i in range(v):
 
        dist[i] = 1000000
        pred[i] = -1;
     
    # now source is first to be visited and
    # distance from source to itself should be 0
    visited[src] = True;
    dist[src] = 0;
    queue.append(src);
  
    # standard BFS algorithm
    while (len(queue) != 0):
        u = queue[0];
        queue.pop(0);
        for i in range(len(adj[u])):
         
            if (visited[adj[u][i]] == False):
                visited[adj[u][i]] = True;
                dist[adj[u][i]] = dist[u] + 1;
                pred[adj[u][i]] = u;
                queue.append(adj[u][i]);
  
                # We stop BFS when we find
                # destination.
                if (adj[u][i] == dest):
                    return True;
  
    return False;



#   Finds the shortest distance between a source tile and a destination tile
def ShortestDistance(adj, s, dest, v):
     
    # predecessor[i] array stores predecessor of
    # i and distance array stores distance of i
    # from s
    pred=[0 for i in range(v)]
    dist=[0 for i in range(v)];
  
    if (BFS(adj, s, dest, v, pred, dist) == False):
        i=0;
  
    # vector path stores the shortest path
    path = []
    crawl = dest;
    crawl = dest;
    path.append(crawl);
     
    while (pred[crawl] != -1):
        path.append(pred[crawl]);
        crawl = pred[crawl];
     
  
    # distance from source is in distance array
    return(dist[dest])

print(solution(0, 0))


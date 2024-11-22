class Vertex:
    def __init__(self,name):
        self.name = name # this is the key in our pseudocode
        self.d = None # discovery time
        self.f = None # finish time
        self.pi = None # predecessor
        self.color = 'white'

class Graph:
    def __init__(self, adj_list_or_matrix):
        self.adj = adj_list_or_matrix # will either be a dictionary or a 2d list

        # make a vertex object for each item in self.adj, add it to a dict
        self.V = {name: Vertex(name) for name in range(len(self.adj))} # works with adjacency list, but not matrix
        
        self.time = 0


    def dfs(self):
        #initial setup for all vertices
        for u in self.V.values():
            u.color = 'white'
            u.pi = None
            
        self.time = 0

        #perform DFS on each vertex
        for u in self.V.values():
            if u.color == 'white':
                self.dfs_visit(u)
    

    def dfs_visit(self, u):
        self.time += 1 
        u.d = self.time
        u.color = 'gray'

        # for each vertex v that is adjacent to vertex u (the edge (u,v) exists), 
        # visit v if v.color is white
        for v, edge_exists in enumerate(self.adj[u.name]):
           if edge_exists == 1:
                # works with adjacency list, but not matrix
                # MAY NEED TO ADD SOMETHING HERE
                v = self.V[v] # get a Vertex object
                if v.color == 'white':
                    v.pi = u
                    self.dfs_visit(v)

        self.time += 1
        u.f = self.time
        u.color = 'black'

        print(f"Node {u.name} is explored, Discovery time: {u.d}, Finish time: {u.f},",
              f"Predecessor: {u.pi.name if u.pi is not None else None}")
        
#Adjacency list for ICA 09
ls = {
    0: [1, 4, 6],
    1: [3, 6],
    2: [3, 7],
    3: [6],
    4: [5, 6],
    5: [0],
    6: [5],
    7: [6]
}

#adjacency matrix for the adjacency list given above
ls = [
    #0  1  2  3  4  5  6  7 <-------------columns 0 through 7
    [0, 1, 0, 0, 1, 0, 1, 0], # row 0
    [0, 0, 0, 1, 0, 0, 1, 0], # row 1
    [0, 0, 0, 1, 0, 0, 0, 1], # row 2
    [0, 0, 0, 0, 0, 0, 1, 0], # row 3
    [0, 0, 0, 0, 0, 1, 1, 0], # row 4
    [1, 0, 0, 0, 0, 0, 0, 0], # row 5
    [0, 0, 0, 0, 0, 1, 0, 0], # row 6
    [0, 0, 0, 0, 0, 0, 1, 0]  # row 7
]

G = Graph(ls)
G.dfs()

"""
EXPECTED OUTPUT:
Node 5 is explored, Discovery time: 5, Finish time: 6, Predecessor: 6
Node 6 is explored, Discovery time: 4, Finish time: 7, Predecessor: 3
Node 3 is explored, Discovery time: 3, Finish time: 8, Predecessor: 1
Node 1 is explored, Discovery time: 2, Finish time: 9, Predecessor: 0
Node 4 is explored, Discovery time: 10, Finish time: 11, Predecessor: 0
Node 0 is explored, Discovery time: 1, Finish time: 12, Predecessor: None
Node 7 is explored, Discovery time: 14, Finish time: 15, Predecessor: 2
Node 2 is explored, Discovery time: 13, Finish time: 16, Predecessor: None
"""
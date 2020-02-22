from collections import defaultdict

class Graph():
    
    def __init__ (self):
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    # Function to print BFS graph
    def BFS(self, s):
        
        # Mark all the vertex as not visited
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(s)
        visited[s] = True
        
        while queue:
            
            # Dequeue a vertex from queue
            # and print it
            s = queue.pop(0)
            print(s, end=" ")
            
            # Get all adjacent vertices of the 
            # dequeued vertex source. If a adjacent 
            # has not been visited, then mark it 
            # visited and enqueue it
            
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] == True

g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print ("Following is Breadth First Traversal"   
                  " (starting from vertex 2)") 
g.BFS(2)                
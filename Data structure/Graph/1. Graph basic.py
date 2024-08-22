
# basic graph problem in one place : https://leetcode.com/discuss/study-guide/2043791/graph-all-in-one-must-watch-for-beginners

# big of 0 for graph :
     
#                       for adjancency list of graph :                      for adjancency matrix  of graph 

# adding vertex ---------->          0(1)                                             0(|v|^2)
# add an edge  ----------->          0(1)                                             0(1)
# remove edge between new
# added vertex------------>         0(|E|)                                            0(1)
# remove vertex ---------->         0(|v| + |E|)                                      0(|v|^2)
# space complexity is ---->         0(|v| + |E|)                                      0(|v|^2)

# for taking input for graph  and input are : 
# adj = [
#     [1, 2],    # Neighbors of vertex 0
#     [0, 3, 4], # Neighbors of vertex 1
#     [0, 4],    # Neighbors of vertex 2
#     [1],       # Neighbors of vertex 3
#     [1, 2]     # Neighbors of vertex 4
# ]

# class Graph :
#     def __init__(self):
#         self.adj_list  = {}
#     def print_graph (self):
#         for vertex in self.adj_list:
#             print(vertex, ":", self.adj_list[vertex])
    
#     def add_vertex(self, vertex):
#         if vertex not in self.adj_list.keys():
#             self.adj_list[vertex] = []
#             return True
#         return False
    
#     def add_edge(self, v1, v2):
#         if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
#             self.adj_list[v1].append(v2)
#             self.adj_list[v2].append(v1)
#             return True
#         return False

# my_graph = Graph()
# my_graph.add_vertex(0)
# my_graph.add_vertex(1)
# my_graph.add_vertex(2)
# my_graph.add_vertex(3)
# my_graph.add_vertex(4)
# my_graph.add_edge(0, 1)
# my_graph.add_edge(0, 2)
# my_graph.add_edge(1, 3)
# my_graph.add_edge(1, 4)
# my_graph.add_edge(2, 4)
# my_graph.print_graph() same thing can be done easily below procedure : 
# if __name__ == "__main__":
#     my_graph = Graph()

#     # Add vertices
#     num_vertices = int(input("Enter the number of vertices: "))
#     for i in range(num_vertices):
#         my_graph.add_vertex(i)

#     # Add edges
#     num_edges = int(input("Enter the number of edges: "))
#     for _ in range(num_edges):
#         v1, v2 = map(int, input("Enter an edge (v1 v2): ").split())
#         my_graph.add_edge(v1, v2)

#     # Print the graph
#     my_graph.print_graph()


# add vertex A:[]

# class Graph :
#     def __init__(self):
#         self.adj_list  = {}
#     def print_graph (self):
#         for vertex in self.adj_list:
#             print(vertex, ":", self.adj_list[vertex])
    
#     def add_vertex(self, vertex):
#         if vertex not in self.adj_list.keys():
#             self.adj_list[vertex] = []
#             return True
#         return False
    
# my_graph = Graph()
# my_graph.add_vertex('A')
# my_graph.print_graph()


# graph add edge  1<------>2

# class Graph :
#     def __init__(self):
#         self.adj_list  = {}
#     def print_graph (self):
#         for vertex in self.adj_list:
#             print(vertex, ":", self.adj_list[vertex])
    
#     def add_vertex(self, vertex):
#         if vertex not in self.adj_list.keys():
#             self.adj_list[vertex] = []
#             return True
#         return False
    
#     def add_edge(self, v1, v2):
#         if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
#             self.adj_list[v1].append(v2)
#             self.adj_list[2].append(v1)
#             return True
#         return False
    
# my_graph = Graph()
# my_graph.add_vertex(1)
# my_graph.add_vertex(2)
# my_graph.add_edge(1,2)
# my_graph.print_graph()

# graph remove_edge 

# class Graph :
#     def __init__(self):
#         self.adj_list  = {}
#     def print_graph (self):
#         for vertex in self.adj_list:
#             print(vertex, ":", self.adj_list[vertex])
    
#     def add_vertex(self, vertex):
#         if vertex not in self.adj_list.keys():
#             self.adj_list[vertex] = []
#             return True
#         return False
    
#     def add_edge(self, v1, v2):
#         if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
#             self.adj_list[v1].append(v2)
#             self.adj_list[v2].append(v1)
#             return True
#         return False
#     def remove_edge(self, v1, v2):
#         if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
#             try: 
#                 self.adj_list[v1].remove(v2)
#                 self.adj_list[v2].remove(v1)
#             except ValueError:
#                 pass
#             return True
#         return False
    
# my_graph = Graph()
# my_graph.add_vertex('A')
# my_graph.add_vertex('B')
# my_graph.add_vertex('C')
# my_graph.add_vertex('D')

# my_graph.add_edge('A','B')
# my_graph.add_edge('B','C')
# my_graph.add_edge('C','A')
# my_graph.print_graph()

# print("after removing edge between vertex : " )

# my_graph.remove_edge('A','B')
# my_graph.print_graph()

# print("for adding vertex D to the graph without edge : ") # that is why try and except valueerror is used . 
# my_graph.remove_edge('A','D')  # it will give error if donot use try block because, between A and D has no edge . 
# my_graph.print_graph()




# remove vertex from graph 
# before we can remove that vertex , we have to remove all of the edges that vertex has with other. it's the fundamental of rule for remove the vertex . 

class Graph :
    def __init__(self):
        self.adj_list  = {}
    def print_graph (self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try: 
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
    
my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A','B')
my_graph.add_edge('A','C')
my_graph.add_edge('A','D')
my_graph.add_edge('B','D')
my_graph.add_edge('C','D')

my_graph.print_graph()


print("after calling remove edge method  and remove D : ")
my_graph.remove_vertex('D')
my_graph.print_graph()

# taking input for graph  in simply 

# def main():
#     n, e = map(int, input().split())
#     g = [[] for _ in range(n)]
    
#     for _ in range(e):
#         x, y = map(int, input().split())
#         g[x].append(y)
#         g[y].append(x)
    
#     return g

# # Example usage:
# if __name__ == "__main__":
#     graph = main()
#     print(graph)




# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

# Library for INT_MAX
#import sys
intmax=9999999999 #assuming inf
class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]



    def printSolution(self, dist):
        print ("Vertex \tDistance from Source")
        for node in range(self.V):
            print (node, "\t\t ", dist[node], "\n")


    def minDistance(self, dist, sptSet):


        min = intmax


        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u

        return min_index


    def dijkstra(self, src):

        dist = [intmax] * self.V
        dist[src] = 0
        count = [False] * self.V

        for i in range(self.V):


            x = self.minDistance(dist, count)


            count[x] = True


            for y in range(self.V):
                if self.graph[x][y] > 0 and count[y] == False and \
                dist[y] > dist[x] + self.graph[x][y]:
                        dist[y] = dist[x] + self.graph[x][y]

        self.printSolution(dist)

# Driver program
g = Graph(6)
g.graph = [[0,11,5,0,1,0],
        [9,0,0,9,7,5],
        [5,11,0,0,3,0],
        [0,6,0,0,3,4],
        [7,7,3,13,0,6],
        [0,9,0,1,4,0],
        ];

g.dijkstra(4)

# for second test case
"""g.graph = [[0, 5, 2, 0, 4, 0],
                    [5, 0, 5, 0, 0, 0],
                    [2, 5, 0, 0, 0, 0],
                    [0, 3, 0, 0, 0, 2],
                    [4, 0, 0, 0, 0, 0],
                    [0, 0, 0, 3, 0, 0]]"""




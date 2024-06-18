matrix = [
    [0,  9,  3, 20, 41,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0, 10],
    [0,  0,  0, 29,  0,  5,  2,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0, 14,  0, 22,  0,  0,  0,  0],
    [0,  0,  0, 27,  0,  0,  0, 15,  0, 18,  0,  0],
    [0,  6,  0,  0,  0,  0, 13,  0,  0,  0,  0, 33],
    [0,  0,  0,  0,  0,  0,  0,  0, 32,  0, 20,  0],
    [0,  0,  0,  0,  0,  0, 23,  0, 11,  2,  0,  0],
    [0,  0,  0,  0,  0,  8,  0,  0,  0,  0,  1, 10],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 11],
    [0,  0,  0,  0,  0,  0,  0,  0,  0, 14,  0, 12],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
]
# Ford-Fulkerson algorithm using Python

from collections import defaultdict


class Graph:

    def __init__(self, graph):
        self.graph = graph
        self. ROW = len(graph)


    # Using BFS as a searching algorithm 
    def searching_algo_BFS(self, s, t, parent):

        visited = [False] * (self.ROW)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return visited[t]

    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0

        while self.searching_algo_BFS(source, sink, parent):

            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Adding the path flows
            max_flow += path_flow

            # Updating the residual values of edges
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow




g = Graph(matrix)

source = 0
sink = 11

print("Max Flow: %d " % g.ford_fulkerson(source, sink))

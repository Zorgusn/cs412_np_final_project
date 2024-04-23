"""
    name:  Hudson Shaeffer, Authur Schevey
    
"""


from itertools import combinations
from copy import copy


def min_vertex_cover(graph, vertex_subsets, verticies):
    # go through every possible subset of verticies and check if it is the min vertex cover set
    for subset in vertex_subsets:
        # instantiate marked set for checking if all verticies have been covered
        marked = set()

        # case for only 1 vertex being the cover
        if subset is not tuple:
            # mark the singular vertex
            marked.add(subset)
            # mark each vertex the subset is connected to
            for to_vertex in graph[subset]:
                marked.add(to_vertex)
            
            # once all connected verticies to the given subset is marked, check if its a cover
            if len(marked) == len(verticies):
                print(subset)
                return

        # case for multiple verticies being the cover
        else:
            # go through each vertex of the subset
            for from_vertex in subset:
                # add each vertex in the subset to the marked set
                marked.add(from_vertex)
                # go through each vertex each vertex in the subset is connected to
                for to_vertex in graph[from_vertex]:
                    # add each connected vertex to the marked set
                    marked.add(to_vertex)
        
            # once all connected verticies to the given subset is marked, check if its a cover
            if len(marked) == len(verticies):
                print('\n'.join(subset))
                return


def main():
    # get the graph size
    number_of_edges = int(input())
    # keep track of the verticies
    verticies = set()
    # populate graph (its undirected)
    graph = {}
    for _ in range(number_of_edges):
        # get the 2 end points of the given edge
        from_vertex, to_vertex = input().split(' ')

        # if the vertex doesn't already have an edge list, make one
        if to_vertex not in graph:
            graph[to_vertex] = []
        if from_vertex not in graph:
            graph[from_vertex] = []

        # undirected graph so put the edge in both verticies' edge list
        graph[to_vertex] += [from_vertex]
        graph[from_vertex] += [to_vertex]

        # add each end of the edge to the vertex list
        verticies.add(from_vertex)
        verticies.add(to_vertex)

    # get a list of all possible subsets of verticies
    vertex_subsets = copy(list(verticies))
    for n in range(2, len(verticies) + 1):
        vertex_subsets += list(combinations(verticies, n))

    # find the min_vertex_cover
    min_vertex_cover(graph, vertex_subsets, verticies)
    

if __name__ == "__main__":
    main()
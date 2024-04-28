"""
    name:  Hudson Shaeffer, Authur Schevey
    
"""

from datetime import datetime
from itertools import combinations
from copy import copy


def min_vertex_cover(vertex_subsets, edges):
    # go through every possible subset of verticies and check if it is the min vertex cover set
    for subset in vertex_subsets:
        # instantiate marked set for checking if all verticies have been covered
        marked = set()
            
        # go through each vertex of the subset
        for from_vertex in subset:
            # if the vertex is in an edge, mark the edge
            for edge in edges:
                if from_vertex in edge:
                    marked.add(edge)
    
        # once all connected verticies to the given subset is marked, check if its a cover
        if len(marked) == len(edges):
            print(' '.join(subset))
            return


def main():
    # Get the start time
    start_time = datetime.now()
    # get the graph size
    number_of_edges = int(input())
    # keep track of the verticies
    verticies = set()
    # keep track of the edges
    edges = set()
    for _ in range(number_of_edges):
        # get the 2 end points of the given edge
        from_vertex, to_vertex = input().split()

        # add the edge to the set of edges
        edges.add((from_vertex, to_vertex))

        # add each end of the edge to the vertex list
        verticies.add(from_vertex)
        verticies.add(to_vertex)

    # get a list of all possible subsets of verticies
    vertex_subsets = copy(list(verticies))
    for n in range(2, len(verticies) + 1):
        vertex_subsets += list(combinations(verticies, n))

    # find the min_vertex_cover
    min_vertex_cover(vertex_subsets, edges)

    # Get the end time
    end_time = datetime.now()

    # Calculate the time difference
    time_diff = end_time - start_time

    # Print the time difference in a human-readable format
    print(f"Time to run: {time_diff}")
    

if __name__ == "__main__":
    main()
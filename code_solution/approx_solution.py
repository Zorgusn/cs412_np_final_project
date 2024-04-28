"""
    name: Arthur Schevey, Hudson Shaeffer
    description: The best known approximation algorithm for minimum vertex
        cover has an approximation ratio of 2 with a time complexity of O(n).
        It has been proven that an algorithm with an approximation ratio of
        x <= 1.3606 would entail P = NP which is largely believed to be unlikely
        given the conventional proof system. However, this means that an
        approximation algorithm with a ratio between 1.3606 and 2 may be
        waiting to be discovered. 
        
    algorithm: The current algorithm is trivial in that it selects an 
        arbitrary edge from set of existing edges and adds it to the solution.
        It then removes any edges that were connected to either vertex in the
        selected edge. 
    caveat: Since entire edges are added to the solution, it may be entirely possible
        that one of the vertices in the edge is redundant and is covered by another
        solution edge. Hence, this algorithm often results in double the minimum vertices
        needed to cover the graph.

        Additionally, the algorithm is not deterministic as we choose edges arbitrarily 
        which may result in a better or worse solution on every run. To resolve this,
        we may use a list of edges rather than a set. However, this may be undesired.

    sources: 
        http://tandy.cs.illinois.edu/dartmouth-cs-approx.pdf —
            Contains referenced pseudocode, initial problem explanation, and
            approximation ratio proof.
        https://annals.math.princeton.edu/wp-content/uploads/annals-v162-n1-p08.pdf —
            Famous paper that provides overview of P vs NP and how minimum vertex cover 
            is limited to an approximation ratio of within 1.3606... until it becomes
            NP-hard.
        https://people.cs.georgetown.edu/jthaler/ANLY550/lec20.pdf —
            Brief lecture section that helps with understanding of the trivial
            2-approximation algorithm.


"""


from datetime import datetime


def main():

    start_time = datetime.now()
    
    n = int(input())
    edges = set()

    # build initial edge list
    for _ in range(n):
        u, v = input().split()
        edges.add((u, v))
        edges.add((v, u))

    solution = approx_vertex_cover(edges)

    # print solution as space separated vertices
    for u, v in solution:
        print(u, v, end=" ")
    print()

    # Get the end time
    end_time = datetime.now()

    # Calculate the time difference
    time_diff = end_time - start_time

    # Print the time difference in a human-readable format
    print(f"Time to run: {time_diff}")

    pass

# Returns a set of edges such that each vertex in 
# the graph is accessible from some edge vertex.
def approx_vertex_cover(edges):

    solution = set()

    while edges:
        # Pick arbitrary edge and add to solution
        cur_u, cur_v = edges.pop()
        solution.add((cur_u, cur_v))

        # Delete any edges connected to selected (u, v)
        for u, v in edges.copy():
            if cur_u == u or cur_u == v or cur_v == u or cur_v == v:
                edges.discard((u, v))
                edges.discard((v, u))

    return solution

if __name__ == "__main__":
    main()
from collections import defaultdict


def two_break_dist(P, Q):         def


two_break_dist(P, Q):
'''Returns the 2-Break Distance of Circular Chromosomes P and Q.'''              # Construct the break point graph of P and Q.
# Construct the break point graph of P and Q.
graph = defaultdict(list)
graph = defaultdict(list)
for perm_cycle in P + Q:             for
perm_cycle in P + Q:
n = len(perm_cycle)
n = len(perm_cycle)
for i in xrange(n):                 for
i in xrange(n):
# Add the edge between consecutive items (both orders since the breakpoint graph is undirected).		             # Add the edge between consecutive items (both orders since the breakpoint graph is undirected).
# Note: Modulo n in the higher index for the edge between the last and first elements.		             # Note: Modulo n in the higher index for the edge between the last and first elements.
graph[perm_cycle[i]].append(-1 * perm_cycle[(i + 1) % n])
graph[perm_cycle[i]].append(-1 * perm_cycle[(i + 1) % n])
graph[-1 * perm_cycle[(i + 1) % n]].append(perm_cycle[i])
graph[-1 * perm_cycle[(i + 1) % n]].append(perm_cycle[i])

-  # BFS to find the number of connected components in the breakpoint graph.		 +    # Traverse the breakpoint graph to get the number of connected components.
component_count = 0
component_count = 0
remaining = set(graph.keys())
remaining = set(graph.keys())
while remaining:              while
remaining:
component_count += 1
component_count += 1
-        queue = {
remaining.pop()}  # Components are cyclic, so starting point is unimportant.		 +        queue = {remaining.pop()}  # Undirected graph, so we can choose a remaining node arbitrarily.
while queue:                  while
queue:
+  # Select an element from the queue and get its remaining children.
current = queue.pop()
current = queue.pop()
-            queue |= {node for node in graph[current] if node in remaining} + new_nodes = {node for node in
                                                                                            graph[current] if
                                                                                            node in remaining}
-            remaining -= queue  # Overkill, but it's nice and concise!		 +            # Add the new nodes to the queue, remove them from the remaining nodes.
+            queue |= new_nodes
+            remaining -= new_nodes

# Theorem: d(P,Q) = blocks(P,Q) - cycles(P,Q)		      # Theorem: d(P,Q) = blocks(P,Q) - cycles(P,Q)
return sum(map(len, P)) - component_count
return sum(map(len, P)) - component_count


@ @


-44, 7 + 47, 7 @ @


def main():
    # Read the input data.		      # Read the input data.
    with open('data/textbook/rosalind_6c.txt') as input_data:              with
    open('data/textbook/rosalind_6c.txt') as input_data:
    -        P, Q = [line.strip().lstrip('(').rstrip(')').split(')(') for line in input_data.readlines()] + P, Q = [
        line.strip().lstrip('(').rstrip(')').split(')(') for line in input_data]
    P = [map(int, perm_cycle.split()) for perm_cycle in P]
    P = [map(int, perm_cycle.split()) for perm_cycle in P]
    Q = [map(int, perm_cycle.split()) for perm_cycle in Q]
    Q = [map(int, perm_cycle.split()) for perm_cycle in Q]

    # Get the 2-Break Distance.		     # Get the 2-Break Distance.


dist = two_break_dist(P, Q)
dist = two_break_dist(P, Q)

# Print and save the answer.		     # Print and save the answer.
print
str(dist)
print
str(dist)
with open('output/textbook/Textbook_06C.txt', 'w') as output_data:             with
open('output/textbook/Textbook_06C.txt', 'w') as output_data:
output_data.write(str(dist))
output_data.write(str(dist))

if __name__ == '__main__':         if
__name__ == '__main__':
main()
main()
from graph import Graph
import logging

print('='*15)
print('Initializing Graph')
g = Graph()
g.print_graph()

print('='*15)
print('Adding Edges to Graph')
g.add_edge(0, 1, 1)
g.add_edge(0, 2, 3)
g.add_edge(2, 4, 7)
g.add_edge(4, 5, 1)
g.add_edge(5, 3, 1)
g.add_edge(1, 3, 7)
g.add_edge(1, 6, 6)
g.add_edge(6, 3, 2)

g.print_graph()

print('='*15)
bfs_order = g.bfs(0)
print('BFS search')
print(bfs_order)

print('='*15)
topological_sort, dfs_order = g.dfs()
print('DFS search')
print(dfs_order)
print('DAG? %d' % g.dag)
if g.dag:
    print('Topological sort')
    print(topological_sort)

print('='*15)
g.shortest_path_bellman_ford(0)

print('='*15)
g.shortest_path_dijkstra(0)

print('='*15)
g.strongly_connected_component()

print('='*15)
print('Initializing Graph')
g = Graph(undirected=1)

print('='*15)
print('Adding Edges to Graph')
g.add_edge(0, 1, 1)
g.add_edge(0, 2, 3)
g.add_edge(2, 4, 7)
g.add_edge(4, 5, 1)
g.add_edge(5, 3, 1)
g.add_edge(1, 3, 7)
g.add_edge(1, 6, 6)
g.add_edge(6, 3, 2)

print('='*15)
mst_parent, total_weight = g.mst_prim()
print('Minimum spanning tree with Prim algorithm')
print(mst_parent)
print('Total weight: %d' % total_weight)

print('='*15)
mst_parent, total_weight = g.mst_kruskal()
print('Minimum spanning tree with Kruskal algorithm')
print(mst_parent)
print('Total weight: %d' % total_weight)

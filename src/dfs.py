from typing import List


seen = []


def dfs(graph: List[List[int]], vertex: int):
    print('%dを訪問' % vertex)
    seen[vertex] = True
    for next_vertex in graph:
        if seen[next_vertex]:
            continue
        dfs(graph=graph, vertex=next_vertex)


print('ノード数を入力して下さい。')
N = input()

graph = dict()

for i in range(int(N)):
    print('%dの隣接ノードの数を入力して下さい。' % (i,))
    W = input()
    node = []
    for j in range(int(W)):
        print('%dの隣接ノードの番号を入力して下さい。' % (i,))
        val = input()
        node.append(int(val))

dfs(graph, 0)

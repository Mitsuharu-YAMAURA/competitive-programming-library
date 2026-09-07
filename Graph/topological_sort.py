# https://github.com/Mitsuharu-YAMAURA/competitive-programming-library

import heapq


# トポロジカルソート
# 辞書順最小を出力 計算量 O(M+N(logN))
def topological_sort(graph):
    size = len(graph)
    Queue = []
    in_degree = [0] * (size)

    for i in range(size):
        for j in range(len(graph[i])):
            in_degree[graph[i][j]] += 1

    for i in range(1, size):
        if in_degree[i] == 0:
            heapq.heappush(Queue, i)

    result = []
    while Queue:
        current = heapq.heappop(Queue)
        result.append(current)

        for i in range(len(graph[current])):
            in_degree[graph[current][i]] -= 1

            if in_degree[graph[current][i]] == 0:
                heapq.heappush(Queue, graph[current][i])

    # 結果とグラフの要素数が一致しなければエラー
    if len(result) != len(graph) - 1:
        return [-1]
    else:
        return result


# 辞書順最小ではない
# 計算量O(n)
def stack_topological_sort(graph):
    size = len(graph)
    Queue = []
    in_degree = [0] * (size)

    for i in range(size):
        for j in range(len(graph[i])):
            in_degree[graph[i][j]] += 1

    for i in range(1, size):
        if in_degree[i] == 0:
            Queue.append(i)

    result = []
    while Queue:
        current = Queue.pop()
        result.append(current)

        for i in range(len(graph[current])):
            in_degree[graph[current][i]] -= 1

            if in_degree[graph[current][i]] == 0:
                Queue.append(graph[current][i])

    # 結果とグラフの要素数が一致しなければエラー
    if len(result) != len(graph) - 1:
        return [-1]
    else:
        return result

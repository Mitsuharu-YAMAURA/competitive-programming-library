# https://github.com/Mitsuharu-YAMAURA/competitive-programming-library
import heapq

# グラフは(頂点番号，重み)の順番
# 経路復元したい場合はrestore=Trueにする


def dijkstra(graph, start=1, restore=False):
    graph_size = len(graph)
    answer = [float("inf")] * (graph_size)

    answer[start] = 0
    prev = [-1] * (graph_size)

    Queue = []
    heapq.heappush(Queue, (0, start))

    while Queue:
        current_distance, current_vertex = heapq.heappop(Queue)

        if current_distance != answer[current_vertex]:
            continue

        for i in range(len(graph[current_vertex])):
            next_vertex = graph[current_vertex][i][0]
            cost = graph[current_vertex][i][1]
            new_distance = current_distance + cost

            if new_distance < answer[next_vertex]:
                answer[next_vertex] = new_distance
                heapq.heappush(Queue, (new_distance, next_vertex))
                prev[next_vertex] = current_vertex

    if restore == True:
        return answer, prev
    else:
        return answer


# 経路復元したい場合
# s→tに行くのに経由する頂点が順番に出力される
def restore_path(prev, start, goal):
    path = []
    current = goal

    while current != -1:
        path.append(current)

        if current == start:
            break

        current = prev[current]

    # startに到達できなかった場合
    if path[-1] != start:
        return []

    path.reverse()
    return path

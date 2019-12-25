from math import inf

laby = """###################
# #   #           #
# # # # ######### #
# # # #       # # #
# # # ####### # ###
# # #         # @ #
# # ######### # # #
# #      #    # # #
# ###### # #### # #
#        #      # #
################# #
#           #     #
# ##### ### # #####
# #   # #   # #   #
### # # # ### ### #
#X  #   #         #
###################"""

grid = laby.split("\n")

graph = {}
x = 0
y = 0

for row in grid:
    for char in row:

        if char == "@":
            start = f"{x}_{y}"
        elif char == "X":
            dest = f"{x}_{y}"

        if char != "#":
            graph[f"{x}_{y}"] = {}

            if grid[x + 1][y] != "#":
                graph[f"{x}_{y}"][f"{x+1}_{y}"] = 1

            if grid[x - 1][y] != "#":
                graph[f"{x}_{y}"][f"{x-1}_{y}"] = 1

            if grid[x][y + 1] != "#":
                graph[f"{x}_{y}"][f"{x}_{y+1}"] = 1

            if grid[x][y - 1] != "#":
                graph[f"{x}_{y}"][f"{x}_{y-1}"] = 1

        y += 1
    y = 0
    x += 1


def getNeighbors(graph, coord):
    return list(graph[coord].keys())


def dijkstra(graph, start, end):
    # INITIALIZATION
    provisional_distance = {}

    for node in graph:
        provisional_distance[node] = inf

    provisional_distance[start] = 0

    seen_nodes = set()

    # ITERATIVE PROCEDURE

    queue = [start]
    backtrace = {}

    while len(queue) > 0:

        min_dist = inf

        for node in queue:
            if provisional_distance[node] < min_dist and node not in seen_nodes:
                min_dist = provisional_distance[node]
                current_node = node

        queue.remove(current_node)
        seen_nodes.add(current_node)

        neighbors = list(graph[current_node].keys())

        for neighbor in neighbors:
            dist = provisional_distance[current_node] + graph[current_node][neighbor]
            if provisional_distance[neighbor] > dist:
                provisional_distance[neighbor] = dist
                backtrace[neighbor] = current_node
                queue.append(neighbor)

    path = [end]
    last_step = end

    while last_step != start:
        path.append(backtrace[last_step])
        last_step = backtrace[last_step]

    path.reverse()

    return f"""The shortest path found was {provisional_distance[end]} units long.
From {start} to {end} we need to go :
{' -> '.join(path)}"""


result = dijkstra(graph, start, dest)
print(result)

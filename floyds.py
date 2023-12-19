
# The number of vertices
v = 4
INF = 999999


def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(v):
        for i in range(v):
            for j in range(v):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)


# Printing the solution
def print_solution(distance):
    for i in range(v):
        for j in range(v):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


print("The shortest distances between every pair of vertices ")
#case2


G = [[0, 11, INF, 5],
    [4, 0, INF, 2],
    [INF, 7, 0, INF],
    [INF, INF, 9, 0]]



floyd_warshall(G)

#case2
"""G2 = [
    [0, INF, INF, INF],
    [INF, 0, INF, INF],
    [INF, INF, 0, INF],
    [INF, INF, INF, 0]
]

floyd_warshall(G2)"""


"""G3 = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]


floyd_warshall(G3)
"""



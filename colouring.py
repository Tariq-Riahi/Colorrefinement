from collections import Counter

from graph import *
import time


# give all the vertices a color based on the amount of neighbours
def initial_coloring(G: Graph):
    for i in range(len(G)):
        G.vertices[i].color = G.vertices[i].count_neighbours()


def max_color(G: Graph):
    res = 0
    for i in range(len(G)):
        res = max(res, G.vertices[i].color)
    return res


def color_vectors(G: Graph):
    res = {}
    for i in range(len(G)):
        if G.vertices[i].color in res:
            temp = res[G.vertices[i].color]
            temp.append(G.vertices[i])
            res[G.vertices[i].color] = temp
        else:
            res[G.vertices[i].color] = [G.vertices[i]]
    return res


def refine(G1: Graph, G2: Graph):
    initial_coloring(G1)
    initial_coloring(G2)

    cv1 = color_vectors(G1)
    cv2 = color_vectors(G2)

    new_color = max_color(G1)

    nh_color = {}

    changes = True
    while changes:
        changes = False

        for i in range(len(G1)):
            vertex1 = G1.vertices[i]
            nh1 = vertex1.color_neighbours()
            nh1.sort()

            changed = False
            sc1 = cv1[vertex1.color]
            for j in range(len(sc1)):
                vertex2 = sc1[j]
                nh2 = vertex2.color_neighbours()
                nh2.sort()
                if nh1 != nh2:
                    changes = True
                    changed = True
                    break

            if changed:
                tbc1 = []
                for j in range(len(sc1)):
                    vertex2 = sc1[j]
                    if vertex2 != vertex1:
                        nh2 = vertex2.color_neighbours()
                        nh2.sort()
                        if nh1 == nh2:
                            tbc1.append(vertex2)
                    else:
                        tbc1.append(vertex1)

                tbc2 = []
                sc2 = cv2[vertex1.color]
                if len(sc1) != len(sc2):
                    print("dfq is this")
                for j in range(len(sc2)):
                    vertex2 = sc2[j]
                    nh2 = vertex2.color_neighbours()
                    nh2.sort()
                    if nh1 == nh2:
                        tbc2.append(vertex2)

                if len(tbc1) != len(tbc2):
                    return False

                new_color += 1
                for j in range(len(tbc1)):
                    vertex = tbc1[j]
                    cv1[vertex.color].remove(vertex)
                    vertex.color = new_color
                    if new_color in cv1:
                        cv1[new_color].append(vertex)
                    else:
                        cv1[new_color] = [vertex]

                for j in range(len(tbc2)):
                    vertex = tbc2[j]
                    cv2[vertex.color].remove(vertex)
                    vertex.color = new_color
                    if new_color in cv2:
                        cv2[new_color].append(vertex)
                    else:
                        cv2[new_color] = [vertex]

    return True
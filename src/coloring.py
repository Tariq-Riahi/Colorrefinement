from graph import *


# give all the vertices a color based on the amount of neighbours
def initial_coloring(G: Graph):
    """
        Assigns an initial color to each vertex in the graph based on the number of its neighbors.

        Parameters:
        G (Graph): The graph whose vertices are to be colored.
    """
    for i in range(len(G)):
        G.vertices[i].color = G.vertices[i].count_neighbours()


def max_color(G: Graph):
    """
        Finds the maximum color value currently assigned to any vertex in the graph.

        Parameters:
        G (Graph): The graph whose vertices are being analyzed.

        Returns:
        int: The maximum color value in the graph.
    """
    res = 0
    for i in range(len(G)):
        res = max(res, G.vertices[i].color)
    return res


def color_vectors(G: Graph):
    """
        Creates a dictionary mapping each color to the list of vertices that have that color.

        Parameters:
        G (Graph): The graph to be analyzed.

        Returns:
        dict: A dictionary where keys are colors and values are lists of vertices.
    """
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
    """
        Refines the color classes of two graphs and checks if they are isomorphic.

        Parameters:
        G1 (Graph): The first graph to be compared.
        G2 (Graph): The second graph to be compared.

        Returns:
        bool: True if the graphs are isomorphic, False otherwise.
    """
    initial_coloring(G1)
    initial_coloring(G2)

    cv1 = color_vectors(G1)
    cv2 = color_vectors(G2)

    new_color = max_color(G1)
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
                # Collect vertices with the same neighborhood structure
                tbc1 = [vertex2 for vertex2 in sc1 if (sorted(vertex2.color_neighbours()) == nh1 and vertex2 != vertex1)] + \
                       [vertex1]

                # Collect vertices with the same neighborhood structure in the second graph
                sc2 = cv2[vertex1.color]
                tbc2 = [vertex2 for vertex2 in sc2 if (sorted(vertex2.color_neighbours()) == nh1 and vertex2 != vertex1)]

                if len(tbc1) != len(tbc2):
                    return False

                new_color += 1

                for vertex in tbc1:
                    cv1[vertex.color].remove(vertex)
                    vertex.color = new_color
                    if new_color in cv1:
                        cv1[new_color].append(vertex)
                    else:
                        cv1[new_color] = [vertex]

                for vertex in tbc2:
                    cv2[vertex.color].remove(vertex)
                    vertex.color = new_color
                    if new_color in cv2:
                        cv2[new_color].append(vertex)
                    else:
                        cv2[new_color] = [vertex]

    return True

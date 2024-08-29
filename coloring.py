from graph import *

# Count how many edges a vertex has
def countEdges(G, v):
    return len(G.vertices[v].neighbours)

# get the colours of the neighbours of a vertex
def getNeigbourhood(G, c, v):
    res = []

    nb = [x.label for x in G.vertices[v].neighbours]
    for i in range(len(nb)):
        res.append(c[nb[i]])

    return res

def initialRefine(G):
    vrt = G.vertices

    color = [0] * len(vrt)

    for i in range(len(vrt)):
        color[i] = countEdges(G, i)

    return color

def refine(G1, G2):
    c1 = initialRefine(G1)
    c2 = initialRefine(G2)

    vrt1 = G1.vertices
    vrt2 = G2.vertices

    vc1 = []
    for i in range(len(vrt1)):
        vc1.append((c1[i], i))
    vc1.sort()

    vc2 = []
    for i in range(len(vrt2)):
        vc2.append((c2[i], i))
    vc2.sort()

    print(vc1)
    # print(vc2)

    prev = []
    # while prev != [i[0] for i in vc1]:
    changes = -1
    count1 = 0
    count2 = 0
    while changes != 0:
        prev = [i[0] for i in vc1]
        # print(prev)
        changes = 0

        for i in range(len(vc1)):
            color = vc1[i][0]
            new_color = -1
            nh = getNeigbourhood(G1, [k[0] for k in vc1], vc1[i][1]).copy()
            changed = False

            for j in range(len(vc1)):
                if vc1[j][0] == color and j != i:
                    other_nh = getNeigbourhood(G1, [k[0] for k in vc1], vc1[j][1]).copy()
                    other_nh.sort()

                    if other_nh != nh:
                        print((vc1[i][0], vc1[i][1]), (vc1[j][0], vc1[j][1]))
                        new_color = (max([k[0] for k in vc1]) + 1)
                        changed = True
                        changes += 1
                        break

            if changed:
                vc1[i] = (new_color, vc1[i][1])
                tbc1 = []
                tbc2 = []
                for j in range(len(vc1)):
                    if vc1[j][0] == color and j != i:
                        other_nh = getNeigbourhood(G1, [k[0] for k in vc1], vc1[j][1]).copy()
                        other_nh.sort()
                        if other_nh == nh:
                            # vc1[j] = (new_color, vc1[j][1])
                            tbc1.append(j)
                            count1 += 1

                    if vc2[j][0] == color:
                        other_nh = getNeigbourhood(G2, [k[0] for k in vc2], vc2[j][1]).copy()
                        other_nh.sort()
                        if other_nh == nh:
                            # vc2[j] = (new_color, vc2[j][1])
                            tbc2.append(j)
                            count2 += 1

                for j in range(len(tbc1)):
                    vc1[tbc1[j]] = (new_color, vc1[j][1])

                for j in range(len(tbc2)):
                    vc2[tbc2[j]] = (new_color, vc2[j][1])


    # vc1.sort()
    # vc2.sort()
    print("vc1:", [i[0] for i in vc1])
    print("vc2:", [i[0] for i in vc2])
    print(count1, count2)

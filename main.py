from graph import *
from graph_io import *
from colouring import *
import time

TEST_FILES = [
    "SignOffColRefFri1.grl",
    "SignOffColRefFri2.grl",
    "SignOffColRefFri3.grl",
    "SignOffColRefFri4.grl",
    "SignOffColRefFri5.grl",
    "SignOffColRefFri6.grl",
    # "colorref_largeexample_4_1026.grl", "colorref_largeexample_6_960.grl"
    # "colorref_smallexample_2_49.grl", "colorref_smallexample_4_7.grl",
    # "colorref_smallexample_4_16.grl" , "colorref_smallexample_6_15.grl",
    # "cref9vert3comp_10_27.grl",
    # "cref9vert_4_9.grl"
]
start_time = time.time()
for file_name in TEST_FILES:
    with open('SignOff/' + file_name, 'r') as file:
        graph_list, options = load_graph(file, read_list=True)

        print(file_name)
        print('Sets of possibly isomorphic graphs:')

        paired_graphs = []

        for i in range(len(graph_list)):
            if i not in paired_graphs:
                g1 = graph_list[i]
                x = [i]
                for j in range(len(graph_list)):
                    if i != j:
                        g2 = graph_list[j]
                        if refine(g1, g2):
                            x.append(j)
                            paired_graphs.append(j)
                            if len([x.color for x in g1.vertices]) == len(set([x.color for x in g1.vertices])):
                                res = str(x) + " discrete"
                            else:
                                res = x
                print(res)
    print()
print(time.time() - start_time)

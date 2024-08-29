from graph_io import *
from coloring import *
import time

# List of test graph files to be processed
TEST_FILES = [
    "Test1.grl",
    "Test2.grl",
    "Test3.grl",
    "Test4.grl",
    "Test5.grl",
    "Test6.grl",
]

# Record the start time of the script
start_time = time.time()

# Loop through each file in the list
for file_name in TEST_FILES:
    with open('data/' + file_name, 'r') as file:
        graph_list, options = load_graph(file, read_list=True)

        print(file_name)
        print('Sets of possibly isomorphic graphs:')

        # Keeps track of paired graphs
        paired_graphs = []

        for i in range(len(graph_list)):
            if i not in paired_graphs:
                g1 = graph_list[i]
                x = [i]
                res = None
                for j in range(len(graph_list)):
                    if i != j:
                        g2 = graph_list[j]
                        # Check if the two graphs are isomorphic
                        if refine(g1, g2):
                            x.append(j)
                            paired_graphs.append(j)
                            if len([x.color for x in g1.vertices]) == len(set([x.color for x in g1.vertices])):
                                res = str(x) + " discrete"
                            else:
                                res = x
                print(res)
    print()

# Print the total execution time
print(time.time() - start_time)

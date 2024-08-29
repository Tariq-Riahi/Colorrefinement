# Graph Isomorphism Detection with Color Refinement

This project implements an algorithm for detecting possibly isomorphic graphs using color refinement. The algorithm is applied to a set of graphs, and it identifies pairs of graphs that may be isomorphic.

## Project Structure

- **src/**: Contains the main Python scripts.
- **data/**: Contains the graph files used for testing.

## Requirements

- Python 3.7+

## Usage
1. You can add a graph to the data folder
or use one of the test graphs already present.

2. Run the main script:
   ```bash
   python src/main.py
   ```
3. The script will output sets of possibly isomorphic graphs based on the color refinement algorithm.

## Creating a New Graph File
To create a new graph file for this project, follow the steps below:

1. Format Overview:

- Each graph should be represented as a series of vertices and edges. 
- A file can contain multiple graphs, each separated by the --- Next graph: line.

2. Structure of a Graph:

- Number of vertices: This line indicates the total number of vertices (nodes) in the graph.
- Edge list: Each edge is represented by a pair of numbers separated by a comma. Each pair denotes a connection (edge) between two vertices.

Example:
```text
# Number of vertices:
27
# Edge list:
13,5
3,11
25,22
...

--- Next graph:
# Number of vertices:
27
# Edge list:
0,18
6,14
10,17
...

```
## How It Works

The color refinement algorithm works by iteratively coloring the vertices of a graph until the color distribution stabilizes. If two graphs have the same color distribution after stabilization, they are considered possibly isomorphic.
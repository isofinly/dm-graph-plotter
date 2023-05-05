import networkx as nx
import matplotlib.pyplot as plt

data = [
    [0,4,0,0,3,3,0,5,3,4,0,2],
    [4,0,0,0,0,4,0,0,5,0,0,0],
    [0,0,0,2,4,0,0,3,0,2,0,0],
    [0,0,2,0,1,3,1,4,1,0,4,4],
    [3,0,4,1,0,1,2,0,0,0,1,4],
    [3,4,0,3,1,0,0,2,0,0,3,5],
    [0,0,0,1,2,0,0,0,0,0,0,0],
    [5,0,3,4,0,2,0,0,4,2,5,0],
    [3,5,0,1,0,0,0,4,0,0,0,1],
    [4,0,2,0,0,0,0,2,0,0,0,0],
    [0,0,0,4,1,3,0,5,0,0,0,0],
    [2,0,0,4,4,5,0,0,1,0,0,0]
]

G = nx.Graph()

# Add nodes to the graph
for i in range(len(data)):
    G.add_node(i+1)

# Set the threshold for edge weights
threshold = 3

# Add edges to the graph
for i in range(len(data)):
    for j in range(len(data)):
        if data[i][j] > threshold:
            G.add_edge(i+1, j+1, weight=data[i][j])

# Draw the graph
pos = nx.circular_layout(G)  # Use a circular layout
nx.draw(G, pos, with_labels=True, font_weight='bold')

# Add edge labels
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()

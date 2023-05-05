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

# Define the dictionary for merging nodes
merge_dict = {1: {1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12}, 7: {7}}
# Create a new graph for the merged nodes
merged_G = nx.Graph()

# Add nodes to the merged graph
for nodes in merge_dict.values():
    merged_G.add_node(tuple(sorted(list(nodes))))

# Add edges to the merged graph
for i in range(len(data)):
    for j in range(len(data)):
        if data[i][j] != 0:
            for nodes1 in merge_dict.values():
                if i+1 in nodes1:
                    for nodes2 in merge_dict.values():
                        if j+1 in nodes2 and nodes1 != nodes2:
                            merged_G.add_edge(tuple(sorted(list(nodes1))), tuple(sorted(list(nodes2))), weight=data[i][j])

# Set the circular layout
pos = nx.circular_layout(merged_G)

# Draw the merged graph
nx.draw(merged_G, pos, with_labels=True, font_weight='bold')

# Add edge labels
labels = nx.get_edge_attributes(merged_G, 'weight')
nx.draw_networkx_edge_labels(merged_G, pos, edge_labels=labels)

plt.show()

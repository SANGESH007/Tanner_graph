# This program is used to create a Tanner graph visualization for LDPC H matrix
import matplotlib.pyplot as plt
import scipy.io
import numpy as np

# Load the matrix from the MATLAB .mat file
mat_data = scipy.io.loadmat('H.mat')  # Replace "H.mat" with the actual file path of the matrix
matrix = mat_data['H']

# Plot the graph using matplotlib
fig, ax = plt.subplots(figsize=(10, 5))

# Plot the CN nodes starting from 32
cn_nodes = range(32, 32 + matrix.shape[0])
ax.scatter(cn_nodes, np.zeros_like(cn_nodes), label='CN', color='skyblue', s=50)

# Plot the VN nodes
vn_nodes = range(matrix.shape[1])
ax.scatter(vn_nodes, np.ones_like(vn_nodes), label='VN', color='orange', s=50)

# Connect CN to VN based on matrix values
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if matrix[i, j] == 1:
            ax.plot([i + 32, j], [0, 1], color='gray', linestyle='-', linewidth=0.5)

# Set title
ax.set_title('Bipartite Graph of CN and VN Connections')

# Add legend
ax.legend()

# Save the graph
plt.savefig('bipartite_graph_matplotlib.png', dpi=1000)

plt.show()

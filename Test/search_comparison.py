import json
import matplotlib.pyplot as plt

# Load runtime data from JSON files
with open("Cache/p_bfs_runtimedata.json", "r") as f:
    data1 = json.load(f)
with open("Cache/p_dfs_runtimedata.json", "r") as f:
    data2 = json.load(f)

# Get shared keys
shared_keys = set(data1.keys()) & set(data2.keys())

# Prepare data for plotting
labels = list(shared_keys)
values1 = [data1[key] for key in labels]
values2 = [data2[key] for key in labels]

# Save original values for annotation
original_values1 = values1.copy()
original_values2 = values2.copy()

# Create the bar chart
x = range(len(labels))
width = 0.35
fig, ax = plt.subplots()

# Find index of execution time
execution_time_index = labels.index('execution_time_sec')

# Scale execution_time for plotting (to ms)
values1[execution_time_index] *= 1000
values2[execution_time_index] *= 1000

# Draw bars
rects1 = ax.bar(x, values1, width, label='P-BFS')
rects2 = ax.bar([i + width for i in x], values2, width, label='P-DFS')

# Annotate the bars with the original values
def autolabel(rects, originals):
    for i, rect in enumerate(rects):
        height = rect.get_height()
        label_val = originals[i]
        if i == execution_time_index:
            label_val = f'{label_val:.3f}s'
        else:
            label_val = f'{label_val}'
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,
                label_val,
                ha='center', va='bottom', fontsize=8)

autolabel(rects1, original_values1)
autolabel(rects2, original_values2)

# Add labels, title, etc.
ax.set_ylabel('Values')
ax.set_title('Comparison of P-BFS and P-DFS Runtime Data')
ax.set_xticks([i + width / 2 for i in x])
ax.set_xticklabels(labels)
ax.legend()

# Display the chart
plt.tight_layout()
plt.show()

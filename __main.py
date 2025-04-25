import random
import math
import matplotlib.pyplot as plt
from matplotlib.path import Path
import modules.fs_operations as fs_operations
import modules.plot_operations as plot_operations
import modules.point_operations as point_operations
import modules.graph_searching_algorithms.parallel_bfs as bfs_operations
import modules.area_operations as area_operations
import modules.graph_searching_algorithms.p_bfs as p_bfs_operations
import modules.graph_searching_algorithms.p_dfs as p_dfs_operations
import modules.maximize_nodes as maximize_nodes_operations
# Set random seed for reproducibility


config = fs_operations.read_file("config.json")
# print(config)

# Generate random latitude/longitude points
points = fs_operations.read_file("Datasets/points.json")

start_point = point_operations.get_points_by_name(points,config["start_point"])
end_point = point_operations.get_points_by_name( points,config["end_point"])



rectangle = area_operations.calculate_rectangle(start_point, end_point)

# Build polygon path for checking containment
polygon_path = Path(rectangle + [rectangle[0]])  # Close the polygon

# Filter points inside the polygon
filtered_points = [p for p in points if polygon_path.contains_point((p["x"], p["y"]))]

outliers = [p for p in points if not polygon_path.contains_point((p["x"], p["y"]))]

# Output
# print("Filtered Points (Inside Rectangle Region):")
# for p in filtered_points:
#     print(p)

fs_operations.write_file("Cache/filtered_points.json", filtered_points)

fs_operations.write_file("Cache/outliers.json", outliers)

if __name__ == "__main__": 
    # from modules.graph_searching_algorithms.p_bfs import p_bfs_all_paths_parallel
    from modules.graph_searching_algorithms.p_dfs import parallel_dfs_all_paths  
    
    # import your function if needed

    # paths = p_bfs_all_paths_parallel(filtered_points, start_point, end_point)
    # paths = parallel_dfs_all_paths(filtered_points, start_point, end_point)
    
    # print(paths)


# paths = bfs_operations.p_bfs(filtered_points, start_point, end_point)
# paths = p_bfs_operations.p_bfs(filtered_points, start_point, end_point)

# print(paths)

# Plot everything
"""plt.figure(figsize=(12, 6))

# Plot outliers in grey
for p in outliers:
    plt.plot(p["x"], p["y"], 'o', color='grey')
    plt.text(p["x"] + 1, p["y"] + 1, f'{p["name"]} ({p["x"]},{p["y"]})', fontsize=8, color='grey')

# Plot filtered points in cyan
for p in filtered_points:
    plt.plot(p["x"], p["y"], 'o', color='purple')
    plt.text(p["x"] + 1, p["y"] + 1, f'{p["name"]} ({p["x"]},{p["y"]})', fontsize=8, color='purple')


# Rectangle shading
x_rect, y_rect = zip(*rectangle)
plt.fill(x_rect + (x_rect[0],), y_rect + (y_rect[0],), color='orange', alpha=0.3, label='Shaded Region')

# Plot line and points
plt.plot([start_point["x"], end_point["x"]], [start_point["y"], end_point["y"]], 'r-', label='Path Line')
plt.plot(start_point["x"], start_point["y"], 'go', label='Start Point')  # Green dot
plt.plot(end_point["x"], end_point["y"], 'ro', label='End Point')  # Red dot

plt.title("Geo Points with Shaded Region Around Path")
plt.xlabel("Longitude (x)")
plt.ylabel("Latitude (y)")
plt.grid(True)
plt.xlim(-190, 190)
plt.ylim(-100, 100)
plt.legend()
plt.tight_layout()
plt.show()"""

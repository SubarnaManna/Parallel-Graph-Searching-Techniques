import matplotlib.pyplot as plt
import math
from collections import deque
from modules.point_operations import get_points_by_name, distance

# --- Helper: Distance Function ---


# --- Build Graph: Connect every pair in filtered points ---



def p_bfs(filtered_points,start_point, end_point):

    print("Filtered Points: ")
    graph = {}
    for p1 in filtered_points:
        graph[p1["name"]] = []
        for p2 in filtered_points:
            if p1 != p2:
                dist = distance(p1, p2)
                graph[p1["name"]].append((p2["name"], dist))
    # --- BFS for all shortest paths ---
    # def get_point_by_name(name):
    #     return next(p for p in filtered_points if p["name"] == name)
    
    def bfs_all_shortest_paths(start, end):
        queue = deque()
        queue.append(([start], 0))  # (path_so_far, total_distance)
        visited = {start: 0}
        results = []

        while queue:
            path, total_dist = queue.popleft()
            current = path[-1]
            if current == end:
                results.append((path, total_dist))
                continue
            for neighbor, dist in graph[current]:
                if neighbor not in path:  # avoid cycles
                    new_dist = total_dist + dist
                    if visited.get(neighbor, float("inf")) >= new_dist:
                        visited[neighbor] = new_dist
                        queue.append((path + [neighbor], new_dist))
        
        # Sort results by distance
        results.sort(key=lambda x: x[1])
        return results

    # --- Run BFS from K to R ---
    paths = bfs_all_shortest_paths(start_point["name"], end_point["name"])

    # --- Print Paths with Distances ---
    for i, (path, dist) in enumerate(paths, 1):
        print(f"Path {i}: {' -> '.join(path)} | Distance: {dist:.2f}")

    return paths

    """# --- Plotting the Paths ---
    plt.figure(figsize=(12, 6))

    # Plot all filtered nodes
    for p in filtered_points:
        plt.plot(p["x"], p["y"], 'o', color='cyan')
        plt.text(p["x"] + 1, p["y"] + 1, p["name"], fontsize=9, color='cyan')

    # Plot shortest paths with distance as edge weight
    colors = ['red', 'green', 'blue', 'purple', 'orange']
    for i, (path, dist) in enumerate(paths[:5]):  # limit to first 5 paths for clarity
        for j in range(len(path) - 1):
            p1 = get_point_by_name(path[j])
            p2 = get_point_by_name(path[j + 1])
            plt.plot([p1["x"], p2["x"]], [p1["y"], p2["y"]], '-', color=colors[i % len(colors)])
            mid_x = (p1["x"] + p2["x"]) / 2
            mid_y = (p1["y"] + p2["y"]) / 2
            d = distance(p1, p2)
            plt.text(mid_x, mid_y, f"{d:.1f}", fontsize=8, color=colors[i % len(colors)])

    plt.title("Shortest Paths from K to R (Filtered Points)")
    plt.xlabel("Longitude (x)")
    plt.ylabel("Latitude (y)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
"""

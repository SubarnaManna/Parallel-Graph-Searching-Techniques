import json

def get_top_paths_by_nodes_within_range(json_file):
    with open(json_file, 'r') as f:
        paths = json.load(f)

    if not paths:
        print("No paths found.")
        return

    base_distance = paths[0]["distance"]
    max_distance = 1.3 * base_distance

    # Filter paths under threshold
    filtered = [p for p in paths if p["distance"] <= max_distance]

    # Sort by number of nodes (descending), then by distance (ascending)
    sorted_paths = sorted(filtered, key=lambda x: (-len(x["path"]), x["distance"]))

    # Take top 5
    top_5 = sorted_paths[:5]

    # Print the results
    print(f"Base Distance: {base_distance:.3f} | 30% Range: {max_distance:.3f}\n")
    for i, p in enumerate(top_5, 1):
        print(f"#{i}: Nodes = {len(p['path'])} | Distance = {p['distance']:.3f} | Path = {' -> '.join(p['path'])}")



def get_top_paths_by_nodes_within_range_from_paths(paths):
    """
    Takes a list of paths (already in memory) and returns top 5 filtered paths.

    Each path should be a dict: { "path": [...], "distance": ... }
    """

    if not paths:
        return []

    # Assume paths are already sorted by distance (or at least first path is the shortest)
    base_distance = paths[0]["distance"]
    max_distance = 1.3 * base_distance

    # Filter paths under 30% threshold
    filtered = [p for p in paths if p["distance"] <= max_distance]

    # Sort by number of nodes (descending), then by distance (ascending)
    sorted_paths = sorted(filtered, key=lambda x: (-len(x["path"]), x["distance"]))

    # Take top 5
    top_5 = sorted_paths[:5]

    return top_5

# Example usage
# get_top_paths_by_nodes_within_range("./Cache/all_parallel_bfs_paths.json")

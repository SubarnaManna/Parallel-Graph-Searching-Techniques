"""import json
from math import sqrt
from itertools import permutations
from multiprocessing import Pool, Manager

def distance(p1, p2):
    return sqrt((p1["x"] - p2["x"])**2 + (p1["y"] - p2["y"])**2)

def build_graph(points):
    graph = {p["name"]: [] for p in points}
    for p1 in points:
        for p2 in points:
            if p1 != p2:
                dist = distance(p1, p2)
                graph[p1["name"]].append((p2["name"], dist))
    return graph

def get_point(points, name):
    return next(p for p in points if p["name"] == name)

def find_all_paths(graph, current, end, path, all_paths):
    path.append(current)
    if current == end:
        all_paths.append(list(path))
    else:
        for neighbor, _ in graph[current]:
            if neighbor not in path:
                find_all_paths(graph, neighbor, end, path, all_paths)
    path.pop()

def compute_path_distance(path, points):
    total = 0
    for i in range(len(path) - 1):
        p1 = get_point(points, path[i])
        p2 = get_point(points, path[i + 1])
        total += distance(p1, p2)
    return {"path": path, "distance": round(total, 3)}

def p_bfs_all_paths_parallel(points, start, end):
    graph = build_graph(points)
    all_paths = []
    find_all_paths(graph, start["name"], end["name"], [], all_paths)

    with Pool() as pool:
        results = pool.starmap(compute_path_distance, [(path, points) for path in all_paths])

    results.sort(key=lambda x: x["distance"])
    with open("./Cache/all_parallel_paths.json", "w") as f:
        json.dump(results, f, indent=4)

    print(f"Found {len(results)} paths. Results written to 'all_parallel_paths.json'.")
    return results
"""

import json
import time
from math import sqrt
from itertools import permutations
from multiprocessing import Pool
from datetime import datetime

def distance(p1, p2):
    return sqrt((p1["x"] - p2["x"])**2 + (p1["y"] - p2["y"])**2)

def build_graph(points):
    graph = {p["name"]: [] for p in points}
    for p1 in points:
        for p2 in points:
            if p1 != p2:
                dist = distance(p1, p2)
                graph[p1["name"]].append((p2["name"], dist))
    return graph

def get_point(points, name):
    return next(p for p in points if p["name"] == name)

def find_all_paths(graph, current, end, path, all_paths):
    path.append(current)
    if current == end:
        all_paths.append(list(path))
    else:
        for neighbor, _ in graph[current]:
            if neighbor not in path:
                find_all_paths(graph, neighbor, end, path, all_paths)
    path.pop()

def compute_path_distance(path, points):
    total = 0
    for i in range(len(path) - 1):
        p1 = get_point(points, path[i])
        p2 = get_point(points, path[i + 1])
        total += distance(p1, p2)
    return {"path": path, "distance": round(total, 3)}

def p_bfs_all_paths_parallel(points, start, end):
    start_time = time.time()
    start_timestamp = datetime.now().isoformat()

    graph = build_graph(points)
    all_paths = []
    find_all_paths(graph, start["name"], end["name"], [], all_paths)

    with Pool() as pool:
        results = pool.starmap(compute_path_distance, [(path, points) for path in all_paths])

    results.sort(key=lambda x: x["distance"])

    with open("./Cache/all_parallel_bfs_paths.json", "w") as f:
        json.dump(results, f, indent=4)

    end_time = time.time()
    end_timestamp = datetime.now().isoformat()
    duration = round(end_time - start_time, 3)
    throughput = round(len(results) / duration, 3) if duration > 0 else None

    runtime_metrics = {
        "start_timestamp": start_timestamp,
        "end_timestamp": end_timestamp,
        "execution_time_sec": duration,
        "total_paths": len(results),
        "throughput_paths_per_sec": throughput,
        "compute_notes": {
            "processes_used": Pool()._processes,
            "parallel": True,
            "memory_estimate": "TBD",
            "workload_distribution": "TBD"
        }
    }

    with open("./Cache/p_bfs_runtimedata.json", "w") as f:
        json.dump(runtime_metrics, f, indent=4)

    print(f"Found {len(results)} paths in {duration} sec. Runtime data written to 'p_bfs_runtimedata.json'.")
    return results

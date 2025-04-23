import json
import time
from math import sqrt
from multiprocessing import Pool
from datetime import datetime

def distance(p1, p2):
    return sqrt((p1["x"] - p2["x"])**2 + (p1["y"] - p2["y"])**2)

def build_graph(points):
    graph = {p["name"]: [] for p in points}
    for p1 in points:
        for p2 in points:
            if p1 != p2:
                d = distance(p1, p2)
                graph[p1["name"]].append((p2["name"], d))
    return graph

def get_point(points, name):
    return next(p for p in points if p["name"] == name)

def dfs_collect_paths(graph, current, end, path, all_paths):
    path.append(current)
    if current == end:
        all_paths.append(list(path))
    else:
        for neighbor, _ in graph[current]:
            if neighbor not in path:
                dfs_collect_paths(graph, neighbor, end, path, all_paths)
    path.pop()

def compute_path_distance(path, points):
    total = 0.0
    for i in range(len(path) - 1):
        a = get_point(points, path[i])
        b = get_point(points, path[i+1])
        total += distance(a, b)
    return {"path": path, "distance": round(total, 3)}

def parallel_dfs_all_paths(points, start, end):
    # ---- Metrics start ----
    t0 = time.time()
    ts_start = datetime.now().isoformat()

    # ---- Build graph & collect all paths via DFS ----
    graph = build_graph(points)
    all_paths = []
    dfs_collect_paths(graph, start["name"], end["name"], [], all_paths)

    # ---- Parallel distance computation ----
    with Pool() as pool:
        results = pool.starmap(compute_path_distance, [(p, points) for p in all_paths])

    # ---- Sort & write paths ----
    results.sort(key=lambda x: x["distance"])
    with open("./Cache/all_parallel_dfs_paths.json", "w") as f:
        json.dump(results, f, indent=4)

    # ---- Metrics end ----
    t1 = time.time()
    ts_end = datetime.now().isoformat()
    duration = round(t1 - t0, 3)
    throughput = round(len(results) / duration, 3) if duration > 0 else None

    runtime_data = {
        "start_timestamp": ts_start,
        "end_timestamp": ts_end,
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
    with open("./Cache/p_dfs_runtimedata.json", "w") as f:
        json.dump(runtime_data, f, indent=4)

    print(f"DFS found {len(results)} paths in {duration}s. Results in 'all_parallel_dfs_paths.json' and metrics in 'p_dfs_runtimedata.json'.")
    return results


    
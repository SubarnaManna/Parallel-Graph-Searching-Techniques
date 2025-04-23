
import math
def get_points_by_name(points, name):
    """
    Get points by name from the list of points.
    
    :param points: List of point dictionaries.
    :param name: Name of the point to search for.
    :return: List of points with the specified name.
    """
    for point in points:
        if point["name"] == name:
            return point 
# return [point if point["name"] == name]

def distance(p1, p2):
    return math.hypot(p1["x"] - p2["x"], p1["y"] - p2["y"])

def get_point_by_name(points,name):
    return next(p for p in points if p["name"] == name)
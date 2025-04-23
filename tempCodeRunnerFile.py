def get_point_by_name(name):
    return next(p for p in points if p["name"] == name)
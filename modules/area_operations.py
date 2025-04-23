
import math


def calculate_rectangle(start, end, width_ratio=0.30):
    # Vector from start to end
    dx = end["x"] - start["x"]
    dy = end["y"] - start["y"]
    length = math.hypot(dx, dy)

    # Normalize perpendicular vector (rotate 90°)
    perp_dx = -dy / length
    perp_dy = dx / length

    # Half of width (7.5% of length on each side)
    half_width = (width_ratio * length) / 2

    # Four corners of rectangle
    corner1 = (start["x"] + perp_dx * half_width, start["y"] + perp_dy * half_width)
    corner2 = (start["x"] - perp_dx * half_width, start["y"] - perp_dy * half_width)
    corner3 = (end["x"] - perp_dx * half_width, end["y"] - perp_dy * half_width)
    corner4 = (end["x"] + perp_dx * half_width, end["y"] + perp_dy * half_width)

    return [corner1, corner2, corner3, corner4]
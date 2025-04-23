import random, json

points = [
    {"name": chr(65 + i), "x": random.randint(-180, 180), "y": random.randint(-90, 90)}
    for i in range(20)
]

with open('points.json', 'w') as f:
    json.dump(points, f, indent=4)
    f.close()
print("Points generated and saved to points.json")  



from matplotlib import pyplot as plt


"""def plot_points(points, title="TestCase Points"):
    # Plotting
    plt.figure(figsize=(12, 6))
    for point in points:
        plt.plot(point["x"], point["y"], 'bo')  # Blue dot
        label = f'{point["name"]} ({point["x"]:.1f}, {point["y"]:.1f})'
        plt.text(point["x"] + 1, point["y"] + 1, label, fontsize=8)

    plt.title("Geo Points with Coordinates")
    plt.xlabel("Longitude (x)")
    plt.ylabel("Latitude (y)")
    plt.grid(True)
    plt.xlim(-190, 190)
    plt.ylim(-100, 100)
    plt.tight_layout()
    plt.show()
    """
    

# def plot_line(point1 ,point2, title="TestCase Points"):
    
class PlotOperations:
    def __init__(self):
        # self.points = points
        pass
    def get_plot():
        plt= plt.figure(figsize=(12, 6))
        return plt
    
    def show_plot(self, plt,title="TestCase Points"):
        plt.title(title)
        plt.xlabel("Longitude (x)")
        plt.ylabel("Latitude (y)")
        plt.grid(True)
        plt.xlim(-190, 190)
        plt.ylim(-100, 100)
        plt.tight_layout()
        plt.show()

    
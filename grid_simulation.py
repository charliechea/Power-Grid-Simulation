
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

def draw_grid(buses, lines, positions, failed_line=None):
    for bus, (x, y) in positions.items():
        power = buses[bus]
        color = 'green' if power > 0 else 'red'
        plt.scatter(x, y, s=600, color=color)
        plt.text(x, y, f"{bus}\n{power} MW", color='white', ha='center', va='center', fontsize=9)

    for line in lines:
        x0, y0 = positions[line[0]]
        x1, y1 = positions[line[1]]
        if failed_line == line or failed_line == tuple(reversed(line)):
            plt.plot([x0, x1], [y0, y1], 'k--', linewidth=2, label='Failed Line')
        else:
            plt.plot([x0, x1], [y0, y1], 'k-', linewidth=2)

    plt.title("Simple Power Grid Simulation", fontsize=14)
    plt.axis('off')
    plt.show()

# Define buses and power in MW
buses = {
    "Bus 1 (Gen)": 100,   # Generator
    "Bus 2 (Load)": -60,  # Load
    "Bus 3 (Load)": -40   # Load
}

# Define transmission lines (connections)
lines = [
    ("Bus 1 (Gen)", "Bus 2 (Load)"),
    ("Bus 1 (Gen)", "Bus 3 (Load)")
]

# Coordinates for plotting (manual layout)
positions = {
    "Bus 1 (Gen)": (0, 0),
    "Bus 2 (Load)": (2, 1),
    "Bus 3 (Load)": (2, -1)
}

# Draw the network

draw_grid(buses, lines, positions, failed_line=("Bus 1 (Gen)", "Bus 2 (Load)"))



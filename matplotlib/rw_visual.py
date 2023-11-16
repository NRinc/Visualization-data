import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:  # Loop to generate random walks
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(dpi= 168, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    # plt.plot(rw.x_values, rw.y_values, '-', c='blue', linewidth=1)
    # # Emphasize the first and last points.
    # plt.plot(0, 0, 'go', markersize=7)  # Green dot for start point
    # plt.plot(rw.x_values[-1], rw.y_values[-1], 'ro', markersize=7)  # Red dot for end point

    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolor='none', s=1)
    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=35)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',s=35)

    # Remove the axes.
    plt.axis('off')

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == 'n':
        break  # Exit the loop if the user enters 'n'





















"""
import matplotlib.pyplot as plt

x_values = list(range(1, 5000))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
 edgecolor='none', s=10)
# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0,5500 , 0, 130000000000])
plt.show()
"""

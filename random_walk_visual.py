import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making random walks.
while True:

    # Make a random walk.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)
    # Show the disparity between the first and last points.
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, edgecolors='none', s=1)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Equal spacing between tick marks.
    ax.set_aspect('equal')

    # Display random walk.
    plt.show()

    keep_running = input("Make another random walk? (y/n): ")
    # Stop making random walks.
    if keep_running == 'n':
        break


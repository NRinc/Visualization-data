import matplotlib.pyplot as plt
import pygal
from random_walk import RandomWalk
from die import Die

# Die Rolling Visualization with Matplotlib

die_1 = Die()
die_2 = Die()

results = [die_1.roll() + die_2.roll() for _ in range(50000)]

max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]

plt.bar(range(2, max_result + 1), frequencies, align='center', alpha=0.7)
plt.title("Results of rolling two D6 dice 50000 times")
plt.xlabel("Result")
plt.ylabel("Frequency of Result")
plt.show()

# Random Walk Visualization with Pygal

rw = RandomWalk(50000)
rw.fill_walk()

hist = pygal.Line()

hist.title = "Random Walk Visualization"
hist.add("Random Walk", [(rw.x_values[i], rw.y_values[i]) for i in range(rw.num_points)])
hist.render_to_file('random_walk_visual.svg')

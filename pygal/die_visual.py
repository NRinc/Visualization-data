import pygal
from die import Die

# Create a D6.
die_1 = Die()
die_2 = Die()


# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for _ in range(50000)]

# Analyze the results using list comprehensions.
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(1, max_result + 1)]

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 50000 times."
# Use list comprehension to automatically generate x_labels.
hist.x_labels = [str(value) for value in range(1, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6*D6', frequencies)
hist.render_to_file('die_visual.svg')

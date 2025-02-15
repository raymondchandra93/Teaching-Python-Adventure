import matplotlib.pyplot as plt

""" -- Matplotlib -- """

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# -- Basic Plot
plt.plot(x, y)

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')

# Display the plot
# plt.show()

# -- Bar Chart
plt.bar(x, y)
# plt.show()

# -- Scatter Plot
plt.scatter(x, y)
# plt.show()

# -- Histogram
data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
plt.hist(data, bins=5)
# plt.show()

# -- Customizing Plot
plt.plot(x, y, color='red', linestyle='--', marker='o')
plt.grid(True)
# plt.show()

# -- Multiple Plot
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.plot(x, y1, label='Line 1', color='blue')
plt.plot(x, y2, label='Line 2', color='green')

plt.legend()  # Add legend
#plt.show()

# -- Subplot
plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st plot
plt.plot(x, y1)
plt.title('First Plot')

plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd plot
plt.plot(x, y2)
plt.title('Second Plot')

plt.tight_layout()  # Adjust spacing
#plt.show()

# -- Saving a plot
plt.plot(x, y)
plt.savefig('plot.png')  # Saves the plot as an image file
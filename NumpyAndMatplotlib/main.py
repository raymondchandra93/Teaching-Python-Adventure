import numpy as np
import matplotlib.pyplot as plt

# -- Numpy Array
l = [1, 2, 3, 4, 5]
a = np.array([1, 2, 3, 4, 5])

print(l * 2)
print(a * 2)

# -- Numpy Reshape
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape(2, 3)        # Reshape into 2 rows, 3 columns
print(reshaped_arr)

# -- Numpy Arrange
print(np.arange(3))             # [0,1,2] - Starts from 0, stops before 3, step is 1.
print(np.arange(3, 7, 2))       # [3,5] - Starts from 3, adds 2, stops before 7.

# -- Numpy Zeros
zeros_arr = np.zeros((2, 3))    # 2x3 array of zeros
print(zeros_arr)

# -- Numpy Ones
ones_arr = np.ones((3, 2))      # 3x2 array of ones
print(ones_arr)

# -- Numpy Linspace
linspace_arr = np.linspace(0, 10, 5)  # 5 evenly spaced values between 0 and 10
print(linspace_arr)

# -- Statistical Functions
arr = np.array([10, 20, 30, 40])

print(np.mean(arr))   # 25.0  (average)
print(np.median(arr)) # 25.0  (median)
print(np.std(arr))    # 11.18 (standard deviation)
print(np.min(arr))    # 10    (minimum value)
print(np.max(arr))    # 40    (maximum value)

# -- Indexing and Slicing
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])    # 10 (first element)
print(arr[-1])   # 50 (last element)
print(arr[1:4])  # [20, 30, 40] (slicing)

# -- Boolean Masking & Filtering
arr = np.array([1, 2, 3, 4, 5])

print(arr[arr > 3])  # [4 5]
print(arr % 2 == 0)  # [False  True False  True False]

# -- Matrix Operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(np.dot(A, B))   # Matrix multiplication
print(A.T)            # Transpose of A
print(np.linalg.inv(A)) # Inverse of A

# -- Random Number Generation
andom_arr = np.random.rand(3, 3)    # Random values between 0 and 1
rand_int_arr = np.random.randint(1, 10, (2, 2))  # Random integers from 1 to 9

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
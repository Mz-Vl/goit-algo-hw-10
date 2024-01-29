import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


# Definition of the function and integration limits
def f(x):
    return x ** 2


a = 0  # Lower limit
b = 2  # Upper limit

# Creating a range of values for x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Creating the plot
fig, ax = plt.subplots()

# Plotting the function
ax.plot(x, y, 'r', linewidth=2)

# Filling the area under the curve
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Setting up the plot
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Adding integration limits and plot title
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Integration graph f(x) = x^2 from ' + str(a) + ' to ' + str(b))
plt.grid()
plt.show()

# Monte Carlo method for integral estimation
max_y = f(b)  # Maximum value of f(x) on the interval [a, b]
num_points = 70000
random_points = np.random.uniform(a, b, num_points)
random_values = np.random.uniform(0, max_y, num_points)
points_under_curve = sum(random_values <= f(random_points))
integral_estimate = (points_under_curve / num_points) * (b - a) * max_y

# Calculating the integral using the quad function
result_quad, error_quad = spi.quad(f, a, b)

# Displaying the results
print(f"Evaluation of the integral (Monte Carlo): {integral_estimate}")
print("Analytical result (quad):", result_quad)

# Displaying the deviation of the Monte Carlo method from the analytical result
deviation = np.abs(integral_estimate - result_quad)
print(f"Deviation: {deviation}")

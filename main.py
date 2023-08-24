
import matplotlib.pyplot as plt
import numpy as np

# Get inputs from the user
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# Define the quadratic equation function
def quadratic_equation(x):
    return a * x**2 + b * x + c

# Generate x values for the plot
x_values = np.linspace(-10, 10, 400)  # You can adjust the range and number of points

# Calculate y values using the quadratic equation
y_values = quadratic_equation(x_values)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label=f'{a}x^2 + {b}x + {c} = 0')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of the Quadratic Equation')
plt.grid(True)
plt.legend()
plt.show()



# import matplotlib.pyplot as plt
# import numpy as np

# # Get inputs from the user
# a = float(input("Enter the value of a: "))
# b = float(input("Enter the value of b: "))
# c = float(input("Enter the value of c: "))

# # Define the quadratic equation function
# def quadratic_equation(x):
#     return a * x**2 + b * x + c

# # Generate x values for the plot
# x_values = np.linspace(-10, 10, 400)  # You can adjust the range and number of points

# # Calculate y values using the quadratic equation
# y_values = quadratic_equation(x_values)

# # Create the plot
# plt.figure(figsize=(8, 6))
# plt.plot(x_values, y_values, label=f'{a}x^2 + {b}x + {c} = 0')
# plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
# plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
# plt.xlabel('x')


import os
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    generate_plot()  # Generate the plot
    return render_template('index.html')

def generate_plot():
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
    plt.savefig('static/plot.png')  # Save the plot image
    plt.close()  # Close the plot to prevent displaying in the console

if __name__ == '__main__':
    # os.makedirs('static', exist_ok=True)  # Create 'static' directory if it doesn't exist
    # app.run(host='0.0.0.0', port=8000)
    # static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    # os.makedirs(static_dir, exist_ok=True)  # Create 'static' directory if it doesn't exist
    # app.run(host='0.0.0.0', port=8000)
    # jenkins_home = os.path.expanduser('~jenkins')  # Modify 'jenkins' to the actual Jenkins username
    # static_dir = os.path.join(jenkins_home, 'static')
    # os.makedirs(static_dir, exist_ok=True)  # Create 'static' directory if it doesn't exist
    # app.run(host='0.0.0.0', port=8000)
    
    user_home = os.path.expanduser('~')  # Get the home directory of the user (Jenkins)
    static_dir = os.path.join(user_home, 'static')
    os.makedirs(static_dir, exist_ok=True)  # Create 'static' directory if it doesn't exist
    app.run(host='0.0.0.0', port=9000)


# plt.ylabel('y')
# plt.title('Graph of the Quadratic Equation')
# plt.grid(True)
# plt.legend()
# plt.show()


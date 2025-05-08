
# # import matplotlib.pyplot as plt
# # import numpy as np

# # # Get inputs from the user
# # a = float(input("Enter the value of a: "))
# # b = float(input("Enter the value of b: "))
# # c = float(input("Enter the value of c: "))

# # # Define the quadratic equation function
# # def quadratic_equation(x):
# #     return a * x**2 + b * x + c

# # # Generate x values for the plot
# # x_values = np.linspace(-10, 10, 400)  # You can adjust the range and number of points

# # # Calculate y values using the quadratic equation
# # y_values = quadratic_equation(x_values)

# # # Create the plot
# # plt.figure(figsize=(8, 6))
# # plt.plot(x_values, y_values, label=f'{a}x^2 + {b}x + {c} = 0')
# # plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
# # plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
# # plt.xlabel('x')


# # import os
# # import matplotlib.pyplot as plt
# # import numpy as np
# # from flask import Flask, render_template
# # app.debug = True

# # app = Flask(__name__)

# # @app.route('/')
# # def index():
# #     generate_plot()  # Generate the plot
# #     return render_template('index.html')

# # def generate_plot():
# #     # Get inputs from the user
# #     a = float(input("Enter the value of a: "))
# #     b = float(input("Enter the value of b: "))
# #     c = float(input("Enter the value of c: "))

# #     # Define the quadratic equation function
# #     def quadratic_equation(x):
# #         return a * x**2 + b * x + c

# #     # Generate x values for the plot
# #     x_values = np.linspace(-10, 10, 400)  # You can adjust the range and number of points

# #     # Calculate y values using the quadratic equation
# #     y_values = quadratic_equation(x_values)

# #     # Create the plot
# #     plt.figure(figsize=(8, 6))
# #     plt.plot(x_values, y_values, label=f'{a}x^2 + {b}x + {c} = 0')
# #     plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
# #     plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
# #     plt.xlabel('x')
# #     plt.ylabel('y')
# #     plt.title('Graph of the Quadratic Equation')
# #     plt.grid(True)
# #     plt.legend()
# #     plt.savefig('static/plot.png')  # Save the plot image
# #     plt.close()  # Close the plot to prevent displaying in the console

# # if __name__ == '__main__':
# #     # os.makedirs('static', exist_ok=True)  # Create 'static' directory if it doesn't exist
# #     # app.run(host='0.0.0.0', port=8000)
# #     # static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
# #     # os.makedirs(static_dir, exist_ok=True)  # Create 'static' directory if it doesn't exist
# #     # app.run(host='0.0.0.0', port=8000)
# #     # jenkins_home = os.path.expanduser('~jenkins')  # Modify 'jenkins' to the actual Jenkins username
# #     # static_dir = os.path.join(jenkins_home, 'static')
# #     # os.makedirs(static_dir, exist_ok=True)  # Create 'static' directory if it doesn't exist
# #     # app.run(host='0.0.0.0', port=8000)
    
# #     user_home = os.path.expanduser('~')  # Get the home directory of the user (Jenkins)
# #     static_dir = os.path.join(user_home, 'static')
# #     os.makedirs(static_dir, exist_ok=True)  # Create 'static' directory if it doesn't exist
# #     app.run(host='0.0.0.0', port=8000)


# # plt.ylabel('y')
# # plt.title('Graph of the Quadratic Equation')
# # plt.grid(True)
# # plt.legend()
# # plt.show()



# from flask import Flask, render_template, request, redirect, url_for
# import os
# import matplotlib.pyplot as plt
# import numpy as np


# app = Flask(__name__)
# app.debug = True

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         # Get user input from the form
#         a = float(request.form['a'])
#         b = float(request.form['b'])
#         c = float(request.form['c'])
        
#         generate_plot(a, b, c)  # Generate the plot with user input values
    
#     return render_template('index.html')

# def generate_plot(a, b, c):
#     # Define the quadratic equation function
#     def quadratic_equation(x):
#         return a * x**2 + b * x + c

#     # Generate x values for the plot
#     x_values = np.linspace(-10, 10, 400)  # You can adjust the range and number of points

#     # Calculate y values using the quadratic equation
#     y_values = quadratic_equation(x_values)

#     # Create the plot
#     plt.figure(figsize=(8, 6))
#     plt.plot(x_values, y_values, label=f'{a}x^2 + {b}x + {c} = 0')
#     plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
#     plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.title('Graph of the Quadratic Equation')
#     plt.grid(True)
#     plt.legend()
#     static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
#     os.makedirs(static_dir, exist_ok=True)
#     plot_path = os.path.join(static_dir, 'plot.png')
#     plt.savefig(plot_path)
    
#     plt.close()  # Close the plot to prevent displaying in the console
    
#     # plt.savefig('static/plot.png')  # Save the plot image
#     # plt.close()  # Close the plot to prevent displaying in the console

# if __name__ == '__main__':
#     os.makedirs('static', exist_ok=True)  # Create 'static' directory if it doesn't exist
#     app.run(host='0.0.0.0', port=8000)



from flask import Flask, render_template, request, redirect, url_for
import os
import matplotlib.pyplot as plt
import numpy as np

# 🔐 Hardcoded secret (vulnerability)
SECRET_KEY = "supersecretkey123"

app = Flask(__name__)
app.secret_key = SECRET_KEY  # 🔐 using hardcoded key
app.debug = True  # 🔥 Debug mode enabled

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 🛑 No input validation or sanitization
        a = float(request.form['a'])
        b = float(request.form['b'])
        c = float(request.form['c'])
        
        # 🚨 Eval usage (DANGEROUS — code injection risk)
        user_input = request.form.get('expression', 'a + b + c')
        result = eval(user_input)  # ⚠️ Intentionally dangerous

        generate_plot(a, b, c)
        return render_template('index.html', result=result)

    return render_template('index.html')

def generate_plot(a, b, c):
    def quadratic_equation(x):
        return a * x**2 + b * x + c

    x_values = np.linspace(-10, 10, 400)
    y_values = quadratic_equation(x_values)

    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label=f'{a}x^2 + {b}x + {c} = 0')
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph of the Quadratic Equation')
    plt.grid(True)
    plt.legend()

    # 🛑 Path traversal risk if user input is involved
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    os.makedirs(static_dir, exist_ok=True)
    plot_path = os.path.join(static_dir, 'plot.png')
    plt.savefig(plot_path)
    plt.close()

@app.after_request
def add_headers(response):
    # 🚫 No security headers set (CSP, X-Content-Type-Options, etc.)
    return response

if __name__ == '__main__':
    os.makedirs('static', exist_ok=True)
    app.run(host='0.0.0.0', port=8000)


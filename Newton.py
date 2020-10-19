import numpy as np
import matplotlib.pyplot as plt
import random
import sys


def newton_method():
    print("------------------------------------------")
    func = input("What function should I evaluate?\t")
    lower_bound = int(input("What lower bound should I use?\t"))
    upper_bound = int(input("What upper bound should I use?\t"))
    x_1 = random.randint(lower_bound, upper_bound)
    print("------------------------------------------")

    N = 10000
    # number of functions evaluations.

    xvals = np.linspace(lower_bound, upper_bound)
    # the space between the upper and lower bounds on the x axis

    h = 1 / (N * 1.0)

    # h here is a very small number
    # not the same as taking a limit, but helps in approximating one

    def f(x):
        return eval(func)

    def f_prime(x):
        newVal = (f(x + h) - f(x)) / h
        return newVal

    count = 0
    while count <= 20:
        count += 1
        print(x_1)
        x_1 = x_1 - (f(x_1)) / (f_prime(x_1))

    yvals = []

    for i in xvals:
        derivative = f_prime(i)
        yvals.append(derivative)

    fvals = []

    for i in xvals:
        function = f(i)
        fvals.append(function)

    plt.plot(xvals, yvals, 'b')  # plotting derivative of function
    plt.plot(xvals, fvals, 'r')  # plotting function
    plt.scatter(x_1, 0)  # plotting the roots over time
    plt.grid()
    plt.title("Plotting f\'(x) and f(x)")
    plt.show()

    sys.exit()


newton_method()

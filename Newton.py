import numpy as np
import matplotlib.pyplot as plt
import random
import sys


def newton_method():
    print("------------------------------------------")
    func = input("What function should I evaluate?\t")
    lower_bound = int(input("What lower bound should I use?\t"))
    upper_bound = int(input("What upper bound should I use?\t"))
    count_desired = int(input("How many functions do you want me to evaluate for?"))
    x_1 = random.randint(lower_bound, upper_bound)
    # the above line simply gives us the starting value
    # it will be within the lower and upper bound, but doesn't need to be a precise value
    print("------------------------------------------")

    N = 10000
    # number of functions evaluations.

    xvals = np.linspace(lower_bound, upper_bound)
    # the space between the upper and lower bounds on the x axis

    h = 1 / (N * 1.0)

    # h here is a very small number
    # not the same as taking a limit, but helps in approximating one

    def f(x):
        '''
        now we define the function presented earlier as
        just returning the evaluated version of that function
        the users' input becomes effectively code
        '''
        return eval(func)


    def f_prime(x):
        '''
        the derivative of the original function
        using the definition of a derivative and instead of having a limit
        simply letting h become a very small number
        '''
        newVal = (f(x + h) - f(x)) / h
        return newVal


    '''
    the count function here is just to give us a set number of
    iterations of newton's method, we can set it to be lower if desired
    '''
    count = 0
    while count <= count_desired:
        count += 1
        print(x_1)
        x_1 = x_1 - (f(x_1)) / (f_prime(x_1))

    yvals = []
    '''
    xvals is a linear space between the upper and lower bound
    basically, for each point in that space, the list of f'(x) values is added to
    since the for loop goes through each item in xvals, there will be an equal number of
    datasets returned
    '''
    for i in xvals:
        derivative = f_prime(i)
        yvals.append(derivative)

    '''
    the same idea as before, but just evaluating the function, not the derivative
    of the function
    '''
    fvals = []

    for i in xvals:
        function = f(i)
        fvals.append(function)

    plt.plot(xvals, yvals, 'b')  # plotting derivative of function
    plt.plot(xvals, fvals, 'r')  # plotting function
    plt.scatter(x_1, 0, 'w')  # plotting the roots over time
    plt.grid()
    plt.title("Plotting f\'(x) and f(x)")
    plt.show()

    sys.exit()


newton_method()

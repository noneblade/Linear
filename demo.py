from numpy import *

def gradient_descent_runner(points,b,m,learning_rate,num_iterations):


def run():
    points = genfromtxt("data.csv", delimiter = ',')
    #hyperparameters - how fast our model learns
    learning_rate = 0.0001
    #y = mx + b
    initial_b = 0
    initial_m = 0
    num_iterations = 1000
    [b,m] = gradient_descent_runner(points,initial_b,initial_m,learning_rate,num_iterations)
    print(b)
    print(m)

run()
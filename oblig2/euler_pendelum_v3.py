import math
from matplotlib import pyplot as plt

# Function to plot the plot_results
def plot_results(time, theta1):
    plt.plot(time, theta1)
    s = '(Initelle vinkelen = ' + str(theta0) + ' degrees)'
    plt.title("Oblig2 d)" + s)
    plt.ylabel('vinkel')
    plt.legend(['lineær'], loc='lower right')
    plt.show()

# Algorithm description
# Define constants and variables (temporary storage)
# Define initial conditions (time, theta and v)
# Call the function v, theta = lin_pendel_euler(v0, theta0, g, L, N, h)
# Inside function iterate and use Euler's equations


# Constants ++
# Will be parameters to the function
# v, theta = lin_pendel_euler(v0, theta0, g, L, N, h);
g = 9.81
L = 1.0
T = 4.0
N = 2**5
h = T/N

# building array with time values to be used in plot
# not good if function goes in its own package
# In the pendelum.py this is done by np.arange(0, 10, 0.025)
# but that requires the package numpy
t = []
t0 = 0

# Initial values
theta0 = math.pi/2 # Can also used built-in pow() or ** math.pow() converts arguments to float first
v0 = 0

def lin_pendel_euler(v0, theta0, g, L, N, h):
    # Definition of storage; store the values for ploting and calculations
    theta = []
    v = []
    slopev_array = []
    slopetheta_array = []

    # Store the initial values in Python lists
    t.append(t0)
    theta.append(theta0)
    v.append(v0)
    # And initial calculations
    slopev_array.append(-g*theta[0])
    slopetheta_array.append(v[0]/L)

    # Use built-in range to iterate over a sequence of numbers k = 1, 2, ... N-1
    for k in range(1, N):
        # Values at the next step k
        tt = t[k-1] + h
        thetat = theta[k-1] + h*slopetheta_array[k-1]
        vt = v[k-1] + h*slopev_array[k-1]

        # Store the values in the Python lists for the point k+1 (because starting at 0)
        t.append(tt)
        theta.append(thetat)
        v.append(vt)
        slopev_array.append(-g*theta[k])
        slopetheta_array.append(v[k]/L)
    return v, theta


# Using the Euler's method to approximate a solution of the linearized
# version of differential equations
v, theta = lin_pendel_euler(v0, theta0, g, L, N, h)

# plott resultatene
plot_results(t, theta)

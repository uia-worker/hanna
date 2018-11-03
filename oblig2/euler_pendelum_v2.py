import math
from matplotlib import pyplot as plt

# Funksjon for å vise resultater
def plot_results(time, theta1):
    plt.plot(time, theta1)
    s = '(Initelle vinkelen = ' + str(theta0) + ' radianer)'
    plt.title("Oblig2 d)" + s)
    plt.ylabel('vinkel')
    plt.legend(['lineær'], loc='lower right')
    plt.show()

# Pseudo-code
# Define constants and variables (temporary storage)
# Define initial conditions (time, theta and v)
# Iterate over a sequence of integers (for each k do the following)
#  # Values at the next step (k=2)
# t2 = t1 + h
# theta2 = theta1 + h*slopetheta_array[1]
# v2 = v1 + h*slopev_array[1]

# Definition of storage; store the values for ploting and calculations
t = []
theta = []
v = []
slopev_array = []
slopetheta_array = []

# Constants ++
# Will be parameters to the function
# v, theta = lin_pendel_euler(v0, theta0, g, L, N, h);
g = 9.81
L = 1.0
T = 4.0
#N = math.pow(2,5)
N = 2**5
print(N)
h = T/N
p = 8

# Initial values
t0 = 0 # Using this to follow the theory for the Euler's method
theta0 = round(math.pi/2, p) # Can also used built-in pow() or ** math.pow() converts arguments to float first
v0 = 0
t.append(t0)
theta.append(theta0)
v.append(v0)

# And initial calculations
slopev_array.append(round(-g*theta[0], p))
slopetheta_array.append(round(v[0]/L, p))

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
    slopev_array.append(round(-g*theta[k], p))
    slopetheta_array.append(round(v[k]/L, p))

# plott resultatene
plot_results(t, theta)

import math
from matplotlib import pyplot as plt

# Function to plot the plot_results
def plot_results(time, theta1, theta2, theta3):
    plt.plot(time, theta1)
    plt.plot(time, theta2)
    plt.plot(time, theta3)
    s = '(Initelle vinkelen = ' + str(theta0) + ' radianer)'
    plt.title("Oblig2 d)" + s)
    plt.ylabel('vinkel')
    plt.grid(True)
    plt.legend(['lineær numerisk', 'linæar analytisk', 'ikke lineær'], loc='lower left')
    plt.show()

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

def pendel_euler(v0, theta0, g, L, N, h):
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
    slopev_array.append(-g*math.sin(theta[0]))
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
        slopev_array.append(-g*math.sin(theta[k]))
        slopetheta_array.append(v[k]/L)
    return v, theta

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

# Oblig2 part e)
# In this section the error is calculated (could be implemented
# as own function)
#
# There are some caveats in the code:
#     o  there are a global variable t, which is a python list
#        and has to be cleared after each loop
#     o  the loop is running over pow2list which include
#        alle powers of 2 from 5 to 10 (see e) in assignment
#
# Only the last pair of values are used.
# That can give a wrong impression if the function are periodic
# (plot the solution from euler_pendelum_v4 with different
# values of N and reflect upon the results...)
#

def pow2(b):
    return 2**b
pow2list = list(map(pow2, range(5,11)))

print("N" + "|" + "h" + "|" + "error(h)")
print(5*"-" + "|" + 10*"-" + "|" + 10*"-")

# Make a place for the errors
ehlist = []
p = []

for N in pow2list:
    h = T/N
    # Using the Euler's method to approximate a solution of the linearized
    # version of differential equations
    v, theta = lin_pendel_euler(v0, theta0, g, L, N, h)


    # Using the analytical solution of (3)
    theta2 = [(theta0 * math.cos(math.sqrt(g/L)*tt) + v0/math.sqrt(g/L) * math.sin(math.sqrt(g/L)*tt)) for tt in t]

    # Calculate the error
    eh = abs(theta[len(theta)-1:][0] - theta2[len(theta)-1:][0])
    ehlist.append(eh)
    if len(ehlist) > 1:
        p.append(math.log( ehlist[len(ehlist)-2]/ehlist[len(ehlist)-1])/math.log( 2*h/h ))

    # Print the results in a table

    print(str(N) + "|" + str(h) + "|" + str( round( eh, 4) ))

    if theta2:
        theta2.clear()
    if t:
        t.clear()

print(p)


# plott resultatene
# Using the analytical solution of (3)
# Checking the values of h and N (not a good practice to modify those non-global structures...)
print("h = " + str(h) + ", N = " + str(N) + ", len(t) = " + str(len(t)))
v, theta1 = lin_pendel_euler(v0, theta0, g, L, N, h)
theta2 = [(theta0 * math.cos(math.sqrt(g/L)*tt) + v0/math.sqrt(g/L) * math.sin(math.sqrt(g/L)*tt)) for tt in t]
print("h = " + str(h) + ", N = " + str(N) + ", len(t) = " + str(len(t)))
t = []
t0 = 0
h = T/N
v, theta3 = pendel_euler(v0, theta0, g, L, N, h)
print("h = " + str(h) + ", N = " + str(N) + ", len(t) = " + str(len(t)))
print(len(theta1), len(theta2), len(theta3))
plot_results(t, theta1, theta2, theta3)

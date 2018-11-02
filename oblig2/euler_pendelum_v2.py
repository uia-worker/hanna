import math

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
N = math.pow(2,5)
h = T/N

# Initial values
t0 = 0 # Using this to follow the theory for the Euler's method
theta0 = round(math.pi/2, 2) # Can also used built-in pow() or ** math.pow() converts arguments to float first
v0 = 0

# Here are all of the values for the initial point
# We'll make this (printing) as separate function later
print("k" + "\t" +
        "tk" + "\t" +
        "thetak" + "\t" +
        "vk" + "\t" +
        "slopev" + "\t" +
        "slopetheta"
)

# Use built-in range to iterate over a sequence of numbers k = 0, 1, ... N-1
for k in range(N):
# Values at the next step k
    tt = t[k-1] + h
    thetat = theta[k-1] + h*slopetheta_array[k-1]
    vt = v[k-1] + h*slopev_array[k-1]

    # Store the values in the Python lists for the point k+1 (because starting at 0)
    t.append(tt)
    theta.append(thetat)
    v.append(vt)
    slopev_array.append(round(-g*theta[k], 2))
    slopetheta_array.append(round(v[k]/L, 2))

    # Here is all of the values after the second step
    print(str(k) + "\t" +
        str(t[2]) + "\t" +
        str(theta[2]) + "\t" +
        str(v[2]) + "\t" +
        str(slopev_array[2]) + "\t" +
        str(slopetheta_array[2])
    )

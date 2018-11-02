import math

# Main loop
k = 0 # have to make a loop up to 2pow5=32
p = 3

# Definition of storage; store the values for ploting and calculations
t = []
theta = []
v = []
slopev_array = []
slopetheta_array = []

# Constants
g = 9.81
L = 1.0

# Initial values
t0 = 0
theta0 = round(math.pi/2, p)
v0 = 0

# First point (initial), values put in the lists
t.append(t0)
theta.append(theta0)
v.append(v0)
slopev_array.append(round(-g*theta[0], p))
slopetheta_array.append(round(v[0]/L, p))

# Here is all of the values for the initial point
print("k" + "\t" +
        "tk" + "\t" +
        "thetak" + "\t" +
        "vk" + "\t" +
        "slopev" + "\t" +
        "slopetheta"
)
print(str(k) + "\t" +
        str(t[0]) + "\t" +
        str(theta[0]) + "\t" +
        str(v[0]) + "\t" +
        str(slopev_array[0]) + "\t" +
        str(slopetheta_array[0])
)

# Continue to the next step k = 1 (making first step now)
k = 1

# We need to define the step size
T = 4.0
N = math.pow(2,5)
h = T/N

# Values at the next step (k=1)
t1 = t0 + h
theta1 = round((theta0 + h*slopetheta_array[0]), p)
v1 = round((v0 + h*slopev_array[0]), p)

# Second point, values put in the lists
t.append(t1)
theta.append(theta1)
v.append(v1)
slopev_array.append(round(-g*theta[1], p))
slopetheta_array.append(round(v[1]/L, p))

# Here are all of the values after the first step
print(str(k) + "\t" +
        str(t[1]) + "\t" +
        str(theta[1]) + "\t" +
        str(v[1]) + "\t" +
        str(slopev_array[1]) + "\t" +
        str(slopetheta_array[1])
)

# Lets do one more step
k = 2

# Values at the next step (k=2)
t2 = t1 + h
theta2 = round((theta1 + h*slopetheta_array[1]), p)
v2 = round((v1 + h*slopev_array[1]), p)

# Third point, values put in the lists
t.append(t2)
theta.append(theta2)
v.append(v2)
slopev_array.append(round(-g*theta[2], p))
slopetheta_array.append(round(v[2]/L, p))

# Here is all of the values after the second step
print(str(k) + "\t" +
        str(t[2]) + "\t" +
        str(theta[2]) + "\t" +
        str(v[2]) + "\t" +
        str(slopev_array[2]) + "\t" +
        str(slopetheta_array[2])
)

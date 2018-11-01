import math

# Main loop
# Remove this one, since it will be the counter in an iterative loop
# According to the oblig2, you run first up to math.pow(2,5) and
# then up to math.pow(2,10) (or 32 and )

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
theta0 = round(math.pi/2, 2)
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

# We have to put this part in the loop
# Lets do one more step
k = 2

# Values at the next step (k=2)
t2 = t1 + h
theta2 = theta1 + h*slopetheta_array[1]
v2 = v1 + h*slopev_array[1]

# Third point, values put in the lists
t.append(t2)
theta.append(theta2)
v.append(v2)
slopev_array.append(round(-g*theta[2], 2))
slopetheta_array.append(round(v[2]/L, 2))

# Here is all of the values after the second step
print(str(k) + "\t" +
        str(t[2]) + "\t" +
        str(theta[2]) + "\t" +
        str(v[2]) + "\t" +
        str(slopev_array[2]) + "\t" +
        str(slopetheta_array[2])
)

import numpy as np
from numpy import sin, cos
from scipy.integrate import odeint
from matplotlib import pyplot as plt

# definere ligninger
def equations(y0, t):
    # y0 er state vektor som liste
    theta, x = y0
    f = [x, -g/l * sin(theta)]
    return f

def plot_results(time, theta1, theta2):
    plt.plot(time, theta1[:,0]) # bare forste kolonne ?
    plt.plot(time, theta2) # bare en liste

    s = '(Initelle vinkelen = ' + str(initial_angle) + ' degrees)'
    plt.title("Oppgave 2" + s)
    plt.ylabel('vinkel i radianer')
    plt.grid(True)
    plt.legend(['ikke linear', 'linear'], loc='lower right')
    plt.show()

# parametre
g = 9.81 # approximation, linearization
l = 1.0

time = np.arange(0, 10, 0.025) # tidstep for fange opp ikke linearitet

# initielle betingelser
initial_angle = 45.0  # setter opp i grader / linearitet <1010grader
theta0 = np.radians(initial_angle)
x0 = np.radians(0.0) # grader per sekundet er verdien i paranteser

# finn loesningen til det ikke lineare problemet
theta1 = odeint(equations, [theta0, x0], time)

# finn loesningen til det lineare problemet
w = np.sqrt(g/l)
theta2 = [theta0 * cos(w*t) for t in time]

# plott resultatene
plot_results(time, theta1, theta2)

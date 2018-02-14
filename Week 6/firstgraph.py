# Imporing a pylab
import pylab as plt
# Setting a few lists
samples = []
linear = []
quad = []
cubic = []
exp = []

# Appending numbers in lists
for i in range(30):
    samples.append(i)
    linear.append(i)
    quad.append(i**2)
    cubic.append(i**3)
    exp.append(1.5**i)

# Figure is used to open seperate window
plt.figure('Linear')
# Adding Title to graph
plt.title('Linear')
# Adding xLabel to graph
plt.xlabel('Sample Points')
# Adding yLabel to graph
plt.ylabel('Linear Function')
# Setting limit on yaxis
plt.ylim(0, 1000)
# Plotting our linear function
plt.plot(samples, linear)
plt.figure('Quadratic')
plt.title('Quadratic')
plt.xlabel('Sample Points')
plt.ylabel('Quadratic Function')
plt.ylim(0, 1000)
# Plotting our quadratic function
plt.plot(samples, quad)
plt.figure('Cubic')
plt.title('Cubic')
plt.xlabel('Sample Points')
plt.ylabel('Cubic Function')
plt.ylim(0, 1000)
# Plotting our cubic function
plt.plot(samples, cubic)
plt.figure('Exponential')
plt.title('Exponential')
plt.xlabel('Sample Points')
plt.ylabel('Exponential Function')
plt.ylim(0, 1000)
# Plotting our exponential function
plt.plot(samples, exp)


plt.figure('lin quad')
plt.clf()
plt.plot(samples, linear, 'b-', label='Linear', linewidth=2.0)
plt.plot(samples, quad, 'ro', label='Quadratic', linewidth=2.0)
plt.legend(loc='upper left')
plt.title('Linear VS. Quadratic')

plt.figure('cube exp')
plt.clf()
plt.plot(samples, cubic, 'g^', label='Cubic', linewidth=2.0)
plt.plot(samples, exp, 'r--', label='Exponential', linewidth=2.0)
plt.legend()
plt.title('Cubic VS. Exponential')

plt.show()

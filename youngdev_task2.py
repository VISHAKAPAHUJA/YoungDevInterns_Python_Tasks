# make a sine and cosine graph using matplotlib module
import matplotlib.pyplot as plt
import numpy as np
# Generate x values from 0 to 2*pi
x = np.linspace(0, 2*np.pi, 50)
# Calculate sine and cosine values
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.plot(x,y_sin,marker='o',color='red',lw='3')
plt.plot(x,y_cos,marker='*',color='blue',lw='3')
plt.title("Sine and Cosine graph")
plt.xlabel("Angle")
plt.ylabel("Function Value")
plt.show()




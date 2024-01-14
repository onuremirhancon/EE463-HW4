import matplotlib.pyplot as plt
import numpy as np

# Define the gain function as per the equation provided
def gain(D, Rl, Rload):
    return 1 / ((1 - D) + (Rl / ((1 - D) * Rload)))


# Define the gain function as per the equation provided
def gain_ideal(D):
    return 1 / ((1 - D))

# Create a range of D values from 0 to 1 (excluding 1 as it would cause division by zero in the equation)
D_values = np.linspace(0, 0.99, 100)
Rl = 0.1  # Assuming Rl (internal resistance?) to be 1 ohm for this example
Rload_values = [24]  # Different Rload values for different plots

# Plot the gain function for different Rload values
plt.figure(figsize=(10, 6))

for Rload in Rload_values:
    plt.plot(D_values, gain(D_values, Rl, Rload), label=f'Rload = {Rload} & Resr = {Rl}  Ohm')

plt.plot(D_values, gain_ideal(D_values), label=f'Ideal formula')

plt.title('Boost-converter Gain with and without Resr')
plt.xlabel('Duty Cycle (D)')
plt.ylabel('Gain (G)')
plt.legend()
plt.grid(True)
plt.ylim(0,20)
plt.show()
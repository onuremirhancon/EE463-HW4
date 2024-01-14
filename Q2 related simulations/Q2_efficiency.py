import matplotlib.pyplot as plt
import numpy as np

V_in = 18
V_out = 48
R_load = 24
R_esr = 0.1
L = 4*pow(10,-6)
T = 1/400000
P_out = V_out*V_out/R_load


def I_L_on(t, D):
    global V_in, V_out, R_load, R_esr, L, T
    return V_out / (R_load * (1 - D)) + (D * T / L) * (V_in / (R_load * (1 - D)) - V_out * (t - 0.5 * D * T) / (R_load * (1 - D)))

def calculate_efficiency(D):
    global T, R_esr, P_out
    t_now  = 0 
    t_step = pow(10,-9)
    power_loss = 0
    while t_now < (T*D):
        I_L = I_L_on(t_now, D)
        power_loss = I_L*I_L* t_step + power_loss
        t_now += t_step

    power_loss = (R_esr / (D*T)) * power_loss
    efficiency = P_out/(P_out + power_loss)
    return efficiency

def mean_inductor_current(D):
    global V_out, R_load
    mean_current = V_out / (R_load * (1 - D))
    return mean_current
    

D_values = np.linspace(0, 0.99, 1000)
efficiency_values = []
mean_inductor_current_values = []
for D in D_values:
    #efficiency_values.append(calculate_efficiency(D))
    mean_inductor_current_values.append(mean_inductor_current(D))

plt.figure(figsize=(10, 6))
plt.plot(D_values, mean_inductor_current_values)
plt.title('Inductor mean current when ESR = 0.1 Ohms')
plt.xlabel('Duty Cycle (D)')
plt.ylabel('Current (A)')
plt.ylim(0,25)
plt.grid(True)
plt.show()

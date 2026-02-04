# Kalman Filter Example: Extracting Truth from Noisy Sensor Data

import numpy as np
import matplotlib.pyplot as plt

# 1. Setup the "Truth" (The actual temperature at Logan)
true_temp = 15.0  # 15°C
measurements = true_temp + np.random.normal(0, 2, size=50)  # Add "Noise" (flickering)

# 2. Initial Kalman Variables
est_temp = 20.0  # Our initial "guess" (slightly wrong)
est_error = 2.0  # How much we trust our guess
sensor_error = 1.0  # How much we trust the sensor

kalman_estimates = []

# 3. The Kalman Loop (Predict and Update)
for m in measurements:
    # PREDICT: (In this simple case, we assume temp stays the same)
    # UPDATE: Calculate the "Kalman Gain" (Who do we trust?)
    kalman_gain = est_error / (est_error + sensor_error)
    
    # ADJUST our estimate based on the sensor measurement
    est_temp = est_temp + kalman_gain * (m - est_temp)
    
    # UPDATE our uncertainty
    est_error = (1 - kalman_gain) * est_error
    
    kalman_estimates.append(est_temp)

# 4. Visualize the "Noise" vs the "Truth"
plt.plot(measurements, label='Raw "Noisy" Sensor Data (Neural/Data)', alpha=0.5)
plt.plot(kalman_estimates, label='Kalman Filter Estimate (Neuro-Symbolic)', color='red')
plt.axhline(true_temp, color='black', linestyle='--', label='Actual Temperature')
plt.legend()
plt.title("Kalman Filter: Extracting Truth from Logan Sensor Noise")
plt.show()
import numpy as np

# Original list
temps_list = [28, 32, 30, 37, 36, 38]

# Convert list to NumPy array
temps = np.array(temps_list)

# Print max and min temperature
print("Maximum Temperature:", np.max(temps))
print("Minimum Temperature:", np.min(temps))

# Calculate average temperature
print("Average Temperature:", np.mean(temps))

# Display last 3 days temperature
print("Last 3 Days Temperature:", temps[-3:])
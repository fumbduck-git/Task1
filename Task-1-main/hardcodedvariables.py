import matplotlib.pyplot as plt

a = 0.015
b = -0.7 
c = 20 

temperature = 22.0  
humidity = 75.0    

precipitation = a * temperature**2 + b * humidity + c
print(f"Precipitation: {precipitation}")

temperature_range = range(0, 31)
precipitation_values = [a * temp**2 + b * humidity + c for temp in temperature_range]

plt.figure(figsize=(8, 6))
plt.plot(temperature_range, precipitation_values, marker='o', linestyle='-')
plt.xlabel('Temperature (°C)')
plt.ylabel('Precipitation (mm)')
plt.title('Relationship between Temperature and Precipitation')
plt.grid(True)
plt.show()

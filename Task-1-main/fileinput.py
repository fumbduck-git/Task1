import csv
import matplotlib.pyplot as plt

file_path = "wth.csv"
results = []

a = 0.015
b = -0.7
c = 20

with open(file_path, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        temperature = float(row["temperature"])
        humidity = float(row["humidity"])
        pressure = float(row["pressure"])
        
        precipitation = a * temperature**2 + b * humidity + c
        
        results.append({
            "temperature": temperature,
            "humidity": humidity,
            "pressure": pressure,
            "precipitation": precipitation
        })
temperature_values = [result["temperature"] for result in results]
precipitation_values = [result["precipitation"] for result in results]

plt.figure(figsize=(10, 6))
plt.scatter(temperature_values, precipitation_values, marker='o', edgecolors='black', alpha=0.7, label='Weather Data')
plt.xlabel('Temperature (°C)')
plt.ylabel('Precipitation (mm)')
plt.title('Relationship between Temperature and Precipitation')
plt.legend()
plt.grid(True)
plt.savefig('weather_plot.png')
plt.show()

for result in results:
    print(f"Temperature: {result['temperature']}°C, Humidity: {result['humidity']}%, "
          f"Pressure: {result['pressure']}hPa, Precipitation: {result['precipitation']} mm")

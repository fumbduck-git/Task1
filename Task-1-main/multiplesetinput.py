import matplotlib.pyplot as plt
sets_of_inputs = []
while True:
    temperature = float(input("Enter coefficient temperature: "))
    pressure = float(input("Enter coefficient pressure: "))
    humidity = float(input("Enter coefficient humidity: "))
    time = float(input("Enter time: "))
    sets_of_inputs.append([temperature, pressure, humidity, time])
    if input("Add another set? (yes/no): ").lower() != "yes":
        break
weather_parameters = {}
for i, set_of_inputs in enumerate(sets_of_inputs):
    temperature, pressure, humidity, time = set_of_inputs
    weather_parameter = temperature * time**2 + pressure * time + humidity
    weather_parameters[f"Set {i+1}"] = weather_parameter
for key, value in weather_parameters.items():
    print(f"{key}: {value}")
temperature_range = range(0, 31)
precipitation_values = [temperature * time**2 + pressure * time + humidity for temperature in temperature_range]
plt.figure(figsize=(8, 6))
plt.plot(temperature_range, precipitation_values, marker='o', linestyle='-')
plt.xlabel('Temperature (°C)')
plt.ylabel('Precipitation (mm)')
plt.title('Relationship between Temperature and Precipitation')
plt.grid(True)
plt.show()

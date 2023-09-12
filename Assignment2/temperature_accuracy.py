import matplotlib.pyplot as plt
import random
from collections import deque
from sense_hat import SenseHat
from time import sleep
from datetime import datetime, timedelta

class AutoDeque(deque):
    def __init__(self, max_size):
        super().__init__(maxlen=max_size)

    def replace(self, item):
        if len(self) == self.maxlen:
            self.popleft()  # Remove the oldest element
        self.append(item)  # Add the new item

# Initialize an empty list to store temperature data
temperature_data = AutoDeque(max_size=10)
avg_data = AutoDeque(max_size=10)
time_data = AutoDeque(max_size=10)
sense=SenseHat()
# Create an empty plot
plt.ion()

fig, ax = plt.subplots()
line, = ax.plot([], [], marker='o', linestyle='-',label="Temperatures")
line1, = ax.plot([], [], marker='x', linestyle='-',label="Average Temperatures")
ax.set_title('Temperature vs. Time')
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Temperature (°C)')
ax.legend()
ax.grid(True)
timestamp = datetime.now()

def update_plot():
    # x_data = list(range(len(temperature_data)))
    # y_data = temperature_data
    line.set_data(time_data, temperature_data)
    line1.set_data(time_data, avg_data )
    ax.relim()
    ax.autoscale_view()
    plt.pause(1)



try:
    while True:
        #time.sleep(3)
        temperature= sense.get_temperature()
        timestamp = datetime.now().second
        time_data.replace(timestamp)
        temperature_data.replace(temperature)
        avg_data.replace(sum(temperature_data)/len(temperature_data))
        update_plot()
except KeyboardInterrupt:
    # Stop the program when the user presses Ctrl+C
    pass
finally:
    plt.ioff()
    plt.show()


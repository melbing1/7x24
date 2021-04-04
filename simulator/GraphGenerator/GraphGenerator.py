# Library:                              Why it was imported:
import sys                              # System (used to take arguments)
import numpy as np                      # Poisson Distribution
import matplotlib.pyplot as plt         # Show the plot
import DataGenLib as DataGen            # Misc Functions
# Source : https://numpy.org/doc/stable/reference/random/generated/numpy.random.poisson.html
# Source : https://matplotlib.org/2.0.2/users/pyplot_tutorial.html


print("***Hofstra 7x24 Challenge - GraphGenerator v1.0***")

cold_start_cost = DataGen.getFloatInput(
    "(1/5) Enter the cost for a Cold Start: ")
print("")


idle_time_cost = DataGen.getFloatInput(
    "(2/5) Enter the cost for each unit of idle time: ")
print("")


simulation_length = DataGen.getIntInput(
    "(3/5) Enter the simulation length: ")
print("")

"""
idle_time = DataGen.getIntInput(
    "(3/5) Enter the time spent idle after a call: ")
print("")
"""

mean = DataGen.getIntInput(
    "(4/5) Enter a mean time units between calls: ")
print("")

# Poisson Distribution - generates the data usuing a Poisson Distribution
# Consistent Value - generates data with exactly X units of time between each call
print("(5/5) Please select from the following data models (enter the respective number): ")
data_model = DataGen.getIntInput(
    "1 - Poisson Distribution \n2 - Consistent Value\nSelection: ", [1, 2])
print("")

# Declare the Axis that will be graphed

xAxis = []
# The X-Axis is 0-100
for x in range(0, simulation_length + 1):
    xAxis.append(x)

yAxis = []
# Generate the data for the Y-Axis
if (data_model == 1):
    for x in range(0, simulation_length + 1):
        (cold_starts, warm_starts, idle, pointless) = DataGen.generatePoissonData(
            simulation_length, x, mean)
        cost = float(len(cold_starts)) * cold_start_cost + \
            float(idle) * idle_time_cost
        yAxis.append(cost)

elif (data_model == 2):
    for x in range(0, simulation_length + 1):
        (cold_starts, warm_starts, idle,
         pointless) = DataGen.generateConsistentData(simulation_length, x, mean)
        cost = float(len(cold_starts)) * cold_start_cost + \
            float(idle) * idle_time_cost
        yAxis.append(cost)

else:
    print("An unknown error has occured")

# Now we graph the data

# Load in the data
plt.plot(xAxis, yAxis, 'r-')

# Set the axis
# The X-Axis goes from 0 - simulation_length
# The Y-Axis goes from 0 to the lowest round number above max(yAxis)
yMax = DataGen.sigFigRound(max(yAxis))
while max(yAxis) > yMax:
    yMax = yMax * 2

plt.axis([0, simulation_length, 0, yMax])

# Label each axis and title
plt.title('Idle Time Vs Cost')
plt.xlabel('Idle Time')
plt.ylabel('Cost')

# Show the graph
plt.show()

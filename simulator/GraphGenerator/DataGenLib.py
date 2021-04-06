# Library:                              Why it was imported:
import numpy as np                      # Poisson Distribution
from itertools import repeat            # Simlifies generateConsistentData()
from math import log10, floor           # Used for sigFigRound()

"""
Index:
1. generatePoissonData()
2. generateConsistentData()
3. runSimulation()
4. getFloatInput()
5. sigFigRound()
"""


# Input:
#   simulation_length: the amount of time units the sumulation should run
#   idle_time: the amount of time units the system should stay idle after a call
#   mean: the mean of the Poisson distribution
# Output (Comes from runSimulation()):
#   (cold, warm, idle, pointless)
#   cold_starts: A list of the cold starts times
#   warm_starts: A list of the warm starts times
#   idle: The total amount of time idle
#   pointless: The amount of wasted idle time

def generatePoissonData(simulation_length, idle_time, mean):
    # Makes an numpy array of random values following a poisson distribution
    distribution = np.random.poisson(mean, simulation_length)

    # Copying the variable so we don't ruin the oringinal in case we want to show the graph
    # Also the numpy arrays are different so we have to convert it and sort it so we can use it
    data = distribution.tolist()
    # Run the generated data to feed to the simulator
    return data
    # return runSimulation(simulation_length, idle_time, data)


def generateConsistentData(simulation_length, idle_time, mean):
    # Create a data list with all the same values occuring more than enough times
    data = []
    data.extend(repeat(mean, simulation_length))
    # Run the generated data to feed to the simulator
    return data
    # return runSimulation(simulation_length, idle_time, data)

# Input:
#   simulation_length: the amount of time units the sumulation should run
#   idle_time: the amount of time units the system should stay idle after a call
#   data: A list containing the time between each call
# Output:
#   (cold, warm, idle, pointless)
#   cold_starts: A list of the cold starts times
#   warm_starts: A list of the warm starts times
#   idle: The total amount of time idle
#   pointless: The amount of wasted idle time


def runSimulation(simulation_length, idle_time, data):
    simulation_data = []
    for item in data:
        simulation_data.append(int(item))

    # Run the simulation
    # This code is not very efficient but for a problem this small it works fine

    # Stores the cold and warm start times. This could have just been an int, but I left it as a list in case we choose to extent the code
    cold_starts = []
    warm_starts = []

    # Time until shutdown
    warm = 0
    # Time spent running
    idle = 0
    # Time spent running without another call coming
    pointless = 0
    pointlessTmp = 0
    # Time until function call
    call = simulation_data.pop(0)
    # Each unit of time
    for x in range(1, simulation_length + 1):
        # Check if the function was called at that point
        if call == 0:
            # And for each time it was
            # Check if it was cold or warm and count accordingly
            if warm > 0:
                warm_starts.append(x)
                pointlessTmp = 0
            else:
                cold_starts.append(x)
                pointless += pointlessTmp
                pointlessTmp = 0
            # Reset the time until shutdown and prepare for the next call
            warm = idle_time
            call = simulation_data.pop(0)
        # Pass one unit of time
        else:
            if warm > 0:
                # print("Running - Warm for " + str(warm - 1) + " longer")
                pointlessTmp += 1
                idle += 1
                warm = warm - 1
            call = call - 1

    # Add the last pointless idle time
    pointless += pointlessTmp
    pointlessTmp = 0

    # Show result:
    return (cold_starts, warm_starts, idle, pointless)


# Input: Prompt to the user, [Optional] List of acceptable values (if not present, any float is accepted)
def getFloatInput(prompt, acceptedValues=[]):
    valid = False
    value = None
    while valid == False:
        try:
            value = float(input(prompt))
            if value in acceptedValues or acceptedValues == []:
                valid = True
            else:
                print("Input out of range - please try again")
        except:
            print("Input not understood - please try again")
    return value

# Same as getFloatInput, but with the int data type
# Input: Prompt to the user, [Optional] List of acceptable values (if not present, any float is accepted)


def getIntInput(prompt, acceptedValues=[]):
    valid = False
    value = None
    while valid == False:
        try:
            value = int(input(prompt))
            if value in acceptedValues or acceptedValues == []:
                valid = True
            else:
                print("Input out of range - please try again")
        except:
            print("Input not understood - please try again")
    return value

# Rounds input x to the nearest significant figure


def sigFigRound(x):
    # This function comes from: https://stackoverflow.com/questions/3410976/how-to-round-a-number-to-significant-figures-in-python
    return round(x, -int(floor(log10(abs(x)))))

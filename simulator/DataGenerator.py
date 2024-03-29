# Library:                              Why it was imported:
import sys                              # System (used to take arguments)
import numpy as np                      # Poisson Distribution
import matplotlib.pyplot as plt         # Show the plot
# Source : https://numpy.org/doc/stable/reference/random/generated/numpy.random.poisson.html

# Check to ensure the correct number of arguments
if len(sys.argv) < 4:
    # The symbols are escape characters to make the text red
    print('\033[91m' + "ERROR - Read the start of the code to see the 4 arguments needed" + '\033[0m')
    exit()

try:
    # Parameter Values
    # How long the simulation should test
    simulation_length = int(sys.argv[1])  # Parameter 1
    # How long the system should stay warm after an execution
    idle_time = int(sys.argv[2])  # Parameter 2
    # The mean for the poisson distribution
    mean = float(sys.argv[3])  # Parameter 3
    # The size for the poisson distribution does not matter and is intentionally kept long
    # Parameter 4: You can optionally add "-graph" as a 5th paramter to show a graph of the distribution at the end

except:
    print('\033[91m' + "ERROR - There was an issue with one or more arguments. Please check the formatting and try again" + '\033[0m')
    exit()

# Makes an numpy array of random values following a poisson distribution
distribution = np.random.poisson(mean, simulation_length)

# Copying the variable so we don't ruin the oringinal in case we want to show the graph
# Also the numpy arrays are different so we have to convert it and sort it so we can use it
data = distribution.tolist()


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
            print("Warm Start: " + str(x))
            warm_starts.append(x)
            pointlessTmp = 0
        else:
            print("Cold Start: " + str(x))
            cold_starts.append(x)
            pointless += pointlessTmp
            pointlessTmp = 0
        # Reset the time until shutdown and prepare for the next call
        warm = idle_time
        call = simulation_data.pop(0)
    # Pass one unit of time
    else:
        if warm > 0:
            #print("Running - Warm for " + str(warm - 1) + " longer")
            pointlessTmp += 1
            idle += 1
            warm = warm - 1
        call = call - 1

# Add the last pointless idle time
pointless += pointlessTmp
pointlessTmp = 0

# Show result:
print("*********RESULTS*********")
print("Cold Starts: " + str(len(cold_starts)))
print("Warm Starts: " + str(len(warm_starts)))
print("Idle Time: " + str(idle))
print("Pointless Idle Time: " + str(pointless))
print("*************************")

# This should run last, otherwise the rest of gthe progran won't run until you close the graph
if len(sys.argv) > 4:
    if sys.argv[4] == "-graph":
        count, bins, ignored = plt.hist(distribution, 14)
        plt.show()

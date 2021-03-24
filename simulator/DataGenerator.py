# Library:          Why it was imported:
import sys          # System (used to take arguments)
import numpy as np  # Poisson Distribution
import matplotlib.pyplot as plt
# SOurce : https://numpy.org/doc/stable/reference/random/generated/numpy.random.poisson.html

# Check to ensure the correct number of arguments
if len(sys.argv) < 5:
    # The symbols are excape charadcters to make the text red
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
    # The size for the poisson distribution
    size = int(sys.argv[4])  # Parameter 4
    # Parameter 5: You can optionally add "-graph" as a 5th paramter to show a graph of the distribution at the end

except:
    print('\033[91m' + "ERROR - There was an issue with one or more arguments. Please check the formatting and try again" + '\033[0m')
    exit()

# Makes an numpy array of random values following a poisson distribution
distribution = np.random.poisson(mean, size)

# Copying the variable so we don't ruin the oringinal in case we want to show the graph
# Also the numpy arrays are different so we have to convert it and sort it so we can use it
data = distribution.tolist()

# Sort the data
data.sort()

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
# Each unit of time
for x in range(1, simulation_length + 1):
    # Check if the function was called at that point
    if x in data:
        # And for each time it was
        for y in range(data.count(x)):
            # Check if it was cold or warm and count accordingly
            if warm > 0:
                print("Warm Start: " + str(x))
                warm_starts.append(x)
            else:
                print("Cold Start: " + str(x))
                cold_starts.append(x)
            # Reset the time until shutdown
            warm = idle_time
    # Pass one unit of time
    elif warm > 0:
        warm = warm - 1

# Show result:
print("*********RESULTS*********")
print("Cold Starts: " + str(len(cold_starts)))
print("Warm Starts: " + str(len(warm_starts)))
print("*************************")

# This should run last, otherwise the rest of gthe progran won't run until you close the graph
if len(sys.argv) > 5:
    if sys.argv[5] == "-graph":
        count, bins, ignored = plt.hist(distribution, 14)
        plt.show()

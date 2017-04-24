###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    total_list = []
    transported_cows = {}
    #pick heaviest cow under the limit, let's recursively do this!
    #convert the dict to a list of tuples sorted by weight
    #while there are cows still not transported
    while cows.keys() != transported_cows.keys():  
      trip_list = []
      avail = limit
      for cow in sorted(cows, reverse = True, key=(lambda x: cows[x])):
        w = cows[cow]
        if w <= avail and cow not in transported_cows:
          #take this cow!
          transported_cows[cow] = 1  #mark this cow as transported
          trip_list.append(cow)      #add cow to this trip
          avail -= cows[cow] 	   #reduce avail for this trip by the cow we just took
      total_list.append(trip_list)   #add this trip to the list of total trips
    return total_list  

# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    best_num_trips = len(cows)	#worst-case number of trips it will take (one cow at a time)
    #iterate through partitions of cows
    for trip_list in get_partitions(cows):
      invalid_trip = False
      num_trips = 0
    #check weight limit of each trip, give up if any trip goes over the limit
      for trip in trip_list:
        weight = 0
        for cow in trip:
          weight += cows[cow]	#accumulate total weight of cows on this trip
        if weight > limit:	#if weight is over limit...
          #print('invalid trip', trip)
          invalid_trip = True
          break			#...move on to next trip_list
        num_trips += 1
      if invalid_trip: 
        #print('about to continue', trip_list)
        continue
      if num_trips <= best_num_trips:
        best_trip_list = trip_list
        best_num_trips = num_trips 
    #keep track of num_trips if all trips in partitions meet weight req
    #keep only this valid trip_list if it is shorter than the best_trip_list
    return best_trip_list

# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))



# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:00:25 2019

@author: admin
"""

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
    
    heaviest = 0
    cow_clone = cows.copy()
    trip_list = []
    
   
    while limit >= 0:
        trip = []
        
        for name,weight in cow_clone.items():
            if weight > heaviest:
                heaviest = weight
                
        limit -= heaviest
        
        if limit >=0 :
            trip.append(name)
            cow_clone.pop(name)
        
        else:
                trip_list.append(trip)
                if cow_clone.keys != 0:
                    limit = 10
        
            
    return trip_list    


cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
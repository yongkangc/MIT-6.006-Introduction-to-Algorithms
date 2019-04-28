# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:14:25 2019

@author: admin
"""
cows = {'Maggie': 3, 'Herman': 7, 'Betsy': 9, 'Oreo': 6, 'Moo Moo': 3, 'Milkshake': 2, 'Millie': 5, 'Lola': 2, 'Florence': 2, 'Henrietta': 9}
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
    cows_clone = cows.copy()
    sortedCows = sorted(cows_clone.items(), key=lambda x: x[1], reverse = True)
    trip_list = []
    
    
            
    while sum(cows_clone.values()) > 0:
        trip = []
    
        for name,weight in sortedCows:
             if limit >= weight:
                    limit -= weight
                    trip.append(name)
                    cows_clone.pop(name)
        trip_list.append(trip)
    return trip_list
    
limit = 100
print(greedy_cow_transport(cows, limit))
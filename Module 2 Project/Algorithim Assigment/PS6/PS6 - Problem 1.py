#python 3
"""
MIT Algorithims Module 6.006: Introduction to Algorithim

Problem Set 6: Social Network Friend Suggestion 

Problem:
designing an algorithm that computes the strength of the strongest connection
between a given user s and every other user v to whom s is connected with vagueness at most
k, in O(kE + V ) time (i.e., for every pair of s and v for v ∈ V \{s}, compute the strength of the
strongest connection between them with vagueness at most k). Assume that the network has |V |
users and |E| friend pairs. 

Solution:

Find the shortest path from s to v for all vertices with path less than or equals to k.
"""
from collections import defaultdict 
  
#Class to represent a graph 
class Graph: 
  
    def __init__(self,vertices,distance): 
        self.V= vertices #No. of vertices 
        self.graph = [] # default dictionary to store graph 
    
   
    # function to add an edge to graph 
    def addEdge(self,u,v,w): 
        self.graph.append([u, v, w]) 
          
     

    def Klength_Bellman_Ford(s,k):
        dist = [float("Inf")] * self.V 
        dist[src] = 0 
        
        for i in range (1,k):
            t = {}
            for i in range(self.V - 1): 
            # Update dist value and parent index of the adjacent vertices of 
            # the picked vertex. Consider only those vertices which are still in 
            # queue 
            for u, v, w in self.graph: 
                if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                            t[v] = dist[u] + w 
            
            for v in t:
                dist[v] = t[v]

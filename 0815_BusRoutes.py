"""
You are given an array routes representing bus routes where routes[i] 
is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 
1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), 
and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.
"""
from typing import List
from collections import defaultdict,deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stop_to_buses = defaultdict(list)

        for bus_id, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(bus_id)

        if source not in stop_to_buses or target not in stop_to_buses:
            return -1
        
        if source == target:
            return 0

        queue = deque([source])
        buses_taken = set()
        stops_visited = set()
        res = 0

        while queue:
            # Increment the res for each level of stops
            res += 1
            stops_to_process = len(queue)

            for _ in range(stops_to_process):
                current_stop = queue.popleft()

                # Check buses passing through the current stop
                for bus_id in stop_to_buses[current_stop]:
                    if bus_id in buses_taken:
                        continue

                    buses_taken.add(bus_id)

                    # Check stops reachable from the current bus
                    for next_stop in routes[bus_id]:
                        if next_stop in stops_visited:
                            continue

                        # If the target is reached, return the res
                        if next_stop == target:
                            return res

                        # Add the next stop to the queue and mark it as visited
                        queue.append(next_stop)
                        stops_visited.add(next_stop)
        return -1

print(Solution().numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6))
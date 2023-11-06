"""
Design a system that manages the reservation state of n seats that are numbered from 1 to n.

Implement the SeatManager class:

SeatManager(int n) Initializes a SeatManager object that will manage n seats numbered from 1 to n. 
All seats are initially available.
int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.
"""
import queue
class SeatManager:

    def __init__(self, n: int):
        self.my = queue.PriorityQueue()
        for i in range(n):
            self.my.put((i+1,i+1)) #seat numbers start from 1

    def reserve(self) -> int:
        return self.my.get()[1]
    def unreserve(self, seatNumber: int) -> None:
        self.my.put((seatNumber,seatNumber))


#Your SeatManager object will be instantiated and called as such:
seatManager = SeatManager(5) #Initializes a SeatManager with 5 seats.
seatManager.reserve()
seatManager.reserve() 
seatManager.unreserve(2)
seatManager.reserve()
seatManager.reserve()
seatManager.reserve()
seatManager.reserve()
seatManager.unreserve(5)
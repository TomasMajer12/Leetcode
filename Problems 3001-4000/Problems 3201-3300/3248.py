
from typing import List

class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        
        current_pos = (0,0)

        for com in commands:
            match com:
                case "UP":
                    current_pos = (current_pos[0] - 1,current_pos[1])
                
                case "DOWN":
                    current_pos = (current_pos[0] + 1,current_pos[1])
                
                case "LEFT":
                    current_pos = (current_pos[0],current_pos[1] - 1)
                
                case "RIGHT":
                    current_pos = (current_pos[0],current_pos[1] + 1)
        
        return current_pos[0] * n + current_pos[1]
    

print(Solution().finalPositionOfSnake(2,["RIGHT","DOWN"]))
print(Solution().finalPositionOfSnake(3,["DOWN","RIGHT","UP"]))
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                collision = stack[-1] + asteroid
                if collision < 0:  
                    stack.pop()
                elif collision > 0: 
                    asteroid = 0
                    break
                else: 
                    stack.pop()
                    asteroid = 0  
                    break
            if asteroid != 0:
                stack.append(asteroid)
        return stack

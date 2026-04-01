class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # iterate thru list, add + to ne stack,
        # if -, use a while loop to keep popping the 
        # top of the stack until either stack is empty 
        # OR the added elem is +
        stack = []
        for a in asteroids:
            if a >= 0:
                stack.append(a)
            else:
                # need to account for after a clashes with every elem in stack
                a_survived = True
                while len(stack) > 0:
                    # if top of stack is right direction
                    if stack[-1] > 0:
                        top = stack.pop()
                        if abs(top) > abs(a):
                            stack.append(top)
                            a_survived = False # a is destroyed
                            break
                        
                        # if left aes destroys top of stack, 
                        # go to next top of stack
                        elif abs(top) < abs(a):
                            continue
                        # destroy both and break while loop
                        else:
                            a_survived = False 
                            break
                    # if top of stack is left direction
                    else:
                        break
                if a_survived == True:
                    stack.append(a)
        return stack
        
                    

                    

        


        
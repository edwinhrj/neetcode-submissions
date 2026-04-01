class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort the position desc
        # position = [10, 8, 5, 3, 0]
        # stack = []
        # iterate thru position, if current time to get to target
        # <= time for top of stack, do not add curr
        # if > time for top of stack, add curr -> new "fleet"
        # return len(stack)
        car_list = []
        for i in range(len(position)):
            pair = (position[i], speed[i])
            car_list.append(pair)
        car_list = sorted(car_list, key=lambda x: x[0], reverse=True)
        stack = []
        for i in range(len(car_list)):
            if len(stack) > 0:
                curr_time = (target - car_list[i][0]) / car_list[i][1]
                front_time = (target - stack[-1][0]) / stack[-1][1]
                if curr_time > front_time:
                    stack.append(car_list[i])
            else:
                stack.append(car_list[i])
        return len(stack)

        
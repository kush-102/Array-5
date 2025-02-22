class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # maintain either clockwise or anti clockwise movement
        # N-->E-->S-->--W
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        idx = 0
        x = 0
        y = 0

        for i in range(4):
            for c in instructions:
                if c == "G":
                    x += directions[idx][0]
                    y += directions[idx][1]

                elif c == "R":
                    idx = (idx + 1) % 4
                elif c == "L":
                    idx = (idx + 3) % 4
            if x == 0 and y == 0 or idx != 0:
                return True
        return False

    # ime complexity is O(n) where n is length of instructions
    # space complexity is O(4) since we 4 directions array

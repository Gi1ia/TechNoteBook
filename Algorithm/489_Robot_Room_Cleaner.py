"""
This is the robot's control interface.
You should not implement it, or speculate about its implementation
"""
class Robot:
   def move(self):
       """
       Returns true if the cell in front is open and robot moves into the cell.
       Returns false if the cell in front is blocked and robot stays in the current cell.
       :rtype bool
       """

   def turnLeft(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

   def turnRight(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

   def clean(self):
       """
       Clean the current cell.
       :rtype void
       """

class Solution:
    def cleanCell(self, robot, x, y, visited):
        if (x, y) in visited:
            return
        visited[(x, y)] = 1
        robot.clean()

        if self.goUp(robot):
            self.cleanCell(robot, x, y + 1, visited)
            self.goDown()
        if self.goLeft(robot):
            self.cleanCell(robot, x - 1, y, visited)
            self.goRight
        if self.goRight(robot):
            self.cleanCell(robot, x + 1, y, visited)
            self.goLeft
        if self.goDown(robot):
            self.cleanCell(robot, x, y - 1, visited)
            self.goUp
            
    def goUp(self, robot):
        ok = robot.move()
        return ok
    
    def goLeft(self, robot):
        robot.turnLeft()
        ok = robot.move()
        robot.turnRight()
        return ok
    
    def goRight(self, robot):
        robot.turnRight()
        ok = robot.move()
        robot.turnLeft()
        return ok
    
    def goDown(self, robot):
        robot.turnLeft()
        robot.turnLeft()
        ok = robot.move()
        robot.turnLeft()
        robot.turnLeft()
        return ok

    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.cleanCell(robot, 0, 0, {})
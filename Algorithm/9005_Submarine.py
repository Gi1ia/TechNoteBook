class HitSubmarine():
    def __init__(self, sbm, speed):
        self.sbm_x = sbm[0]
        self.sbm_y = sbm[1]
        self.blt_x = 0
        self.blt_y = 0
        self.speed = speed
    
    def shoot_bullet(self):
        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        step = 1
        d = 0

        while True: # Could be infinite                   
            for s in range(step):
                if self.hit():
                    return (self.blt_x, self.blt_y)
                self.blt_x += directions[d][0]
                self.blt_y += directions[d][1]
                self.move_sbm()
            
            # Change step
            if d == 1 or d == 3:
                step += 1

            # change direction
            d += 1
            d %= 4 
        
        return (float('inf'), float('inf'))

    def move_sbm(self):
        self.sbm_x += self.speed[0]
        self.sbm_y += self.speed[1]
    
    def hit(self):
        return self.sbm_x == self.blt_x and \
        self.sbm_y == self.blt_y

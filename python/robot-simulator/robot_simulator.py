# Globals for the directions
# Change the values as you see fit
EAST = 'east'
NORTH = 'north'
WEST = 'west'
SOUTH = 'south'

directions_dict = {NORTH: {'R': EAST, 'L': WEST}, 
              EAST: {'R': SOUTH, 'L': NORTH},
              SOUTH: {'R': WEST, 'L': EAST},
              WEST: {'R': NORTH, 'L': SOUTH}
             }

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.coordinates = (self.x_pos, self.y_pos)


    def move(self, direction_str: str):
        for element in direction_str:
            if element != 'A':
                self.direction = directions_dict[self.direction][element]
            if element == 'A':
                if self.direction == EAST:
                    self.x_pos += 1
                if self.direction == WEST:
                    self.x_pos -= 1
                if self.direction == NORTH:
                    self.y_pos += 1
                    print('executed')
                if self.direction == SOUTH:
                    self.y_pos -= 1
            self.coordinates = (self.x_pos, self.y_pos)

        
                
                

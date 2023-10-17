# Globals for the directions
# Change the values as you see fit
EAST = 'east'
NORTH = 'north'
WEST = 'west'
SOUTH = 'south'

TURN_RIGHT = 'R'
TURN_LEFT = 'L'
DIRECTIONS = {
    NORTH: {TURN_RIGHT: EAST, TURN_LEFT: WEST},
    EAST: {TURN_RIGHT: SOUTH, TURN_LEFT: NORTH},
    SOUTH: {TURN_RIGHT: WEST, TURN_LEFT: EAST},
    WEST: {TURN_RIGHT: NORTH, TURN_LEFT: SOUTH},
}

OFFSET = {
    NORTH: (0, 1),
    EAST: (1, 0),
    SOUTH: (0, -1),
    WEST: (-1, 0),
}


class Robot:
    def __init__(self, direction: str = NORTH, x_pos: int = 0, y_pos: int = 0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos

    @property
    def coordinates(self):
        return (self.x_pos, self.y_pos)

    def move(self, move_request: str) -> None:
        for element in move_request:
            if element != 'A':
                self.direction = DIRECTIONS[self.direction][element]
            else:
                increase_x, increase_y = OFFSET[self.direction]
                self.x_pos += increase_x
                self.y_pos += increase_y
                
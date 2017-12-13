#!/usr/bin/env python


def main():
    spiral = SpiralCursor()
    val = 0
    while val < 368078:
        spiral.advance()
        print "Val: %s" % spiral.val
        val = spiral.val


class SpiralCursor(object):

    def __init__(self, init_val=1):
        # Tuple of current coord (x,y)
        self.pos = (0, 0)
        self.val = init_val
        self.grid = {self.pos: self.val}
        self.direction = 'east'

    def advance(self):
        # Calculate the new position
        self.increment_position()
        # Get new val and add them to the grid
        self.get_new_val()
        self.grid[self.pos] = self.val
        # Check direction, change if past the 'edge'
        self.adjust_direction()
        # Return the new value
        return self.val

    def adjust_direction(self):
        if not self.is_value_to_left():
            self.next_direction()
        print self.direction

    def next_direction(self):
        """Cycle through the directions, counter-clockwise."""
        directions = ['east', 'north', 'west', 'south', 'east']
        current = directions.index(self.direction)
        self.direction = directions[current + 1]

    def increment_position(self):
        """Get the next coord, depending on direction"""
        if self.direction == 'east':
            pos = (self.pos[0] + 1, self.pos[1])
        elif self.direction == 'north':
            pos = (self.pos[0], self.pos[1] + 1)
        elif self.direction == 'west':
            pos = (self.pos[0] - 1, self.pos[1])
        elif self.direction == 'south':
            pos = (self.pos[0], self.pos[1] - 1)

        self.pos = pos

    def is_value_to_left(self):
        to_check = False
        if self.direction == 'east':
            to_check = (self.pos[0], self.pos[1] + 1)
        if self.direction == 'north':
            to_check = (self.pos[0] - 1, self.pos[1])
        if self.direction == 'west':
            to_check = (self.pos[0], self.pos[1] - 1)
        if self.direction == 'south':
            to_check = (self.pos[0] + 1, self.pos[1])

        return bool(self.grid.get(to_check, False))

    def get_neighbors(self):
        """lol"""
        neighbors = []
        neighbors.append((self.pos[0] + 1, self.pos[1]))
        neighbors.append((self.pos[0] - 1, self.pos[1]))
        neighbors.append((self.pos[0] + 1, self.pos[1] + 1))
        neighbors.append((self.pos[0] - 1, self.pos[1] + 1))
        neighbors.append((self.pos[0] + 1, self.pos[1] - 1))
        neighbors.append((self.pos[0] - 1, self.pos[1] - 1))
        neighbors.append((self.pos[0], self.pos[1] - 1))
        neighbors.append((self.pos[0], self.pos[1] + 1))
        print neighbors
        return neighbors

    def get_new_val(self):
        val = 0
        print self.grid
        for n in self.get_neighbors():
            try:
                val += self.grid.get(n, 0)
            except KeyError:
                continue

        self.val = val


# Take a grid, produce the next value
# Insert the value into the grid
# Repeat, check value

if __name__ == '__main__':
    main()

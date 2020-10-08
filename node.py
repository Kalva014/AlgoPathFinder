import pygame

# Board and path colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
purple = (128, 0, 128)
orange = (255, 165, 0)
grey = (128, 128, 128)
turquoise = (64, 224, 208)

# These are the squares that will be marked in the grid
class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.total_rows = total_rows
        self.x = row * width
        self.y = col * width
        self.color = white
        self.neighbors = []

    # Returns position of the node
    def get_position(self):
        return self.row, self.col

    # If node is green then it is open
    def is_open(self):
        if(self.color == green):
            return True
        else:
            return False
    
    # If node is red then it is closed
    def is_closed(self):
        if(self.color == red):
            return True
        else:
            return False

    # If node is black then it is a wall
    def is_wall(self):
        if(self.color == black):
            return True
        else:
            return False

    # If node is orange then it is the starting node
    def is_start(self):
        if(self.color == orange):
            return True
        else:
            return False

    # If node is purple then it is the ending node
    def is_end(self):
        if(self.color == purple):
            return True
        else:
            return False

    # Resets color of node
    def reset_node(self):
        self.color = white

    # Marks the node
    def open_node(self):
        self.color = green
        
    # Already checked node
    def close_node(self):
        self.color = red

    # Make a wall
    def walled_node(self):
        self.color = black

    def start_node(self):
        self.color = orange

    def end_node(self):
        self.color = turquoise

    def path_node(self):
        self.color = purple

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []

        if((self.row < self.total_rows - 1) and not (grid[self.row + 1][self.col].is_wall())): # DOWN
            self.neighbors.append(grid[self.row - 1][self.col])
        
        if((self.row > 0) and not (grid[self.row - 1][self.col].is_wall())): # up
            self.neighbors.append(grid[self.row - 1][self.col])
        
        if((self.col < self.total_rows - 1) and not (grid[self.row][self.col + 1].is_wall())): # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])
        
        if((self.col > 0) and not (grid[self.row][self.col - 1].is_wall())): # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False
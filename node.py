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
    def __init__(self, color, row, column, node_margin, board_width):
        self.color = color
        self.row = row
        self.column = column
        self.board_width = board_width
        self.x = row * node_margin
        self.y = column * node_margin
        self.node_margin = node_margin

    # Returns position of node
    def get_position(self):
        return row, column

    # Checks if the node is the starting node for the search algorithm
    def is_start(self):
        if self.color == green:
            return True
        else:
            return False

    # Checks if the node is the ending node for the search algorithm
    def is_end(self):
        if self.color == red:
            return True
        else:
            return False

    # Resets the node to white to show nothing has happened to it
    def reset_node(self):
        self.color = white

    # Sets starting node to green
    def set_start(self):
        self.color = green

    # Sets starting node to red
    def set_end(self):
        self.color = red
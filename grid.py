from node import *

class Grid:
    def __init__(self, number_of_rows, number_of_columns, window, window_width):
        self.number_of_rows = number_of_rows
        self.number_of_columns = number_of_columns
        self.window = window
        self.window_width = window_width
        
        # Initialize an empty list to represent the grid and then add nodes to it
        self.grid_list = []

    # Initializes the grid by drawing it onto the screen and returns the grid's array that holds all of the nodes
    def draw_grid(self):
        self.draw_squares()
        self.draw_lines(1)

        pygame.display.update()

        return self.grid_list

    # Draw squares onto the screen
    def draw_squares(self):
        for row in self.grid_list:
            for node in row:
                    pygame.draw.rect(self.window, node.color, (node.x, node.y, node.node_margin, node.node_margin))

    # Draw the lines onto the screen
    def draw_lines(self, initial_grid=None):
        # Initialize the node's margin by doing integer division between the size of the window and amount of rows
        node_margin = self.window_width // self.number_of_rows 
        
        # Kind of complicated but pretty much if the grid_array is empty then intialize it with this, else update the grid
        if(initial_grid != None):
            for x in range(self.number_of_rows):
                # For every row, a list will be appended to grid and add all of the columns and its respective nodes
                self.grid_list.append([])
                
                # Draw the rows onto the window
                pygame.draw.line(self.window, grey, (0, x * node_margin), (self.window_width, x * node_margin))
                
                for y in range(self.number_of_columns):
                    # Initialize the node and make all nodes white. Then append to the row
                    node = Node(white, x, y, node_margin, self.window_width)
                    self.grid_list[x].append(node)
                    
                    # Draw the columns onto the window
                    pygame.draw.line(self.window, grey, (y * node_margin, 0), (y * node_margin, self.window_width))
        
        # Just draws the lines to update the grid since the grid is already initialized
        else:
            for x in range(self.number_of_rows):
                # Draw the rows onto the window
                pygame.draw.line(self.window, grey, (0, x * node_margin), (self.window_width, x * node_margin))
                
                for y in range(self.number_of_columns):
                    # Draw the columns onto the window
                    pygame.draw.line(self.window, grey, (y * node_margin, 0), (y * node_margin, self.window_width))

    # Every time an event occurs the grid will update the nodes that have been changed
    def update_grid(self, new_grid_list):
        self.grid_list = new_grid_list
        
        self.draw_squares()
        self.draw_lines()
        
        pygame.display.update()
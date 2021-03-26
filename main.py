import sys
from grid import *
from algorithm import *

# Window that shows the graph details
pygame.init()
height = 700
width = 700
window = pygame.display.set_mode((height, width))
window.fill(white)
pygame.display.set_caption("Path Finding Visualizer")

# Algorithms is a global variable so it can be used in the other functions
algorithm = None

# To stop the menu from running any further we change the value to false
def stop_menu_running():
    menu_running = False
    print(menu_running)

# Get the clicked position of the mouse to find the node
def get_clicked_position(mouse_position, rows):
    node_margin = width // rows
    
    x, y = mouse_position

    row = x // node_margin
    column = y // node_margin

    return row, column

# Code is controlled from here
def main(window, width):
    # Create specific sized grid
    amount_of_rows = 20
    amount_of_columns = 20
    grid = Grid(amount_of_rows, amount_of_columns, window, width)
    grid_array = grid.draw_grid()

    # Set start node and stop node to none
    start_node = None
    stop_node = None 

    # To keep the window running and starting with opening the menu first 
    run = True
    while run == True:
        for event in pygame.event.get():
            # User closes the window or something, end right away
            if event.type == pygame.QUIT:
                run = False

            # If a button is pressed
            if event.type == pygame.KEYDOWN: 
                # User hovers over square and clicks 's' on the keyboard
                if event.key == pygame.K_s:
                    if start_node == None:
                        mouse_position = pygame.mouse.get_pos()

                        clicked_row, clicked_column = get_clicked_position(mouse_position, amount_of_rows)

                        node = grid_array[clicked_row][clicked_column]
                        node.set_start()
                        grid_array[clicked_row][clicked_column] = node

                        # Update the grid with any new events
                        grid.update_grid(grid_array)

                        # Set start to the node mouse is on
                        start_node = node

                # User hovers over square and clicks 'e' on the keyboard
                if event.key == pygame.K_e:
                    if stop_node == None:
                        mouse_position = pygame.mouse.get_pos()
                
                        clicked_row, clicked_column = get_clicked_position(mouse_position, amount_of_rows)
                    
                        node = grid_array[clicked_row][clicked_column]
                        node.set_end()
                        grid_array[clicked_row][clicked_column] = node

                        # Update the grid with any new events
                        grid.update_grid(grid_array)

                        # Set stop to the node mouse is on
                        stop_node = node

                # User hovers over square and left clicks on their mouse to make a wall
                if event.key == pygame.K_w:
                    mouse_position = pygame.mouse.get_pos()
                    
                    clicked_row, clicked_column = get_clicked_position(mouse_position, amount_of_rows)
                    
                    node = grid_array[clicked_row][clicked_column]
                    node.set_wall()
                    grid_array[clicked_row][clicked_column] = node

                    # Update the grid with any new events
                    grid.update_grid(grid_array)

                # User presses space bar and the algorithm runs displaying the optimal path to from starting node to ending node
                if event.key == pygame.K_SPACE:
                    grid.add_neighbors()

                    if (start_node != None) or (stop_node != None):
                        dijkstras_algorithm(grid, start_node, stop_node)

main(window, width)
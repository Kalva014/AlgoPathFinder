import sys
from grid import *

# Window details
height = 700
width = 700
window = pygame.display.set_mode((height, width))
window.fill(white)
pygame.display.set_caption("Path Finding Visualizer")
    

# Get the clicked position of the mouse to find the node
def get_clicked_position(mouse_position, rows):
    node_margin = width // rows
    
    x, y = mouse_position

    row = x // node_margin
    column = y // node_margin

    return row, column

# Code is controlled from here
def main(window, width):
    # Initialize pygame
    pygame.init()

    # Create specific sized grid
    amount_of_rows = 20
    amount_of_columns = 20
    grid = Grid(amount_of_rows, amount_of_columns, window, width)
    grid_array = grid.draw_grid()

    # To keep the window running
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
                    mouse_position = pygame.mouse.get_pos()

                    clicked_row, clicked_column = get_clicked_position(mouse_position, amount_of_rows)

                    node = grid_array[clicked_row][clicked_column]
                    node.set_start()
                    grid_array[clicked_row][clicked_column] = node
                    
                    print(str(node.x) + ', ' + str(node.y))
                    # Update the grid with any new events
                    grid.update_grid(grid_array)
                    print("Set start")

                # User hovers over square and clicks 'e' on the keyboard
                if event.key == pygame.K_e:
                    mouse_position = pygame.mouse.get_pos()
             
                    clicked_row, clicked_column = get_clicked_position(mouse_position, amount_of_rows)
                    
                    node = grid_array[clicked_row][clicked_column]
                    node.set_end()
                    grid_array[clicked_row][clicked_column] = node

                    # Update the grid with any new events
                    grid.update_grid(grid_array)
                    print("Set end")

            #pygame.display.update()
        
        
main(window, width)
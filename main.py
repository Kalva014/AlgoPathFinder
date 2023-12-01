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

# Enum for different algorithms
class Algorithm:
    DIJKSTRA = "Dijkstra's Algorithm"
    BFS = "Breadth-First Search"
    # Add more algorithms as needed

# Function to run the selected algorithm
def run_algorithm(selected_algorithm, grid, start_node, stop_node):
    if selected_algorithm == Algorithm.DIJKSTRA:
        dijkstras_algorithm(grid, start_node, stop_node)
    elif selected_algorithm == Algorithm.BFS:
        BFS(grid, start_node, stop_node)

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

    # Algorithm menu variables
    algorithm_menu_font = pygame.font.SysFont(None, 30)
    algorithm_menu_text = [algorithm_menu_font.render(f"{i+1}. {algo}", True, black) for i, algo in enumerate([Algorithm.DIJKSTRA, Algorithm.BFS])]
    algorithm_menu_rects = [text.get_rect(topleft=(10, 40 * (i + 1))) for i, text in enumerate(algorithm_menu_text)]
    selected_algorithm = None

    # To keep the window running and starting with opening the menu first 
    run = True
    algorithm_menu_open = False
    while run == True:
        for event in pygame.event.get():
            # User closes the window or something, end right away
            if event.type == pygame.QUIT:
                run = False

            # If a button is pressed
            if event.type == pygame.KEYDOWN:
                
                # User presses 'a' to open/close the algorithm menu
                if event.key == pygame.K_a:
                    algorithm_menu_open = not algorithm_menu_open 
                
                # Handle algorithm selection when the menu is open
                if algorithm_menu_open and event.key in [pygame.K_1, pygame.K_2]:
                    # Clear the previous selection
                    selected_algorithm = None

                    # Subtracting pygame.K_1 to get the index (0-based)
                    index = event.key - pygame.K_1
                    if 0 <= index < len(algorithm_menu_text):
                        selected_algorithm = [Algorithm.DIJKSTRA, Algorithm.BFS][index]

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
                if event.key == pygame.K_SPACE and selected_algorithm:
                    grid.add_neighbors()

                    if (start_node != None) or (stop_node != None):
                        run_algorithm(selected_algorithm, grid, start_node, stop_node)

        # Draw the algorithm menu
        if algorithm_menu_open:
            for i, (text, rect) in enumerate(zip(algorithm_menu_text, algorithm_menu_rects)):
                if selected_algorithm == [Algorithm.DIJKSTRA, Algorithm.BFS][i]:
                    pygame.draw.rect(window, yellow, rect)
                if selected_algorithm != [Algorithm.DIJKSTRA, Algorithm.BFS][i]:
                    pygame.draw.rect(window, white, rect)
                window.blit(text, rect)

        pygame.display.update()

main(window, width)

import pygame
import math
from node import *

# Window details
width = 700
screen = pygame.display.set_mode((width, width))
pygame.display.set_caption("Path Finding Visualizer")

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

def reconstruct_path(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		current.make_path()
		draw()

# Creates the grid full of nodes
def create_grid(rows, width):
    grid = []
    width_of_cubes = width // rows

    for i in range(rows):
        grid.append([])

        for j in range(rows):
            node = Node(i, j, width_of_cubes, rows)
            grid[i].append(node)

    return grid

# Draws the grid onto the screen
def draw_grid(screen, rows, width):
    width_of_cubes = width // rows

    for i in range(rows):
        pygame.draw.line(screen, grey, (0, i * width_of_cubes), (width, i * width_of_cubes))

        for j in range(rows):
            pygame.draw.line(screen, grey, (j * width_of_cubes, 0), (j * width_of_cubes, width))

#
def draw(screen, grid, rows, width):
    screen.fill(white)

    for row in grid:
        for node in row:
            node.draw(screen)

    draw_grid(screen, rows, width)

    pygame.display.update()

# 
def get_clicked_node_position(position, rows, width):
    width_of_cubes = width // rows
    y, x = position

    row = y // width_of_cubes
    col = x // width_of_cubes

    return row, col


def main(screen, width):
    rows = 50
    grid = create_grid(rows, width)

    start = None
    end = None
    run = True

    while run:
        draw(screen, grid, rows, width)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            # Pressed the left mouse button
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_node_position(pos, rows, width)
                node = grid[row][col]

                if((not start) and (node != end)):
                    start = node
                    start.start_node()

                elif((not end) and (node != start)):
                    end = node
                    end.end_node()

                elif ((node != end) and (node != start)):
                    node.walled_node()

            # Pressed the right mouse button
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_node_position(pos, rows, width)
                node = grid[row][col]
                node.reset_node()

                if(node == start):
                    start = None
                
                elif(node == end):
                    end = None
            
            if(event.type == pygame.KEYDOWN):
                if((event.key == pygame.K_SPACE) and start and end):
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

					#algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
                
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

    pygame.quit()

main(screen, width)
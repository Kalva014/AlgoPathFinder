from grid import *

# Used to color the optimal path and retrace back
def backtrack(explored, start, end):
    path = [end]
    
    while path[0] != start:
        path[0].set_actual_path()
        path.append(explored[path[0]])
    
    path.reverse()
    
    return path

# This is the Breadth First Search for finding shortest path from node start to node finish
def BFS(graph, start, stop):
    # Track all explored nodes
    explored = {}

    # Track all paths to be checked
    queue = []
    queue.append([start])

    # Loop until all possible paths have been checked 
    while len(queue) != 0:
        # Pop the first box from the queue and then add its neighbors to the queue
        curr_list_of_nodes = queue.pop(0)

        queue.append(curr_list_of_nodes[0].neighbors)

        for visitedList in queue:
            for node in visitedList:
                node.set_visited()
                explored = visitedList.pop()

                if(node == stop):
                    backtrack(explored, start, stop)

        graph.update_grid(graph.grid_list)

def dijkstras_algorithm(graph, start, stop):
    # Initialize all the nodes to be infinity
    infinity = 9999999
    shortest_distance = [[infinity] * 20 for _ in range(20)]  # Corrected initialization
    predecessor = [[None] * 20 for _ in range(20)]  # Corrected initialization
    path = []
    unseen_nodes = []

    # Add every node to unseen nodes
    for curr_node_row in graph.grid_list:
        for i in range(len(curr_node_row)):
            unseen_nodes.append(curr_node_row[i])

    # Set starting node to have a distance of 0
    shortest_distance[start.row][start.column] = 0

    while unseen_nodes:
        min_node = None

        for curr_node in unseen_nodes:
            if min_node is None or shortest_distance[curr_node.row][curr_node.column] < shortest_distance[min_node.row][min_node.column]:
                min_node = curr_node

        for child_node in min_node.neighbors:
            if not child_node.is_wall():
                if child_node.distance + shortest_distance[min_node.row][min_node.column] < shortest_distance[child_node.row][child_node.column]:
                    shortest_distance[child_node.row][child_node.column] = child_node.distance + shortest_distance[min_node.row][min_node.column]
                    predecessor[child_node.row][child_node.column] = min_node

        min_node.set_visited()
        graph.update_grid(graph.grid_list)

        unseen_nodes.remove(min_node)

    current_node = stop
    while current_node != start:
        path.insert(0, current_node)
        current_node = predecessor[current_node.row][current_node.column]

    path.insert(0, start)

    # Show shortest path and color it on the GUI
    for node in path:
        node.set_actual_path()
    
    graph.update_grid(graph.grid_list)
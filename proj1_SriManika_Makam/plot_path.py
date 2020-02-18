import numpy as np
import os


class Puzzle:
    def __init__(self, node_index, node_data, parent):
        self.node_index = node_index
        self.node_data = node_data
        self.parent = parent

def BlankTileLocation(node):
    i,j = np.where(node == 0)
    return i,j


def ActionMoveLeft(node):
    i, j = BlankTileLocation(node)
    if j == 0:
        return None
    else:
        temp_arr = np.copy(node)
        temp = temp_arr[i, j - 1]
        temp_arr[i, j] = temp
        temp_arr[i, j - 1] = 0
        return temp_arr


def ActionMoveRight(node):
    i, j = BlankTileLocation(node)
    if j == 2:
        return None
    else:
        temp_arr = np.copy(node)
        temp = temp_arr[i, j + 1]
        temp_arr[i, j] = temp
        temp_arr[i, j + 1] = 0
        return temp_arr


def ActionMoveUp(node):
    i, j = BlankTileLocation(node)
    if i == 0:
        return None
    else:
        temp_arr = np.copy(node)
        temp = temp_arr[i - 1, j]
        temp_arr[i, j] = temp
        temp_arr[i - 1, j] = 0
        return temp_arr


def ActionMoveDown(node):
    i, j = BlankTileLocation(node)
    if i == 2:
        return None
    else:
        temp_arr = np.copy(node)
        temp = temp_arr[i + 1, j]
        temp_arr[i, j] = temp
        temp_arr[i + 1, j] = 0
        return temp_arr

def MoveTile(action, node):
    if action == 'Up':
        return ActionMoveUp(node)
    if action == 'Down':
        return ActionMoveDown(node)
    if action == 'Left':
        return ActionMoveLeft(node)
    if action == 'Right':
        return ActionMoveRight(node)
    else:
        return None

def BFS(x,goal_node):
    actions = ["Down", "Up", "Left", "Right"]
    node = [x]
    nodes_list = []
    visited_nodes = []
    nodes_list.append(node[0].node_data.tolist())  
    visited_nodes.append(x)
    index = 0

    while node:
        current_node = node.pop(0)
        if current_node.node_data.tolist() == goal_node.tolist():
            print("Goal state reached")
            return current_node, nodes_list, visited_nodes

        for move in actions:
            temp = MoveTile(move, current_node.node_data)
            if temp is not None:
                index += 1
                child_node = Puzzle(index, np.array(temp), current_node)

                if child_node.node_data.tolist() not in nodes_list: 
                    node.append(child_node)
                    nodes_list.append(child_node.node_data.tolist())
                    visited_nodes.append(child_node)
                    if child_node.node_data.tolist() == goal_node.tolist():
                        print("Goal state reached")
                        return child_node, nodes_list, visited_nodes
    return None

def GeneratePath(node):  
    path = []  
    path.append(node)
    parent_node = node.parent
    while parent_node is not None:
        path.append(parent_node)
        parent_node = parent_node.parent
    return list(reversed(path))





input_node = [1,2,3,4,0,5,6,7,8]  
# print("Enter the 9 numbers which forms the initial node (press enter after each number)")
# # iterating till the range 
# for i in range(0, 9): 
#     ele = int(input()) 
#     input_node.append(ele) # adding the element 

input_node = np.reshape(input_node, (3,3))
print("Input node:  ")
print(input_node)

# posiiton = BlankTileLocation(input_node)
# print(position)

goal_node = np.array([[1,2,3],[4,5,6],[7,8,0]])
print("Goal node:  ")
print(goal_node)


obj = Puzzle(0, input_node, None)

goal, nodes_list, visited_nodes = BFS(obj, goal_node)

if goal is not None and nodes_list is not None and visited_nodes is not None: 

    shortest_path = GeneratePath(goal)
    print("\n The shortest path to reach the goal is: ")
    for node in shortest_path:
        print("\n")
        print(node.node_data)


    if os.path.exists("nodePath.txt"):
        os.remove("nodePath.txt")
    f = open("nodePath.txt", "a")
    for node in shortest_path:
        transpose = zip(*node.node_data)
        l = np.reshape(transpose, 9)
        f.write(str(np.reshape(l, 9)) + "\n" )
    f.close()


    if os.path.exists("Nodes.txt"):
        os.remove("Nodes.txt")
    f = open("Nodes.txt", "a")
    for node in visited_nodes:
        transpose = zip(*node.node_data)
        l = np.reshape(transpose, 9)
        f.write(str(np.reshape(l, 9)) + "\n" )
    f.close()


    if os.path.exists("NodesInfo.txt"):
        os.remove("NodesInfo.txt")
    f = open("NodesInfo.txt", "a")
    for node in visited_nodes:
        if node.parent is not None:
            f.write(str(node.node_index) +"\t" + str(node.parent.node_index) + "\n")
    f.close()

else:
    print("Goal state could not be reached")
















    






















import numpy as np


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
    if action == 'up':
        return ActionMoveUp(node)
    if action == 'down':
        return ActionMoveDown(node)
    if action == 'left':
        return ActionMoveLeft(node)
    if action == 'right':
        return ActionMoveRight(node)
    else:
        return None

def BFS(x,goal_node):
    actions = ["down", "up", "left", "right"]
    node = [x]
    nodes_list = []
    visited_nodes = []
    nodes_list.append(node[0].node_data.tolist())  
    visited_nodes.append(x)
    index = 0

    while node:
        current_node = node.pop(0)
        if current_node.node_data.tolist() == goal_node.tolist():
            print("Goal node reached")
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
                        print("Goal node reached")
                        return child_node, nodes_list, visited_nodes
    return None







input_node = [1, 0,3,4,2,5,7,8,6]  
# print("Enter the 9 numbers which forms the initial node (press enter after each number)")
# # iterating till the range 
# for i in range(0, 9): 
#     ele = int(input()) 
#     input_node.append(ele) # adding the element 

input_node = np.reshape(input_node, (3,3))
print("Input node: \n ")
print(input_node)

# posiiton = BlankTileLocation(input_node)
# print(position)

goal_node = np.array([[1,2,3],[4,5,6],[7,8,0]])
print("Goal node: \n ")
print(goal_node)


obj = Puzzle(0, input_node, None)

goal, nodes_list, visited_nodes = BFS(obj, goal_node)


for i in range(len(nodes_list)):
    print("\n")
    print(np.reshape(nodes_list[i], (3,3)))











    






















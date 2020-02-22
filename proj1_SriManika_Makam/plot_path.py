import numpy as np
import os
import collections 


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

def CreateKey(arr):
    num = np.reshape(arr, 9)
    # print(num)
    num = int(''.join(str(i) for i in num))
    return num

def BFS(x,goal_node):
    actions = ["Down", "Up", "Left", "Right"]
    # node = [x]
    node = collections.deque([x])
    nodes_list = {CreateKey(node[0].node_data) : node[0].node_index}
    visited_nodes = []
    # nodes_list.append(node[0].node_data.tolist())  
    visited_nodes.append(x)
    index = 0

    while node:
        current_node = node.popleft()
        if current_node.node_data.tolist() == goal_node.tolist():
            print("Goal state reached")
            return current_node, visited_nodes

        for move in actions:
            temp = MoveTile(move, current_node.node_data)
            if temp is not None:
                index += 1
                child_node = Puzzle(index, np.array(temp), current_node)


                if CreateKey(child_node.node_data) not in nodes_list: 
                    node.append(child_node)
                    nodes_list[CreateKey(child_node.node_data)] = child_node.node_index
                    visited_nodes.append(child_node)
                    if child_node.node_data.tolist() == goal_node.tolist():
                        print("Goal state reached")
                        return child_node, visited_nodes
    return None

def GeneratePath(node):  
    path = []  
    path.append(node)
    parent_node = node.parent
    while parent_node is not None:
        path.append(parent_node)
        parent_node = parent_node.parent
    return list(reversed(path))

def CheckInput(l):
    l = np.reshape(l, 9)
    flag=1
    for i in range(len(l)): 
        for i1 in range(len(l)): 
            if i != i1: 
                if l[i] == l[i1]: 
                    flag = 0
    return flag

    
def CheckSolvability(l):
    l = np.reshape(l, 9)
    count = 0
    for i in range(len(l)): 
        for j in range(i + 1, len(l)): 
            if (l[i] > l[j] and l[i]!=0 and l[j]!=0): 
                count += 1
    if count % 2 == 0:
        return 1 
    else:
        return 0





# input_node = [1,4,7,0,2,8,3,5,6]  
print("If the node is [[1,0,3],[4,2,5],[7,8,6]], then give the input as [1,4,7,0,2,8,3,5,6]")
print("Enter the 9 numbers which forms the initial node (press enter after each number)")

input_node=[]
for i in range(0, 9): 
    ele = int(input()) 
    input_node.append(ele) 

input_node = np.reshape(input_node, (3,3))
input_node = zip(*input_node)
input_node = np.reshape(input_node, (3,3))
print("Input node:  ")
print(input_node)


# posiiton = BlankTileLocation(input_node)
# print(position)

goal_node = np.array([[1,2,3],[4,5,6],[7,8,0]])
print("Goal node:  ")
print(goal_node)

inp= CheckInput(input_node)
sol = CheckSolvability(input_node)

if inp==1: 

    if sol==1:

        obj = Puzzle(0, input_node, None)

        goal, visited_nodes = BFS(obj, goal_node)

        if goal is not None and visited_nodes is not None: 

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
    else:

        print("The puzzle cannot be solved")
else:
    print ("Given input is invalid because it does not contain distinct numbers") 















    






















import numpy as np

# def print_matrix(state):
#     counter = 0
#     for row in range(0, len(state), 3):
#         if counter == 0 :
#             print("-------------")
#         for element in range(counter, len(state), 3):
#             if element <= counter:
#                 print("|", end=" ")
#             print(int(state[element]), "|", end=" ")
#         counter = counter +1
#         print("\n-------------")

# fname = 'nodePath.txt'
# data = np.loadtxt(fname)
# if len(data[1]) is not 9:
#     print("Format of the text file is incorrect, retry ")
# else:
#     for i in range(0, len(data)):
#         if i == 0:
#             print("Start Node")
#         elif i == len(data)-1:
#             print("Achieved Goal Node")
#         else:
#             print("Step ",i)
#         print_matrix(data[i])
#         print()
#         print()






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








input_node = [1, 0,3,4,2,5,7,8,6]  
# print("Enter the 9 numbers which forms the initial node (press enter after each number)")
# # iterating till the range 
# for i in range(0, 9): 
#     ele = int(input()) 
#     input_node.append(ele) # adding the element 

input_node = np.reshape(input_node, (3,3))
print("Input node: " , input_node) 

# posiiton = BlankTileLocation(input_node)
# print(position)




    






















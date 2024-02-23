rows = 9
cols = 9
u = 0
board = {}
view_board = {}
remove_board = {}
temp_board = {}
#user_input = 0
trials = 0

#####
# functions
##### 

# function for repetitive code in remove_board portion
def remove_check(column,row):
    # this function tests to see if the compared cell has a single value, in which case the value can be removed from possiblities of current cell
    # board, remove_board, x, and y should all be global variables that do not need definitions in the function
    # column and row are the inputs, which have different names depending on the test condition
    if len(board[(column,row)]) == 1:
        v = board[(column,row)]
        g = v[0]
        if v != board[(x,y)] and g not in remove_board[(x,y)]:
            remove_board[(x,y)].append(g)

#####
# Main code
#####            

# I think the input might work better as just one array or list input from the user, but I will leave it as single item for now
for x in range(cols):
    for y in range(rows):  
       u = u + 1         
       board[(x,y)] = []  # I dont like the indexing you are using. why have +1 on everything?
       print("digit", u)
       user_input = input()
       if user_input == "":
          board[(x,y)] = list(range(1,10))
       else:
          board[(x,y)] = [int(user_input)]
       remove_board[(x,y)] = []
       

while max(board,key=len) > 1 and trials < 100:     # for this, there should be some stop condition. a while loop based on the length of all of the board entries perhaps
    trials += 1
    # test the cell to see if any values can be removed from possibility bc they are already in other cells in the column, row, or square
    for x in range(cols):   
        for y in range (rows):
            # test columns
            for j in range(cols):
                remove_check(j,y)

            # test rows
            for i in range(rows):
                remove_check(x,i)

            # test squares -- will try to make a function. in the meantime, this should increase the y values first so the code has to check fewer times
            if x < 2.9 and y < 2.9:
                for q in range(3):
                    for p in range(3):
                        remove_check(q,p)
            elif x < 5.9 and y < 2.9:
                for q in range(3,6):
                    for p in range(3):
                        remove_check(q,p) 
            elif x < 8.9 and y < 2.9:
                for q in range(6,9):
                    for p in range(3):
                        remove_check(q,p)
            elif x < 2.9 and y < 5.9:
                for q in range(3):
                    for p in range(3,6):
                        remove_check(q,p)
            elif x < 5.9 and y < 5.9:
                for q in range(3,6):
                    for p in range(3,6):
                        remove_check(q,p) 
            elif x < 8.9 and y < 5.9:
                for q in range(6,9):
                    for p in range(3,6):
                        remove_check(q,p)
            elif x < 2.9 and y < 8.9:
                for q in range(3):
                    for p in range(6,9):
                        remove_check(q,p)
            elif x < 5.9 and y < 8.9:
                for q in range(3,6):
                    for p in range(6,9):
                        remove_check(q,p)
            elif x < 8.9 and y < 8.9:
                for q in range(6,9):
                    for p in range(6,9):
                        remove_check(q,p)   

            # remove any values from main board that have been added to the remove list    
            board[(x,y)] = [t for t in board[(x,y)] if t not in remove_board[(x,y)]]

    # go through each cell again and test whether a number that has not been removed is in a cell in the same column or row
    for x in range(cols):
        for y in range(rows):
            if len(board[(x,y)]) != 1:
                temp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for i in range(cols):
                    for num in board[(x,i)]:
                        if num in temp_list and i != y:
                            temp_list.remove(num)
                    if len(temp_list) == 0:
                        break
                if len(temp_list) == 1:
                    board[(x,y)] = temp_list
    for x in range(cols):
        for y in range(rows):
            if len(board[(x,y)]) != 1:
                temp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for j in range(rows):
                    for num in board[(j,y)]:
                        if num in temp_list and j != x:
                            temp_list.remove(num)
                    if len(temp_list) == 0:
                        break
                if len(temp_list) == 1:
                    board[(x,y)] = temp_list

# print the board                    
for x in range(cols):
    for y in range (rows):
        if len(board[(x,y)]) == 1:
            view_board[(x,y)] = board[(x,y)] 
        else:
           view_board[(x,y)] = 'x'
for x in range(cols):
    for y in range(rows):
        print(view_board[(x,y)], end= '  ')
    print()
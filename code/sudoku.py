rows = 9
cols = 9
u = 0
board = {}
view_board = {}
remove_board = {}
temp_board = {}
#user_input = 0
trials = 0

# I think the input might work better as just one array or list input from the user, but I will leave it as single item for now
for x in range(cols):
    for y in range(rows):  
       u = u + 1         
       board[(x+1,y+1)] = []  # I dont like the indexing you are using. why have +1 on everything?
       print("digit", u)
       user_input = input()
       if user_input == "":
          board[(x+1,y+1)] = list(range(1,10))
       else:
          board[(x+1,y+1)] = [int(user_input)]
       remove_board[(x+1,y+1)] = []
       

for trials in range(5):     # for this, there should be some stop condition. a while loop based on the length of all of the board entries perhaps
    for x in range(cols):   # I dont think we need to go through each cell three times
        for y in range (rows):
            # test columns
            for j in range(cols):
                if len(board[(j+1,y+1)]) == 1:
                    v = board[(j+1,y+1)]
                    g = v[0]
                    if v != board[(x+1,y+1)] and g not in remove_board[(x+1,y+1)]:
                        remove_board[(x+1,y+1)].append(g)

            # test rows
            for i in range(rows):            
                if len(board[(x+1,i+1)])== 1:
                    v = board[(x+1,i+1)]
                    g = v[0]
                    if v != board[(x+1,y+1)] and g not in remove_board[(x+1,y+1)]:
                        remove_board[(x+1,y+1)].append(g)

            # test squares
            if x < 2.9 and y < 2.9:
                for q in range(3):
                    for p in range(3):
                        if len(board[q+1,p+1]) == 1:
                            v = board[(q+1,p+1)]
                            g = v[0]
                            if v != board[x+1,y+1] and g not in remove_board[(x+1,y+1)]:
                                remove_board[(x+1,y+1)].append(g)
            elif x < 5.9 and y < 2.9:
                for q in range(3):
                    for p in range(3):
                        if len(board[q+4,p+1]) == 1:
                            v = board[(q+4,p+1)]
                            g = v[0]
                            if v != board[x+1,y+1] and g not in remove_board[(x+1,y+1)]:
                                remove_board[(x+1,y+1)].append(g) 
            elif x < 8.9 and y < 2.9:
                for q in range(3):
                    for p in range(3):
                        if len(board[q+7,p+1]) == 1:
                            v = board[(q+7,p+1)]
                            g = v[0]
                            if v != board[x+1,y+1] and g not in remove_board[(x+1,y+1)]:
                                remove_board[(x+1,y+1)].append(g)
            elif x < 2.9 and y < 5.9:
                for q in range(3):
                    for p in range(3):
                        if len(board[q+1,p+4]) == 1:
                            v = board[(q+1,p+4)]
                            g = v[0]
                            if v != board[x+1,y+1] and g not in remove_board[(x+1,y+1)]:
                                remove_board[(x+1,y+1)].append(g)
            elif x < 5.9 and y < 5.9:
                for q in range(3):
                    for p in range(3):
                        if len(board[q+4,p+4]) == 1:
                            v = board[(q+4,p+4)]
                            g = v[0]
                            if v != board[x+1,y+1] and g not in remove_board[(x+1,y+1)]:
                                remove_board[(x+1,y+1)].append(g) 
            elif x < 8.9 and y < 5.9:
                for q in range(3):
                    for p in range(3):
                        if len(board[q+7,p+4]) == 1:
                            v = board[(q+7,p+4)]
                            g = v[0]
                            if v != board[x+1,y+1] and g not in remove_board[(x+1,y+1)]:
                                remove_board[(x+1,y+1)].append(g)
            elif x < 2.9 and y < 8.9:
                for q in range(3):
                    for p in range(3):
                        if len(board[q+1,p+7]) == 1:
                            v = board[(q+1,p+7)]
                            g = v[0]
                            if v != board[x+1,y+1] and g not in remove_board[(x+1,y+1)]:
                                remove_board[(x+1,y+1)].append(g)
            elif x < 5.9 and y < 8.9:
                for q in range(3):
                    for p in range(3):
                        if len(board[q+4,p+7]) == 1:
                            v = board[(q+4,p+7)]
                            g = v[0]
                            if v != board[x+1,y+1] and g not in remove_board[(x+1,y+1)]:
                                remove_board[(x+1,y+1)].append(g) 
            elif x < 8.9 and y < 8.9:
                for q in range(3):
                    for p in range(3):
                        if len(board[q+7,p+7]) == 1:
                            v = board[(q+7,p+7)]
                            g = v[0]
                            if v != board[x+1,y+1] and g not in remove_board[(x+1,y+1)]:
                                remove_board[(x+1,y+1)].append(g)   

            # remove any values from main board that have been added to the remove list    
            board[(x+1,y+1)] = [t for t in board[(x+1,y+1)] if t not in remove_board[(x+1,y+1)]]

    # go through each cell again and test whether a number that has not been removed is in a cell in the same column or row
    for x in range(cols):
        for y in range(rows):
            if len(board[(x+1,y+1)]) != 1:
                temp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for i in range(cols):
                    for num in board[(x+1,i+1)]:
                        if num in temp_list and i != y:
                            temp_list.remove(num)
                    if len(temp_list) == 0:
                        break
                if len(temp_list) == 1:
                    board[(x+1,y+1)] = temp_list
    for x in range(cols):
        for y in range(rows):
            if len(board[(x+1,y+1)]) != 1:
                temp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for j in range(rows):
                    for num in board[(j+1,y+1)]:
                        if num in temp_list and j != x:
                            temp_list.remove(num)
                    if len(temp_list) == 0:
                        break
                if len(temp_list) == 1:
                    board[(x+1,y+1)] = temp_list
for x in range(cols):
    for y in range (rows):
        if len(board[(x+1,y+1)]) == 1:
            view_board[(x+1,y+1)] = board[(x+1,y+1)] 
        else:
           view_board[(x+1,y+1)] = 'x'
for x in range(cols):
    for y in range(rows):
        print(view_board[(x+1,y+1)], end= '  ')
    print()
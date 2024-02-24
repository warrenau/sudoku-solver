u = 0
board = {}
view_board = {}
remove_board = {}
temp_board = {}
nine_list = [x for x in range(1,10)]
thre_list = [x for x in range(1,4)]
for y in nine_list:
    for x in nine_list:
            board[(x,y)] = nine_list # generate 81 unique cells each with possible numbers 1-9
            remove_board[((x,y))] = [] # generate empty dictionary. this will be used to remove values from the board
board[1,1] = [1]
board[7,1] = [2]
board[3,2] = [6]
board[6,2] = [3]
board[1,3] = [3]
board[5,3] = [1]
board[7,3] = [9]
board[8,3] = [4]
board[3,4] = [7]
board[4,4] = [9]
board[7,4] = [4]
board[8,4] = [8]
board[5,5] = [8]
board[7,5] = [7]
board[9,5] = [6]
board[1,6] = [4]
board[9,6] = [2]
board[2,7] = [5]
board[4,7] = [7]
#board[5,7] = [3] # removing this cell becomes unsolvable
board[9,8] = [8]
board[1,9] = [6]
board[5,9] = [9]
board[7,9] = [3]
board[8,9] = [1]
#for y in nine_list: #receive the values of each cell from user
#    for x in nine_list:  
#        u += 1         
#        board[(x,y)] = []
#        remove_board[(x,y)] = []
#        print("digit", u)
#        user_input = input()
#        if user_input == "":
#           board[(x,y)] = nine_list
#        else:
#            board[(x,y)] = [int(user_input)]
for trials in range(10):  # 48 - 67 determine what values cannot exist in given cell
    for x in nine_list:
        for y in nine_list:
            if len(board[(x,y)]) != 1:
                for j in nine_list:
                    if len(board[(j,y)]) == 1:
                        v = board[(j,y)]
                        if v != board[(x,y)] and v[0] not in remove_board[(x,y)]:
                            remove_board[(x,y)].append(v[0])
                for i in nine_list:            
                    if len(board[(x,i)])== 1:
                        v = board[(x,i)]
                        if v != board[(x,y)] and v[0] not in remove_board[(x,y)]:
                            remove_board[(x,y)].append(v[0])              
                for q in thre_list:
                    for p in thre_list:
                        if len(board[q+(x-1-((x-1) % 3)),p+(y-1-((y-1) % 3))]) == 1:
                            v = board[q+(x-1-((x-1) % 3)),p+(y-1-((y-1) % 3))]
                            if v != board[x,y] and v[0] not in remove_board[(x,y)]:
                                remove_board[(x,y)].append(v[0]) 
    for x in nine_list:  # 68 - 71 update the board to remove all non-possible digits
        for y in nine_list:            
            temp_board[(x,y)] = [t for t in board[(x,y)] if t not in remove_board[(x,y)]]
    board = temp_board
    for x in nine_list: #72- 85 check every cell in each column for every cell. if all other cells in the column cant be X, then the cell you are looking at must be X
        for y in nine_list:
            if len(board[(x,y)]) != 1:
                temp_list = [x for x in nine_list]
                for i in nine_list:
                    if i == y:
                        continue
                    for num in board[(x,i)]:
                        if num in temp_list:
                            temp_list.remove(num)
                    if len(temp_list) == 0:
                        break
                if len(temp_list) == 1:
                    board[(x,y)] = temp_list
    for x in nine_list: #86- 99 check every cell in each row for every cell. if all other cells in the row cant be X, then the cell you are looking at must be X
        for y in nine_list:
            if len(board[(x,y)]) != 1: # I would think these 3 lines could be removed but when i remove them it doesnt work
                temp_list = [x for x in nine_list]
                for j in nine_list:
                    if x == j:
                        continue
                    for num in board[(j,y)]:
                        if num in temp_list:
                            temp_list.remove(num)
                    if len(temp_list) == 0:
                        break
                if len(temp_list) == 1:
                    board[(x,y)] = temp_list
    for x in nine_list: #100 - 115 check every cell in each square for every cell. if all other cells in the square cant be X, then the cell you are looking at must be X
        for y in nine_list:
            if len(board[(x,y)]) != 1: # these 3 lines too, not sure why they are necessary
                temp_list = [x for x in nine_list]
                for q in thre_list:
                    for p in thre_list:
                        if q+(x-1-((x-1) % 3)) == x: 
                            if p+(y-1-((y-1) % 3)) == y:
                                continue
                        for num in board[q+(x-1-((x-1) % 3)),p+(y-1-((y-1) % 3))]:
                            if num in temp_list: 
                                temp_list.remove(num)
                    if len(temp_list) == 0:
                        break
                if len(temp_list) == 1:
                    board[(x,y)] = temp_list
for x in nine_list: # 116-121 generate a dictionary 'view board' thats easy to print
    for y in nine_list:
        if len(board[(x,y)]) == 1:
            view_board[(x,y)] = board[(x,y)] 
        else:
           view_board[(x,y)] = 'x'
for y in nine_list: #122- 125 print the board
    for x in nine_list:
        print(view_board[(x,y)], end= '  ')
    print()
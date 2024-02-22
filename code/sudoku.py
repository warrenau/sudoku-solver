u = 0
board = {}
view_board = {}
remove_board = {}
temp_board = {}
nine_list = [x for x in range(1,10)] # addition of lists to help indexing
thre_list = [x for x in range(1,4)]
# I do not know how to have the input be a list/array, would love to see how it could be done. End goal is for program to enter the numbers itself though
for x in nine_list:
    for y in nine_list:  
        u += 1         
        board[(x,y)] = [] # indexing fixed. ur welcome.
        remove_board[(x,y)] = []
        print("digit", u)
        user_input = input()
        if user_input == "":
           board[(x,y)] = nine_list
        else:
            board[(x,y)] = [int(user_input)]
for trials in range(10): # havent setup a while loop yet for a few reasons but is a good idea
    for x in nine_list: # we probably dont need to go through each cell 3 times but when i tried to do it all at once it wasn't working. breaking it into 3 separate checks got it working lol
        for y in nine_list:
            for j in nine_list:
                if len(board[(j,y)]) == 1:
                    v = board[(j,y)]
                    g = v[0]
                    if v != board[(x,y)] and g not in remove_board[(x,y)]:
                        remove_board[(x,y)].append(g)
    for x in nine_list:
        for y in nine_list:
            for i in nine_list:            
                if len(board[(x,i)])== 1:
                    v = board[(x,i)]
                    g = v[0]
                    if v != board[(x,y)] and g not in remove_board[(x,y)]:
                        remove_board[(x,y)].append(g)
    for x in nine_list:
        for y in nine_list:
            if x < 3.9 and y < 3.9:
                for q in thre_list:
                    for p in thre_list:
                        if len(board[q,p]) == 1:
                            v = board[(q,p)]
                            g = v[0]
                            if v != board[x,y] and g not in remove_board[(x,y)]:
                                remove_board[(x,y)].append(g)
            elif x < 6.9 and y < 3.9:
                for q in thre_list:
                    for p in thre_list:
                        if len(board[q+3,p]) == 1:
                            v = board[(q+3,p)]
                            g = v[0]
                            if v != board[x,y] and g not in remove_board[(x,y)]:
                                remove_board[(x,y)].append(g) 
            elif x < 9.9 and y < 3.9:
                for q in thre_list:
                    for p in thre_list:
                        if len(board[q+6,p]) == 1:
                            v = board[(q+6,p)]
                            g = v[0]
                            if v != board[x,y] and g not in remove_board[(x,y)]:
                                remove_board[(x,y)].append(g)
            elif x < 3.9 and y < 6.9:
                for q in thre_list:
                    for p in thre_list:
                        if len(board[q,p+3]) == 1:
                            v = board[(q,p+3)]
                            g = v[0]
                            if v != board[x,y] and g not in remove_board[(x,y)]:
                                remove_board[(x,y)].append(g)
            elif x < 6.9 and y < 6.9:
                for q in thre_list:
                    for p in thre_list:
                        if len(board[q+3,p+3]) == 1:
                            v = board[(q+3,p+3)]
                            g = v[0]
                            if v != board[x,y] and g not in remove_board[(x,y)]:
                                remove_board[(x,y)].append(g) 
            elif x < 9.9 and y < 6.9:
                for q in thre_list:
                    for p in thre_list:
                        if len(board[q+6,p+3]) == 1:
                            v = board[(q+6,p+3)]
                            g = v[0]
                            if v != board[x,y] and g not in remove_board[(x,y)]:
                                remove_board[(x,y)].append(g)
            elif x < 3.9 and y < 9.9:
                for q in thre_list:
                    for p in thre_list:
                        if len(board[q,p+6]) == 1:
                            v = board[(q,p+6)]
                            g = v[0]
                            if v != board[x,y] and g not in remove_board[(x,y)]:
                                remove_board[(x,y)].append(g)
            elif x < 6.9 and y < 9.9:
                for q in thre_list:
                    for p in thre_list:
                        if len(board[q+3,p+6]) == 1:
                            v = board[(q+3,p+6)]
                            g = v[0]
                            if v != board[x,y] and g not in remove_board[(x,y)]:
                                remove_board[(x,y)].append(g) 
            elif x < 9.9 and y < 9.9:
                for q in thre_list:
                    for p in thre_list:
                        if len(board[q+6,p+6]) == 1:
                            v = board[(q+6,p+6)]
                            g = v[0]
                            if v != board[x,y] and g not in remove_board[(x,y)]:
                                remove_board[(x,y)].append(g)   
    for x in nine_list:
        for y in nine_list:            
            temp_board[(x,y)] = [t for t in board[(x,y)] if t not in remove_board[(x,y)]]
    board = temp_board
    for x in nine_list:
        for y in nine_list:
            if len(board[(x,y)]) != 1:
                temp_list = [x for x in nine_list]
                for i in nine_list:
                    for num in board[(x,i)]:
                        if num in temp_list and i != y:
                            temp_list.remove(num)
                    if len(temp_list) == 0:
                        break
                if len(temp_list) == 1:
                    board[(x,y)] = temp_list
    for x in nine_list:
        for y in nine_list:
            if len(board[(x,y)]) != 1:
                temp_list = [x for x in nine_list]
                for j in nine_list:
                    for num in board[(j,y)]:
                        if num in temp_list and j != x:
                            temp_list.remove(num)
                    if len(temp_list) == 0:
                        break
                if len(temp_list) == 1:
                    board[(x,y)] = temp_list
for x in nine_list:
    for y in nine_list:
        if len(board[(x,y)]) == 1:
            view_board[(x,y)] = board[(x,y)] 
        else:
           view_board[(x,y)] = 'x'
for x in nine_list:
    for y in nine_list:
        print(view_board[(x,y)], end= '  ')
    print()
# i want the program to automatically enter the values into the online sudoku website.
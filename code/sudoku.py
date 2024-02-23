u = 0
board = {}
view_board = {}
remove_board = {}
temp_board = {}
nine_list = [x for x in range(1,10)]
thre_list = [x for x in range(1,4)]
for x in nine_list:
    for y in nine_list:  
        u += 1         
        board[(x,y)] = []
        remove_board[(x,y)] = []
        print("digit", u)
        user_input = input()
        if user_input == "":
           board[(x,y)] = nine_list
        else:
            board[(x,y)] = [int(user_input)]
for trials in range(10):
    for x in nine_list:
        for y in nine_list:
            if len(board[(x,y)]) != 1:
                for j in nine_list:
                    if len(board[(j,y)]) == 1:
                        v = board[(j,y)]
                        if v != board[(x,y)] and v[0] not in remove_board[(x,y)]:
                            remove_board[(x,y)].append(v[0])     
    for x in nine_list:
        for y in nine_list:
            if len(board[(x,y)]) != 1:                  
                for i in nine_list:            
                    if len(board[(x,i)])== 1:
                        v = board[(x,i)]
                        if v != board[(x,y)] and v[0] not in remove_board[(x,y)]:
                            remove_board[(x,y)].append(v[0])    
    for x in nine_list:
        for y in nine_list:
            if len(board[(x,y)]) != 1:                   
                for q in thre_list:
                    for p in thre_list:
                        if len(board[q+(x-1-((x-1) % 3)),p+(y-1-((y-1) % 3))]) == 1:
                            v = board[q+(x-1-((x-1) % 3)),p+(y-1-((y-1) % 3))]
                            if v != board[x,y] and v[0] not in remove_board[(x,y)]:
                                remove_board[(x,y)].append(v[0]) 
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
#    for x in nine_list:
#        for y in nine_list:
#            if len(board[(x,y)]) != 1: 
#                temp_list = [x for x in nine_list]
#                for q in thre_list:
#                    for p in thre_list:
#                        for num in board[q+(x-1-((x-1) % 3)),p+(y-1-((y-1) % 3))]:
#                            if q+(x-1-((x-1) % 3)) != x and p+(y-1-((y-1) % 3)) != y:
#                                if num in temp_list: 
#                                    temp_list.remove(num)
#                        if len(temp_list) == 0:
#                            break
#                if len(temp_list) == 1:
#                    board[(x,y)] = temp_list
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
class FBoard:
    """FBoard game"""
    
    def __init__(self):
         # 8x8 grid where -1 represents empty, 0 represents 'O' and 10 represents 'X'
        self.__boardList = [[10,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,0],
                        [-1,-1,-1,-1,-1,-1,0,-1],
                        [-1,-1,-1,-1,-1,0,-1,0]]

        self.__gameState = {
            "X_WON": False,
            "O_WON": False,
            "UNFINISHED": True
        }
        
        self.__xPieceLocation = [0,0]
        
    ###### Methods #######
    def get_game_state(self):
        return self.__gameState
    
    def set_game_state_x_won(self):
        self.__gameState["X_WON"] = True
        self.__gameState["UNFINISHED"] = False

    def set_game_state_o_won(self):
        self.__gameState["O_WON"] = True
        self.__gameState["UNFINISHED"] = False
        
    def get_board(self):
        return self.__boardList
        
    def move_x(self, x, y):
        if self.is_x_move_legal(x,y) == False:
            return False
        retVal = self.set_board_location(10, x, y)
        if retVal == False:
            return False
        else:
            #reset the original position to empty in the board
            xLocation = self.get_x_piece_location()
            self.clear_board_location(xLocation[0], xLocation[1])
            #update x tracker
            self.set_x_piece_location(x,y)
            #check if x has won
            if x == 7 and y == 7:
                self.set_game_state_x_won()
            return True

    def get_x_piece_location(self):
        return self.__xPieceLocation
        
    def set_x_piece_location(self, x, y):
        self.__xPieceLocation = [x,y]
        return
    
    def move_o(self, from_x, from_y, to_x, to_y):
        if self.is_o_move_legal(from_x, from_y, to_x, to_y) == False:
            return False
        retVal = self.set_board_location(0, to_x, to_y)
        if retVal == False:
            return False
        else:
            #reset the original position to empty in the board
            self.clear_board_location(from_x, from_y)
            #check if game is finished (i.e. does x have legal moves)
            if self.does_x_have_legal_moves() == False:
                self.set_game_state_o_won()
            return True

    def does_x_have_legal_moves(self):
        xLocation = self.get_x_piece_location()
        board = self.get_board()
        xVal = xLocation[0]
        yVal = xLocation[1]
        boardVal1 = 0
        boardVal2 = 0
        boardVal3 = 0
        boardVal4 = 0
        #Compute next moves and see if that square is empty or off-board
        if xVal+1 < 8 and yVal+1 < 8:
            boardVal1 = board[xVal+1][yVal+1]
        if xVal-1 > -1 and yVal-1 > -1:
            boardVal2 = board[xVal-1][yVal-1]
        if xVal-1 > -1 and yVal+1 < 8:
            boardVal3 = board[xVal-1][yVal+1]
        if xVal+1 < 8 and yVal-1 > 0:
            boardVal4 = board[xVal+1][yVal-1]
        if boardVal1 != -1 and boardVal2 != -1 and boardVal3 != -1 and boardVal4 != -1:
            return False
        return True
        
    #Set a location on the board
    def set_board_location(self, value, x, y):
        self.get_board()[x][y] = value
        return True
    
    #Sets this square to empty
    def clear_board_location(self, x, y):
        self.get_board()[x][y] = -1
        return
        
    def is_x_move_legal(self, x, y):
        #game should not have been finished
        if self.is_game_over() == True:
            return False
        #move should not be off-board
        if x < 0 or x > 7 or y < 0 or y > 7:
            return False
        #square to move to should be empty
        if self.get_board()[x][y] != -1:
            return False
        #diagonal check
        xLocation = self.get_x_piece_location()
        if xLocation != [x-1,y-1] and xLocation != [x+1,y+1] and xLocation != [x-1,y+1] and xLocation != [x+1,y-1] :
            return False
        return True
        
    def is_o_move_legal(self, from_x, from_y, to_x, to_y):
        #game should not have been finished
        if self.is_game_over() == True:
            return False
        #move should not be off-board
        if to_x < 0 or to_x > 7 or to_y < 0 or to_y > 7 or from_x < 0 or from_x > 7 or from_y < 0 or from_y > 7 :
            return False
        #to square should be empty
        to_square = self.get_board()[to_x][to_y]
        if to_square != -1:
            return False
        #check that the from square has o's piece or not
        from_square = self.get_board()[from_x][from_y]
        if from_square != 0:
            return False
        #check if its a legal diagonal move for 'o'
        if [from_x,from_y] != [to_x+1,to_y+1] and [from_x,from_y] != [to_x-1,to_y+1] and [from_x,from_y] != [to_x+1,to_y-1]:
            return False
        return True
        
    def is_game_over(self):
        #game should not have been finished
        gameState = self.get_game_state()
        if self.get_game_state()["UNFINISHED"] != True:
            return True
        return False

############## print helper ##############

    def print(self):
        print("Hello world")
        
        retVal = self.set_board_location(10,0,0)
        print(self.get_board())
        print(self.get_game_state())
        
         #illegal x move
        self.move_x(1,2)
        print(self.get_x_piece_location())
        print(self.get_board())
        
        #test does_x_have_legal_moves method
        print(self.does_x_have_legal_moves())

        #winning moves for x
        print("### Test X Win ###")
        # self.move_o(6,6,5,5)
        # self.move_o(5,5,4,4)
        # self.move_o(4,4,3,5)
        # print(self.move_o(7,7,6,6))
        # print(self.move_o(6,6,7,7)) #illegal move so should not work
        # print(self.move_o(6,6,7,7))
        # print(self.move_o(6,6,5,5))
        # print(self.move_o(5,5,4,6))
        # self.move_x(1,1)
        # self.move_x(2,2)
        # self.move_x(3,3)
        # self.move_x(4,4)
        # self.move_x(5,5)
        # print(self.move_x(6,6))
        # self.move_x(7,7)
        # print(self.get_board())
        # print(self.get_game_state())

        # print("### Test O Win ###")
        self.move_o(6,6,5,5)
        self.move_o(5,5,4,4)
        self.move_o(4,4,3,3)
        self.move_o(3,3,2,2)
        self.move_o(2,2,1,1)
        print(self.get_board())
        print(self.get_game_state())


###### test code ########
fb = FBoard();
fb.print();

fb2 = FBoard();
fb2.move_x(1,1);
fb2.move_x(2,0);
fb2.move_o(6,6,5,5);
print(fb.get_game_state());

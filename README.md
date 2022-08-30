# FBoardGame

## Game played with 2 players on an 8x8 grid where player x is trying to get her piece to corner square (7,7) and player o is trying to make it so player x doesn't have any legal moves. 

## Grid template
    [X-------]
    [--------]
    [--------]
    [--------]
    [--------]
    [-------O]
    [------O-]
    [-----O-O]

## It has the following private data members:
* An 8x8 list of lists for tracking what's on each square of the board.
* A data member for tracking the game state, that holds one of the following string values: "X_WON", "O_WON", or "UNFINISHED".
* Data members to keep track of where the x piece is.

## Methods
* An init method that initializes the list of lists to represent an empty 8x8 board. Starting position is: Player o has pieces at (5,7), (6,6), (7,5), and (7,7) and player x has piece at (0,0).
* get_game_state - returns the current value of game_state.
* move_x - takes as parameters the row and column of the square to move to.  If the desired move is not allowed, or if the game has already been won, it should just return False.  Otherwise it should make the move and return True.  A piece belonging to x can move 1 square diagonally in any direction.  A piece is not allowed to move off the board or to an occupied square.  If x's move gets her piece to square (7,7), game_state should be set to "X_WON".
* move_o - takes as parameters the row and column to move from, and the row and column to move to.  If the first pair of coordinates doesn't hold o's piece, or if the desired move is not allowed, or if the game has already been won, it should just return False.  Othewise it should make the move and return True.  A piece belonging to o can move 1 square diagonally, **but the row and column cannot both increase**, so any o piece has at most three available moves.  For example, if player o has a piece at (5, 1), it could move to (4, 0), (4, 2), or (6,0), but not to (6, 2).  It is not allowed to move off the board or to an occupied square.  If o's move leaves no legal move for x, game_state should be set to "O_WON".

** Either move method can be called multiple times in a row. **

Here's a very simple example of how the class could be used:
```
   fb = FBoard();
   fb.move_x(1,1);
   fb.move_x(2,0);
   fb.move_o(6,6,5,5);
   print(fb.get_game_state());
```

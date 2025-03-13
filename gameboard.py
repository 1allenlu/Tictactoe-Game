class BoardClass():
    '''
    A simple class to store and handle information about BoardClass
    Attributes:
        playername (str): The player name entered from the user/player
        player_lastturn (str): User name of the last player to have a turn
        num_win (int): Number of wins
        num_ties (int): Number of ties
        num_loss (int): Number of losses
        game_start (int): Number of games started
        board (nested list): a nested list that shows the board to play Tic Tac Toe
    '''
    def __init__(self, playername: str = "", oppo_name: str = "", player_lastturn: str = "", num_win: int = 0, num_ties: int = 0, num_loss: int = 0, game_start: int = 1, board: list = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]) -> None:
        '''Make a BoardClass

        Args:
            playername (str): The player name entered from the user/player
            player_lastturn (str): User name of the last player to have a turn
            num_win (int): Number of wins
            num_ties (int): Number of ties
            num_loss (int): Number of losses
            game_start (int): Number of games started
            board (nested list): a nested list that shows the board to play Tic Tac Toe
        '''
        self.playername = playername
        self.oppo_name = oppo_name
        self.player_lastturn = player_lastturn
        self.num_win = num_win
        self.num_ties = num_ties
        self.num_loss = num_loss
        self.board = board 
        self.game_start = game_start
    
    def updateGamesPlayed(self) -> None:
        '''
        Keeps track and Updates how many games have started
        '''
        self.game_start += 1
    
    def resetGameBoard(self) -> None:
        '''
        Clears all the moves from game board
        Updates the game board with the player's move
        '''
        self.board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    
    
    def updateGameBoard(self, msg, o_x) -> None:
        '''
        Updates the game board with the player's move

        Parameters:
            msg (str): the string of the position that the player wants to make the move
            o_x (str): an indicator for this function to know if "o" or "x" should be put on the board
        '''
        msg = int(msg) - 1
        self.board[msg // 3][msg % 3] = o_x

    def isWinner(self) -> bool:
        '''
        Checks if the latest move results in a win
        Updates the wins and losses count
        
        Returns:
            A boolean expression to determine if there is a winner on the current board.
        '''
        is_Winner = False
        first_col = []
        second_col = []
        third_col = []
        left_diag = []
        right_diag = []
        for index, sublist in enumerate(self.board):
            if len(set(sublist)) == 1:
                is_Winner = True
            first_col.append(sublist[0])
            second_col.append(sublist[1])
            third_col.append(sublist[2])
            left_diag.append(self.board[index][index])
            right_diag.append(self.board[index][len(self.board) - index - 1])    
        if len(set(first_col)) == 1 or len(set(second_col)) == 1 or len(set(third_col)) == 1 or len(set(left_diag)) == 1 or len(set(right_diag)) == 1:
            is_Winner = True
        return is_Winner
    
    def boardIsFull(self) -> bool:
        '''
        Checks if the board is full (I.e. no more moves to make - tie)
        Updates the ties count
        
        Returns:
            A boolean expression to determine if the current board is full or not.
        '''
        is_full = True
        for sublist in self.board:
            for element in sublist:
                if element in "123456789":
                    is_full = False
        if is_full:
            self.num_ties += 1
        return is_full
    
    def printStats(self) -> None:
        '''
        Prints the following each on a new line:
            Prints the players user name
            Prints the user name of the last person to make a move
            prints the number of games
            Prints the number of wins
            Prints the number of losses
            Prints the number of ties
        '''
        print("PlayerName:", self.playername)
        print("LastTurn Player:", self.player_lastturn)
        print("Number of Game Started:", self.game_start)
        print("Number of Wins:", self.num_win)
        print("Number of Losses:",self.num_loss)
        print("Number of Ties:",self.num_ties)
    
    def printBoard(self) -> None:
        '''
        print the current board where it is visualized as a 3 - 3 matrix
        '''
        for sublist in self.board:
            print(f"{sublist}\n")

    def show_board_in_string(self) -> str:
        '''
        turn the nested list into a string
        '''
        nested_list_str = ""
        for sublist in self.board:
            nested_list_str += f"{str(sublist)}\n" 
        return nested_list_str
    
    def computeStats(self) -> str:
        '''
        return  
        the username of both players
        the number of games
        the number of wins
        the number of losses
        the number of ties
        '''
        return f"PlayerName: {self.playername} \nOpponent Player: {self.oppo_name} \nLast Turn Player: {self.player_lastturn}\nNumber of Game Started: {self.game_start} \nNumber of Wins: {self.num_win} \nNumber of Losses: {self.num_loss} \nNumber of Ties {self.num_ties}"

if __name__ == "__main__":
    pass
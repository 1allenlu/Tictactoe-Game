import tkinter as tk
from gameboard import BoardClass
from tkinter import simpledialog

class TicTacToeUIPacker():
    '''
    Create a user interface using  the Tkinter library
    The user interface includes the following components:
        A text entry for the host information
        A text entry for the username
        A Tic Tac Toe board that allows the user to select their move by clicking on that
        A dialog that asks the user if they want to play again (only on player 1)
        A display area where you display the BoardClass's computed statistics when they are done and any other printed information specified in the lab.
        An area indicating who's turn it is currently
        An area where the final results will be displayed
    '''

    '''define a constructor'''
    def __init__(self, title_name, side, my_turn):
        '''initilizing my gameboard class variable'''
        self.board = BoardClass()
        self.title_name = title_name
        self.side = side
        self.oppo_side = "o" if self.side == 'x' else "x"
        self.sk = None
        self.my_turn = my_turn
        self.start_from_me = my_turn
        self.YouLoseGame = None
        self.YouWinGame = None
        self.TieGame = None
        self.master = tk.Tk()
        self.master.withdraw()
        self.ask_for_info()
        self.initTKVariables

    def game_start(self):
        '''once the game starts, these buttons must continuously show on the UI'''
        self.canvasSetup()
        self.master.update()
        self.master.deiconify()
        self.get_client_username()
        self.createWhosTurn()
        self.Update_buttons()
        self.runUI()

    def Update_buttons(self):
        '''once a move is made, update all 9 buttons'''
        self.createTopLeftButton()
        self.createTopMidButton()
        self.createTopRightButton()
        self.createMidLeftButton()
        self.createMidMidButton()
        self.createMidRightButton()
        self.createBottomLeftButton()
        self.createBottomMidButton()
        self.createBottomRightButton()


    def ask_for_info(self):
        '''
        create a simpledialog that asks host IP & host Port
        '''
        self.host_IP = simpledialog.askstring(title = "Input", prompt= "Host IP")
        self.host_port = simpledialog.askstring(title = "Input", prompt= "Host Port")
    

    def ask_for_username(self):
        '''
        create a simpledialog that asks players' username
        '''
        self.username = simpledialog.askstring(title = "Input", prompt= "Username")

    
    def canvasSetup(self):
        '''define a method to set up my canvas'''
        '''initilize my tkinter canvas'''
        self.master.title(self.title_name) #sets the window title
        self.master.geometry("350x380") #sets the default size of the window
        self.master.configure(background="light yellow") #set the background color of the window
        self.master.resizable(0, 0) #setting the x(horizontal) and y(vertical) to not be resizable

    
    def initTKVariables(self):
        '''define a method that initializes my tk variables'''
        self.host = tk.StringVar()
        self.port = tk.StringVar()
        self.username = tk.StringVar()
        self.top_left = tk.StringVar()
        self.top_mid = tk.StringVar()
        self.top_right = tk.StringVar()
        self.mid_left = tk.StringVar()
        self.mid_mid = tk.StringVar()
        self.mid_right = tk.StringVar()
        self.bottom_left = tk.StringVar()
        self.bottom_mid = tk.StringVar()
        self.bottom_right = tk.StringVar()
        self.dialog = tk.StringVar()
        self.statistics = tk.StringVar() #display the BoardClass's computed statistics
        self.turn = tk.StringVar() #indicating who's turn it is currently
        self.result = tk.StringVar() #final results will be displayed
        self.if_enter_host_info = tk.StringVar()
        self.WhosTurn = tk.Label()


    def createTopLeftButton(self):
        '''create the top left button'''
        self.TopLeftButton = tk.Button(self.master, text=self.board.board[0][0], command=lambda: self.button_pressed("1")).grid(row=3, column=0, padx=10, pady=10)

    def createTopMidButton(self):
        '''create the top mid button'''
        self.TopMidButton = tk.Button(self.master, text=self.board.board[0][1], command=lambda: self.button_pressed("2")).grid(row=3, column=1, padx=10, pady=10)

    def createTopRightButton(self):
        '''create the top right button'''
        self.TopRightButton = tk.Button(self.master, text=self.board.board[0][2], command=lambda: self.button_pressed("3")).grid(row=3, column=2, padx=10, pady=10)

    def createMidLeftButton(self):
        '''create the mid left button'''
        self.MidLeftButton = tk.Button(self.master, text=self.board.board[1][0], command=lambda: self.button_pressed("4")).grid(row=4, column=0, padx=10, pady=10)

    def createMidMidButton(self):
        '''create the mid mid button'''
        self.MidMidButton = tk.Button(self.master, text=self.board.board[1][1], command=lambda: self.button_pressed("5")).grid(row=4, column=1, padx=10, pady=10)

    def createMidRightButton(self):
        '''create the mid right button'''
        self.MidRightButton = tk.Button(self.master, text=self.board.board[1][2], command=lambda: self.button_pressed("6")).grid(row=4, column=2, padx=10, pady=10)

    def createBottomLeftButton(self):
        '''create the bottom left button'''
        self.BottomLeftButton = tk.Button(self.master, text=self.board.board[2][0], command=lambda: self.button_pressed("7")).grid(row=5, column=0, padx=10, pady=10)

    def createBottomMidButton(self):
        '''create the bottom mid button'''
        self.BottomMidButton = tk.Button(self.master, text=self.board.board[2][1], command=lambda: self.button_pressed("8")).grid(row=5, column=1, padx=10, pady=10)

    def createBottomRightButton(self):
        '''create the bottom right button'''
        self.BottomRightButton = tk.Button(self.master, text=self.board.board[2][2], command=lambda: self.button_pressed("9")).grid(row=5, column=2, padx=10, pady=10)

    def get_client_username(self):
        '''
        if the side is 'x', then store the board.playername as clientname and board.oppo_name as servername
        if the side is 'o', then store the board.oppo_name as clientname and board.playername as clientname
        '''
        if self.side == "x":
            self.displayed_name = self.board.playername
            self.clientname= self.board.playername
            self.servername = self.board.oppo_name
        if self.side == "o":
            self.displayed_name = self.board.oppo_name
            self.clientname = self.board.oppo_name
            self.servername = self.board.playername

    def switch_displayed_name(self, name:str) -> None:
        '''
        if the parameter is clientname, then switch the displayed_name to the servername
        if the parameter is servername, then switch the displayed_name to the clientname
        '''
        if name == self.clientname:
            self.displayed_name = self.servername
        elif name == self.servername:
            self.displayed_name = self.clientname

    def ask_if_playagain(self):
        '''
        create a simpledialog that asks the client (player1) if they want to play again
        '''
        self.if_playagain = simpledialog.askstring(title = "Input", prompt= "Enters 'y' or 'Y' for play again or \nEnters 'n' or 'N' to end the game")
        
    def createStatistics(self):
        '''
        once the game is done, print statistics according to the computeStats method defined in boardclass
        '''
        displayed_string = self.board.computeStats()
        self.Statistics = tk.Label(self.master, text=displayed_string).grid(row=13, column=1, padx=10, pady=10)

    def createWhosTurn(self):
        '''create a label that displays who's turn it is currently'''
        self.WhosTurn = tk.Label(self.master, text=f"Player's Turn: {self.displayed_name}")
        self.WhosTurn.grid(row=7, column=1, padx=10, pady=10)
    
    def if_want_to_enter_host_info(self):
        '''if connection fails, creates a simpledialog that asks if they want to retry'''
        self.if_enter_host_info = simpledialog.askstring(title = "Input", prompt= "If you want to try again, enter ''y''; if not, enter ''n''.\n")
    
    def createYouLoseGame(self):
        '''create you lose game label'''
        self.YouLoseGame = tk.Label(self.master, text="You lose the game...")
        self.YouLoseGame.grid(row=12, column=1, padx=10, pady=10)

    def createYouWinGame(self):
        '''create you win game label'''
        self.YouWinGame = tk.Label(self.master, text="You win the game!")
        self.YouWinGame.grid(row=12, column=1, padx=10, pady=10)

    def createTieGame(self):
        '''create tie game label'''
        self.TieGame = tk.Label(self.master, text="Tie Game!")
        self.TieGame.grid(row=12, column=1, padx=10, pady=10)
    

    '''define a method start UI'''
    def runUI(self):
        '''starts my UI - event handler'''
        self.master.update()
        if not self.my_turn:
            self.wait_for_opponent()
        self.master.mainloop()


    def resetAllButtons(self):
        '''once players want to restart the game, reset all buttons and the board'''
        self.board.resetGameBoard()
        self.Update_buttons()


    def button_pressed(self, cmd: str):
        '''
        once button is pressed, it will run this function
        first check if a move can be made on the board
        second send the move to the other player
        third update the gameboard and buttons
        fourth switch the displayed name
        and finally check the game outcome (a function) to see if there is a winner or if the game ties
        '''
        if self.my_turn:
            pos = int(cmd) - 1
            if self.board.board[pos // 3][pos % 3] == cmd:
                self.sk.send_msg(cmd)
                self.board.player_lastturn = self.board.playername
                self.board.updateGameBoard(cmd, self.side)
                self.Update_buttons()
                self.WhosTurn.destroy()
                self.switch_displayed_name(self.displayed_name)
                self.createWhosTurn()
                self.master.update()
                result = self.checkGameOutcome("p", self.board.playername)
                if not result:
                    self.my_turn = False
                    self.wait_for_opponent()


    def wait_for_opponent(self):
        '''
        player waits for opponent to send their move
        update the gameborad and buttons
        switch the displayed name
        finally check the game outcome to see if there's a winner or if the game ties
        '''
        cmd = self.sk.recv_msg()
        self.board.player_lastturn = self.board.oppo_name
        self.board.updateGameBoard(cmd, self.oppo_side)
        self.Update_buttons()
        self.WhosTurn.destroy()
        self.switch_displayed_name(self.displayed_name)
        self.createWhosTurn()
        result = self.checkGameOutcome("r", self.board.playername)
        self.master.update()
        if not result:
            self.my_turn = True


    def ask_if_playagain_until_valid_input(self):
        '''
        a recursion function that keeps asking if player1 (client) wants to play again
        if the answer is not 'yY' or 'nN,' then keep asking for if they wanna play again
        '''
        self.ask_if_playagain()
        if self.if_playagain in "yY":
            '''reset all buttons'''
            self.sk.send_msg("Play Again")
            self.commons()
            self.board.updateGamesPlayed()
        elif self.if_playagain in "nN":
            '''exit and print stats'''
            self.sk.send_msg("Fun Times")
            self.createStatistics()
        else:
            self.ask_if_playagain_until_valid_input()


    def restart_game(self, username):
        '''
        once the game is over, run this restart function
        if client, ask if they wanna play again by calling ask_if_playagain_until_valid_input function
        if server, wait to receive the message
        the program executes different codes according to the received message
        if receive 'play again,' restart a new game
        if receive 'fun times,' create the statistics label
        '''
        if username == self.clientname:
            self.ask_if_playagain_until_valid_input()
        elif username == self.servername:
            cmd = self.sk.recv_msg()
            if cmd == "Play Again":
                self.commons()
                self.board.updateGamesPlayed()
            elif cmd == "Fun Times":
                self.resetAllButtons()
                self.createStatistics()


    def commons(self):
        '''
        as the cilent wants to restart the game, run this function
        destory displayed_name label and reset all buttons
        also destroy win/lose/tie labels
        '''
        self.WhosTurn.destroy()
        self.switch_displayed_name(self.servername)
        self.createWhosTurn()
        self.my_turn = self.start_from_me
        self.resetAllButtons()
        if self.YouLoseGame is not None:
            self.YouLoseGame.destroy()
        if self.YouWinGame is not None:
            self.YouWinGame.destroy()
        if self.TieGame is not None:
            self.TieGame.destroy()
        self.YouLoseGame = None
        self.YouWinGame = None
        self.TieGame = None
        self.master.update()
        if not self.my_turn:
            self.wait_for_opponent()


    def checkGameOutcome(self, indicator: str, username: str):
        '''
        whenever a move is updated onto the board, need to check if there is a winner or if the board is full
        '''
        self.if_winner = self.board.isWinner()
        if self.if_winner:
            if indicator == "p":
                '''if indicator == 'p', that means that player is the winner'''
                self.board.num_win += 1
                self.createYouWinGame()
                self.master.update()
                self.restart_game(username)
            elif indicator == "r":
                '''if indicator == 'r', that means that player is the loser'''
                self.board.num_loss += 1
                self.createYouLoseGame()
                self.master.update()
                self.restart_game(username)
            return True
        self.if_full = self.board.boardIsFull()
        if not self.if_winner and self.if_full:
            '''
            if the board is full and there's no winner, run this condition
            a button shows game tie
            run the restart_game function
            '''
            self.createTieGame()
            self.master.update()
            self.restart_game(username)
            return True
        return False


'''for testing'''
if __name__ == "__main__":
    TicTacToe = TicTacToeUIPacker("test")

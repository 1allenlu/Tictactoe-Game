from gameboard import BoardClass
import socket
from tictactoeUI import TicTacToeUIPacker
from socket_functions import socket_connection

def client_connect() -> None:
    '''
    create a client-side GUI
    ask host and port information from client (player1) to connect to the server
    once client connects to the server, player1 enters their username and send the name to player2
    once the name is sent, wait to receive player2's name
    create the board (an attribute) under the boardclass    
    finally start the game
    '''
    clientsideGUI = TicTacToeUIPacker("Tic Tac Toe - Client", "x", True)
    
    '''the boolean variable that keeps the while loop executing'''
    if_connect_to_server = True 

    '''while loop to keep trying to connect to the server '''
    while if_connect_to_server:
        try:
            host_IP = clientsideGUI.host_IP
            host_port = str(clientsideGUI.host_port)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connectionSocket:
                clientsideGUI.sk = socket_connection(connectionSocket)
                clientsideGUI.sk.connect(host_IP, int(host_port))
                if_connect_to_server = False
                clientsideGUI.ask_for_username()

                username = str(clientsideGUI.username)
                '''send the name to player2'''
                clientsideGUI.sk.send_msg(username)
                '''receives player2's name from player1'''
                player2_name = clientsideGUI.sk.recv_msg()
                clientsideGUI.board = BoardClass(username, player2_name)
                clientsideGUI.game_start()

        except:
            clientsideGUI.createFailureConnectionLabel()
            if if_connect_to_server:
                '''ask if client wants to re-enter the host and port information'''
                clientsideGUI.if_want_to_enter_host_info()
                ans = str(clientsideGUI.if_enter_host_info)
                '''if yes, ask them to enter that again'''
                if ans in "yY":
                    clientsideGUI.ask_for_info()
                '''if no, then end the program'''
                if ans in "nN":
                    exit()


def main() -> None:
    '''
    The main function calls client_connect function that tries to 
    open a server and allows clients to connect
    '''
    client_connect()

if __name__ == "__main__":
    main()

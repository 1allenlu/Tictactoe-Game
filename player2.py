from gameboard import BoardClass
import socket
from tictactoeUI import TicTacToeUIPacker
from socket_functions import socket_connection

def server_connect():
    '''
    create a server-side GUI
    ask host and port information from player2 in order to open a server
    once the server is opened, player2 waits to receive the name of player1
    once the player1's name is received, ask player2's name and send the name to player1
    create the board (an attribute) under the boardclass    
    finally start the game
    '''
    serversideGUI = TicTacToeUIPacker("Tic Tac Toe - Server", "o", False)
    host_IP = serversideGUI.host_IP
    host_port = str(serversideGUI.host_port)
    player1 = None
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
        serversideGUI.sk = socket_connection(serverSocket)
        connection, address = serversideGUI.sk.wait_client(host_IP, int(host_port))
        with connection:
            serversideGUI.sk = socket_connection(connection)
            '''receive player1's name'''
            player1 = serversideGUI.sk.recv_msg()
            '''set player2's name to player2 and send it to clients'''
            serversideGUI.ask_for_username()
            player2_name = serversideGUI.username
            serversideGUI.sk.send_msg(player2_name)
            '''create player2 BoardClass'''
            serversideGUI.board = BoardClass(player2_name, player1)
            serversideGUI.game_start()


def main() -> None:
    '''
    The main function calls server_connect function that tries to 
    open a server and allows clients to connect
    '''
    server_connect()


if __name__ == "__main__":
    main()
# 10.8.63.234

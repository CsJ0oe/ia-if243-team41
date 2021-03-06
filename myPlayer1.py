from playerInterface import *
from Goban import Board
import MCTS 


class myPlayer(PlayerInterface):

    def __init__(self):
        self._board = Board()
        self._agent = MCTS.MCTSAgent()
        self._mycolor = None

    def getPlayerName(self):
        return "Team 36"

    def getPlayerMove(self):
        if self._board.is_game_over():
            return "PASS" 
        move = self._agent.select_move(self._board)
        self._board.push(move)
        return Board.flat_to_name(move) 

    def playOpponentMove(self, move):
        self._board.push(Board.name_to_flat(move)) 

    def newGame(self, color):
        self._mycolor = color
        self._opponent = Board.flip(color)

    def endGame(self, winner):
        if self._mycolor == winner:
            print("I won :D")
        else:
            print("I lost :(")



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              from playerInterface import *
from Goban import Board
import MCTS 


class myPlayer(PlayerInterface):

    def __init__(self):
        self._board = Board()
        self._agent = MCTS.MCTSAgent()
        self._mycolor = None

    def getPlayerName(self):
        return "Team 36"

    def getPlayerMove(self):
        if self._board.is_game_over():
            return "PASS" 
        move = self._agent.select_move(self._board)
        self._board.push(move)
        return Board.flat_to_name(move) 

    def playOpponentMove(self, move):
        self._board.push(Board.name_to_flat(move)) 

    def newGame(self, color):
        self._mycolor = color
        self._opponent = Board.flip(color)

    def endGame(self, winner):
        if self._mycolor == winner:
            print("I won :D")
        else:
            print("I lost :(")




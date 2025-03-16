import logging
import time
from typing import Tuple

import util
from game import Actions, Agent, Directions
from logs.search_logger import log_function
from pacman import GameState


class q1a_problem:
    """
    A search problem defines the state space, start state, goal test, successor
    function and cost function.  This search problem can be used to find paths
    to a particular point on the pacman board.

    The state space consists of (x,y) positions in a pacman game.

    Note: this search problem is fully specified; you should NOT change it.
    """
    def __str__(self):
        return str(self.__class__.__module__)

    def __init__(self, gameState: GameState):
        """
        Stores the start and goal.

        gameState: A GameState object (pacman.py)
        costFn: A function from a search state (tuple) to a non-negative number
        goal: A position in the gameState
        """
        self.startingGameState: GameState = gameState

    @log_function
    def getStartState(self):
        "*** YOUR CODE HERE ***"
        return self.startingGameState.getPacmanPosition()



    @log_function
    def isGoalState(self, state):
        "*** YOUR CODE HERE ***"
        foodGrid = self.startingGameState.getFood()
        for x in range(len(foodGrid)):
            for y in range(len(foodGrid[0])):
                if foodGrid[x][y]:
                    return state == (x, y)
        return False


    @log_function
    def getSuccessors(self, state):
        """
        Returns successor states, the actions they require, and a cost of 1.

         As noted in search.py:
             For a given state, this should return a list of triples,
         (successor, action, stepCost), where 'successor' is a
         successor to the current state, 'action' is the action
         required to get there, and 'stepCost' is the incremental
         cost of expanding to that successor
        """
        # ------------------------------------------
        "*** YOUR CODE HERE ***"
       successors = []
        walls = self.startingGameState.getWalls()
        # 遍历四个方向
        for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            dx, dy = Actions.directionToVector(action)
            next_state = (int(state[0] + dx), int(state[1] + dy))
            # 如果下一个位置没有墙
            if not walls[next_state[0]][next_state[1]]:
                successors.append((next_state, action, 1))
        return successors


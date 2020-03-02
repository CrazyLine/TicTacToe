#class that implements the MiniMax algorithm.
import random
import sys

import Square
from TicTacToeAction import TicTacToeAction


class MiniMax:
    def __init__(self):
        self.numberOfStates=0
        self.usePruning=False

    def MinValue(self,state, alpha, beta):
        self.numberOfStates+=1
        if (state.isTerminal()):
            return state.getUtility()
        else :
            v = float("inf")
            for i in range(len(state.getActions1())):
                v=min(v, self.MaxValue(state.getResult(state.getActions1()[i]), alpha, beta))
                if (self.usePruning):
                    if (v <= alpha):
                        return v
                    beta = min(beta, v)
            return v

    def MinimaxDecision(self,state, usePruning):
        self.usePruning = usePruning
        self.numberOfStates = 0
        list1 = state.getActions()
        key = []
        value = []
        for i in range(len(list1)):
            v = self.MinValue(state.getResult(list1[i]), -sys.maxsize, sys.maxsize)
            key.append(list1[i].getPosition())
            value.append(v)
        for j in range(len(key)):
            flag = False
            for k in range (len(key) - j - 1):
                if (value[k] < value[k + 1]):
                    temp = value[k]
                    value[k] =value[k + 1]
                    value[k + 1]= temp
                    temp1 = key[k]
                    key[k]= key[k + 1]
                    key[k + 1] =temp1
                    flag = True
            if (flag==False):
                break
        list_max = []
        mark = 0
        for i in range(len(key)):
            if (value[0]==(value[i])):
                list_max.append(key[i])
            if (key[i] == 4):
                mark=i
        r = random.randint(0,len(list_max)-1)
        if (mark != 0):
            r=mark
        print("State space size: " , self.numberOfStates)
        return TicTacToeAction(Square.X, list_max[r])

    def MaxValue(self,state,alpha,beta):
        self.numberOfStates+=1
        if (state.isTerminal()):
            return state.getUtility()
        else:
            v = float("-inf")
            for i in range(len(state.getActions())):
                v=max(v, self.MinValue(state.getResult(state.getActions()[i]), alpha, beta))
                if (self.usePruning):
                    if (v >= beta):
                        return v
                    alpha = max(alpha, v)
            return v
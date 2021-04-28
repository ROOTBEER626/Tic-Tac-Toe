import sys
import random

#This class will be placeholder for the board values
class mySquare():
        EMPTY = ' '
        X = 'X'
        O = 'O'

#class to get the current player and positions       
class Action:
        def __init__(self, player, position):
                self.player = player
                self.position = position
        def getPosition(self):
                return self.position
        
        def getPlayer(self):
                return self.player
                
#represents the state of the game and handles the logic of the game           
class State:
        def __init__(self):
                self.board = []
                for i in range(9):
                        self.board.append(mySquare.EMPTY)#initilize the board to all empty
                self.player = mySquare.X#initial player is X
                self.playerToMove = mySquare.X#X is also first to move
                self.score = 0#initilize score to 0
                
        #gets the score of a board       
        def updateScore(self):
                #for i in range(9):
                        #print("Board at: ", i , "is: ", self.board[i])
                #Checks the rows
                if ((self.board[0] == (self.board[1]) and self.board[1] == self.board[2] and self.board[0] != (mySquare.EMPTY)) or (self.board[3]==(self.board[4]) and self.board[4] == self.board[5] and self.board[3] != mySquare.EMPTY) or (self.board[6] == self.board[7] and self.board[7] == self.board[8] and self.board[6] != (mySquare.EMPTY))):
                        if self.playerToMove==(mySquare.X):
                                self.score=-1
                        else:
                                self.score=1
                #checks the columns
                elif ((self.board[0]==self.board[3] and self.board[3]==self.board[6] and self.board[0]!= (mySquare.EMPTY)) or (self.board[1]==(self.board[4]) and self.board[4]== self.board[7] and self.board[1]!=mySquare.EMPTY) or (self.board[2]==(self.board[5]) and self.board[5]==(self.board[8]) and self.board[2]!=(mySquare.EMPTY))):
                        if (self.playerToMove==(mySquare.X)):
                                self.score = -1
                        else: 
                                self.score = 1
                #checks the diagnols
                elif ((self.board[0]==(self.board[4]) and self.board[4]==(self.board[8])and self.board[0]!=(mySquare.EMPTY)) or (self.board[2]==self.board[4] and self.board[4]==self.board[6] and self.board[2] !=(mySquare.EMPTY))):
                        if (self.playerToMove==(mySquare.X)):
                                self.score=-1
                        else:
                                self.score=1
                
                elif (self.checkNoMoves):
                        self.score = 0
        #just checks if the board is terminal with no winner but returns True or False instead of 0               
        def checkNoMoves(self):
                for i in range(9):
                        if (self.board[i]==(mySquare.EMPTY)):
                                num +=1 
                if(num==0):
                        return True
                return False
        
        #gets the possible Actions for the X player
        def getActions(self):
                list = []
                for i in range(9):
                        if (self.board[i]==(mySquare.EMPTY)):
                                list.append(Action(mySquare.X, i))
                return list
        #gets the possible Actions for the O player
        def getActions1(self):
                list = []
                for i in range(9):
                        if (self.board[i] == (mySquare.EMPTY)):
                                list.append(Action(mySquare.O, i))
                return list
                
        def getScore(self):
                return self.score
        #given the action if it is the right position and is empty make the move       
        def getResults(self, action):
                state = State()
                for i in range(9):
                        if (i == action.getPosition() and state.board[i] == (mySquare.EMPTY)):
                                state.board[i] = action.getPlayer()
                        else:
                                state.board[i] = self.board[i]
                if (action.getPlayer()==(mySquare.X)):
                        state.playerToMove = mySquare.O
                else:
                        state.playerToMove = mySquare.X
                state.updateScore()
                return state
                
        def isTerminal(self):
                if (self.score == 1 or self.score == -1):
                        return True
                num = 0
                for i in range(9):
                        if (self.board[i]==(mySquare.EMPTY)):
                                num +=1 
                if(num==0):
                        return True
                return False
                
        def print(self):
                s = "----\n"
                s += "" + self.board[0] + "|" + self.board[1] + "|" + self.board[2] + "\n"
                s += "-----\n"
                s += "" + self.board[3] + "|" + self.board[4] + "|" + self.board[5] + "\n"
                s += "-----\n"
                s += "" + self.board[6] + "|" + self.board[7] + "|" + self.board[8] + "\n"
                print(s)
              
class MiniMax: 
        def __init__(self):
                self.numberOfStates = 0
                self.usePruning = False
        
        def MinValue(self, state, alpha, beta):
                self.numberOfStates += 1
                if (state.isTerminal()):
                        return state.getScore()
                else:
                        v = float("inf")
                        for i in range(len(state.getActions1())):
                                v = min(v,self.MaxValue(state.getResults(state.getActions1()[i]),alpha, beta))
                                if (self.usePruning):
                                        if (v<=alpha): 
                                                return v
                                        beta = min(beta, v)
                        return v
        
        def MinMax(self, state, usePruning):
                self.usePruning = usePruning
                self.numberOfState = 0
                if (state.board[4] == mySquare.EMPTY):
                        return Action(mySquare.X, 4)
                list1 = state.getActions()
                key = []
                value = []
                for i in range(len(list1)):
                        v = self.MinValue(state.getResults(list1[i]), -sys.maxsize, sys.maxsize)
                        key.append(list1[i].getPosition())
                        value.append(v)
                for j in range(len(key)):
                        flag = False
                        for k in range (len(key) - j - 1):
                                if (value[k] < value[k + 1]):
                                        temp = value[k]
                                        value[k] = value[k + 1]
                                        value[k + 1] = temp
                                        temp1 = key[k]
                                        key[k] = key[k+1]
                                        key[k+1] = temp1
                                        flag = True
                        if (flag == False):
                                break
                list_max = []
                mark = 0
                for i in range(len(key)):
                        if (value[0]==(value[i])):
                                list_max.append(key[i])
                        if (key[i]==4): 
                                mark = i
                r = random.randint(0, len(list_max)-1)
                if (mark != 0):
                        r = mark
                print("State space size: ", self.numberOfStates)
                return Action(mySquare.X, list_max[r])
                        
        def MaxValue(self, state, alpha, beta):
                self.numberOfStates += 1
                if (state.isTerminal()):
                        return state.getScore()
                else: 
                        v = float("-inf")
                        for i in range(len(state.getActions())):
                                v = max(v, self.MinValue(state.getResults(state.getActions()[i]), alpha, beta))
                                if (self.usePruning):
                                        if (v >= beta):
                                                return v
                                        alpha = max(alpha, v)
                        return v
                        
if __name__ == '__main__':
        print("The Squares are numbered as follows:")
        print("1|2|3\n---\n4|5|6\n---\n7|8|9\n")
        mark = False
        print("Do you want to use pruning? 1=no, 2=yes ")
        prune = (int)(input())
        if prune == 2:
                mark = True
        print("Who should start? 1=you, 2=computer")
        temp = (int)(input())
        s = State()
        s.print()
        s.player = mySquare.X
        if (temp == 1):
                s.playerToMove = mySquare.O
        else:
                s.playerToMove = mySquare.X
        while (True):
                if (s.playerToMove == mySquare.X):
                        miniMax = MiniMax()
                        s = s.getResults(miniMax.MinMax(s, mark))
                else:
                        print("Which square do you want to set? (1-9) ")
                        while(True):
                                temp = (int)(input())
                                if temp >= 1 and temp <= 9 and s.board[temp-1] == mySquare.EMPTY:
                                        break
                                print("Please Enter a Valid Move")
                        a = Action(mySquare.O, temp -1)
                        s = s.getResults(a)
                s.print()
                if s.isTerminal():
                        break
        print("Score is: ", s.score)
        if (s.getScore()>0):
                print("You Lose")
        elif (s.getScore()< 0):
                print("You win")
        else: print("Draw")
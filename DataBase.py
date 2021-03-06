from collections import deque
import numpy as np


# this class hold the sample of <xn,un,xn+1>  n=k:k+N
class DataBase():


    # Constructor
    def __init__(self, N=10):
        self.size=N
        self.Q = deque(maxlen=N)
        return

    # append receives Xk, Uk, Xk+1 and inserts the sample into the data set. (<xn,un,xn+1>)
    def append(self, xu=None, xn1=None):
        self.Q.append(np.hstack((xu, xn1)))
        return

    # getLast returns the most recent data sample (no delete)
    def getLast(self):
        xn = np.copy(self.Q.pop())
        self.Q.append(np.copy(xn))
        tmpX = np.copy(xn[0, 8:])   # Xk+1
        tmpU = np.copy(xn[0, 6:8])  # Uk  we assume the next u will be close to the previous
        r = np.hstack((tmpX, tmpU))
        return r

    # getAll - returns all data base for training purposes.
    def getAll(self):
        input = np.zeros((self.size, 8))
        target = np.zeros((self.size, 6))
        for i in range(0, self.size):
            tmpOut = self.Q.pop()
            input[i, :] = np.copy(tmpOut[0, :8])
            target[i, :] = np.copy(tmpOut[0, 8:])
        for i in range(0, self.size):
            tmpIn = np.hstack((input[i, :], target[i, :]))
            tmpIn = np.matrix(tmpIn)
            self.Q.appendleft(np.copy(tmpIn))
        return [np.copy(input), np.copy(target)]

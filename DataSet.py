from collections import deque
import numpy as np


# this class hold the sample of <xn,un,xn+1>  n=k:k+N
class DataSet:

    # Constructor
    def __init__(self):
        self.size = 50 #TODO : Change back to 1000
        self.Q = deque(maxlen=self.size)
        return

    # append receives Xk, Uk, Xk+1 and inserts the sample into the data set. (<xn,un,xn+1>)
    def append(self, xk_uk=None, xk_1=None):
        xk_uk_c = np.copy(xk_uk)
        xk_1_c = np.copy(xk_1)
        sample = np.hstack((xk_uk_c, xk_1_c))
        self.Q.append(sample)
        return


    # getAll - returns all data base for training purposes, normalized and shuffled.
    def getAll(self):
        xuIn = np.zeros((self.size, 10))
        xOut = np.zeros((self.size, 8))
        for i in range(0, self.size):
            tmpOut = self.Q.pop()
            xuIn[i, :] = np.copy(tmpOut[:10])
            xOut[i, :] = np.copy(tmpOut[10:])
        for i in range(0, self.size):
            tmpIn = np.hstack((xuIn[i, :], xOut[i, :]))
            self.Q.appendleft(np.copy(tmpIn))
        return [np.copy(xuIn), np.copy(xOut)]
        # TODO: Normalize data and shuffle it

 #   def normalizeData(self):

  #  def shuffleData(self):
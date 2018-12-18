import numpy as np

class StandardScaler:
    def __init__(self):
        self.mean_ = None
        self.scale_ = None


    def fit(self,X):
        '''根据训练数据集获得数据的均值和方差'''
        assert X.ndim == 2,'The dimension of X must be 2'
        self.mean_ = np.array([ np.mean(X[:,i]) for i in range(X.shape[1]) ])
        self.scale_ = np.array([ np.std(X[:,i]) for i in range(X.shap[1]) ])

        return self

    def tranform(self,X):
        '''将X根据StrandardScaler进行均值方差归一化'''
        assert X.ndim == 2, 'The dimension of X must be 2'
        assert self.mean_ is not None and self.scale_ is not None,'must fit before tranform'
        assert X.shape[1] == len(self.mean_),''

        retX = np.empty(shape = X.shape,dtype = float)
        retX = np.array( [ (X[:,i] - self.mean_[i]) / self.scale_[i]  for i in range(X.shape[1]) ])


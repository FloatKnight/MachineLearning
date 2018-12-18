import numpy as np
from .metrics import r2_score

class LinearRegression:
    def __init__(self):
        '''初始化 Linear Regression 模型'''
        self.interception_ = None
        self.coef_ = None
        self._theta = None

    def fit_normal(self,X_train,y_train):
        '''根据X_train,y_train训练simpleLinearRegression训练模型'''
        assert X_train.shape[0] == y_train.shape[0],\
            ' the size of X_train must be equal the size of Y_train '

        X_b = np.hstack([np.ones((len(X_train),1)),X_train])
        self._theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y_train)
        self.interception_ = self._theta[0]
        self.coef_= self._theta[1:]
        return self


    def predict(self,X_predict):
        '''给定待预测数据集X_predict ,返回表示X_predict的结果向量'''

        assert self.coef_ is not None and self.interception_ is not None,\
            'must fit before predict'

        assert X_predict.shape[1] == len(self.coef_),\
            'the featrue number of X_predict must be equal to X_train'
        X_b = np.hstack([np.ones((len(X_predict),1)),X_predict])
        return X_b.dot(self._theta)


    def score(self,x_test,y_test):
        '''根据测试数据集 x_test,y_test确定当前模型的精准度'''

        y_predict = self.predict(x_test)
        return r2_score(y_test,y_predict)

    def _predict(self,x_single):
        '''给定单个待测定数据x_single,返回预测结果值'''
        return self.a_*x_single+self.b_

    def __repr__(self):
        return 'LinearRegression1()'
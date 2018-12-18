import numpy as np
from .metrics import r2_score

class SimpleLinearRegression:

    def __init__(self):
        self.a_ = None
        self.b_ = None

    def fit(self,x_train,y_train):
        '''根据x_train,y_train训练simpleLinearRegression训练模型'''
        assert x_train.ndim == 1,\
            'simpleLinearRegression can only solve single feature training data'
        assert len(x_train) == len(y_train),\
            'the size of x_train must be equal to the size of y_train'

        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)

        self.a_ = (x_train-x_mean).dot(y_train-y_mean)/(x_train-x_mean).dot(x_train-x_mean)
        self.b_ = y_mean - self.a_*x_mean

        return self

    def predict(self,x_predict):
        '''给定待预测数据集x_predict ,返回表示x_predict的结果向量'''
        assert x_predict.ndim == 1,\
            'simpleLinearRegression can only solve single feature training data'
        assert self.a_ is not None and self.b_ is not None,\
            'must fit before predict'

        return np.array([self.a_*i+self.b_ for i in x_predict])

    def score(self,x_test,y_test):
        '''根据测试数据集 x_test,y_test确定当前模型的精准度'''

        y_predict = self.predict(x_test)
        return r2_score(y_test,y_predict)

    def _predict(self,x_single):
        '''给定单个待测定数据x_single,返回预测结果值'''
        return self.a_*x_single+self.b_

    def __repr__(self):
        return 'SimpleLinearRegression()'
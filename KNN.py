from numpy import argsort, sqrt, sum,array
from collections import Counter
from .metrics import accuracy_score

class kNNClassifier:
    def __init__(self,k):
        '''初始化分类器'''
        assert k>0, 'k must be valid'

        self.k = k
        self._X_train = None
        self._y_train = None


    def fit(self,X_train,y_train):
        """根据训练数据集X_train和y_train训练kNN分类器"""
        assert X_train.shape[0] == y_train.shape[0],\
            'the size of X_train must be equal to the size of y_train'

        assert self.k<= X_train.shape[0],\
            'the size of X_train must be at least k.'
        self._X_train = X_train
        self._y_train = y_train
        return self
    def predict(self,X_predict):
        """给定待预测数据集X_predict，返回表示X_predict的结果向量"""
        assert self._X_train is not None and self._y_train is not None, \
            "must fit before predict!"
        assert X_predict.shape[1] == self._X_train.shape[1], \
            "the feature number of X_predict must be equal to X_train"

        distances =array([ [ sqrt(sum((x_train - i)**2)) for x_train in self._X_train ]  for i in X_predict ])
        return  array([Counter( self._y_train[argsort(i)[:self.k]] ).most_common()[0][0] for i in distances ])

    def score(self,X_test,y_test):
        """根据测试数据集 X_test 和 y_test 确定当前模型的准确度"""
        y_predict = self.predict(X_test)
        return accuracy_score(y_test,y_predict)

    def __repr__(self):
        return 'KNN(k=%r)' %self.k



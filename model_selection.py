import numpy as np

def train_test_split( X,y,test_ratio=0.2,seed=None ):
    """将数据 X 和 y 按照test_ratio分割成X_train, X_test, y_train, y_test"""
    assert X.shape[0] == y.shape[0],'the size of X must be equal the size of y'
    assert 0.0<=test_ratio<=1.0,'test_ration must be valid'


    if seed:np.random.seed(seed)
    shuffled_indexs = np.random.permutation(len(X))
    X_train = X[shuffled_indexs[int(len(X)*test_ratio):]]
    X_test = X[shuffled_indexs[:int(len(X)*test_ratio)]]
    y_train = y[shuffled_indexs[int(len(X)*test_ratio):]]
    y_test = y[shuffled_indexs[:int(len(X)*test_ratio)]]

    return X_train,X_test,y_train,y_test
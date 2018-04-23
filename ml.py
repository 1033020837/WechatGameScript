import os
import cv2
import numpy as np
from sklearn import neighbors
import pickle
from sklearn.linear_model import LogisticRegression

def load_train_data():
    """加载训练数据"""
    res = []
    c = []
    for root,dir,file in os.walk('TrainChar'):
        if len(file) != 0:
            _class = root.split(os.path.sep)[-1]
            if _class.isdigit():
                __class = int(_class)
            elif _class == '+':
                __class = 10
            elif _class == '-':
                __class = 11
            elif _class == '=':
                __class = 12
            for f in file:
                img = cv2.imread(os.path.join(root, f), 0)
                if img is None or img.shape != (60,30):
                    continue
                res.append(np.array(img).reshape(1,-1).tolist()[0])
                c.append(__class)
    res = np.array(res)
    res[res == 255] = 1
    return res,c

def dumpModel():
    train_data, train_target = load_train_data()
    # knn = neighbors.KNeighborsClassifier()
    # # 训练数据集
    # knn.fit(train_data, train_target)

    l = LogisticRegression()

    l.fit(train_data,train_target)

    #保存模型
    with open('lr.pickle', 'wb') as fw:
        pickle.dump(l, fw)
        print('保存模型完毕')

dumpModel()

#预测
# index = 0
# for t in train_data:
#     predict = knn.predict(t.reshape(1, -1))[0]
#     if predict != train_target[index]:
#         print('sss')
#     index += 1
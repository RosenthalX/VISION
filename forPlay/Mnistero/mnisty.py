from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt
import numpy as np
import cv2
from sklearn.linear_model import SGDClassifier

mnist = fetch_openml('mnist_784',version=1,return_X_y=False)

print(mnist.keys())

X,y = mnist["data"],mnist["target"]

print(X.shape)
print(y.shape)


some_digit = X[0]
some_digit_image = some_digit.reshape(28,28)

#print(y[0])
#plt.imshow(some_digit_image,cmap="binary")
#plt.axis("off")
#plt.show()


y = y.astype(np.uint8)

xtrain,xtest,ytrain,ytest = X[:60000],X[60000:],y[:60000],y[60000:]

ytrain_5 = (ytrain==5)
ytest_5 = (ytest==5)

sgd = SGDClassifier(random_state=42)
sgd.fit(xtrain,ytrain_5)

##Medir la presicion usando cross-validation
from sklearn.base import clone
from sklearn.model_selection import StratifiedKFold 
from sklearn.model_selection import cross_val_score

skfold = StratifiedKFold(n_splits=3,random_state=42)

for train_index, test_index in skfold.split(xtrain,ytrain_5):
    clone_sgd = clone(sgd)
    xtrain_folds = xtrain[train_index]
    ytrain_folds = ytrain_5[train_index]

    xtest_folds = xtrain[test_index]
    ytest_folds = ytrain_5[test_index]

    clone_sgd.fit(xtrain_folds,ytrain_folds)
    y_pred = clone_sgd.predict(xtest_folds)
    n_correct = sum(y_pred == ytest_folds)
    print(n_correct/len(y_pred))
print(cross_val_score(sgd,xtrain,ytrain_5,cv=3,scoring="accuracy"))


from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.model_selection import cross_val_predict

ytrain_pred = cross_val_predict(sgd,xtrain,ytrain_5,cv=3)
print(confusion_matrix(ytrain_5,ytrain_pred))
print(f1_score(ytest_folds,y_pred))





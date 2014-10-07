import numpy as np
from sklearn.cross_validation import cross_val_score
from sklearn.linear_model import LogisticRegression

labels = [ l.strip() for l in open('labels.txt', 'r') ]
f_dan  = np.float_([ tuple(l.strip().split(',')[:-1]) for l in open('features_dan.csv', 'r') ][1:])
f_joe  = np.float_([ tuple(l.strip().split(',')[:-1]) for l in open('features_joe.csv', 'r') ][1:])

X = np.concatenate((f_dan, f_joe), axis=1)
classes, y = np.unique(labels, return_inverse=True)

clf = LogisticRegression()
acc = np.mean( cross_val_score(clf, X, y, cv=10) )

print 'Acc: %.3f' % acc

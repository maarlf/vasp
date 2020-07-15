import sys

import pandas as pd

from sklearn.preprocessing import Normalizer
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, confusion_matrix


if __name__ == '__main__':
    import warnings
    warnings.filterwarnings('ignore')

    # Input arguments
    train_data = sys.argv[1]
    test_data = sys.argv[2]

    # Load datasets
    print('==== Load datasets ====')

    normalizer = Normalizer()

    df_train = pd.read_csv(train_data)
    df_test = pd.read_csv(test_data)

    X_train = df_train.drop(['a', 'b', 'x', 'class'], axis=1)
    X_train_norm = normalizer.fit_transform(X_train)
    y_train = df_train['class'].values

    X_test = df_test.drop(['a', 'b', 'x', 'class'], axis=1)
    X_test_norm = normalizer.fit_transform(X_test)
    y_test = df_test['class'].values

    selected = ['m1', 'm2', 'm3', 'mtot', 'n_el', 'tot_en', 'z3', 'z5', 'z6', 'z7']
    X_train2 = df_train[selected]
    X_train2_norm = normalizer.fit_transform(X_train2)

    X_test2 = df_test[selected]
    X_test2_norm = normalizer.fit_transform(X_test2)

    print('Done: datatrain.csv, datatest.csv')

    # ML
    print('==== Training SVM ====')
    
    kernel = ['linear', 'rbf', 'poly', 'sigmoid']
    C = [0.1, 1, 10, 100, 1000]
    gamma = [0.1, 0.01, 0.001, 0.0001, 0.00001]
    degree = [1, 2, 3, 4, 5]
    n_folds = 5

    param_grid = {
        'kernel': kernel,
        'C': C,
        'gamma': gamma,
        'degree': degree
    }
    
    grid = GridSearchCV(estimator=SVC(), 
        param_grid=param_grid, 
        cv=KFold(n_splits=n_folds), 
        refit=True)
    grid.fit(X_train2_norm, y_train)

    print('Best score: {}'.format(grid.score(X_test2_norm, y_test)))
    print('Best params: {}'.format(grid.best_params_))

    # Result
    print('==== Result ====')

    y_pred = grid.predict(X_test2_norm)
    accuracy = accuracy_score(y_pred, y_test)

    print('SVM Accuracy with best params: {}'.format(accuracy))
    print('Actual test label:    {}'.format(y_test))
    print('Predicted test label: {}'.format(y_pred))

    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1_score = f1_score(y_test, y_pred)

    print('Precision: {}'.format(precision))
    print('Recall: {}'.format(recall))
    print('F Score: {}'.format(f1_score))

    # Outputing result
    print('==== Writing result to CSV ====')

    df_test['structure'] = df_test['a'] + df_test['b'] + df_test['x']
    structures = df_test['structure'].to_list()
    result = {
        'structure': structures,
        'class': y_pred
    }

    df_result = pd.DataFrame(result)
    df_result = df_result[['structure', 'class']] 
    df_result.to_csv('output.csv', index=False)

    print('Done writing result to output.csv')
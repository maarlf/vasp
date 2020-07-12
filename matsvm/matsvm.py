import sys
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


if __name__ == '__main__':
    import warnings
    warnings.filterwarnings('ignore')

    # Input arguments
    train_data = sys.argv[1]
    test_data = sys.argv[2]

    # Load datasets
    print()
    print('==== Load datasets ====')

    df_train = pd.read_csv(train_data)
    df_test = pd.read_csv(test_data)

    X_train = df_train.drop(['structure', 'class'], axis=1)
    y_train = df_train['class'].values

    X_test = df_test.drop(['structure', 'class'], axis=1)
    y_test = df_test['class'].values

    structures = df_test['structure'].to_list()

    print()
    print('Done: datatrain.csv, datatest.csv')

    # ML
    print()
    print('==== Training machine learning ====')
    print()

    kernel = ['linear', 'rbf', 'poly']

    param_grid = {
        'kernel': kernel,
        'C': [0.1, 0.5, 1, 10, 30, 40, 50, 70, 100, 500, 1000],
        'gamma': [0.0001, 0.001, 0.005, 0.01, 0.05, 0.07, 0.1, 0.5, 1, 5, 10, 50]
    }
    
    grid = GridSearchCV(estimator=SVC(), param_grid=param_grid, cv=5, refit=True)
    grid.fit(X_train, y_train)

    print('Best score: {}'.format(grid.score(X_test, y_test)))
    print('Best params: {}'.format(grid.best_params_))

    # Result
    print()
    print('==== Result ====')
    print()

    y_pred = grid.predict(X_test)
    print('SVM Accuracy with best params: {}%'.format(accuracy_score(y_pred, y_test) * 100))
    print('Actual test label:    {}'.format(y_test))
    print('Predicted test label: {}'.format(y_pred))

    # Outputing result
    print()
    print('==== Writing result to CSV ====')
    print()

    result = {
        'structures': structures,
        'class': y_pred
    }

    df_result = pd.DataFrame(result)
    df_result.to_csv('output.csv', index=False)

    print('Done writing result to output.csv')
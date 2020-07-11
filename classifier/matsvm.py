import pandas as pd
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from tqdm import tqdm

if __name__ == '__main__':
    import warnings
    warnings.filterwarnings('ignore')

    # Load datasets
    print()
    print('==== Load datasets ====')

    df_train = pd.read_csv('../datasets/datatrain.csv')
    df_test = pd.read_csv('../datasets/datatest.csv')

    X_train = df_train.drop(['structure', 'class'], axis=1)
    y_train = df_train['class'].values

    X_test = df_test.drop(['structure', 'class'], axis=1)
    y_test = df_test['class'].values

    print()
    print('Done: datatrain.csv, datatest.csv')

    # ML
    print()
    print('==== Training machine learning ====')
    print()

    kernel = ['linear', 'rbf', 'poly']
    pipe = [('classifier', SVC())]
    param_grid = {
        'classifier__kernel': kernel,
        'classifier__C': [0.1, 0.5, 1, 10, 30, 40, 50, 70, 100, 500, 1000],
        'classifier__gamma': [0.0001, 0.001, 0.005, 0.01, 0.05, 0.07, 0.1, 0.5, 1, 5, 10, 50]
    }
    pipeline = Pipeline(pipe)

    print('Tuning SVM hyperparameters')
    print()

    for n in tqdm(range(4, 9)):
        grid = GridSearchCV(pipeline, param_grid=param_grid, cv=KFold(n_splits=n))
        grid.fit(X_train, y_train)

    clf = SVC(kernel=grid.best_params_['classifier__kernel'],
               gamma=grid.best_params_['classifier__gamma'],
               C=grid.best_params_['classifier__C'])
    clf.fit(X_train, y_train)

    print()
    print('Done: {}'.format(clf))

    # Result
    print()
    print('==== Result ====')
    print()

    y_pred = clf.predict(X_test)
    print('SVM Accuracy with best params: {}%'.format(accuracy_score(y_pred, y_test) * 100))
    print('Actual test label:    {}'.format(y_test))
    print('Predicted test label: {}'.format(y_pred))
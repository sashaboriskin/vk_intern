import pandas as pd
from sklearn.metrics import ndcg_score
from catboost import Pool, CatBoostClassifier

train_df = pd.read_csv('data/train_df.csv')
test_df = pd.read_csv('data/test_df.csv')

X_train = train_df.drop(['search_id', 'target'], axis=1)
y_train = train_df['target']
X_test = test_df.drop(['search_id', 'target'], axis=1)
y_test = test_df['target']

model = CatBoostClassifier(
    iterations=210,
    learning_rate=0.1,
    depth=6,
    loss_function='Logloss',
    verbose=False
)
model.fit(X_train, y_train)
predictions = model.predict_proba(X_test)[:, 1]

print('ndcg with classifier: ', ndcg_score([list(y_test)], [list(predictions)]))
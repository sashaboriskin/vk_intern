import pandas as pd
from sklearn.metrics import ndcg_score
from catboost import CatBoostRanker, Pool

train_df = pd.read_csv('data/train_df.csv')
test_df = pd.read_csv('data/test_df.csv')

X_train = train_df.drop(['search_id', 'target'], axis=1)
y_train = train_df['target']
group_train = train_df.groupby('search_id').size().to_numpy()

X_test = test_df.drop(['search_id', 'target'], axis=1)
y_test = test_df['target']
group_test = test_df.groupby('search_id').size().to_numpy()

train_pool = Pool(data=X_train, label=y_train, group_id=train_df['search_id'])
test_pool = Pool(data=X_test, label=y_test, group_id=test_df['search_id'])

ranker = CatBoostRanker(
    iterations=100,
    learning_rate=0.01,
    depth=6,
    loss_function='YetiRank',
    verbose=False
)

ranker.fit(train_pool, eval_set=test_pool)

predictions = ranker.predict(test_pool)
print('ndcg with ranker: ', ndcg_score([list(y_test)], [list(predictions)]))
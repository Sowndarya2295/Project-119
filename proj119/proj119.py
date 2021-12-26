import pandas as pd


col_names =  ["PassengerId","Pclass","Sex","Age","SibSp","Parch","Survived"]
df = pd.read_csv("titanic.csv", names=col_names).iloc[1:]
print(df.head())

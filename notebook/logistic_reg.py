from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

import pandas as pd

class Logistic_regression:
    def __init__(self,Processed_Data_Path):
        self.Processed_Data_Path = Processed_Data_Path

    def Logistic_Reg(self):
        data = pd.read_csv(self.Processed_Data_Path)

        features = ["Returns","Volatility_ratio","Acceleration","Volume_spike","Position"]
        target = "Target"

        X = data[features]
        y = data[target]

        split = int(len(data) * 0.8)

        X_train = X.iloc[:split]
        X_test  = X.iloc[split:]

        y_train = y.iloc[:split]
        y_test  = y.iloc[split:]

        model = LogisticRegression(class_weight="balanced")

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        proba = model.predict_proba(X_test)[:, 1]

        y_pred = (proba > 0.5).astype(int)

        accuracy = accuracy_score(y_test, y_pred)
        cm = confusion_matrix(y_test, y_pred)
        Classification_report = classification_report(y_test, y_pred)
        

        return  accuracy,cm,Classification_report
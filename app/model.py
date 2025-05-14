import pandas as pd
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("data/disease_dataset.csv")
X = df.drop("disease", axis=1)
y = df["disease"]

model = DecisionTreeClassifier()
model.fit(X, y)

def predict_disease(symptoms: dict):
    input_data = [[symptoms.get("fever", 0), symptoms.get("cough", 0), symptoms.get("headache", 0)]]
    return model.predict(input_data)[0]

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import joblib

# Load cleaned dataset
df = pd.read_csv("data/clean_toxic_dataset.csv")

# Combine symptom columns into one text feature
df["features"] = (
    df["cns"].astype(str) + " " +
    df["cvs"].astype(str) + " " +
    df["respiratory"].astype(str) + " " +
    df["gi"].astype(str) + " " +
    df["other"].astype(str) + " " +
    df["odour"].astype(str)
)

# Input and output
X = df["features"]
y = df["toxin"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ML Pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", RandomForestClassifier(n_estimators=200))
])

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f" Model Accuracy: {accuracy * 100:.2f}%")

# Save model
joblib.dump(model, "model/toxic_detection_model.pkl")

print("✅ Model saved successfully!")
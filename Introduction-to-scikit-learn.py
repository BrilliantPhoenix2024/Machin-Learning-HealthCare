
# ==========================================
# 1- Get the Data Ready
# ==========================================

import pandas as pd
import numpy as np
from pathlib import Path

file_path = Path(__file__).resolve().parent / "heart-disease.csv"
heart_disease = pd.read_csv(file_path)

# Create X (features matrix)
x = heart_disease.drop("target", axis=1)

# Create y (labels)
y = heart_disease["target"]


# ==========================================
# 2- Choose the Right Model and Hyperparameters
# ==========================================

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Check the model hyperparameters
print(clf.get_params())


# ==========================================
# 3- Fit the Model to the Training Data
# ==========================================

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train the model
clf.fit(x_train, y_train)

# Make a prediction for a single sample
y_label = clf.predict(x_test.iloc[[0]])

# Make predictions for all test samples
y_preds = clf.predict(x_test)

print("Single prediction:", y_label)
print("All predictions:", y_preds)


# ==========================================
# 4- Evaluate the Model
# ==========================================

from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score
)

# Evaluate on training and test data
print("Training accuracy:", clf.score(x_train, y_train))
print("Testing accuracy:", clf.score(x_test, y_test))

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_preds))

# Confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_preds))

# Accuracy score
print("\nAccuracy Score:")
print(accuracy_score(y_test, y_preds))


# ==========================================
# 5- Improve the Model
# ==========================================

# Try different numbers of n_estimators
# Keep the original clf unchanged

for i in range(10, 100, 10):
    print(f"Trying model with {i} estimators")

    test_model = RandomForestClassifier(
        n_estimators=i,
        random_state=42
    )

    # Train the experimental model
    test_model.fit(x_train, y_train)

    # Evaluate the experimental model
    print(
        f"Model accuracy on test set: "
        f"{test_model.score(x_test, y_test) * 100:.2f}%"
    )
    print("")


# ==========================================
# 6- Save a Model and Load It
# ==========================================

import pickle

# Save the original model (100 estimators)
model_path = Path(__file__).resolve().parent / "Random_forest_model_1.pkl"

with open(model_path, "wb") as file:
    pickle.dump(clf, file)

# Load the saved model
with open(model_path, "rb") as file:
    loaded_model = pickle.load(file)

# Evaluate the loaded model
print("\nOriginal model accuracy:")
print(clf.score(x_test, y_test))

print("\nLoaded model accuracy:")
print(loaded_model.score(x_test, y_test))

# Check the number of trees
print("\nNumber of trees:")
print(loaded_model.n_estimators)

# Compare predictions
original_preds = clf.predict(x_test)
loaded_preds = loaded_model.predict(x_test)

print("\nAre predictions identical?")
print(np.array_equal(original_preds, loaded_preds))

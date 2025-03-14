
# ==========================================
# 1- Get the Data Ready
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

heart_disease = pd.read_csv("heart-disease.csv")

# 1- Getting data ready to be used with machine learning
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
# Splitting the data into training and test sets
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
pickle.dump(clf, open('Random_forest_model_1.pkl', 'wb'))

# Load the saved model
loaded_model = pickle.load(open('Random_forest_model_1.pkl', 'rb'))
print(loaded_model.score(x_test, y_test))

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


# Make sure it's all numerical
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# 1. Load dataset
car_sales = pd.read_csv('car-sales-extended.csv')
print(car_sales.dtypes)

# 2. Split into X and y
x = car_sales.drop('Price', axis=1)
y = car_sales['Price']

# 3. Convert categorical features to numerical
categorical_features = ["Make", "Colour", 'Doors']

one_hot = OneHotEncoder(handle_unknown="ignore")

transformer = ColumnTransformer(
    transformers=[
        ("one_hot", one_hot, categorical_features)
    ],
    remainder="passthrough"
)

transformed_X = transformer.fit_transform(x)

# 4. Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    transformed_X,
    y,
    test_size=0.2,
    random_state=42
)

# 5. Build machine learning model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# 6. Train model
model.fit(X_train, y_train)

# 7. Evaluate model
print("Model R2 Score:", model.score(X_test, y_test))

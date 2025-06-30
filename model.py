from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# Load inbuilt diabetes dataset
data = load_diabetes()
X = data.data
y = data.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
predicted = model.predict(X_test[:1])
print("Sample prediction for first test input:", predicted)

# Save the trained model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
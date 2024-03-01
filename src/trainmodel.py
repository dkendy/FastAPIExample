from pydantic import BaseModel
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from typing import List

 

# Train and evaluate model function
def train_and_evaluate_model(ftest_size: float = 0.2, random_state: int = 42, n_neighbors: int = 3) -> float:
    
    iris_data = load_iris()
    X = iris_data.data  # Features
    y = iris_data.target  # Target labels

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 
    # Initialize and train a k-Nearest Neighbors classifier
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = knn.predict(X_test)

    # Calculate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy

 
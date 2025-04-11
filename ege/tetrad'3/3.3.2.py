import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import make_classification  


X, y = make_classification(n_samples=1000, n_features=20, random_state=42)


n_neighbors_values = [1, 5, 10]
test_size_percentage = 0.15  


results = {}

for n_neighbors in n_neighbors_values:
    results[n_neighbors] = {}


    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size_percentage, random_state=42
    )

    # Create KNN classifier
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)

    # Train the classifier
    knn.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = knn.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    results[n_neighbors]['accuracy'] = accuracy
    results[n_neighbors]['report'] = report
    results[n_neighbors]['y_pred'] = y_pred
    results[n_neighbors]['y_test'] = y_test

    print(f"Results for k = {n_neighbors}:")
    print(f"  Accuracy: {accuracy:.4f}")
    print(f"  Classification Report:\n{report}")
    print("-" * 40)


accuracies = [results[k]['accuracy'] for k in n_neighbors_values]

plt.figure(figsize=(8, 6))
plt.plot(n_neighbors_values, accuracies, marker='o')
plt.xlabel("Number of Neighbors (k)")
plt.ylabel("Accuracy")
plt.title("KNN Accuracy vs. Number of Neighbors")
plt.xticks(n_neighbors_values)
plt.grid(True)
plt.show()


print("\nAnalysis of Results:")
print("-----------------------")
print("The accuracy of the KNN classifier varies depending on the number of neighbors (k).")
print("Generally, a small value of k can lead to overfitting, while a large value of k can lead to underfitting.")
print("The optimal value of k depends on the specific dataset.")
print("In this experiment:")

for n_neighbors in n_neighbors_values:
  print(f"\nFor k = {n_neighbors}:")
  print(f"  Accuracy: {results[n_neighbors]['accuracy']:.4f}")

print("\nFurther Analysis:")
print("Consider the classification reports for each k value to understand precision, recall, and F1-score for each class.")
print("This will help in identifying if the model is performing well for all classes or if there are specific classes where it is struggling.")
print("Experiment with different test_size values to see how the model generalizes with different amounts of data for testing.")

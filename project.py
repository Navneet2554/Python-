import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeClassifier

# Assuming the dataset file is named "loan_dataset.csv"
dataset = pd.read_csv("loan_dataset.csv")

# Display the first few rows of the dataset
print(dataset.head())

# Get summary statistics of the dataset
print(dataset.describe())

# Check data types and missing values
print(dataset.info())

# Handle missing values
dataset.fillna(method='ffill', inplace=True)

# Countplot for loan status
sns.countplot(x='Loan_status', data=dataset)

# Pairplot for numeric attributes
sns.pairplot(dataset[['Dependents', 'CoapplicantIncome', 'LoanAmount', 'ApplicantIncome', 'Credit_history']], hue='Loan_status')

plt.show()

X = dataset.drop(columns=['Loan_status', 'Loan_id'])
y = dataset['Loan_status']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Decision Tree model
model = DecisionTreeClassifier(random_state=42)

# Fit the model on the training dataset
model.fit(X_train, y_train)

# Predict loan status on test data
y_pred = model.predict(X_test)

# Calculate accuracy on test data
test_accuracy = accuracy_score(y_test, y_pred)
print("Test Accuracy:", test_accuracy)

# Create confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
import warnings
# from sklearn.model_selection import cross_val_score

warnings.filterwarnings('ignore')

# Load the dataset
df = pd.read_csv('Crop_recommendation.csv')

# Explore the dataset
print(df.head())
print(df.tail())
print(df.info())
print(df.shape)
print(df.isnull().sum())
print(df.describe())
print(df['label'].unique())
print(df.columns)
print(df['label'].value_counts())
print(df.dtypes)


# Define features and target variable
features = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
target = df['label']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    features, target, test_size=0.2, random_state=2)

# Train a Random Forest model
RF = RandomForestClassifier(
    n_estimators=29, criterion='entropy', random_state=0)
RF.fit(X_train, y_train)
predicted = RF.predict(X_test)

x = metrics.accuracy_score(y_test, predicted)

print("Random Forest Accuracy is ", x * 100)
print(classification_report(y_test, predicted))

# Perform prediction
data = np.array([[13, 53, 73, 10, 12, 8.50, 112.9]])
prediction = RF.predict(data)
print(prediction)

# Save the trained model to disk using pickle
with open('model.pkl', 'wb') as model_file:
    pickle.dump(RF, model_file)

# Display conclusion
print("We are using Random Forest because of its accuracy and precision.")

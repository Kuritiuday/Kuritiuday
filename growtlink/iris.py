# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("IRIS.csv")

# Convert species column to categorical values
df["species"] = df["species"].astype("category").cat.codes

# Exploratory Data Analysis (EDA) - Pairplot
sns.pairplot(df, hue="species", diag_kind="hist", palette="Set1")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.drop(columns=["species"]).corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.show()

# Split dataset into features and target
X = df.drop(columns=["species"])
y = df["species"]

# Train-test split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Train a Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Model predictions
y_pred = clf.predict(X_test)

# Model evaluation
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Feature importance analysis
feature_importance = clf.feature_importances_
feature_df = pd.DataFrame({"Feature": X.columns, "Importance": feature_importance}).sort_values(by="Importance", ascending=False)

# Plot feature importance
plt.figure(figsize=(8, 5))
sns.barplot(x="Importance", y="Feature", data=feature_df, palette="viridis")
plt.title("Feature Importance in Iris Classification")
plt.xlabel("Importance Score")
plt.ylabel("Feature")
plt.show()

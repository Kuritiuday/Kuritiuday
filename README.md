- 👋 Hi, I’m @Kuritiuday
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...

<!---
Kuritiuday/Kuritiuday is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
1️⃣ Data Preprocessing
Steps Performed:
Loading Data: Read the IRIS.csv dataset.
Handling Missing Values: No missing values found.
Encoding Target Variable:
Converted categorical species names (Iris-setosa, Iris-versicolor, Iris-virginica) to numerical labels (0, 1, 2).
Feature Scaling:
No scaling was applied since Random Forest does not require normalization.
Train-Test Split:
80% Training, 20% Testing using train_test_split() with stratify=y.

2️⃣ Model Selection
Models Considered:
Model	Accuracy	Pros	Cons
Logistic Regression	~85%	Simple, interpretable	May struggle with complex boundaries
K-Nearest Neighbors	~88%	Non-parametric, easy to understand	Slower for large datasets
Decision Tree	~89%	Captures non-linearity	Prone to overfitting
Random Forest	90%	Handles non-linearity, robust	Slower than simple models
SVM	~88%	Works well with small datasets	Computationally expensive
Why Random Forest?
Best balance of accuracy and generalization
Handles non-linearity and feature importance well
Less prone to overfitting than Decision Trees

3️⃣ Model Evaluation
Performance Metrics
Accuracy: 90%

Precision, Recall, F1-Score:

txt
Copy
Edit
              precision    recall  f1-score   support
    0       1.00      1.00      1.00        10
    1       0.82      0.90      0.86        10
    2       0.89      0.80      0.84        10

  accuracy                           0.90        30
 macro avg       0.90      0.90      0.90        30
weighted avg 0.90 0.90 0.90 30

4️⃣ Feature Importance Results
The most important features:
Petal Length: Most significant
Petal Width: Second most important
Sepal Length & Sepal Width: Less significant

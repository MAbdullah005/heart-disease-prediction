# ❤️ Heart Disease Prediction

This project uses machine learning to predict whether a person has heart disease based on clinical data. It covers the full ML pipeline: preprocessing, exploratory data analysis (EDA), feature engineering, model training, and evaluation.

---

## 📦 Dataset

- **Source:** [UCI Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/heart+Disease)
- **Samples:** ~300 (may vary by version)
- **Target:** Presence (1) or Absence (0) of heart disease
- **Features Include:**
  - Age, Sex, Chest Pain Type (`cp`)
  - Resting Blood Pressure (`trestbps`)
  - Cholesterol (`chol`)
  - Fasting Blood Sugar (`fbs`)
  - Rest ECG (`restecg`)
  - Max Heart Rate (`thalach`)
  - Exercise Induced Angina (`exang`)
  - ST Depression (`oldpeak`)
  - Slope, Number of Vessels (`ca`), Thalassemia (`thal`)

---

## 🔍 Data Preprocessing

### 🧹 Missing Values Handling
- Used **KNN Imputation** (`fancyimpute.KNN`) to fill missing values based on similar instances.
- Missing value ratio per feature is inspected before imputation.

### 🧪 Feature Engineering
- **Label Encoding** for binary categorical features like `sex`, `fbs`, `exang`.
- **One-Hot Encoding** for multi-class features like:
  - Chest Pain Type (`cp`)
  - Slope of ST Segment (`slope`)
  - Thalassemia (`thal`)

> Used `sklearn.preprocessing.LabelEncoder` and `pd.get_dummies()` for encoding.

---

## 📊 Exploratory Data Analysis (EDA)
- Visualized class distribution of the target.
- Correlation heatmap to identify strongly related features.
- Distribution plots for numerical features.
- Box plots to observe outliers and relationships.

---

## 🤖 Models Used

| Model                | Description                  |
|---------------------|------------------------------|
| Logistic Regression | Baseline linear classifier   |
| Random Forest       | Ensemble of decision trees   |
| XGBoost             | Boosted gradient trees       |
| SVM (RBF Kernel)    | Support Vector Machine       |
| KNN                 | K-Nearest Neighbors          |

---

## 📈 Model Evaluation

### ✅ Metrics:
- Accuracy
- Confusion Matrix
- Classification Report (Precision, Recall, F1-Score)
- ROC-AUC Score
- Cross-Validation (where applicable)

### 📉 Accuracy Comparison

| Model                | Accuracy |
|---------------------|----------|
| Logistic Regression | 88.52%   |
| Random Forest       | 90.16%   |
| XGBoost             | 89.34%   |
| SVM                 | 88.52%   |
| KNN                 | 85.25%   |

> Plotted accuracy comparison with `matplotlib`.

---

## 🧪 How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the script
python main.py

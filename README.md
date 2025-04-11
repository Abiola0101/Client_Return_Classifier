# Client_Return_Classifier
This project is a machine learning-based classification system designed to **predict whether a client is likely to return** or not based on behavioral, demographic, and transaction features. The aim is to help organizations **improve customer retention strategies** by proactively identifying high-risk clients.

---

## Project Overview

**Client_Return_Classifier** is a binary classification project that applies machine learning to classify customers into two groups:
- **Class 1 (Return)**: Clients likely to return
- **Class 0 (Not Return)**: Clients unlikely to return

The project includes:
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Model training using **Random Forest Classifier**
- Model evaluation and iteration
- Explainability using **SHAP** and **LIME**
- Deployment via a **Flask API**

---

## Dataset Description

The dataset contains client-level data with features such as:
- **Last Visit Date**
- **Purchase Frequency**
- **Client Tenure**
- **Region**
- **Customer Type**
- **Product Usage Metrics**
- **Return Status** (target variable)

The dataset was cleaned to handle:
- Missing values
- Categorical encodings
- Date transformations
- Imbalanced class distribution


## Exploratory Data Analysis

EDA insights included:
- Class imbalance (fewer returns)
- Correlation between purchase frequency and return likelihood
- Client segments with higher retention
- Impact of tenure and seasonality on return rates

Visual tools used:
- Matplotlib / Seaborn
- Count plots, box plots, histograms
- Correlation heatmaps

---

## Model Details

### Algorithm:
- **Random Forest Classifier**

### Preprocessing:
- Label Encoding for categorical features
- Scaling (optional)
- Train-test split

### Evaluation Metrics:
```
Accuracy: 0.91
Precision: 0.89
Recall: 0.94
F1-Score: 0.91
```

---

## Model Explainability

### SHAP (SHapley Additive exPlanations):
- Visualized **global feature importance**
- Local explanations for individual predictions using `force_plot` and `summary_plot`

### LIME (Local Interpretable Model-agnostic Explanations):
- Explained single predictions to help business users understand **why a client is predicted to not return**

These explainability tools help build **trust** in the model’s decisions, especially in stakeholder-facing environments.

---

## Deployment

The model is deployed via a **Flask REST API**:

### Endpoint:
`POST /predict`

### Input:
JSON payload containing client feature values

### Output:
```
{
  "prediction": [1]
}
```

### Example:
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '[{"tenure": 24, "region": "North", "last_visit": "2023-12-15", ...}]'
```

---

## Technologies Used

- Python 3.x
- Pandas, NumPy, Scikit-learn
- SHAP, LIME
- Flask
- Matplotlib / Seaborn

---

## Potential Use Cases

- Customer churn prediction in retail or subscription businesses
- Targeted marketing campaigns
- Social support service follow-up scheduling
- Personalized engagement strategy development

---

## Future Enhancements

- Implement **Streamlit dashboard** for business users
- Use **XGBoost or LightGBM** for performance comparison
- Automate model retraining with new data
- Incorporate time-series behavior features

---

## Project Structure

```
Client_Return_Classifier/
├── data/                      # Raw and processed data files
├── model/                     # Saved model files (.pkl)
├── notebooks/                 # Jupyter Notebooks for EDA, training, SHAP, LIME
├── app.py                     # Flask app for prediction API
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
```

---

## Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Client_Return_Classifier.git
cd Client_Return_Classifier
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Flask app:
```bash
python app.py
```

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request to suggest improvements or new features.


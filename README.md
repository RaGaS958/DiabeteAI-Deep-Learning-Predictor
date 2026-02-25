<div align="center">

<!-- ANIMATED HEADER BANNER -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=DiabeteAI%20%F0%9F%A9%BA&fontSize=60&fontColor=ffffff&animation=twinkling&fontAlignY=35&desc=Deep%20Learning%20Diabetes%20Predictor&descAlignY=55&descSize=20" width="100%"/>

<!-- LIVE BADGES ROW 1 -->
<p align="center">
  <a href="https://diabeteai-deep-learning-predictor-bzciyukl49rf3t7lmmhuud.streamlit.app/">
    <img src="https://img.shields.io/badge/🚀%20Live%20Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit App"/>
  </a>
  <a href="https://hub.docker.com/r/ragas111/diabetes-ai">
    <img src="https://img.shields.io/badge/🐳%20Docker%20Hub-ragas111%2Fdiabetes--ai-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker Hub"/>
  </a>
  <a href="https://github.com/RaGaS958/DiabeteAI-Deep-Learning-Predictor">
    <img src="https://img.shields.io/badge/⭐%20Star%20This%20Repo-GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
  </a>
</p>

<!-- TECH BADGES -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/TensorFlow-2.20.0-FF6F00?style=flat-square&logo=tensorflow&logoColor=white"/>
  <img src="https://img.shields.io/badge/Keras-3.13.2-D00000?style=flat-square&logo=keras&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-1.54.0-FF4B4B?style=flat-square&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/scikit--learn-1.8.0-F7931E?style=flat-square&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat-square&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-00d4aa?style=flat-square"/>
</p>

<!-- PERFORMANCE BADGES -->
<p align="center">
  <img src="https://img.shields.io/badge/Accuracy-96.2%25-00d4aa?style=flat-square&logo=checkmarx&logoColor=white"/>
  <img src="https://img.shields.io/badge/Precision-95.8%25-0096ff?style=flat-square"/>
  <img src="https://img.shields.io/badge/Recall-97.1%25-a855f7?style=flat-square"/>
  <img src="https://img.shields.io/badge/F1%20Score-96.4%25-ffa502?style=flat-square"/>
  <img src="https://img.shields.io/badge/AUC--ROC-0.983-ff4757?style=flat-square"/>
</p>

<br/>

**[🌐 Live App](https://diabeteai-deep-learning-predictor-bzciyukl49rf3t7lmmhuud.streamlit.app/) · [🐳 Docker Hub](https://hub.docker.com/r/ragas111/diabetes-ai) · [📓 Notebook](Diabetes_DeepLearning.ipynb) · [📊 Dataset](#-dataset-overview) · [🚀 Quick Start](#-quick-start)**

</div>

---

## 🩺 What is DiabeteAI?

**DiabeteAI** is a production-grade, multi-page **Streamlit** web application powered by a **TensorFlow/Keras Artificial Neural Network** trained on **100,000 clinical patient records**. It provides:

- ⚡ **Instant diabetes risk prediction** using 26 validated clinical biomarkers
- 📊 **Interactive analytics dashboard** with stage distribution, feature importance & model performance
- 🔬 **Clinical insights** — glycemic thresholds, risk factor analysis & prevention strategies
- 🐳 **Fully Dockerized** and deployed on **Streamlit Cloud**

> ⚕️ *For clinical decision support only. Always consult a qualified healthcare professional.*

---

## 📸 App Preview

<div align="center">

| 🏠 Home Dashboard | 🔬 Prediction Engine |
|:-----------------:|:--------------------:|
| Dataset stats, model accuracy, feature highlights | 26-feature clinical input form with live risk output |

| 📊 Analytics Tab | 🤖 Model Architecture |
|:----------------:|:---------------------:|
| Age/BMI distributions, feature importance bars | Layer diagram, training config, confusion matrix |

</div>

---

## 🚀 Quick Start

### Option 1 — Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/RaGaS958/DiabeteAI-Deep-Learning-Predictor.git
cd DiabeteAI-Deep-Learning-Predictor

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the app
streamlit run main.py
```
> App will open at **http://localhost:8501**

---

### Option 2 — Docker (Recommended)

#### Pull from Docker Hub & Run

```bash
# Pull the latest image
docker pull ragas111/diabetes-ai:latest

# Run the container
docker run -p 8501:8501 ragas111/diabetes-ai:latest
```
> App will be available at **http://localhost:8501**

#### Build from Source

```bash
# Build the image
docker build -t diabetes-ai .

# Run the container
docker run -p 8501:8501 diabetes-ai
```

#### Docker Compose

```yaml
# docker-compose.yml
version: '3.8'
services:
  diabetes-ai:
    image: ragas111/diabetes-ai:latest
    ports:
      - "8501:8501"
    restart: unless-stopped
```
```bash
docker-compose up -d
```

---

### Option 3 — Streamlit Cloud ☁️

Click below — no installation needed:

<div align="center">

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://diabeteai-deep-learning-predictor-bzciyukl49rf3t7lmmhuud.streamlit.app/)

</div>

---

## 🐳 Docker Details

<div align="center">

| Property | Value |
|----------|-------|
| **Image** | `ragas111/diabetes-ai:latest` |
| **OS / Architecture** | `linux/amd64` |
| **Compressed Size** | `1008.32 MB` |
| **Base Image** | `python:3.11-slim` |
| **Exposed Port** | `8501` |
| **Index Digest** | `sha256:832fa26ca1980df1aff7acc5d2d42ed0f0739bc747634dbe66b5a3cbe770e978` |
| **Manifest Digest** | `sha256:c6b94359880703bc3a9535179ea4828541857aa3ed5f8d858b8e97ac91a092b5` |

</div>

🔗 **[View on Docker Hub →](https://hub.docker.com/layers/ragas111/diabetes-ai/latest/images/sha256:c6b94359880703bc3a9535179ea4828541857aa3ed5f8d858b8e97ac91a092b5?uuid=786C439D-9961-4215-AED0-1F3E00BF86E2)**

---

## 📂 Repository Structure

```
DiabeteAI-Deep-Learning-Predictor/
│
├── 🐍 main.py                        ← Streamlit multi-page app (entry point)
├── 🧠 ann_model.h5                   ← Trained ANN weights (Keras HDF5 format)
├── ⚙️  scaler.pkl                    ← Fitted StandardScaler (joblib serialized)
│
├── 📊 diabetes_dataset.csv           ← Raw dataset — 100,000 records, 31 features
├── 📊 DIABETES_DATASET_CLEAN.csv     ← Preprocessed & encoded — 88,263 records, 39 cols
│
├── 📓 Diabetes_DeepLearning.ipynb    ← Training notebook (EDA → training → evaluation)
│
├── 🐳 Dockerfile                     ← Container build (python:3.11-slim base)
├── 🚫 .dockerignore                  ← Files excluded from Docker build context
│
└── 📦 requirements.txt               ← Pinned Python dependencies
```

---

## 📊 Dataset Overview

<div align="center">

```
┌─────────────────────────────────────────────────────────────────┐
│                    DATASET AT A GLANCE                          │
├──────────────────────┬──────────────────────────────────────────┤
│  Total Records       │  100,000 patients                        │
│  Clean Records       │  88,263 (after preprocessing)            │
│  Raw Features        │  31 columns                              │
│  Model Features      │  26 (post encoding & selection)          │
│  Positive Cases      │  59,998  ████████████░░░  60.0%          │
│  Negative Cases      │  40,002  ████████░░░░░░░  40.0%          │
│  Age Range           │  18 – 90 years  (mean: 50.1 yrs)         │
│  Mean BMI            │  25.6  kg/m²                             │
│  Mean HbA1c          │  6.52%                                   │
│  Mean Fasting Gluc.  │  111.1  mg/dL                            │
└──────────────────────┴──────────────────────────────────────────┘
```

</div>

### Diabetes Stage Distribution

```
Type 2 Diabetes   ████████████████████████████████████  59,774  (59.8%)
Pre-Diabetes      ████████████████████                  31,845  (31.8%)
No Diabetes       █████                                  7,981  ( 8.0%)
Gestational       ▏                                        278  ( 0.3%)
Type 1            ▏                                        122  ( 0.1%)
```

### Clinical Feature Summary

| Feature | Range | Mean | Clinical Significance |
|---------|-------|------|-----------------------|
| **HbA1c** | 4.0 – 9.8 % | 6.52% | Primary DM biomarker |
| **Fasting Glucose** | 60 – 172 mg/dL | 111.1 | Overnight blood sugar |
| **Post-Prandial Glucose** | 70 – 300 mg/dL | — | 2hr after-meal glucose |
| **Insulin Level** | 0 – 100 μIU/mL | — | Pancreatic function |
| **BMI** | 15.0 – 39.2 | 25.6 | Obesity indicator |
| **Waist-Hip Ratio** | 0.6 – 1.2 | — | Abdominal adiposity |
| **Systolic BP** | 80 – 200 mmHg | — | Cardiovascular risk |
| **Total Cholesterol** | 100 – 400 mg/dL | — | Lipid panel |
| **Diabetes Risk Score** | 0 – 100 | — | Composite risk index |
| **Age** | 18 – 90 yrs | 50.1 | Age-related resistance |

---

## 🤖 Model Architecture

### Artificial Neural Network (ANN)

```
Input Layer          ──── 26 features (StandardScaler normalized)
        │
Dense (128)          ──── ReLU · BatchNorm · Dropout(0.3)
        │
Dense (64)           ──── ReLU · BatchNorm · Dropout(0.2)
        │
Dense (32)           ──── ReLU · Dropout(0.1)
        │
Dense (16)           ──── ReLU
        │
Output (1)           ──── Sigmoid  →  Binary classification (Diabetic / Non-Diabetic)
```

### Training Configuration

| Parameter | Value |
|-----------|-------|
| **Framework** | TensorFlow 2.20 / Keras 3.13 |
| **Optimizer** | Adam (lr = 0.001) |
| **Loss Function** | Binary Cross-Entropy |
| **Batch Size** | 32 |
| **Epochs** | 100 (Early Stopping) |
| **Validation Split** | 20% |
| **Preprocessing** | StandardScaler (Z-score normalization) |
| **Regularization** | L2 + Dropout + BatchNormalization |
| **Model Format** | HDF5 (`.h5`) |

---

## 📈 Model Performance

<div align="center">

```
╔══════════════╦══════════╦════════════════════════════════════════╗
║   METRIC     ║  VALUE   ║  VISUAL                                ║
╠══════════════╬══════════╬════════════════════════════════════════╣
║  Accuracy    ║  96.2 %  ║  ████████████████████████████████░░   ║
║  Precision   ║  95.8 %  ║  ████████████████████████████████░░   ║
║  Recall      ║  97.1 %  ║  █████████████████████████████████░   ║
║  F1 Score    ║  96.4 %  ║  ████████████████████████████████░░   ║
║  AUC-ROC     ║  0.983   ║  █████████████████████████████████░   ║
╚══════════════╩══════════╩════════════════════════════════════════╝
```

</div>

### Top Feature Importance

```
HbA1c (%)                ████████████████████████████████████████  94 %
Diabetes Risk Score      ███████████████████████████████████████   91 %
Fasting Glucose          ██████████████████████████████████████    89 %
Post-Prandial Glucose    █████████████████████████████████████     86 %
BMI                      ███████████████████████████████          78 %
Insulin Level            ██████████████████████████████           74 %
Waist-to-Hip Ratio       ████████████████████████████             69 %
Age                      █████████████████████████                63 %
Systolic BP              ██████████████████████                   55 %
Family History           █████████████████████                    51 %
```

---

## 🖥️ App Pages

### 🏠 Home
- Hero banner with project overview
- 5 key dataset stats (100K patients, 60% diagnosis rate, model accuracy, avg age, avg BMI)
- Diabetes stage distribution bar chart
- Clinical metrics reference table
- ANN performance metrics (Accuracy, Precision, Recall, F1, AUC)
- 9 prediction feature highlights with descriptions

### 🔬 Prediction

Five color-coded clinical input sections:

| Section | Features |
|---------|----------|
| 👤 **Demographics & Lifestyle** | Age, Gender, Alcohol, Smoking, Sleep, Screen Time, Activity, Diet, Employment |
| 📏 **Anthropometric** | BMI (with live BMI category badge), Waist-to-Hip Ratio |
| ❤️ **Cardiovascular Panel** | Systolic BP, Diastolic BP, Heart Rate, Total / HDL / LDL Cholesterol, Triglycerides |
| 🩸 **Glycemic & Metabolic** | Fasting Glucose, Post-Prandial Glucose, Insulin Level, HbA1c (live classifier), Risk Score |
| 📋 **Medical History** | Family History, Hypertension History, Cardiovascular History |

**Output:** Probability score + Risk category (Low / Moderate / Elevated / High) + input summary + 3-factor risk gauges

### 📊 About & Analytics

Four tabs:
- **Analytics** — Age/BMI distribution charts, feature importance bars, dataset stats
- **Model Architecture** — Layer diagram, training config, performance metrics
- **Clinical Insights** — Glycemic thresholds, risk factors, prevention strategies
- **About** — Project files, dataset summary, technology stack, disclaimer

---

## 🧪 26 Model Features (Exact Scaler Order)

```python
FEATURE_ORDER = [
    "age",                          # 1.  Patient age (years)
    "alcohol_consumption_per_week", # 2.  Weekly alcohol intake
    "sleep_hours_per_day",          # 3.  Daily sleep duration
    "screen_time_hours_per_day",    # 4.  Daily screen exposure
    "family_history_diabetes",      # 5.  Genetic risk flag (0/1)
    "hypertension_history",         # 6.  Hypertension flag (0/1)
    "cardiovascular_history",       # 7.  CVD history flag (0/1)
    "bmi",                          # 8.  Body Mass Index
    "waist_to_hip_ratio",           # 9.  Abdominal adiposity
    "systolic_bp",                  # 10. Systolic blood pressure (mmHg)
    "diastolic_bp",                 # 11. Diastolic blood pressure (mmHg)
    "heart_rate",                   # 12. Resting heart rate (bpm)
    "cholesterol_total",            # 13. Total cholesterol (mg/dL)
    "ldl_cholesterol",              # 14. LDL cholesterol (mg/dL)
    "triglycerides",                # 15. Serum triglycerides (mg/dL)
    "glucose_fasting",              # 16. Overnight fasting glucose (mg/dL)
    "glucose_postprandial",         # 17. 2hr post-meal glucose (mg/dL)
    "insulin_level",                # 18. Serum insulin (μIU/mL)
    "hba1c",                        # 19. Glycated haemoglobin (%)
    "diabetes_risk_score",          # 20. Composite clinical risk score
    "gender_Male",                  # 21. Gender encoding (binary)
    "ethnicity_Other",              # 22. Ethnicity OHE
    "ethnicity_White",              # 23. Ethnicity OHE
    "employment_status_Employed",   # 24. Employment OHE
    "employment_status_Unemployed", # 25. Employment OHE
    "smoking_status_Former",        # 26. Smoking OHE
]
```

---

## 🧬 Clinical Reference

### Glycemic Diagnostic Thresholds (ADA Guidelines)

| Test | Normal | Pre-Diabetes | Diabetes |
|------|--------|-------------|---------|
| **HbA1c** | < 5.7% | 5.7 – 6.4% | ≥ 6.5% |
| **Fasting Glucose** | < 100 mg/dL | 100 – 125 mg/dL | ≥ 126 mg/dL |
| **2hr Post-Prandial** | < 140 mg/dL | 140 – 199 mg/dL | ≥ 200 mg/dL |

### BMI Classification (WHO)

| BMI Range | Category | Diabetes Risk |
|-----------|----------|--------------|
| < 18.5 | Underweight | 🔵 Low |
| 18.5 – 24.9 | Normal Weight | 🟢 Minimal |
| 25.0 – 29.9 | Overweight | 🟠 Moderate |
| 30.0 – 34.9 | Obese Class I | 🔴 High |
| ≥ 35.0 | Obese Class II/III | 🔴 Very High |

---

## 📦 Tech Stack

<div align="center">

| Layer | Technology | Version |
|-------|-----------|---------|
| **Deep Learning** | TensorFlow / Keras | 2.20.0 / 3.13.2 |
| **Frontend** | Streamlit | 1.54.0 |
| **ML Utilities** | scikit-learn | 1.8.0 |
| **Data** | Pandas, NumPy | 2.3.3 / 2.4.2 |
| **Visualization** | Plotly | 6.5.2 |
| **Serialization** | joblib, h5py | 1.5.3 / 3.15.1 |
| **Containerization** | Docker | linux/amd64 |
| **Deployment** | Streamlit Cloud | — |
| **Language** | Python | 3.11 |

</div>

---

## ⚠️ Medical Disclaimer

> This application is intended **for educational and clinical decision support purposes only**. It is **not a substitute** for professional medical advice, diagnosis, or treatment. Risk predictions are based on statistical patterns and **must be interpreted alongside clinical judgment by a qualified healthcare provider**. Never disregard professional medical advice or delay seeking it because of results from this tool.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>

**Built with ❤️ by [RaGaS958](https://github.com/RaGaS958)**

[![GitHub](https://img.shields.io/badge/GitHub-RaGaS958-181717?style=flat-square&logo=github)](https://github.com/RaGaS958)
[![Docker Hub](https://img.shields.io/badge/Docker-ragas111-2496ED?style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/r/ragas111/diabetes-ai)
[![Streamlit App](https://img.shields.io/badge/🚀%20Live-DiabeteAI-FF4B4B?style=flat-square)](https://diabeteai-deep-learning-predictor-bzciyukl49rf3t7lmmhuud.streamlit.app/)

*⭐ Star this repo if you found it useful!*

</div>

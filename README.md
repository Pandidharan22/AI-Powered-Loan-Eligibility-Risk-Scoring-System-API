# AI-Powered Loan Eligibility & Risk Scoring System

## 🚀 Overview
An end-to-end machine learning system to predict loan default risk and serve predictions via a FastAPI backend.

## 🎯 Objectives
- Predict probability of loan default (risk score)
- Provide interpretable insights into model decisions
- Serve predictions through a production-ready API

## 🧱 Tech Stack
- Python 3.10+
- FastAPI (Backend)
- Scikit-learn (ML)
- Pandas, NumPy (Data Processing)

## 🏗️ Project Structure

## 🏗️ Project Structure
```
loan-risk-scoring/
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_model_training.ipynb
│
├── src/
│   ├── api/
│   │   ├── main.py
│   │   ├── dependencies.py
│   │   ├── routes/
│   │   │   ├── prediction.py
│   │   │   ├── model.py
│   │   │   └── health.py
│   │   └── schemas/
│   │       ├── request.py
│   │       └── response.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── logger.py
│   │   └── constants.py
│   │
│   ├── pipeline/
│   │   ├── preprocessing.py
│   │   ├── feature_engineering.py
│   │   └── training.py
│   │
│   ├── services/
│   │   ├── prediction_service.py
│   │   └── model_service.py
│   │
│   └── utils/
│       └── helpers.py
│
├── models/
├── tests/
├── visualizations/
│
├── .env
├── .env.example
├── requirements.txt
├── pyproject.toml
├── README.md
└── Dockerfile  # (to be added later)
```
## 🧠 Development Journey

### Phase 0: Setup & System Design
- Designed a modular project architecture separating API, services, and ML pipeline
- Set up isolated Python environment to ensure reproducibility
- Implemented configuration management using Pydantic Settings
- Introduced structured logging for observability

#### Challenges Faced
- Initial environment included unnecessary deep learning dependencies, which were removed to maintain a clean and lightweight setup
- Understood how environment variables override default config values in Pydantic

#### Key Learnings
- Importance of environment isolation in ML systems
- Difference between writing code vs designing a system
- Early logging and config management significantly improve scalability

### Phase 1: Exploratory Data Analysis (EDA)

- Performed comprehensive data inspection including schema validation, data types, and summary statistics
- Identified the problem as a **binary classification task with significant class imbalance (~11.6% defaults)**
- Conducted univariate analysis to understand feature distributions and detect anomalies
- Performed bivariate and multivariate analysis using KDE plots, correlation heatmaps, and pairplots
- Analyzed feature relationships with the target to identify potential predictive signals
- Evaluated categorical variables using **default rate distributions instead of raw counts** for better insight
- Discovered that most features exhibit **weak linear relationships but non-linear separability**
- Identified that the dataset is likely **synthetic**, with uniform distributions and minimal feature correlation

#### Challenges Faced
- Initial assumption that correlation would reveal strong signals proved incorrect due to near-zero linear relationships
- Difficulty interpreting patterns in a dataset with **uniform distributions and low natural variance**
- Misleading nature of standard plots (e.g., countplots) required shifting to **probability-based analysis**
- Understanding why features showed separation in KDE but weak correlation required deeper statistical reasoning

#### Key Learnings
- **Correlation ≠ Predictive Power** — non-linear relationships can exist even when correlation is weak
- Feature distributions and interactions provide more insight than summary statistics alone
- In low-signal datasets, **feature engineering becomes more important than model selection**
- Importance of analyzing **relative relationships (ratios, interactions)** rather than absolute values
- Real-world ML problems often require extracting signal rather than relying on obvious patterns

### Phase 2: Feature Engineering & Preprocessing

- Designed a structured feature engineering strategy based on EDA insights, focusing on extracting signal from weakly correlated features
- Implemented ratio-based, interaction, and stability features to capture real-world financial risk relationships
- Developed a modular `DataPreprocessor` class to encapsulate feature engineering and preprocessing logic
- Built a `ColumnTransformer` pipeline to handle numerical scaling and categorical encoding in a unified workflow
- Ensured proper ML workflow by applying preprocessing only on training data to prevent data leakage
- Serialized the preprocessing pipeline using `joblib` for reuse in model training and API inference

#### Challenges Faced
- Encountered misleading feature behavior due to synthetic-like data with weak linear relationships
- Faced data leakage risk while integrating preprocessing with train-test workflow
- Debugged `ModuleNotFoundError` due to notebook execution context and resolved using proper path handling
- Encountered `IntCastingNaNError` during binary encoding, highlighting the need for robust and defensive data transformations
- Faced stale import issues while modifying pipeline code, requiring module reload during iterative development

#### Key Learnings
- Feature engineering is the primary driver of performance in low-signal datasets
- Importance of designing **idempotent and robust preprocessing pipelines** that work across different data states
- Real-world ML systems require strict separation between training and inference workflows
- Serialization of preprocessing is as important as model persistence for deployment
- Debugging environment and import issues is a critical part of ML engineering, not just modeling

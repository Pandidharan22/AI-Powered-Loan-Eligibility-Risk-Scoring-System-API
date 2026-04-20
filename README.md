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

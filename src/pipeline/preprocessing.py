import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

class DataPreprocessor:
    def __init__(self):
        self.preprocessor = None
    
    def _engineer_features(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
    
        df['Loan_to_Income'] = df['LoanAmount'] / df['Income']
        df['Income_per_CreditLine'] = df['Income'] / df['NumCreditLines']
        df['Loan_per_CreditLine'] = df['LoanAmount'] / df['NumCreditLines']
    
        df['Risk_Interaction'] = df['CreditScore'] * df['InterestRate']
        df['Debt_Stress'] = df['DTIRatio'] * df['LoanAmount']
    
        df['Employment_Stability'] = df['MonthsEmployed'] / df['Age']
    
        df['CreditScore_bin'] = pd.cut(df['CreditScore'], bins=5)
        df['DTI_bin'] = pd.cut(df['DTIRatio'], bins=[0, 0.3, 0.6, 1])
    
        binary_map = {'Yes': 1, 'No': 0}
    
        df['HasMortgage'] = df['HasMortgage'].map(binary_map).astype(int)
        df['HasDependents'] = df['HasDependents'].map(binary_map).astype(int)
        df['HasCoSigner'] = df['HasCoSigner'].map(binary_map).astype(int)
    
        return df

    def _get_feature_groups(self):
        num_cols = [
            'Age', 'Income', 'LoanAmount', 'CreditScore',
            'MonthsEmployed', 'NumCreditLines',
            'InterestRate', 'LoanTerm', 'DTIRatio',
            'Loan_to_Income', 'Income_per_CreditLine',
            'Loan_per_CreditLine', 'Risk_Interaction',
            'Debt_Stress', 'Employment_Stability'
        ]

        cat_cols = [
            'Education', 'EmploymentType', 'MaritalStatus',
            'LoanPurpose', 'CreditScore_bin', 'DTI_bin'
        ]
    
        binary_cols = [
            'HasMortgage', 'HasDependents', 'HasCoSigner'
        ]
    
        return num_cols, cat_cols, binary_cols
    
    def _build_preprocessor(self):
        num_cols, cat_cols, binary_cols = self._get_feature_groups()
    
        num_pipeline = Pipeline([
            ('scaler', StandardScaler())
        ])
    
        cat_pipeline = Pipeline([
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ])
    
        preprocessor = ColumnTransformer([
            ('num', num_pipeline, num_cols),
            ('cat', cat_pipeline, cat_cols),
            ('bin', 'passthrough', binary_cols)
        ])
    
        return preprocessor
    
    def fit(self, df: pd.DataFrame):
        df = self._engineer_features(df)
    
        X = df.drop(columns=['LoanID', 'Default'])
    
        self.preprocessor = self._build_preprocessor()
        self.preprocessor.fit(X)
    
        return self
    
    def transform(self, df: pd.DataFrame):
        df = self._engineer_features(df)
    
        X = df.drop(columns=['LoanID', 'Default'])
    
        return self.preprocessor.transform(X)
    
    def fit_transform(self, df: pd.DataFrame):
        return self.fit(df).transform(df)
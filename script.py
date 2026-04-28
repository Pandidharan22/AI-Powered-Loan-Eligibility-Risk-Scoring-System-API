from src.services.prediction_service import prediction_service

sample = {
    "Age": 35,
    "Income": 50000,
    "LoanAmount": 150000,
    "CreditScore": 650,
    "MonthsEmployed": 24,
    "NumCreditLines": 2,
    "InterestRate": 12.5,
    "LoanTerm": 36,
    "DTIRatio": 0.4,
    "Education": "Bachelor's",
    "EmploymentType": "Full-time",
    "MaritalStatus": "Single",
    "HasMortgage": "No",
    "HasDependents": "Yes",
    "LoanPurpose": "Home",
    "HasCoSigner": "Yes"
}

print(prediction_service.predict(sample))
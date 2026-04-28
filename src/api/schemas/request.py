from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):
    Age: int = Field(..., ge=18, le=100)
    Income: int = Field(..., gt=0)
    LoanAmount: int = Field(..., gt=0)
    CreditScore: int = Field(..., ge=300, le=900)
    MonthsEmployed: int = Field(..., ge=0)
    NumCreditLines: int = Field(..., ge=1)
    InterestRate: float = Field(..., gt=0)
    LoanTerm: int = Field(..., ge=1)
    DTIRatio: float = Field(..., ge=0, le=1)

    Education: str
    EmploymentType: str
    MaritalStatus: str
    HasMortgage: str
    HasDependents: str
    LoanPurpose: str
    HasCoSigner: str
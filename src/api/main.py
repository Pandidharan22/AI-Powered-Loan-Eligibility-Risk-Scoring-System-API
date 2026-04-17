from fastapi import FastAPI

app = FastAPI(title="Loan Eligibility Risk Scoring App",
              version="1.0.0")

@app.get("/")
def root():
    return {"message" : "App is running"}
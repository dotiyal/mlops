import pickle
from flask import Flask, request
app = Flask(__name__)

model_pickle = open("mlops_env/classifier.pkl", "rb")
clf = pickle.load(model_pickle)


@app.route("/", methods=['GET'])
def ping():
    return "<H1>Loan Approval App</H1>"


@app.route("/predict", methods=['POST'])
def predictions():
    loan_req = request.get_json()

    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1

    if loan_req['Married'] == "Unmarried":
        Married = 0
    else:
        Married = 1

    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']
    Credit_History= loan_req['Credit_History']

    result = clf.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

    if result == 0:
        pred = "Decline"
    else:
        pred = "Approved"

    return {"loan_approval_status ": pred}


''' input JSON for POST request
{
    "ApplicantIncome":1000000,
    "Credit_History":1.0,
    "Gender":"Male",
    "LoanAmount":120,
    "Married":"Yes"
}
'''
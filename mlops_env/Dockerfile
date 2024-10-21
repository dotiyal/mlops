FROM python:3.12.2-slim

WORKDIR C:\Users\HP User\Documents\GitHub\mlops\Docker

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "-m", "flask", "--app", "./mlops-env/loan_app", "run", "--host=0.0.0.0"]

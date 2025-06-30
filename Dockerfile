FROM python:3.9

WORKDIR /app

COPY model.py .

RUN pip install scikit-learn

CMD ["python", "model.py"]
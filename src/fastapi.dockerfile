FROM python:3.9-slim


WORKDIR /app

# Instale as dependências do Python e o uvicorn
RUN pip install fastapi uvicorn scikit-learn

  
# Copie o código fonte da sua aplicação
COPY src/*.py .
  
CMD ["uvicorn", "mainFastApi:app", "--host", "0.0.0.0", "--port", "80"]
FROM python:3.9-slim

WORKDIR /app
 
# Instale as dependências do Python e o uvicorn 
RUN pip install Flask scikit-learn pydantic

# Copie o código fonte da sua aplicação
COPY src/*.py . 
  
# Exponha a porta em que o aplicativo Flask está ouvindo
EXPOSE 80

# Defina o comando padrão para iniciar o aplicativo Flask
CMD ["python", "mainFlask.py"]

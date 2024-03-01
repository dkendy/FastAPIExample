from flask import Flask
from trainmodel import train_and_evaluate_model

app = Flask(__name__) 

@app.route('/hello') 
def help():
    return {'message': 'Hello, world!'}
     

@app.route('/') 
def get(): 
    accuracy = train_and_evaluate_model(0.2, 42, 3)
    return {"get_accuracy": accuracy} 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
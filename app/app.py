from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Carrega modelo treinado
modelo = joblib.load('../modelo/arvore-decisao-pipeline1.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prever', methods=['POST'])
def prever():
    dados = request.get_json()

    
    entrada = pd.DataFrame([dados])

    # Fazer a predição
    pred = modelo.predict(entrada)

    return jsonify({'predicao': pred[0]})

if __name__ == '__main__':
    app.run(debug=True)

import joblib
import pandas as pd
from sklearn.metrics import accuracy_score
import pytest

# Carregar modelo
modelo = joblib.load('./modelo/arvore-decisao-pipeline1.pkl')

dados_teste = pd.DataFrame([
    {'location': 'United States', 'overall_score': 95.0},
    {'location': 'United Kingdom', 'overall_score': 88.5},
    {'location': 'India', 'overall_score': 60.0},
])

rotulos_reais = ['Alto', 'Alto', 'Médio']  

def test_accuracia_minima():
    predicoes = modelo.predict(dados_teste)

    # Cálculo de acurácia
    acc = accuracy_score(rotulos_reais, predicoes)

    print(f"Acurácia no teste: {acc}")
    
    # Validação com threshold mínimo
    assert acc >= 0.5, f"Acurácia abaixo do esperado: {acc}"

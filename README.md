# 🧠 Classificador de Desempenho Universitário

Projeto **classificar universidades por nível de desempenho** com base em dados do Kaggle ([World University Rankings](https://www.kaggle.com/datasets/aritra100/world-university-ranking)).

O projeto conta com:

- Pré-processamento de dados
- Classificação com KNN, Árvore de Decisão, Naive Bayes e SVM
- Avaliação com métricas como accuracy, precision, recall e F1-score
- Aplicação web full stack com Flask + HTML/JavaScript
- Testes automatizados com PyTest

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/SeuUsuario/MVP_MachineLearning.git
cd MVP_MachineLearning
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

- **Linux/macOS**:
  ```bash
  source venv/bin/activate
  ```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Rode a aplicação Flask

```bash
cd app
python app.py
```

Acesse no navegador: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 Rodando os testes

Na raiz do projeto:

```bash
pytest
```

Os testes automatizados garantem que o modelo atinja um desempenho mínimo (ex: accuracy > 0.8).

---

## 🗂️ Estrutura do Projeto

```
MVP_MachineLearning/
│
├── app/
│   ├── app.py                # API Flask
│   ├── templates/
│   │   └── index.html        # Front-end
│   ├── requirements.txt
│
├── modelo/
│       └── arvore-decisao_pipeline.pkl  # Modelo treinado
│
├── tests/
│   └── test_modelo.py        # Teste PyTest do modelo
│
└── README.md
```

---

## 🧩 Tecnologias utilizadas

- Python 3.11
- Pandas, NumPy
- Scikit-learn
- Flask
- HTML + JavaScript
- PyTest
- Joblib

---

## 📌 Observações

- O arquivo `.pkl` do modelo foi treinado com `scikit-learn==1.6.1`. Para evitar erros de compatibilidade, é recomendado usar a mesma versão.
- O front-end é simples, focado apenas na interação com o modelo. 

---

## 👩‍💻 Autor

Projeto desenvolvido por **Alessandra Rocha Ribas**.

# ProvaSI

# Previsão de Reposição de Gasolina ⛽

Sistema inteligente que prevê a demanda de gasolina nos próximos dias e alerta sobre necessidade de reposição.

## Crie um Ambiente Virutal
Windows:
python -m venv venv
venv\Scripts\activate

Linux/Mac:
python3 -m venv venv
source venv/bin/activate

## Após o inicialização do Amb. Virual

1. Instale as dependências: pip install -r requirements.txt

1.1 Atualize o PIP: python.exe -m pip install --upgrade pip

2. Treine o modelo: python model/modelo_treino.py

3. Execute a interface: python run_app.py

4. Envie um CSV com os dados no seguinte formato:
data,preco_gasolina,temperatura,chuva,feriado
    2024-04-01,5.69,30,0,0
...

## Tecnologias

- Python
- XGBoost
- Streamlit
- Pandas

---

🎯 Repositório mantido para a disciplina de **Sistemas Inteligentes Aplicados - 1º Semestre 2025**.


import pandas as pd
import xgboost as xgb
import joblib

# Carrega os dados
df = pd.read_csv('data/vendas_gasolina.csv', parse_dates=['data'])

# Features
df['dia_semana'] = df['data'].dt.weekday
X = df[['dia_semana', 'preco_gasolina', 'temperatura', 'chuva', 'feriado']]
y = df['vendas_litros']

# Treina o modelo
model = xgb.XGBRegressor()
model.fit(X, y)

# Salva o modelo
joblib.dump(model, 'model/modelo.pkl')
print("Modelo treinado e salvo.")

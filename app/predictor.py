import joblib
import pandas as pd

model = joblib.load('model/modelo.pkl')

def prever_demanda(dados_df):
    dados_df['dia_semana'] = pd.to_datetime(dados_df['data']).dt.weekday
    X = dados_df[['dia_semana', 'preco_gasolina', 'temperatura', 'chuva', 'feriado']]
    previsoes = model.predict(X)
    dados_df['previsao_litros'] = previsoes
    dados_df['alerta_reposicao'] = previsoes > 1800  # exemplo de limite
    return dados_df[['data', 'previsao_litros', 'alerta_reposicao']]

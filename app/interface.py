import streamlit as st
import pandas as pd
from predictor import prever_demanda

st.title("Previsão de Reposição de Gasolina")

arquivo = st.file_uploader("Envie o arquivo CSV com os dados de previsão", type="csv")

if arquivo:
    dados = pd.read_csv(arquivo)
    resultados = prever_demanda(dados)

    st.subheader("Resultados da Previsão")
    st.dataframe(resultados)

    st.subheader("Gráfico de Previsão")
    st.line_chart(resultados.set_index('data')['previsao_litros'])

    st.subheader("Alertas de Reposição")
    alertas = resultados[resultados['alerta_reposicao']]
    st.dataframe(alertas)

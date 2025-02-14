import pandas as pd
import plotly.express as px
import streamlit as st


# Carregar o conjunto de dados
car_data = pd.read_csv('vehicles.csv')  # Substitua pelo caminho correto do arquivo CSV

# Cabeçalho com texto
st.header("Análise de Veículos: Gráficos Interativos")
st.write("Este aplicativo realiza uma análise exploratória do conjunto de dados de veículos. Você pode gerar um histograma da distribuição de preços e um gráfico de dispersão entre preço e quilometragem.")

# Botão para gerar o histograma
hist_button = st.button('Criar Histograma de Preço')

if hist_button:
    # Criando o histograma
    fig_histogram = px.histogram(car_data, x="price", nbins=30, title="Distribuição dos Preços dos Veículos",
                                 labels={"price": "Preço (USD)"})
    st.plotly_chart(fig_histogram, use_container_width=True)

# Botão para gerar o gráfico de dispersão
scatter_button = st.button('Criar Gráfico de Dispersão')

if scatter_button:
    # Criando o gráfico de dispersão
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Preço vs Quilometragem",
                             labels={"odometer": "Quilometragem (milhas)", "price": "Preço (USD)"})
    st.plotly_chart(fig_scatter, use_container_width=True)

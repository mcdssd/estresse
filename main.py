"MODULE"
import streamlit as st
import yfinance as yf 
import plotly.graph_objects as go

#Título do app 
st.title('App aperreio')

#Barra lateral 
st.sidebar.title('Selecione o stock')
ticker_symbol1 = st.sidebar.text_input('stock1', 'AAPL', max_chars=10)
ticker_symbol2 = st.sidebar.text_input('stock2', 'MSFT', max_chars=10)

#Baixar dados
data1 = yf.download(ticker_symbol1, start='2020-01-01', end = 
'2023-06-26')
data2 = yf.download(ticker_symbol2, start='2020-01-01', end = '2023-06-26')

#Exibir dados 
st.subheader("Histórico")
st.dataframe(data1)
st.dataframe(data2)

#Exibir Gráfico 1 
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=data1.index, y = data1['Close'], name = 
'Fechamento'))
fig1.update_layout(title = f"{ticker_symbol1}", xaxis_title = "Data", yaxis_title =
                  "Preço")
st.plotly_chart(fig1)

#Gráfico 2
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=data2.index, y = data2['Close'], name = 'Fechamento'))
fig2.update_layout(title = f"{ticker_symbol2}", xaxis_titles = "Data", yaxis_title = "Preço")
st.plotly_chart(fig2) 

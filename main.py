import streamlit as st 
import yfinance as yf 
import plotly.graph_objects as go


#Título do app 
st.title('App aperreio')

#Barra lateral 
st.sidebar.title('Selecione o stock')
ticker_symbol = st.sidebar.text_input('stock', 'AAPL', max_chars=10)

#Baixar dados
data = yf.download(ticker_symbol, start='2020-01-01', end = 
'2023-06-26')

#Exibir dados 
st.subheader("Histórico")
st.dataframe(data)

#Exibir Gráfico 
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y = data['Close'], name = 
'Fechamento'))
fig.update_layout(title = f"{ticker_symbol}", xaxis_title = "Data", yaxis_title =
                  "Preço")
st.plotly_chart(fig)

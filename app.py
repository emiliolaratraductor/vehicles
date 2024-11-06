import streamlit as st
import pandas as pd
import plotly.express as px
data_path = '/Users/emilio/Desktop/sprint/vehicles/vehicles_us.csv'
df = pd.read_csv(data_path)
# Add a header
st.header("Datos de vehículos")

# Display dataset as a preview in the app
st.write("Un vistazo al conjunto de datos:")
st.write(df.head())

# Create a button to show the histogram
if st.button("Mostrar distribución de precios"):
    # Create a histogram using Plotly Express
    fig = px.histogram(df, x='price', title="Distribución de precios de vehículos")
    
    # Display the histogram
    st.plotly_chart(fig)
 # Crear otro botón para mostrar el gráfico de dispersión
if st.button("Mostrar gráfico de dispersión de precio y kilometraje"):
    # Crear el gráfico de dispersión usando Plotly Express
    fig_scatter = px.scatter(df, x='odometer', y='price', 
                             title="Gráfico de dispersión de precio vs. kilometraje",
                             labels={'odometer': 'Kilometraje', 'price': 'Precio'},
                             trendline="ols")  # Opcional: añadir una línea de tendencia

    # Mostrar el gráfico de dispersión
    st.plotly_chart(fig_scatter)
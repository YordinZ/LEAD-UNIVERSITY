#streamlit run "c:/Users/borge/OneDrive/Documentos/Introducción a la programación/Proyecto_curso_streamlit/app.py"
#Local URL: http://localhost:8501
#Network URL: http://192.168.50.227:8501
#TAREA: df= pd.read_csv('')

import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image


st.set_page_config(page_title='Mi APP', initial_sidebar_state='collapsed')

def main():
    st.title('CASO WALMART')

    # Cargar y mostrar la imagen
    image = Image.open('c:/Users/borge/OneDrive/Documentos/Introducción a la programación/Proyecto_curso_streamlit/icon.png')
    st.image(image, width=150)

    st.sidebar.header('Navegacion')
    
    # Opción 1: Cargar archivo
    uploaded_file = st.file_uploader("Sube tu archivo CSV...", type="csv")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

        # Gráfico de fechas vs precios de combustible
        fig = px.line(df, x='Date', y='Fuel_Price', title='Precio del Combustible por Fecha')
        st.plotly_chart(fig, use_container_width=True)

        #Índice de Precios al Consumidor (CPI)
        df_avg = df.groupby('Date')['CPI'].mean().reset_index()
        fig2 = px.bar(df_avg, x='Date', y='CPI', title='Índice de Precios al Consumidor (CPI) por Fecha')
        st.plotly_chart(fig2, use_container_width=True)
        
        
    else:
        st.info("Por favor sube el archivo Walmart.csv para continuar")
    
if __name__ == '__main__':
    main()
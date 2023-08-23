from graphviz import Digraph
from anytree import Node
import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd
import folium
import geopandas as gpd
import matplotlib.pyplot as plt


def mapa():
    # Cargar los datos del GeoJSON
    prov_geo = "informe/Argentina.geojson"
    geoJSON_df = gpd.read_file(prov_geo)

    # Crear el mapa inicial
    m = folium.Map(location=[-26.8083, -65.2176], zoom_start=3.5)

    # Función para resaltar una provincia en el mapa
    def highlight_province(province_name, count):
        feature_to_highlight = geoJSON_df[geoJSON_df['nombre'] == province_name]
        
        if not feature_to_highlight.empty:
            folium.GeoJson(
                feature_to_highlight,
                style_function=lambda feature: {
                    'fillColor': 'red' if count > 0 else 'gray',
                    'color': 'white',
                    'weight': 2,
                    'fillOpacity': 0.6,
                },
                tooltip=f"{province_name}: {count} teléfonos"
            ).add_to(m)

    # Aplicación Streamlit
    st.title("Tabla con valores de Argentina")

    phone_numbers = []
    # Lista de números de teléfono para verificar
    with open("informe/lineas.txt", "r") as f:
        for line in f:
            phone_numbers.append(line.strip())

    # Crear un DataFrame para los números de teléfono y las provincias
    data = {'Phone_Number': phone_numbers}
    df_phone_numbers = pd.DataFrame(data)

    # Cargar el archivo de Excel
    df_code_area = pd.read_excel('informe/area_code.xlsx', engine='openpyxl')
    code_area = {}
    for index, row in df_code_area.iterrows():
        code_area[str(row['CÓDIGO DE AREA'])] = [row['LOCALIDAD'], row['PROVINCIA']]

    # Definir una función para aplicar a cada número de teléfono en el DataFrame
    def get_province_and_city(phone_number):
        if phone_number[:2] in code_area:
            return code_area[phone_number[:2]][1]
        elif phone_number[:3] in code_area:
            if phone_number[:4] in code_area:
                return code_area[phone_number[:4]][1]
            else:
                return code_area[phone_number[:3]][1]
        elif phone_number[:4] in code_area:
            return code_area[phone_number[:4]][1]
        else:
            return 'Otro'

    # Aplicar la función a la columna 'Phone_Number' para obtener las provincias y ciudades
    df_phone_numbers['Province'] = df_phone_numbers['Phone_Number'].apply(get_province_and_city)

    # Agregar contador de números por provincia
    province_counts = df_phone_numbers['Province'].value_counts().reset_index()
    province_counts.columns = ['Province', 'Count']

    # Mostrar tabla de clúster de números por provincia
    st.write("Clúster de Números de Teléfono por Provincia:")
    st.table(province_counts)

    # Resaltar provincias en el mapa
    for index, row in province_counts.iterrows():
        highlight_province(row['Province'], row['Count'])

    # Mostrar el mapa en Streamlit
    st.markdown("Mapa de Provincias de Argentina:")
    st.components.v1.html(m._repr_html_(), width=700, height=400)

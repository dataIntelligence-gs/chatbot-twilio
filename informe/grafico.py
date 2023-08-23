import streamlit as st
from graphviz import Digraph
from anytree import Node
import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd
import folium
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from informe.constantes import *
import numpy as np

def grafico():
    st.markdown("Graficas de Barras y torta")
    #grafico de tortas entre cantidad_mensajes y responde

    x = np.array([1])
    width = 0.2

    fig, ax = plt.subplots()
    mensaje_bar = ax.bar(x - width, cantidad_mensajes, width, label='Total de Mensajes')
    responde_bar = ax.bar(x, responde, width, label='Responde')
    si_bar = ax.bar(x + width, si, width, label='Sí, me encantaría')
    
    ax.set_ylabel('Cantidad de Mensajes')
    ax.set_title('Grafica de Barras')
    ax.set_xticks(x)
    ax.set_xticklabels([''])

    ax.legend()
    
    for bar in mensaje_bar + responde_bar + si_bar:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval, yval, ha='center', va='bottom')

    st.pyplot(fig)


    labels = ['Responde', 'No responde']
    values = [responde, cantidad_mensajes-responde]


    #hacer grafico de torta y mostrar los values, cantidades y porcentajes
    st.markdown("Porcentaje de respuesta y sin respuesta")
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, shadow=True, explode=(0, 0.1), textprops={'color': 'w'}, pctdistance=0.8, wedgeprops={'linewidth': 1, 'edgecolor': 'w'}, rotatelabels=True)
    st.pyplot(fig)
    


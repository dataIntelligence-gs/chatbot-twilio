from graphviz import Digraph
from anytree import Node
import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd
import folium
import geopandas as gpd
import matplotlib.pyplot as plt
from informe.constantes import Constants


def arbol():
    st.image("informe/imagenes/price.png", caption='Precio de 1000 aperturas y 1000 mensajes', use_column_width=True)
    st.image("informe/imagenes/mensaje.png", caption='Mensaje utilizado para campaña', use_column_width=True)


    tupla = Constants().main()
    print(tupla[0])
    # Crear los nodos del árbol
    root = Node("Arbol")
    mensajes_node = Node(f"Mensajes {tupla[0]}", parent=root)
    responde_node = Node(f"Responde {tupla[1]}", parent=mensajes_node)
    si_node = Node(f"Si, me encantaría {tupla[2]}", parent=responde_node)
    si_porcentaje_node = Node(f"Porcentaje de derivación {tupla[7]}", parent=si_node)
    no_porcentaje_node = Node(f"Porcentaje de no derivación {tupla[8]}", parent=si_node)
    no_en_otro_momento_node = Node(f"No en otro momento {tupla[5]}", parent=responde_node)
    no_responde_node = Node(f"No responde {tupla[6]}", parent=mensajes_node)


    # Crear un objeto Digraph
    dot = Digraph(format='png', graph_attr={'rankdir': 'TB', 'bgcolor': 'black'})
    dot.attr('node', style='filled', shape='box', color='#D9E6F5', fontname='Courier', fontsize='10')
    dot.attr('edge', color='#808080')


    # Agregar las relaciones entre los nodos
    for node in root.descendants:
        if node.parent:
            dot.edge(node.parent.name, node.name)

    # Guarda en un archivo temporal
    graph_filename = "temp_graph"
    dot.render("informe/imagenes/" + graph_filename, cleanup=True)

    # Crear la interfaz de streamlit
    st.title("Arbol de Mensajes")

    tree_image = Image.open("informe/imagenes/temp_graph.png")
    st.image(tree_image, caption="Árbol de Mensajes", use_column_width=True, output_format="PNG")

